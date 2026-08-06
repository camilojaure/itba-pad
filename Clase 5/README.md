# Clase 5 — Datos reales = datos sucios

**Tipo:** Teórico-práctica | **Duración:** 3 horas

## Objetivo
Que el alumno sepa detectar y tratar los problemas más comunes en datos reales: nulos, duplicados, inconsistencias de texto y outliers.

## Contenido
- Checklist de diagnóstico: el primer paso siempre es explorar
- Nulos: detectar, eliminar, imputar — cuándo hacer cada cosa
- Duplicados: detección y eliminación
- Inconsistencias en texto: normalización
- Outliers: IQR, percentiles, winsorizing
- EDA antes vs después de la limpieza

## Materiales
| Archivo | Descripción |
|---------|-------------|
| `Clase_5_Datos_Sucios.ipynb` | Notebook con código guiado + 10 ejercicios |
| `data/transacciones_sucias.csv` | Dataset con nulos, duplicados, outliers y texto inconsistente |

## Dataset: `transacciones_sucias.csv`
El mismo dataset de transacciones pero con problemas introducidos deliberadamente:
- **7%** de nulos en `monto_ars`
- **5%** de nulos en `categoria`
- **4%** de nulos en `fecha`
- **~3%** de filas duplicadas
- Outliers extremos (valores negativos, cero, millones)
- Inconsistencias en `categoria` (mayúsculas mezcladas) y `tipo` (variantes de 'crédito')

## Para el docente
La idea fuerza de esta clase: "la decisión de qué hacer con un nulo NO es técnica, es de negocio". Repetila varias veces. El ejercicio 10 (función `reporte_calidad`) es reutilizable — los alumnos que lo hagan bien tienen una herramienta real para llevar a su trabajo.
