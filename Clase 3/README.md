# Clase 3 — Segmentación y series de tiempo

**Tipo:** Teórico-práctica | **Duración:** 3 horas

## Objetivo
Que el alumno pueda agrupar datos por cualquier dimensión (segmento, categoría, período) y analizar evolución temporal con rolling averages.

## Contenido
- GroupBy: la navaja suiza del analista
- Pivot tables en Python
- Trabajando con fechas: `datetime`, `resample`
- Series de tiempo: evolución mensual, trimestral
- Rolling averages (promedios móviles)
- Visualizaciones: barras, heatmaps, líneas temporales

## Materiales
| Archivo | Descripción |
|---------|-------------|
| `Clase_3_Segmentacion_TimeSeries.ipynb` | Notebook con código guiado + 10 ejercicios |
| `data/transacciones.csv` | Dataset de ~29.000 transacciones de 2024 |

## Dataset: `transacciones.csv`
- **Filas:** ~29.000 transacciones
- **Columnas:** transaccion_id, tarjeta_id, cliente_id, fecha, monto_ars, categoria, tipo, aprobada
- **Categorías:** Supermercado, Restaurant, Combustible, Viajes, Entretenimiento, Salud, Indumentaria, Servicios, E-commerce, Transferencia
- **Período:** Enero-Diciembre 2024

## Para el docente
Dos bloques bien diferenciados: 1h de GroupBy/pivots + 1h de time series. El gráfico de media móvil suele ser el momento "wow" de la clase.
