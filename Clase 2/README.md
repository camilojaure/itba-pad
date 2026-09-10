# Clase 2 — ¿Quién se nos está yendo?

**Tipo:** Teórico-práctica | **Duración:** 3 horas

## Objetivo

Que el alumno entienda que **definir el churn es una decisión de negocio**, y que después pueda cargar
un dataset real, explorarlo, filtrarlo, medirlo y convertir el resultado en una recomendación.

## Estructura

| Bloque | Qué pasa | Tiempo |
|---|---|---|
| **1 · Teoría** | Repaso de Python (20') + qué es el churn y por qué el promedio miente (15'). | 35 min |
| **2 · Práctica guiada** | Resolvemos `Clase_2_Practica_Guiada.ipynb` juntos. | 85 min |
| — | Break | 15 min |
| **3 · Práctica individual** | Resuelven `Clase_2_Practica_Individual.ipynb` solos, con Gemini. | 45 min |

## Contenido

**Negocio**
- Churn: definirlo antes de medirlo, y el costo de cada definición
- Por qué se van los clientes — incluyendo el que nunca se activó
- Segmentación: por qué una tasa global no habilita ninguna decisión

**Técnico**
- Repaso: tipos de datos, listas, `objeto.método()`, librerías, de listas a DataFrame
- Pandas: `read_csv`, `.head()`, `.info()`, `.describe()`
- Selección de columnas y filtros (simples y compuestos)
- Estadísticas descriptivas: promedio vs mediana
- `groupby` como anticipo de la Clase 3
- Histogramas y gráficos de barras

## Materiales

| Archivo | Descripción | ¿Se comparte? |
|---------|-------------|---|
| `Clase_2_Repaso_Python.ipynb` | Repaso escalonado de tipos, listas, métodos y librerías. Se recorre al inicio | Sí |
| `Clase_2_Practica_Guiada.ipynb` | Recorrido resuelto que se hace en clase | Sí |
| `Clase_2_Practica_Individual.ipynb` | 10 ejercicios nuevos, para resolver solos | Sí |
| `Soluciones_Clase_2.ipynb` | Soluciones + lectura de negocio + criterios de corrección | **No — solo docente** |
| `Guion_Clase_2.md` | Guión completo, tiempos y notas de dictado | Solo docente |
| `Deck_Outline_Clase_2.md` | Outline del deck (20 slides) | Solo docente |
| `data/clientes.csv` | Dataset de 1.000 clientes | Se descarga solo desde el repo |

## Dataset: `clientes.csv`

- **Filas:** 1.000 clientes de una fintech argentina ficticia
- **Columnas:** `cliente_id`, `nombre`, `edad`, `provincia`, `segmento`, `antiguedad_años`,
  `balance_ars`, `cant_productos`, `cliente_activo`, `churn`
- **Pregunta de negocio:** ¿qué tipo de cliente tiene más probabilidad de irse?

Las notebooks descargan el CSV directamente desde el repositorio del curso — no hace falta subir nada a Colab.

## Para el docente

Tres cosas que definen si la clase sale bien:

1. **El Bloque 1 va con Colab cerrado.** Si se abre el notebook antes, la conversación de negocio no ocurre.
2. **El ritual de "Guardar una copia en Drive" se hace con chequeo activo** (Bloque 2.0 del guión).
   Si la mitad del grupo no lo hace, la Clase 3 arranca con notebooks pisadas.
3. **La práctica individual no se recorta.** Si falta tiempo, recortar visualizaciones de la guiada.

4. **El repaso de Python del inicio no se saltea.** En la Clase 1 los fundamentos quedaron para
   los últimos veinte minutos y se dieron apurados; sobre el cierre se les prometió retomarlos.
   Si el bloque 1 se estira, recortar los ejemplos de churn, no el repaso.

El detalle completo, con tiempos y frases de dictado, está en `Guion_Clase_2.md`.
