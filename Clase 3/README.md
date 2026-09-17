# Clase 3 — Segmentación y series de tiempo

**Tipo:** Teórico-práctica | **Duración:** 3 horas

## Objetivo

Que el alumno entienda que una serie de tiempo tiene componentes que hay que separar antes de concluir,
y que pueda agrupar datos por cualquier dimensión, armar una serie mensual, suavizarla con un promedio
móvil y no caer en la trampa de los pesos.

## Estructura

| Bloque | Qué pasa | Tiempo |
|---|---|---|
| Apertura | Recap de la Clase 2 | 10 min |
| **1 · Teoría** | Series de tiempo: componentes, calendario argentino, comparar contra qué, inflación. Colab cerrado | 30 min |
| **2 · Práctica guiada** | Resolvemos `Clase_3_Practica_Guiada.ipynb` juntos | 75 min |
| — | Corte | 10 min |
| **3 · Práctica individual** | Resuelven `Clase_3_Practica_Individual.ipynb` solos, con Gemini | 45 min |
| Cierre | Puesta en común de los ejercicios 5, 8 y 10 | 10 min |

## Contenido

**Negocio**
- Qué es una serie de tiempo; tendencia, estacionalidad, ciclo y ruido
- El calendario del consumo argentino
- Comparar contra qué: mes anterior, interanual, promedio móvil
- La trampa de los pesos: monto vs cantidad

**Técnico**
- `groupby` y funciones de agregación; `.agg()` con varias métricas
- `pivot_table` y heatmaps
- `pd.to_datetime`, `.dt`, `resample`
- `rolling` (promedios móviles) y series en base 100

## Materiales

| Archivo | Descripción | ¿Se comparte? |
|---------|-------------|---|
| `Clase_3_Practica_Guiada.ipynb` | Recorrido resuelto que se hace en clase (8 pasos + recomendación) | Sí |
| `Clase_3_Practica_Individual.ipynb` | 10 ejercicios con celda de lectura de negocio + desafío | Sí |
| `Soluciones_Clase_3.ipynb` | Soluciones, lectura esperada, criterios y tabla de números del dataset | **No — solo docente** |
| `Guion_Clase_3.md` | Guión completo, tiempos y notas de dictado | Solo docente |
| `Deck_Clase_3_PARA_GAMMA.md` | Fuente del deck (11 slides), para regenerarlo en Gamma | Solo docente |
| `Deck_Outline_Clase_3.md` | Outline largo (23 slides), previo al rediseño | Solo docente |
| `Clase_3_Segmentacion_TimeSeries.ipynb` | Versión vieja, todo en una notebook. Reemplazada | No |
| `data/transacciones.csv` | ~29.000 transacciones de 2024 | Se descarga solo desde el repo |

## Dataset: `transacciones.csv`

- **Filas:** 28.956 transacciones de 905 clientes
- **Columnas:** transaccion_id, tarjeta_id, cliente_id, fecha, monto_ars, categoria, tipo, aprobada
- **Período:** enero–diciembre 2024

## Para el docente

1. **El bloque de teoría no se saltea.** Sin él, la caída de agosto–septiembre y el base 100 no se pueden leer.
2. **El Paso 6 (promedio móvil) es el momento "wow"** y el Paso 8 es el remate: el monto se duplica mientras operan menos clientes.
3. **No prometer el pico de Viajes en enero:** el dataset muestra julio y noviembre–diciembre, no enero.

El detalle completo, con tiempos y frases de dictado, está en `Guion_Clase_3.md`.
