# Clase 5 — Datos reales = datos sucios

**Tipo:** Teórico-práctica | **Duración:** 3 horas

## Objetivo

Que el alumno entienda que limpiar datos es tomar decisiones de negocio y no aplicar una receta, y que pueda correr un checklist
de diagnóstico, tratar duplicados, texto inconsistente, montos imposibles y nulos justificando cada decisión, y medir cuánto
movió el resultado.

## Estructura

| Bloque | Qué pasa | Tiempo |
|---|---|---|
| Apertura | Recap de la Clase 4 y la pregunta del día: $1.774 M o $2.018 M | 10 min |
| **1 · Teoría** | Por qué se ensucian los datos, seis dimensiones, nulos, outliers, ruido. Colab cerrado | 25 min |
| **2 · Práctica guiada** | Resolvemos `Clase_5_Practica_Guiada.ipynb` juntos | 75 min |
| — | Corte | 10 min |
| **3 · Práctica individual** | Resuelven `Clase_5_Practica_Individual.ipynb` solos, con Gemini | 50 min |
| Cierre | Puesta en común de los ejercicios 5, 6 y 7 | 10 min |

## Contenido

**Negocio**
- Por qué los datos se ensucian: cada sistema nació para operar
- Las seis dimensiones de la calidad del dato
- Ningún dato es crudo: decisiones defendibles, documentadas y medidas
- Nulos: eliminar, imputar o dejar depende de la pregunta
- Outliers: ¿error o cliente grande? ¿Es normal *para este cliente*?
- ¿Es real o es ruido? Tasas sobre bases chicas

**Técnico**
- Checklist: `shape`, `dtypes`, `isna`, `duplicated`, `value_counts`, `describe`
- `drop_duplicates`, `duplicated(keep=False)`
- `str.strip`, `str.capitalize`, `replace`
- `quantile`, IQR, `groupby(...).transform('median')`
- `fillna` con el promedio del grupo y una columna que marca lo imputado

## Materiales

| Archivo | Descripción | ¿Se comparte? |
|---------|-------------|---|
| `Clase_5_Practica_Guiada.ipynb` | Recorrido que se hace en clase (8 pasos + recomendación) | Sí |
| `Clase_5_Practica_Individual.ipynb` | 10 ejercicios con celda de lectura de negocio + desafío `reporte_calidad` | Sí |
| `PAD-Clase-5-Datos-sucios.pdf` | Deck de la clase (15 slides) | Sí |
| `Lecturas_Clase_5.md` | Lecturas de la bibliografía, con links | Sí |
| `Soluciones_Clase_5.ipynb` | Soluciones, lectura esperada, criterios y tabla de números del dataset | **No — solo docente** |
| `Guion_Clase_5.md` | Guión completo, tiempos con hora de reloj y notas de dictado | Solo docente |
| `Deck_Clase_5_PARA_GAMMA.md` | Fuente del deck | Solo docente |
| `Clase_5_Datos_Sucios.ipynb` | Versión vieja, todo en una notebook. Reemplazada | No |
| `data/` | Copia local de `transacciones_sucias.csv` | Se descarga sola desde el repo |

## Dataset: `transacciones_sucias.csv`

Las mismas transacciones de las clases 3 y 4, degradadas a propósito:

- **869** filas duplicadas (mismo `transaccion_id`)
- Nulos: **7%** en `monto_ars`, **5%** en `categoria`, **4%** en `fecha`
- Texto inconsistente: **50** formas de escribir 10 categorías, **11** de escribir débito y crédito
- Montos en cero, negativos y **26 con ceros de más** (hasta $57,5 M)

| | TPV 2024 |
|---|---|
| Archivo sin limpiar | $2.018 M (+13,7%) |
| Receta de manual (borrar nulos y outliers por IQR) | $1.156 M (−34,9%) |
| Limpieza con criterio (la de la guiada) | $1.774 M |
| Tabla conciliada (`transacciones.csv`) | $1.774 M |

## Para el docente

1. **El Paso 7 de la guiada ("Tres analistas") es el remate y arranca a las 20:30 a más tardar.**
2. **El IQR del Paso 5b** marca 1.089 filas, casi todas Viajes y Transferencias legítimas: es el momento de *"lo grande es tu mejor cliente"*.
3. **La trampa de `monto > 0`** (Paso 5a) borra 2.026 nulos sin avisar: preguntar cuántas filas deberían quedar antes de correrla.

El detalle completo, con tiempos y frases de dictado, está en `Guion_Clase_5.md`.
