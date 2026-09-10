# ¿Quién se nos está yendo?

**Programación para el Análisis de Datos**

Clase 2 · Churn y tu primer análisis

Maestría en Fintech · ITBA · 2026

---

# Agenda de hoy

| Hora | Bloque | Tiempo |
|---|---|---|
| 19:00 | Apertura y cómo trabajamos de acá en adelante | 10' |
| 19:10 | **Repaso de Python** — notebook, despacio | 30' |
| 19:40 | **¿Qué es el churn?** — el problema antes que la métrica | 20' |
| 20:00 | **Práctica guiada** — la resolvemos juntos | 60' |
| **21:00** | **Corte** | **10'** |
| 21:10 | **Práctica individual** — la resolvés vos, con Gemini | 45' |
| 21:55 | Cierre y tarea | 5' |

> Todas las clases, de acá en adelante, tienen esta misma forma: teoría, guiada, individual.
> La parte individual es la que hace que el conocimiento quede.

---

# Repaso: los bloques básicos de Python

## Vamos a la notebook

`Clase_2_Repaso_Python.ipynb`

La clase pasada esto lo pasamos rápido, sobre el final. Hoy lo hacemos despacio.

**Clase → Objeto → Método**, y por qué en Python el dato trae sus acciones adentro.

> Treinta minutos. Después no volvemos.

---

# ¿Qué es el churn?

**Churn** (fuga, *attrition*) es la pérdida de un cliente. Suena obvio hasta que hay que marcarlo en una base.

- El que **cerró la cuenta** formalmente → sí
- El que **no cerró nada**, pero hace 8 meses que no opera → ¿?
- El que dejó **$500 para no cerrarla**, pero cobra el sueldo en otro banco → ¿?

> **En servicios financieros casi nadie se despide. Se va sin avisar.**

Por eso el churn no es un dato que te viene dado: es **una definición que alguien tuvo que tomar**.

Y importa como pocas métricas: retener cuesta una fracción de lo que cuesta adquirir, y en una billetera el cliente que se va no avisa, no reclama y no vuelve.

---

# Definirlo es una decisión de negocio

No existe *la* definición correcta. Existe la que elegís y podés defender:

| Definición | Qué captura | Qué se le escapa |
|---|---|---|
| **Baja formal** | Certeza total | Llega tardísimo: ya no hay nada que hacer |
| **Sin actividad 90 días** | Detecta temprano | Confunde estacionalidad con fuga |
| **Caída sostenida de saldo** | Anticipa la salida | Difícil de definir sin ambigüedad |
| **Dejó de ser banco principal** | Lo que de verdad importa | Requiere datos que no siempre tenés |

**El eje sobre el que se para toda definición:**

**Conservadora** (baja formal) → certeza, pero llegás tarde
**Temprana** (sin actividad) → accionable, pero con falsos positivos — y un falso positivo es plata regalada en beneficios a alguien que no se pensaba ir

> Cambiar la ventana de 90 a 180 días puede **duplicar o partir al medio** tu tasa de churn.
> El negocio no cambió. Cambió la definición.
> **La primera pregunta ante cualquier tasa de churn no es cuánto da: es cómo la definiste.**

---

# ¿Y qué se hace con el dato?

Medir el churn no sirve de nada si no cambia una decisión. Los cuatro usos reales:

| Uso | La pregunta que responde | Qué se hace |
|---|---|---|
| **Diagnóstico** | ¿Qué segmento se está yendo? | Cortar la tasa por segmento, antigüedad y canal |
| **Anticipación** | ¿Quién se va a ir el mes que viene? | Un score de propensión sobre señales tempranas |
| **Retención** | ¿A quién llamamos con qué presupuesto? | Priorizar por **valor en riesgo**, no por tasa |
| **Producto** | ¿Por qué se van? | Atacar la causa: onboarding, comisiones, fricción |

**Cómo se gestiona en la práctica**

- **Segmentar siempre.** *"La cartera tiene 20% de churn"* no habilita ninguna decisión. *"38% en Joven y 7% en Premium"* son dos problemas distintos, con dos causas y dos soluciones
- **Separar al que nunca se activó.** Abrió por una promo y jamás usó la cuenta: eso no es churn, es una adquisición que nunca terminó de ocurrir. En la misma bolsa, tu métrica mide dos fenómenos y no podés actuar sobre ninguno
- **Mirar la ventana de riesgo.** Casi siempre está en los primeros meses. Retención pareja sobre toda la base es presupuesto tirado
- **Ordenar por plata, no por porcentaje.** El segmento que más fuga puede ser el que menos valor pone en riesgo

> Hoy vamos a hacer los dos primeros con código, y el cuarto va a ser el remate de la clase.

---

# Práctica guiada

## Vamos a la notebook

`Clase_2_Practica_Guiada.ipynb`

**1.000 clientes de una fintech argentina.** La pregunta: *¿qué tipo de cliente tiene más probabilidad de irse?*

El recorrido: **cargar → explorar → filtrar → medir → ver**, y cerrar con una recomendación.

> Antes de escribir una sola línea: **`Archivo` → `Guardar una copia en Drive`.**

---

# Antes de ejecutar: hacé tu copia

## Práctica individual — `Clase_2_Practica_Individual.ipynb`

La notebook que comparto es **el original del curso**. Si escribís ahí, se pisan entre todos y se pierde el trabajo.

**Los tres pasos, siempre, con cualquier notebook:**

1. Menú **`Archivo`** → **`Guardar una copia en Drive`**
2. Se abre una pestaña nueva que dice *Copia de...* — **esa es la tuya**
3. Clic en el nombre, arriba a la izquierda → renombrala **`Clase2_Individual_TuNombre`**

Y recién ahí, ejecutá. Cerrá la pestaña del original.

> **Es el mismo reflejo que "Guardar como" antes de tocar el Excel compartido del equipo.** Nadie edita el original.
> Tu copia queda en tu Drive, carpeta `Colab Notebooks`, y se guarda sola.

**Las reglas del bloque:** una pregunta por vez · cada ejercicio cierra con una línea de lectura de negocio · **Gemini es copiloto, no piloto** — pedile sintaxis y que te explique errores, nunca criterio ni conclusiones.
