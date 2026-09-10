# Programación para el Análisis de Datos

**Maestría en Fintech · ITBA · 2026**

Repositorio del curso. Acá viven los notebooks de las seis clases y los datasets con los que
trabajamos. Todo corre en Google Colab: no hace falta instalar nada.

---

## Cómo usar este repo

Cada clase tiene su notebook. Hacés click en el badge y se abre en Colab, listo para ejecutar.
Los datasets se descargan solos desde este mismo repositorio — **no tenés que subir ningún archivo**.

> Si querés guardar tus cambios, en Colab andá a *Archivo → Guardar una copia en Drive*.
> Si trabajás sobre el notebook original, tus modificaciones se pierden al cerrar.

---

## Clases

| # | Tema | Notebook | Dataset |
|---|------|----------|---------|
| 1 | El ciclo del dato a la decisión | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/camilojaure/itba-pad/blob/main/Clase%201/Clase_1_Intro.ipynb) [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/camilojaure/itba-pad/blob/main/Clase%201/Clase_1_EstructurasDatos.ipynb) | Churn bancario (externo) |
| 2 | Tu primer análisis de datos | **Repaso** [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/camilojaure/itba-pad/blob/main/Clase%202/Clase_2_Repaso_Python.ipynb) · **Guiada** [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/camilojaure/itba-pad/blob/main/Clase%202/Clase_2_Practica_Guiada.ipynb) · **Individual** [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/camilojaure/itba-pad/blob/main/Clase%202/Clase_2_Practica_Individual.ipynb) | `clientes.csv` |
| 3 | Segmentación y series de tiempo | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/camilojaure/itba-pad/blob/main/Clase%203/Clase_3_Segmentacion_TimeSeries.ipynb) | `transacciones.csv` |
| 4 | Joins: combinando fuentes | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/camilojaure/itba-pad/blob/main/Clase%204/Clase_4_Joins.ipynb) | `clientes` + `tarjetas` + `transacciones` |
| 5 | Datos reales = datos sucios | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/camilojaure/itba-pad/blob/main/Clase%205/Clase_5_Datos_Sucios.ipynb) | `transacciones_sucias.csv` |
| 6 | Evaluación y cierre | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/camilojaure/itba-pad/blob/main/Clase%206/Clase_6_Examen.ipynb) | `portafolio_prestamos.csv` |

---

## Los datos

Todos los datasets representan la misma fintech argentina ficticia y comparten claves entre sí,
así que se pueden combinar. Son sintéticos: no hay información real de ninguna persona.

| Archivo | Filas | Descripción |
|---|---|---|
| `clientes.csv` | 1.000 | Cartera de clientes: segmento, provincia, balance, churn |
| `tarjetas.csv` | 1.534 | Tarjetas emitidas, con su límite y fecha de emisión |
| `transacciones.csv` | ~29.000 | Movimientos de 2024, con categoría de gasto y monto |
| `transacciones_sucias.csv` | ~29.900 | La misma tabla, degradada a propósito: nulos, duplicados, outliers |
| `portafolio_prestamos.csv` | 800 | Cartera de préstamos con estado de mora (Clase 6) |

```
clientes (cliente_id)
    └── tarjetas (tarjeta_id → cliente_id)
            └── transacciones (transaccion_id → tarjeta_id, cliente_id)
clientes (cliente_id)
    └── portafolio_prestamos (prestamo_id → cliente_id)
```

Para levantarlos desde cualquier notebook:

```python
DATOS = 'https://raw.githubusercontent.com/camilojaure/itba-pad/main/datasets/'
df = pd.read_csv(DATOS + 'clientes.csv')
```

---

## Bibliografía

- McKinney, W. (2022). *Python for Data Analysis* (3ra ed.). O'Reilly.
- VanderPlas, J. (2023). *Python Data Science Handbook* (2da ed.). O'Reilly.

---

*Docente: Camilo Jaureguiberry*
