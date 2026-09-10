"""
Generador de tarjetas.csv, transacciones.csv y transacciones_sucias.csv
— dataset del curso PAD (ITBA, Maestría en Fintech).

Reemplaza las versiones anteriores, en las que nada estaba relacionado con nada: el límite
de crédito promedio del segmento Joven era mayor que el de Premium, todos los segmentos
transaccionaban igual, y quien hacía churn gastaba lo mismo que quien se quedaba.

Requiere `clientes.csv` ya generado (ver generar_clientes.py) y se engancha a él:
segmento, saldo, antigüedad y churn del cliente determinan qué tarjetas tiene, cuánto
gasta, en qué categorías y hasta cuándo.

Estructura que este generador garantiza (y que las clases usan):

  Clase 3 — transacciones.csv
    · Jerarquía clara de gasto por categoría
    · Débito vs crédito con perfiles distintos (el pivot categoría × tipo dice algo)
    · Tendencia nominal creciente durante 2024 + pico de diciembre + valle de enero-febrero
    · Viajes con estacionalidad marcada (enero y julio)
    · E-commerce como la categoría de mayor crecimiento Q1 → Q4
    · Viernes y sábado como días de mayor gasto

  Clase 4 — joins
    · Límite de crédito y gasto escalan con el segmento (Premium >> Joven)
    · ~50 clientes SIN tarjeta → el LEFT JOIN muestra algo
    · ~45 clientes CON tarjeta y SIN transacciones → el ejercicio 4 tiene respuesta
    · Quien hizo churn dejó de operar meses antes: gasta menos y deja de aparecer
    · Tasa de rechazo mucho más alta en Joven que en Premium

  Clase 5 — transacciones_sucias.csv
    · ~3% duplicados · ~7% nulos en monto · ~5% en categoría · ~4% en fecha
    · Inconsistencias de texto en `categoria` y `tipo`
    · Montos cero, negativos y outliers extremos

Determinista: mismo seed → mismos archivos.
"""

import numpy as np
import pandas as pd

SEED = 20260814
rng = np.random.default_rng(SEED)

clientes = pd.read_csv("clientes.csv")
N = len(clientes)
FIN = pd.Timestamp("2024-12-31")

# ============================================================ TARJETAS

TIPOS_CREDITO = ["Visa Crédito", "Mastercard Crédito", "Amex Crédito"]

# (p de tener crédito, cantidad máxima de créditos, límite mediano, pesos de marca)
CFG_TARJETA = {
    "Joven":   {"p_cred": 0.40, "max_cred": 1, "limite_med":   150_000, "marca": [0.55, 0.45, 0.00]},
    "Retail":  {"p_cred": 0.72, "max_cred": 2, "limite_med":   600_000, "marca": [0.45, 0.45, 0.10]},
    "PyME":    {"p_cred": 0.92, "max_cred": 3, "limite_med": 2_500_000, "marca": [0.40, 0.35, 0.25]},
    "Premium": {"p_cred": 0.97, "max_cred": 3, "limite_med": 6_000_000, "marca": [0.35, 0.30, 0.35]},
}

# Clientes sin ninguna tarjeta: sesgados a Joven y a quienes hicieron churn.
peso_sin = np.where(clientes.segmento == "Joven", 4.0, 1.0) * np.where(clientes.churn == 1, 3.0, 1.0)
sin_tarjeta = set(rng.choice(clientes.index, size=50, replace=False, p=peso_sin / peso_sin.sum()))

filas_t = []
n_tarjeta = 0
for i, cl in clientes.iterrows():
    if i in sin_tarjeta:
        continue
    cfg = CFG_TARJETA[cl.segmento]
    alta = FIN - pd.Timedelta(days=float(cl["antiguedad_años"]) * 365.25)

    tipos = ["Visa Débito"]
    if rng.random() < cfg["p_cred"]:
        k = 1 + rng.binomial(cfg["max_cred"] - 1, 0.45)
        tipos += list(rng.choice(TIPOS_CREDITO, size=k, replace=False, p=cfg["marca"])) if k <= 3 else []

    # Percentil de saldo dentro del segmento: quien tiene más plata, más límite
    pares = clientes.loc[clientes.segmento == cl.segmento, "balance_ars"]
    pct = (pares < cl["balance_ars"]).mean()

    for tipo in tipos:
        n_tarjeta += 1
        if tipo == "Visa Débito":
            limite = 0
        else:
            bruto = cfg["limite_med"] * (0.55 + 0.9 * pct) * rng.lognormal(0, 0.28)
            limite = int(round(bruto, -4))

        dias = max((FIN - pd.Timedelta(days=30) - alta).days, 1)
        emision = alta + pd.Timedelta(days=int(rng.integers(0, dias)))

        filas_t.append({
            "tarjeta_id": f"T{n_tarjeta:05d}",
            "cliente_id": cl["cliente_id"],
            "tipo_tarjeta": tipo,
            "limite_credito": limite,
            "fecha_emision": emision.strftime("%Y-%m-%d"),
            "activa": int(rng.random() < (0.15 if cl["churn"] == 1 else 0.97)),
        })

tarjetas = pd.DataFrame(filas_t)
tarjetas.to_csv("tarjetas.csv", index=False)

# ============================================================ TRANSACCIONES

CATEGORIAS = ["Supermercado", "Restaurant", "Combustible", "Viajes", "Entretenimiento",
              "Salud", "Indumentaria", "Servicios", "E-commerce", "Transferencia"]

# Mezcla de categorías por segmento — cada perfil consume distinto
MEZCLA = {
    "Joven":   [0.14, 0.16, 0.04, 0.03, 0.14, 0.03, 0.12, 0.08, 0.20, 0.06],
    "Retail":  [0.24, 0.10, 0.12, 0.03, 0.07, 0.07, 0.09, 0.14, 0.10, 0.04],
    "PyME":    [0.12, 0.10, 0.20, 0.04, 0.03, 0.05, 0.04, 0.22, 0.08, 0.12],
    "Premium": [0.14, 0.18, 0.09, 0.12, 0.08, 0.08, 0.09, 0.10, 0.07, 0.05],
}
MEZCLA = {k: np.array(v) / sum(v) for k, v in MEZCLA.items()}

TICKET_MED = dict(zip(CATEGORIAS, [28_000, 22_000, 18_000, 85_000, 15_000,
                                    35_000, 40_000, 12_000, 32_000, 70_000]))

# Probabilidad de que la compra se haga con crédito (si el cliente tiene tarjeta de crédito)
P_CREDITO = dict(zip(CATEGORIAS, [0.35, 0.55, 0.30, 0.92, 0.60,
                                   0.45, 0.80, 0.20, 0.85, 0.05]))

FACTOR_SEG = {"Joven": 0.50, "Retail": 0.85, "PyME": 1.40, "Premium": 2.60}
FREC_SEG   = {"Joven": 2.40, "Retail": 2.80, "PyME": 3.50, "Premium": 3.85}  # transacciones/mes

# Estacionalidad general: valle de verano, pico de diciembre
ESTACION = np.array([0.92, 0.88, 1.00, 0.98, 1.00, 1.05, 1.08, 1.00, 1.00, 1.03, 1.06, 1.30])
# Tendencia nominal creciente a lo largo de 2024
TENDENCIA = np.linspace(1.00, 1.45, 12)

# Multiplicadores por categoría y mes (estacionalidades propias)
MULT_CAT = {c: np.ones(12) for c in CATEGORIAS}
MULT_CAT["Viajes"]        = np.array([2.20, 1.40, 0.70, 0.70, 0.70, 0.80, 2.00, 0.90, 0.70, 0.80, 0.90, 1.60])
MULT_CAT["E-commerce"]    = np.linspace(0.55, 1.95, 12); MULT_CAT["E-commerce"][10] *= 1.50   # Black Friday
MULT_CAT["Indumentaria"]  = np.array([0.85, 0.80, 1.05, 1.10, 1.00, 1.20, 1.00, 0.95, 1.05, 1.05, 1.10, 1.55])
MULT_CAT["Entretenimiento"] = np.array([1.25, 1.10, 0.95, 0.90, 0.90, 0.95, 1.20, 0.95, 0.90, 0.95, 1.00, 1.25])

# Día de la semana: el gasto se concentra en el fin de semana
PESO_DIA = np.array([0.12, 0.12, 0.13, 0.14, 0.18, 0.19, 0.12])  # lun..dom

# Mes en que se fue cada cliente con churn: deja de operar a partir de ahí
mes_baja = np.where(clientes.churn == 1, rng.integers(3, 12, N), 13)

tarj_por_cliente = tarjetas.groupby("cliente_id")
debito_de  = {c: g.loc[g.tipo_tarjeta == "Visa Débito", "tarjeta_id"].tolist() for c, g in tarj_por_cliente}
credito_de = {c: g.loc[g.tipo_tarjeta != "Visa Débito", "tarjeta_id"].tolist() for c, g in tarj_por_cliente}
limite_de  = dict(zip(tarjetas.tarjeta_id, tarjetas.limite_credito))

con_tarjeta = [i for i in clientes.index if clientes.at[i, "cliente_id"] in debito_de]
# Clientes con tarjeta que nunca operaron (ejercicio 4 de la Clase 4)
peso_inact = np.array([4.0 if clientes.at[i, "segmento"] == "Joven" else 1.0 for i in con_tarjeta]) * \
             np.array([3.0 if clientes.at[i, "churn"] == 1 else 1.0 for i in con_tarjeta])
nunca_operaron = set(rng.choice(con_tarjeta, size=45, replace=False, p=peso_inact / peso_inact.sum()))

filas_x = []
for i in con_tarjeta:
    if i in nunca_operaron:
        continue
    cl = clientes.loc[i]
    cid = cl["cliente_id"]
    mezcla = MEZCLA[cl["segmento"]]
    factor = FACTOR_SEG[cl["segmento"]]
    frec = FREC_SEG[cl["segmento"]] * (1.0 if cl["cliente_activo"] else 0.55)
    cred = credito_de.get(cid, [])
    deb = debito_de[cid]

    for mes in range(1, 13):
        if mes > mes_baja[i]:
            continue
        # Los dos meses previos a la baja, la actividad ya viene cayendo
        desgaste = {0: 1.0, 1: 0.55, 2: 0.80}.get(mes_baja[i] - mes, 1.0) if mes_baja[i] <= 12 else 1.0

        lam = frec * ESTACION[mes - 1] * desgaste
        n = rng.poisson(lam)
        if n == 0:
            continue

        cats = rng.choice(CATEGORIAS, size=n, p=mezcla)
        for cat in cats:
            # ¿la categoría "se activa" este mes? (estacionalidad propia)
            if rng.random() > min(MULT_CAT[cat][mes - 1], 1.0) and MULT_CAT[cat][mes - 1] < 1.0:
                continue
            repeticiones = 1 + (1 if MULT_CAT[cat][mes - 1] > 1.6 and rng.random() < 0.45 else 0)

            for _ in range(repeticiones):
                usa_credito = bool(cred) and rng.random() < P_CREDITO[cat]
                tid = rng.choice(cred) if usa_credito else rng.choice(deb)
                tipo = "crédito" if usa_credito else "débito"

                monto = (TICKET_MED[cat] * factor * TENDENCIA[mes - 1]
                         * rng.lognormal(0, 0.55))
                monto = round(float(monto), 2)

                dia_sem = rng.choice(7, p=PESO_DIA)
                dias_mes = pd.Timestamp(2024, mes, 1).days_in_month
                candidatos = [d for d in range(1, dias_mes + 1)
                              if pd.Timestamp(2024, mes, d).dayofweek == dia_sem]
                dia = int(rng.choice(candidatos))

                # Rechazo: más frecuente en Joven, y cuando el monto se acerca al límite
                p_rech = 0.020
                p_rech += {"Joven": 0.075, "Retail": 0.030, "PyME": 0.018, "Premium": 0.004}[cl["segmento"]]
                if usa_credito and limite_de[tid] > 0:
                    p_rech += 0.35 * min(monto / limite_de[tid], 1.0) ** 2
                if mes == 12:
                    p_rech *= 1.25

                filas_x.append({
                    "tarjeta_id": tid,
                    "cliente_id": cid,
                    "fecha": f"2024-{mes:02d}-{dia:02d}",
                    "monto_ars": monto,
                    "categoria": cat,
                    "tipo": tipo,
                    "aprobada": int(rng.random() > p_rech),
                })

transacciones = pd.DataFrame(filas_x).sort_values("fecha", kind="stable").reset_index(drop=True)
transacciones.insert(0, "transaccion_id", [f"TX{i:06d}" for i in range(1, len(transacciones) + 1)])
transacciones = transacciones[["transaccion_id", "tarjeta_id", "cliente_id", "fecha",
                               "monto_ars", "categoria", "tipo", "aprobada"]]
transacciones.to_csv("transacciones.csv", index=False)

# ============================================================ TRANSACCIONES SUCIAS

s = transacciones.copy()

# 1. Outliers y errores de carga en monto
idx = rng.choice(s.index, size=60, replace=False)
s.loc[idx[:25], "monto_ars"] = (s.loc[idx[:25], "monto_ars"] * rng.uniform(60, 400, 25)).round(2)   # ceros de más
s.loc[idx[25:45], "monto_ars"] = 0.0                                                                 # importes en cero
s.loc[idx[45:], "monto_ars"] = -s.loc[idx[45:], "monto_ars"].abs()                                   # signo invertido

# 2. Inconsistencias de texto
idx = rng.choice(s.index, size=int(len(s) * 0.16), replace=False)
estilo = rng.integers(0, 4, len(idx))
s.loc[idx[estilo == 0], "categoria"] = s.loc[idx[estilo == 0], "categoria"].str.upper()
s.loc[idx[estilo == 1], "categoria"] = s.loc[idx[estilo == 1], "categoria"].str.lower()
s.loc[idx[estilo == 2], "categoria"] = "  " + s.loc[idx[estilo == 2], "categoria"] + " "
s.loc[idx[estilo == 3], "categoria"] = s.loc[idx[estilo == 3], "categoria"].str.strip() + "  "

idx = rng.choice(s.index, size=int(len(s) * 0.22), replace=False)
es_credito = s.loc[idx, "tipo"].values == "crédito"
s.loc[idx, "tipo"] = np.where(
    es_credito,
    rng.choice(["credito", "CREDITO", "credit", " crédito ", "Crédito"], size=len(idx)),
    rng.choice(["Débito", "DÉBITO", " débito ", "débito "], size=len(idx)),
)

# 3. Nulos
for col, frac in [("monto_ars", 0.07), ("categoria", 0.05), ("fecha", 0.04)]:
    s.loc[rng.choice(s.index, size=int(len(s) * frac), replace=False), col] = np.nan

# 4. Duplicados exactos (~3%) — se agregan al final para que sigan siendo idénticos
s = pd.concat([s, s.sample(frac=0.03, random_state=7)], ignore_index=True)

s = s.sample(frac=1, random_state=11).reset_index(drop=True)
s.to_csv("transacciones_sucias.csv", index=False)

# ============================================================ VERIFICACIÓN
print(f"tarjetas             : {len(tarjetas):,}")
print(f"transacciones        : {len(transacciones):,}")
print(f"transacciones_sucias : {len(s):,}\n")

m = tarjetas.merge(clientes[["cliente_id", "segmento", "churn"]], on="cliente_id")
print("— límite de crédito promedio por segmento (Clase 4, ej. 2)")
lim = m[m.tipo_tarjeta != "Visa Débito"].groupby("segmento")["limite_credito"].mean()
print((lim / 1e6).round(2).astype(str).add("M").to_string())
print(f"\nclientes sin tarjeta: {N - tarjetas.cliente_id.nunique()}")
print(f"clientes con tarjeta y sin transacciones: {tarjetas.cliente_id.nunique() - transacciones.cliente_id.nunique()}")

x = transacciones.merge(clientes[["cliente_id", "segmento", "churn"]], on="cliente_id")
print("\n— gasto por segmento (Clase 4)")
g = x.groupby("segmento").agg(trx=("transaccion_id", "count"), ticket=("monto_ars", "mean"),
                              total=("monto_ars", "sum"), rechazo=("aprobada", lambda v: 1 - v.mean()))
print(g.assign(ticket=g.ticket.round(0), total=(g.total / 1e6).round(1).astype(str) + "M",
               rechazo=(g.rechazo * 100).round(1).astype(str) + "%").to_string())

print("\n— gasto anual por cliente según churn (Clase 4)")
por_cli = x.groupby(["cliente_id", "churn"])["monto_ars"].agg(["sum", "count"]).reset_index()
print(por_cli.groupby("churn")[["sum", "count"]].mean().round(0).to_string())

print("\n— top categorías (Clase 3)")
print((x.groupby("categoria")["monto_ars"].sum() / 1e6).round(1).sort_values(ascending=False).astype(str).add("M").to_string())

x["mes"] = x.fecha.str[5:7].astype(int)
print("\n— evolución mensual, millones ARS (Clase 3)")
print((x.groupby("mes")["monto_ars"].sum() / 1e6).round(1).to_string())

q = x.assign(trim=lambda d: (d.mes - 1) // 3 + 1)
piv = q.pivot_table(values="monto_ars", index="categoria", columns="trim", aggfunc="sum")
crec = ((piv[4] / piv[1] - 1) * 100).round(0).sort_values(ascending=False)
print("\n— crecimiento Q1 → Q4 por categoría, % (Clase 3, ej. 5)")
print(crec.to_string())

print("\n— Viajes por mes, millones (Clase 3, ej. 8)")
print((x[x.categoria == "Viajes"].groupby("mes")["monto_ars"].sum() / 1e6).round(1).to_string())

x["dia"] = pd.to_datetime(x.fecha).dt.day_name()
print("\n— gasto por día de la semana (Clase 3, ej. 2)")
print((x.groupby("dia")["monto_ars"].sum() / 1e6).round(1).sort_values(ascending=False).to_string())

print("\n— sucio: nulos %")
print((s.isna().mean() * 100).round(1)[lambda v: v > 0].to_string())
print(f"duplicados exactos: {s.duplicated().sum():,}")
print(f"categorías distintas (sucio): {s.categoria.nunique()} · tipos distintos: {s.tipo.nunique()}")
print(f"montos <= 0: {(s.monto_ars <= 0).sum()}")
