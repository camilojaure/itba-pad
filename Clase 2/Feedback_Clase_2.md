---
tipo: feedback_clase
curso: "FIN.06 (20262Q) - Programación para el Análisis de Datos"
clase: 2
fecha_clase: "2026-09-10"
fuente: "audio_transcript.VTT (transcripción con hablantes) + timeline.JSON de la grabación de Class"
fecha_analisis: "2026-09-21"
---

# Feedback — Clase 2 (10 de septiembre de 2026)

## Datos duros

| Métrica | Valor |
|---|---|
| Duración | 02:52:30 — terminaste ~8 minutos antes |
| Intervenciones transcritas | 1.419 |
| Palabras totales | ~23.300 |
| Palabras tuyas | 20.362 (**87%**, contra 80% en la Clase 1) |
| Personas que hablaron | 25 en la transcripción (vos + 24 alumnos); el timeline suma 3 más con micrófono activo pero sin texto (Bosio, Cardenas Ruiz, A. González) |
| Alumnos que no aparecen | 9 de 36 |
| Alumno con más intervenciones | Gallardo (44), seguido de Meneses y Hergenreder (37 cada uno) |

### Reparto de la palabra por tramo

| Tramo | Vos | Total | Tu % |
|---|---|---|---|
| 00:00 | 1.993 | 2.493 | 80% |
| 00:15 | 1.992 | 2.193 | 91% |
| 00:30 | 2.028 | 2.206 | 92% |
| 00:45 | 2.466 | 2.466 | 100% |
| 01:00 | 2.006 | 2.390 | 84% |
| 01:15 | 2.214 | 2.368 | 93% |
| 01:30 | 1.926 | 2.178 | 88% |
| 01:45 | 2.188 | 2.201 | 99% |
| 02:00 | 1.643 | 1.683 | 98% |
| 02:15 | 624 | 714 | 87% |
| 02:30 | 543 | 1.162 | 47% |
| 02:45 | 739 | 1.207 | 61% |

### Cómo se usó el tiempo

| Bloque | Guion | Real |
|---|---|---|
| Termómetro de la Clase 1 + reglas de evaluación | — | 00:00–00:14 (14') |
| Repaso de Python | 20' | 00:14–00:55 (**41'**) |
| Teoría de churn | 15' | 00:55–01:09 (14') |
| Práctica guiada | 85' | 01:09–02:09 (**60'**) |
| Break | 15' | 02:10–02:20 (10') |
| Práctica individual | 30' de trabajo | 02:22–02:39 (**~17'**) |
| Puesta en común | 7' | 02:39–02:51 (12') |

## Los tres hallazgos

### 1. El repaso duró el doble y lo pagó la práctica individual

El guion le daba 20 minutos al repaso de Python y avisaba: *"si el bloque se estira, recortar los
ejemplos de churn, no el repaso"*. Duró **41 minutos** (00:14 a 00:55). La teoría de churn salió en
tiempo (14'), así que el costo se trasladó para abajo: la guiada tuvo 60' de 85', y la individual
quedó en unos **17 minutos de trabajo** (lo anunciaste a las 02:24: *"tómense unos 20 min"*).

El README dice que **la práctica individual no se recorta**. Fue el bloque más recortado de la clase.

### 2. El remate de la clase no llegó

El dataset está construido para que el ranking por tasa de churn sea el inverso del ranking por
balance en riesgo (Premium $29,6M > Retail > PyME > Joven $5,9M). El guion lo pone como cierre
de la puesta en común. **No aparece en la transcripción: cero menciones a "riesgo".**

Lo más cerca que se llegó fue churn por segmento (Joven casi 40%), a las **02:06**, en los últimos
tres minutos de la guiada. Queda la mitad del mensaje, la de "Joven es el problema", que es
justamente la conclusión que el remate estaba pensado para desarmar. En la Clase 3 tampoco se retomó.

### 3. Hablaste más que en la Clase 1, pero participaron más alumnos

Tu share subió de 80% a 87%, y entre 00:15 y 02:15 no bajaste del 84%. La participación estuvo
mejor distribuida: 24 alumnos hablaron al menos una vez (contra 7 que volvieron a hablar después de
presentarse en la Clase 1), y Gallardo bajó de 59 a 44 intervenciones.

Hubo dos momentos que funcionaron como estaban pensados:

- **01:03–01:07, la definición de churn.** Preguntaste cómo lo mide cada uno y salieron dos casos
  reales: Hergenreder (clientes que cobran el sueldo por obligación y vacían la cuenta hacia una
  billetera, un "churn encubierto") y Ponce (grandes empresas del BNA que pasan la recaudación a
  money market, y el banco empezó a bonificar tasa por saldo promedio).
- **02:39–02:51, la puesta en común.** Cuatro manos levantadas, tres presentaron (Hergenreder,
  Meneses, Biteznik). El tramo cayó a 47% tuyo. De ahí salió la mejor lectura de la clase:
  Hergenreder notó solo que la media lejos de la mediana indica sesgo por los balances altos (02:48).

## Otros puntos

- **Ritual de la copia: anunciado, no verificado.** Lo explicaste a las 01:12, sin chequeo activo
  ni convención de nombre. A las 01:34 Correa Argelaguet preguntó si editar la notebook te
  afectaba a vos, porque tenía *"miedo de romper algo"*: no la había copiado.
- **Tropiezos técnicos al cargar datos (01:15–01:32).** Meneses y Farinelo no podían correr la
  carga porque no habían ejecutado la celda de librerías. Lo resolvieron sus compañeros (Biteznik,
  Vazquez). Muradas armó mal la URL del repo y no pudo compartir pantalla.
- **Gemini tiene fricciones de cuenta.** Hubo preguntas sobre la cuota (Hergenreder), la cuenta
  personal contra la del ITBA (Gallardo, López Alonso) y los términos que hay que aceptar
  (Frangella). Repetto contó que con el mail educativo Gemini es gratis un año. Vale la pena ponerlo
  en una slide.
- **Anunciaste un formato de evaluación que no coincide con el repo.** A las 00:07 dijiste que la
  última clase, en su primera mitad, tiene un **multiple choice teórico sobre lo que está en los
  slides**. El repo define la Clase 6 como examen práctico con `portafolio_prestamos.csv`.
  *Resuelto (21/9):* el examen es multiple choice; la idea es que las preguntas se respondan con
  números que salen de una notebook. Falta actualizar el repo.
- **Media ≈ mediana no es normal.** A las ~01:38 leíste la edad como "normalmente distribuida"
  porque la media (40) y la mediana (41) son parecidas. A las 02:04 el histograma mostró que es
  **bimodal** (Joven ~23 y Premium ~52). Es un buen contraejemplo para la Clase 5.
- **No se hizo el recap de la tarea de la Clase 1** (la pregunta que le harían a los datos de su
  empresa) ni la aclaración de que el dataset de la demo de Kaggle es otro.
- **El termómetro de apertura funcionó.** Coronel, Carlucci y Nuñez Dominguez dieron feedback de la
  Clase 1 en los primeros tres minutos, y los tres coincidieron en que el copiloto les baja la
  ansiedad.
- **Las celdas de Lectura quedaron vacías.** Hergenreder dijo que no escribió conclusiones *"porque
  prefería avanzar con el código"*. Biteznik tampoco las completó.

## Qué cambiaría

1. **Poner un corte fijo a la guiada.** Si a las 20:55 no terminó, se corta y se pasa a la
   individual. Lo que no se vio queda en la notebook.
2. **Recuperar el remate en la Clase 4.** Los joins parten de `clientes.csv`, así que balance en
   riesgo por segmento es un buen primer ejemplo de cruce.
3. **Avisarles que el examen cambia de forma.** Se anunció "sobre lo que está en los slides"; si
   va a pedir correr una notebook, conviene decirlo pronto.
4. **En la puesta en común, pedir la Lectura antes que el código.** Si el que presenta arranca por
   la conclusión, las celdas de lectura dejan de ser opcionales.

## Limitaciones de este análisis

- La transcripción es automática y comete errores de reconocimiento, sobre todo con nombres propios
  y términos técnicos ("Chern" por churn, "Geminay" por Gemini). Sirve para reconstruir estructura,
  tiempos y temas; no para citar textual.
- Los horarios de bloque se reconstruyeron a partir de frases de transición; tienen ±2 minutos de
  error.
- El conteo de palabras mide **cuánto se habló**, no la calidad de lo que se dijo.
- **No hablar no es lo mismo que faltar.** La asistencia real está en la solapa Asistencia de Class
  Campus.
