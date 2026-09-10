"""
Generador de clientes.csv — dataset del curso PAD (ITBA, Maestría en Fintech).

Reemplaza la versión anterior, en la que todas las columnas eran independientes entre sí
y por lo tanto ningún análisis del curso encontraba señal.

Estructura que este generador SÍ garantiza (y que las clases usan):
  - Los segmentos tienen perfiles distintos y coherentes con su nombre
    (Joven es efectivamente joven, con poca antigüedad y poco saldo)
  - El churn depende de: segmento, antigüedad, cantidad de productos y saldo
  - `balance_ars` es lognormal → media >> mediana (lección promedio vs mediana)
  - Ranking por TASA de churn ≠ ranking por BALANCE EN RIESGO (desafío Clase 2)
  - Una provincia de base chica queda con tasa alta por azar (lección de bases chicas)

Se preservan `cliente_id` (C0001..C1000) y el orden de las filas, así que los joins con
tarjetas.csv, transacciones.csv y portafolio_prestamos.csv siguen funcionando igual.

Determinista: mismo seed → mismo archivo.
"""

import numpy as np
import pandas as pd

SEED = 20260814
rng = np.random.default_rng(SEED)
N = 1000

# ---------------------------------------------------------------- nombres
NOMBRES = [
    "Sofía", "Mateo", "Valentina", "Benjamín", "Isabella", "Santiago", "Emma", "Joaquín",
    "Catalina", "Tomás", "Martina", "Lucas", "Julieta", "Bautista", "Delfina", "Thiago",
    "Camila", "Franco", "Lucía", "Ignacio", "Renata", "Facundo", "Mía", "Bruno",
    "Emilia", "Nicolás", "Olivia", "Agustín", "Victoria", "Máximo", "Guadalupe", "Lautaro",
    "Paulina", "Ramiro", "Antonella", "Gonzalo", "Florencia", "Matías", "Carolina", "Diego",
    "Mercedes", "Federico", "Rocío", "Alejandro", "Malena", "Sebastián", "Pilar", "Rodrigo",
    "Constanza", "Marcos",
]
APELLIDOS = [
    "González", "Rodríguez", "Gómez", "Fernández", "López", "Martínez", "Díaz", "Pérez",
    "Sánchez", "Romero", "Álvarez", "Torres", "Ruiz", "Ramírez", "Flores", "Benítez",
    "Acosta", "Medina", "Herrera", "Aguirre", "Molina", "Castro", "Ortiz", "Silva",
    "Núñez", "Rojas", "Luna", "Juárez", "Cabrera", "Ríos", "Sosa", "Ferrari",
    "Bianchi", "Moreno", "Vega", "Peralta", "Quiroga", "Ledesma", "Ojeda", "Villalba",
]

# ---------------------------------------------------------------- segmentos
# Distribución: Retail masivo, Joven con base suficiente para que su tasa sea creíble.
SEGMENTOS = ["Retail", "Joven", "Premium", "PyME"]
N_SEG = {"Retail": 420, "Joven": 240, "Premium": 180, "PyME": 160}
assert sum(N_SEG.values()) == N

PERFIL = {
    #            edad (min, max, moda)   antigüedad máx    balance lognormal (mediana, sigma)
    "Joven":   {"edad": (18, 30),  "ant_media": 1.3, "ant_max": 5.0,  "bal_mediana":   45_000, "bal_sigma": 0.85, "prod": (1, 3)},
    "Retail":  {"edad": (25, 65),  "ant_media": 4.5, "ant_max": 14.0, "bal_mediana":  190_000, "bal_sigma": 0.95, "prod": (1, 4)},
    "PyME":    {"edad": (30, 62),  "ant_media": 6.0, "ant_max": 16.0, "bal_mediana":  520_000, "bal_sigma": 1.05, "prod": (2, 6)},
    "Premium": {"edad": (38, 71),  "ant_media": 9.5, "ant_max": 22.0, "bal_mediana": 1_500_000, "bal_sigma": 0.90, "prod": (3, 6)},
}

# ---------------------------------------------------------------- provincias
# "Rosario" era una ciudad listada como provincia — se reemplaza por Entre Ríos.
PROVINCIAS = {
    "Buenos Aires": 0.270,
    "CABA":         0.245,
    "Córdoba":      0.160,
    "Santa Fe":     0.125,
    "Mendoza":      0.090,
    "Entre Ríos":   0.065,
    "Tucumán":      0.045,
}

# ---------------------------------------------------------------- construcción
segmento = np.array(sum([[s] * n for s, n in N_SEG.items()], []))
rng.shuffle(segmento)

edad = np.empty(N, dtype=int)
antiguedad = np.empty(N)
balance = np.empty(N)
productos = np.empty(N, dtype=int)

for seg, p in PERFIL.items():
    m = segmento == seg
    k = m.sum()

    lo, hi = p["edad"]
    # Beta apenas sesgada a la izquierda del rango: evita el "uniforme" que delata datos sintéticos
    edad[m] = np.round(lo + (hi - lo) * rng.beta(2.0, 2.6, k)).astype(int)

    # Antigüedad exponencial truncada, y nunca mayor a (edad - 18)
    a = rng.exponential(p["ant_media"], k)
    a = np.clip(a, 0.1, p["ant_max"])
    a = np.minimum(a, np.maximum(edad[m] - 18, 0.2))
    antiguedad[m] = np.round(a, 1)

    balance[m] = np.round(p["bal_mediana"] * rng.lognormal(0, p["bal_sigma"], k), -2)

    plo, phi = p["prod"]
    productos[m] = rng.integers(plo, phi + 1, k)

provincia = rng.choice(list(PROVINCIAS), size=N, p=list(PROVINCIAS.values()))

# ---------------------------------------------------------------- churn
# Modelo logístico: el churn es CONSECUENCIA del perfil, no una columna independiente.
# Dentro de cada segmento, quien tiene menos antigüedad, menos productos y menos saldo
# fuga más — esa estructura es la que hacen aflorar los ejercicios de la Clase 2.

# Efecto provincial chico y aleatorio: las provincias difieren apenas, de modo que las de
# base chica muestran tasas llamativas que son puro azar (la trampa del Ejercicio 9).
efecto_provincia = {p: v for p, v in zip(PROVINCIAS, rng.normal(0, 0.25, len(PROVINCIAS)))}
efecto_provincia["Tucumán"] = 0.70   # base chica (n≈45) + tasa alta = ruido que parece señal

ant_norm = np.clip(antiguedad, 0, 15) / 15
bal_norm = np.log10(np.clip(balance, 1_000, None)) / 7

base = (
    np.array([efecto_provincia[p] for p in provincia])
    - 0.90 * ant_norm            # más antigüedad → menos fuga (hipótesis del onboarding: verdadera)
    - 0.10 * (productos - 1)     # más productos → más vinculación
    - 0.35 * (bal_norm - 0.75)   # más saldo → menos fuga
    + rng.normal(0, 0.40, N)
)

# Tasa objetivo por segmento. El offset de cada uno se resuelve numéricamente para que la
# probabilidad media del segmento dé exactamente eso — así el dataset es reproducible y las
# conclusiones de clase no dependen del azar del generador.
TASA_OBJETIVO = {"Joven": 0.38, "Retail": 0.18, "PyME": 0.12, "Premium": 0.07}

def sigmoide(z):
    return 1 / (1 + np.exp(-z))

prob = np.empty(N)
for seg, objetivo in TASA_OBJETIVO.items():
    m = segmento == seg
    lo, hi = -12.0, 12.0
    for _ in range(80):                      # bisección
        medio = (lo + hi) / 2
        if sigmoide(base[m] + medio).mean() < objetivo:
            lo = medio
        else:
            hi = medio
    prob[m] = sigmoide(base[m] + (lo + hi) / 2)

# Selección con cuota exacta por segmento (muestreo ponderado sin reemplazo, Efraimidis–Spirakis):
# se eligen exactamente round(n * tasa_objetivo) clientes, con probabilidad proporcional a sus odds.
# Así la tasa por segmento no queda librada al azar del sorteo, pero sí se mantiene la estructura:
# dentro de cada segmento fugan los de menos antigüedad, menos productos y menos saldo.
churn = np.zeros(N, dtype=int)
for seg, objetivo in TASA_OBJETIVO.items():
    idx = np.flatnonzero(segmento == seg)
    k = int(round(len(idx) * objetivo))
    odds = prob[idx] / (1 - prob[idx])
    clave = rng.random(len(idx)) ** (1 / odds)
    churn[idx[np.argsort(-clave)[:k]]] = 1

# Quien se fue casi nunca sigue operando; quien se quedó, casi siempre sí.
p_activo = np.where(churn == 1, 0.12, 0.92)
cliente_activo = rng.random(N) < p_activo

nombres = [f"{NOMBRES[rng.integers(len(NOMBRES))]} {APELLIDOS[rng.integers(len(APELLIDOS))]}" for _ in range(N)]

df = pd.DataFrame({
    "cliente_id": [f"C{i:04d}" for i in range(1, N + 1)],
    "nombre": nombres,
    "edad": edad,
    "provincia": provincia,
    "segmento": segmento,
    "antiguedad_años": antiguedad,
    "balance_ars": balance,
    "cant_productos": productos,
    "cliente_activo": cliente_activo,
    "churn": churn,
})

df.to_csv("clientes.csv", index=False)

# ---------------------------------------------------------------- verificación
print(f"{len(df)} clientes · churn global {df.churn.mean():.1%}\n")

r = df.groupby("segmento").agg(
    clientes=("cliente_id", "count"),
    edad=("edad", "mean"),
    antig=("antiguedad_años", "mean"),
    bal_mediana=("balance_ars", "median"),
    tasa_churn=("churn", "mean"),
    bal_total=("balance_ars", "sum"),
)
r["riesgo"] = r.bal_total * r.tasa_churn
print(r.assign(
    edad=r.edad.round(1),
    antig=r.antig.round(1),
    bal_mediana=(r.bal_mediana / 1000).round(0).astype(int).astype(str) + "k",
    tasa_churn=(r.tasa_churn * 100).round(1).astype(str) + "%",
    bal_total=(r.bal_total / 1e6).round(1).astype(str) + "M",
    riesgo=(r.riesgo / 1e6).round(1).astype(str) + "M",
).sort_values("clientes", ascending=False).to_string())

print(f"\nRanking por TASA   : {' > '.join(r.tasa_churn.sort_values(ascending=False).index)}")
print(f"Ranking por RIESGO : {' > '.join(r.riesgo.sort_values(ascending=False).index)}")
print(f"\nbalance media/mediana = {df.balance_ars.mean()/df.balance_ars.median():.2f}x")
print(f"activos: {df.cliente_activo.mean():.1%}")
print(f"\nantigüedad promedio  se quedaron {df[df.churn==0]['antiguedad_años'].mean():.1f}  |  se fueron {df[df.churn==1]['antiguedad_años'].mean():.1f}")

cp = df.groupby("provincia").agg(n=("cliente_id", "count"), tasa=("churn", "mean")).sort_values("tasa", ascending=False)
print("\nchurn por provincia:")
print(cp.assign(tasa=(cp.tasa * 100).round(1)).to_string())
