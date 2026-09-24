---
tipo: feedback_clase
curso: "FIN.06 (20262Q) - Programación para el Análisis de Datos"
clase: 3
fecha_clase: "2026-09-17"
fuente: "audio_transcript.VTT (transcripción con hablantes) + timeline.JSON de la grabación de Class"
fecha_analisis: "2026-09-21"
---

# Feedback — Clase 3 (17 de septiembre de 2026)

## Datos duros

| Métrica | Valor |
|---|---|
| Duración | 02:30:17 — la clase arrancó a las 19:30, anunciado de antemano |
| Intervenciones transcritas | 1.168 |
| Palabras totales | ~17.200 |
| Palabras tuyas | 14.529 (**84%**) |
| Personas que hablaron | 17 (vos + 16 alumnos); el timeline coincide |
| Alumnos que no aparecen | **20 de 36** |
| Alumno con más intervenciones | Nuñez Dominguez (54), seguido de Correa Argelaguet (35) y Meneses (30) |

### Reparto de la palabra por tramo

| Tramo | Vos | Total | Tu % |
|---|---|---|---|
| 00:00 | 1.861 | 2.427 | 77% |
| 00:15 | 1.567 | 2.330 | 67% |
| 00:30 | 2.010 | 2.177 | 92% |
| 00:45 | 1.995 | 2.090 | 95% |
| 01:00 | 1.780 | 1.836 | 97% |
| 01:15 | 2.154 | 2.179 | 99% |
| 01:30 | 1.547 | 1.590 | 97% |
| 01:45 | 318 | 318 | 100% |
| 02:00 | 643 | 702 | 92% |
| 02:15 | 620 | 1.520 | 41% |
| 02:30 | 34 | 46 | 74% |

### Cómo se usó el tiempo

| Bloque | Guion | Real (tiempo de grabación) |
|---|---|---|
| Apertura: termómetro + TPV como P×Q + agenda | 10' | 00:00–00:13 (13') |
| Recap de la Clase 2 | (en la apertura) | 00:13–00:15 (~1') |
| Teoría de series de tiempo | 30' | 00:15–00:42 (27') |
| Práctica guiada | 75' | 00:42–01:40 (**58'**) |
| Corte | 10' | 01:41–01:47 (6') |
| Práctica individual | 37' | 01:48–02:18 (**30'**, con 5' de demo tuya en el medio) |
| Puesta en común | 10' | 02:18–02:29 (11') |

## Los dos hallazgos

### 1. La teoría fue el mejor bloque de las tres clases

Fue el único tramo del curso en que tu share bajó a **67%** fuera de una ronda de presentaciones o
de una puesta en común. La pregunta sobre tasa de rechazo (00:17) abrió una conversación de ocho
minutos entre gente que la vive a diario: Meneses (94% de aprobación en su procesador, análisis por
tipo de rechazo), Gutierrez (autorizador de Payway; presente rechaza menos que e-commerce),
Frangella (Newpay, transacciones que no son de pago, códigos de respuesta) y Borges (Carrefour,
*"de los dos lados del mostrador"*).

Las preguntas conceptuales las respondió el grupo: estacionalidad y *"enero contra enero"* (00:36),
el dólar oficial con cepo como variable rota (Borges, 00:31), la escala de los ejes (Hergenreder,
01:34), el eje secundario (Repetto, 01:37) y los `NaN` del promedio móvil (Golini y Biteznik,
01:33). La trampa de los pesos se entendió: Hergenreder la levantó solo al ver el resample (*"en
2024…"*, 01:31).

### 2. Por segunda clase seguida, se cayó el remate

Dentro de la guiada, el Paso 2 se abrió en una tangente de unos 20 minutos (00:58–01:19): scatter de
monto contra cantidad por categoría, análisis de cuadrantes y una pregunta sobre regresión. Lo
dijiste en el momento: *"demasiado tiempo con esto, lo sé"*. Desde ahí los pasos 3 a 7 entraron en
21 minutos. El promedio móvil, que el README marca como el momento "wow", duró unos 4.

El **Paso 8** (monto que se duplica mientras los clientes que operan caen de 781 a 727) no
apareció. En la puesta en común se mostraron los ejercicios 1 a 3, lo esperable con 30 minutos de
individual (la consigna es terminarla en casa). El problema es que el guion había puesto el
segundo remate en el ejercicio 10 (clientes que operan 902 → 785, −13%), que nadie llega a hacer
en clase.

Es el mismo patrón de la Clase 2: la conclusión que da sentido a la clase está al final, y es lo
primero que se pierde cuando algo se estira. Además, las dos conclusiones perdidas son la misma
idea vista desde dos tablas: **el crecimiento en pesos tapa una base de clientes que se achica.**

## Otros puntos

- **El ritual de la copia se relativizó en voz alta.** A las 00:45 dijiste *"no hace falta que sí o
  sí cambien el nombre"*, porque las notebooks se abren desde el repo. Es cierto que abiertas
  desde GitHub no se pisan entre ellos; el riesgo real es perder su trabajo. El guion y el
  CLAUDE.md todavía lo tratan como crítico. Conviene elegir una versión y alinear las dos.
- **Le robaste 5 minutos a la individual.** Entre 02:00 y 02:05 mostraste tu propio análisis de
  rechazos (línea de referencia, correlación con volumen semanal, outlier) mientras ellos
  trabajaban. Lo aclaraste: *"no distraer a los que están trabajando"*. El contenido está bueno;
  entra mejor en la puesta en común.
- **La puesta en común tuvo buen nivel.** Nuñez Dominguez leyó crédito contra débito, viernes y
  sábado como días pico y la recomendación de promos lunes y martes, y dijo que el heatmap no le
  permitía separar precio de cantidad. Correa Argelaguet midió capacidad de procesamiento por
  cantidad y no por monto, e hizo un segundo heatmap en cantidades. Esa es la separación
  precio/cantidad del ejercicio 5, a la que llegó solo.
- **Correa Argelaguet es el caso del curso.** No habló en la Clase 1, en la Clase 2 preguntó si iba
  a romper algo y en la Clase 3 fue el segundo más activo y presentó.
- **Dos alumnos de perfil gerencial dijeron que no se ven programando.** Carlucci siente que ahora
  puede *"saber lo que quiero pedir"*. Villanueva dijo que le cuesta seguir algunos temas y que le
  interesa saber qué pedirle a IT. Es una señal sobre una parte del público: para ellos, el
  ejercicio que más les sirve es escribir el pedido al analista, no el código.
- **20 alumnos no aparecen.** Entre ellos está Gallardo, el más participativo de las clases 1 y 2,
  que no figura ni en la transcripción ni en el timeline. Tampoco aparecen Muradas, De Luca,
  Aguilera ni Vazquez.
- **La advertencia del guion sobre Viajes se respetó.** Leíste los picos de julio y diciembre, sin
  prometer enero.

## Qué cambiaría para la Clase 4

1. **Que el remate lo dés vos, no un ejercicio.** Si en clase se llega a los primeros ejercicios,
   la conclusión no puede depender del último. Conviene que sea la última slide de la guiada o
   el cierre de la puesta en común, aunque nadie haya llegado.
2. **Abrir con el remate pendiente.** La Clase 4 es de joins y parte de `clientes.csv`. Cruzar las
   transacciones con clientes permite contestar las dos preguntas que quedaron abiertas: cuánto
   balance hay en riesgo por segmento (Clase 2) y quiénes son los clientes que dejan de operar
   (Clase 3). Da un hilo narrativo a las tres clases en diez minutos.
3. **Poner la conclusión antes de la tangente.** Si la guiada tiene un paso que no se recorta,
   conviene ponerle una hora de reloj en el guion, no solo la etiqueta.
4. **Decidir qué pasa con el ritual de la copia.**

## Limitaciones de este análisis

- La transcripción es automática y comete errores de reconocimiento, sobre todo con nombres propios
  y términos técnicos. Sirve para reconstruir estructura, tiempos y temas; no para citar textual.
- El conteo de palabras mide **cuánto se habló**, no la calidad de lo que se dijo.
- **No hablar no es lo mismo que faltar.** La asistencia real está en la solapa Asistencia de Class
  Campus.
