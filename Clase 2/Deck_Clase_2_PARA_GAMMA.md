# ¿Quién se nos está yendo?

**Programación para el Análisis de Datos**
Clase 2 — ¿Quién se nos está yendo?

Del problema de negocio al primer análisis

Maestría en Fintech · ITBA · 2026

---

# Cómo trabajamos de acá en adelante

Todas las clases tienen la misma forma:

| | Bloque | Qué pasa |
|---|---|---|
| **1** | **Teoría** | El problema de negocio primero. Colab cerrado. |
| **2** | **Práctica guiada** | Resolvemos una notebook juntos, paso a paso. |
| **3** | **Práctica individual** | La resolvés vos, con Gemini al lado. |

> La parte 3 es la que hace que el conocimiento quede. Las partes 1 y 2 la preparan.

---

# REPASO · Los bloques básicos de Python

La clase pasada esto lo pasamos rápido, sobre el final.

Hoy lo hacemos despacio, porque es la base de todo lo que sigue.

> Veinte minutos. Después no volvemos.

---

# Una variable es un nombre con un valor adentro

```
nombre  = "Ana García"     # str   → texto
edad    = 34               # int   → número entero
balance = 250000.75        # float → número con decimales
activo  = True             # bool  → verdadero o falso
```

**El tipo define qué podés hacer con el valor.** Es la única regla que importa hoy.

| | Con números | Con texto |
|---|---|---|
| `+` | suma: `34 + 1` → `35` | pega: `"Ana" + " García"` → `"Ana García"` |

---

# Una lista es una columna

```
balances  = [250000, 89000, 430000, 12000]
segmentos = ["Premium", "Joven", "Retail", "PyME"]
```

Si una variable guarda un valor, una lista guarda muchos.
Es lo más parecido a una columna de Excel.

> Para sacar un elemento se usa su posición: `balances[0]`.
> **La primera posición es la 0, no la 1.**

---

# Los métodos son las fórmulas de Python

En Excel escribís una fórmula alrededor del dato.
En Python el dato ya trae sus acciones adentro, y las llamás con un punto.

| Lo que querés hacer | Excel | Python |
|---|---|---|
| Promedio de una columna | `=PROMEDIO(A:A)` | `df["balance"].mean()` |
| Contar valores | `=CONTAR(A:A)` | `df["balance"].count()` |
| Valor máximo | `=MAX(A:A)` | `df["balance"].max()` |
| Texto en mayúsculas | `=MAYUSC(A1)` | `nombre.upper()` |

> `objeto.método()` — esa notación se repite en todo lo que vamos a hacer.

---

# Una librería es código que ya escribió otro

Nadie programa el promedio desde cero.

```
import pandas as pd
```

Esa línea trae **pandas**, la librería para trabajar con tablas. Se escribe una sola
vez, al principio, y se le pone un apodo corto para no repetir el nombre completo.

---

# De listas sueltas a una tabla

pandas toma las listas y arma con ellas un **DataFrame**: una tabla.
Cada lista es una columna. Cada fila es un cliente.

| segmento | balance | churn |
|---|---|---|
| Premium | 250.000 | 0 |
| Joven | 12.000 | 1 |
| Retail | 38.000 | 0 |
| PyME | 215.000 | 0 |

Y los métodos siguen funcionando, ahora sobre la columna entera:

```
df["churn"].mean()   →   0.25
```

> Ese número es la **tasa de churn**. Con cuatro clientes no dice nada.
> En un rato lo calculamos sobre mil, y ahí sí vamos a poder decidir algo.

---

# La pregunta de hoy

> ### *¿Qué tipo de cliente tiene más probabilidad de irse?*

Para responderla hace falta código.
Pero antes hace falta algo más difícil: **ponerse de acuerdo en qué significa "irse".**

---

# Churn: el problema antes que la métrica

**Churn** (fuga, *attrition*) es la pérdida de un cliente.

Suena obvio hasta que hay que marcarlo en una base:

- El que cerró la cuenta formalmente → sí
- El que no cerró nada, pero hace 8 meses que no opera → ¿?
- El que dejó $500 para no cerrarla, pero cobra el sueldo en otro banco → ¿?

> En servicios financieros casi nadie se despide. **Se va sin avisar.**

---

# Definir el churn es una decisión de negocio

No existe *la* definición correcta. Existe la que elegís y podés defender:

| Definición | Qué captura | Qué se le escapa |
|---|---|---|
| **Baja formal** | Certeza total | Llega tardísimo: ya no hay nada que hacer |
| **Sin actividad 90 días** | Detecta temprano | Confunde estacionalidad con fuga |
| **Caída sostenida de saldo** | Anticipa la salida | Difícil de definir sin ambigüedad |
| **Dejó de ser banco principal** | Lo que de verdad importa | Requiere datos que no siempre tenés |

> Cambiar la ventana de 90 a 180 días puede **duplicar o partir al medio** tu tasa de churn.
> El negocio no cambió. Cambió la definición.

---

# El costo de elegir mal

Toda definición se para en algún lugar de este eje:

**Conservadora** (baja formal) → certeza, pero **llegás tarde**
**Temprana** (sin actividad) → accionable, pero **falsos positivos**

Y un falso positivo no es gratis:

> Le mandás una campaña de retención con beneficios a alguien
> que no se pensaba ir. Eso es plata regalada, y a escala es mucha plata.

**La primera pregunta ante cualquier tasa de churn no es cuánto da. Es cómo la definiste.**

---

# Por qué se van

Rara vez es un solo motivo. Los grandes grupos:

- **Precio y comisiones** — encontraron algo más barato
- **Experiencia** — la app se cae, el trámite es imposible, nadie atiende
- **Ciclo de vida** — se mudó, cambió de trabajo, cerró la PyME
- **Competencia** — una billetera le dio lo mismo con menos fricción
- **Nunca se activó** — abrió por una promo y jamás la usó

> El último grupo es enorme en fintech argentina, y **no es churn**:
> es una adquisición que nunca terminó de ocurrir.
> Si va en la misma bolsa, tu métrica mide dos fenómenos distintos y no podés actuar sobre ninguno.

---

# Segmento: por qué el promedio miente

Un banco no le habla igual a todos. Agrupa por comportamiento y valor:

| Segmento | Perfil típico |
|---|---|
| **Premium** | Alto saldo, varios productos, sensible al servicio |
| **Retail** | Masivo, ticket bajo, sensible al precio |
| **PyME** | Empresa chica, opera fuerte, necesita crédito |
| **Joven** | Poco saldo hoy, alto potencial, muy digital |

**"La cartera tiene 20% de churn"** → no habilita ninguna decisión.
**"38% en Joven y 7% en Premium"** → son dos problemas distintos, con dos causas y dos soluciones.

---

# Lo que vamos a mirar hoy

**1.000 clientes de una fintech argentina**

| Campo | Descripción |
|---|---|
| `segmento` | Premium / Retail / PyME / Joven |
| `edad`, `provincia` | Perfil demográfico |
| `nombre` | Nombre del cliente |
| `balance_ars` | Saldo en cuenta |
| `antiguedad_años` | Años como cliente |
| `cant_productos` | Productos contratados |
| `cliente_activo` | Si opera actualmente |
| `churn` | 1 = se fue · 0 = se quedó |

> Acá `churn` **ya viene calculado**: alguien tomó esa decisión antes que vos.
> En tu trabajo, tomarla va a ser parte del trabajo.

---

# Parte 2: Práctica guiada

**Regla número uno antes de tocar nada:**

### Archivo → Guardar una copia en Drive

- El notebook que comparto es **el original**: no se edita
- Cada uno trabaja sobre **su propia copia**, en su propio Drive
- Renombrala: `Clase2_Guiada_TuNombre`
- Si escriben sobre el original, se pisan entre todos y se pierde el trabajo

> Es el equivalente a "Guardar como" antes de romper el Excel del equipo.

---

# El recorrido de hoy

Cinco movimientos, siempre los mismos, en cualquier análisis:

1. **Cargar** — traer los datos a la sesión
2. **Explorar** — ¿qué hay acá? ¿cuántas filas? ¿de qué tipo?
3. **Filtrar** — quedarme con el subconjunto que me interesa
4. **Medir** — estadísticas que respondan la pregunta
5. **Ver** — un gráfico que comunique lo que el número solo no comunica

> No es una receta de Python. Es el orden en que se piensa un análisis.

---

# Idea 1: el DataFrame es la tabla

Todo lo de hoy pasa sobre un solo objeto: **el DataFrame**.

- Es una tabla: filas × columnas, igual que una hoja de Excel
- Vive en memoria, no en pantalla: lo pedís y te muestra lo que necesitás
- Todo lo que hacemos tiene la misma forma: **`objeto.método()`**

> Excel: `=PROMEDIO(A:A)` — le pasás el rango a la fórmula.
> Python: `df['balance'].mean()` — el método va pegado al objeto.
> Es la misma idea con el orden invertido.

---

# Idea 2: filtrar es escribir una condición

En Excel el filtro es un clic. En Python es una **condición escrita**.

- La condición se evalúa fila por fila y devuelve verdadero o falso
- Te quedás solo con las filas verdaderas
- **Y** / **O** se combinan para preguntas más finas

**Qué se gana con escribirlo:** el filtro queda registrado, es reproducible,
se puede revisar y nadie tiene que adivinar qué clics hiciste hace tres meses.

---

# Idea 3: promedio y mediana, siempre los dos

| | Qué es | Cuándo engaña |
|---|---|---|
| **Promedio** | Suma dividida cantidad | Un cliente con $10M lo mueve para todos |
| **Mediana** | El valor del medio | Casi nunca — por eso es el contraste |

En carteras financieras las distribuciones son **asimétricas**: muchos chicos, pocos enormes.

> Si el promedio es mucho mayor que la mediana, "el cliente promedio" no existe.
> Reportar solo el promedio en ese caso no es un error de cálculo: es un error de comunicación.

---

# Idea 4: agrupar es comparar

La pregunta interesante casi nunca es *"¿cuánto da?"*. Es *"¿cuánto da acá versus allá?"*

- Agrupar = partir la cartera según una columna y medir cada parte
- Es el corazón del análisis de datos, y lo vemos a fondo en la **Clase 3**
- Hoy alcanza con verlo funcionar

> Tasa de churn por segmento, balance promedio por tipo de cliente:
> el mismo dato, partido, empieza a decir algo que el total ocultaba.

---

# Idea 5: el gráfico se lee, no se hace

El código del gráfico lo escribe Gemini en 10 segundos. Lo que no escribe es la lectura.

Ante cualquier gráfico, tres preguntas:

- **¿Qué forma tiene?** ¿Simétrica, con cola, con dos picos?
- **¿Es lo que esperaba?** Si no, ¿el dato está mal o mi supuesto estaba mal?
- **¿Qué decisión cambia?** Si ninguna, el gráfico no era necesario

---

# El caso: ¿qué le decimos al gerente de retención?

Tres preguntas, y con eso se arma la recomendación:

1. ¿Cuál es la **tasa de churn global**?
2. ¿Qué **segmento** concentra la fuga?
3. ¿El **perfil** de quien se va es distinto al de quien se queda?

**El cierre no es una tabla. Son tres bullets:**

> **Problema** — se fue el X% de la cartera
> **Foco** — el segmento [X] fuga Y%, N veces el promedio
> **Perfil** — quien se va tiene $Z de balance, [mayor/menor] que quien se queda

Análisis = **datos + interpretación + recomendación**. Sin el tercero, es un reporte.

---

# Parte 3: ahora lo hacés vos

**Notebook de Práctica Individual** — mismo dataset, preguntas nuevas.

**Cómo se trabaja:**

1. Guardá **tu propia copia** en Drive (igual que antes)
2. Respondé pregunta por pregunta, de a una
3. **Gemini es tu copiloto** — pedile sintaxis, no criterio
4. Cada respuesta cierra con una línea de lectura de negocio, no con un número

> Si Gemini te da un resultado que no tiene sentido para el negocio,
> el problema casi nunca es el código: es la pregunta.

---

# Cómo pedirle bien a Gemini

**Prompt pobre:**
> *"hacé un gráfico de churn"*

**Prompt útil:**
> *"Tengo un DataFrame de pandas llamado `df` con las columnas `segmento`, `balance_ars` y `churn` (1 = se fue). Calculá la tasa de churn por segmento y mostrala en un gráfico de barras horizontal ordenado de mayor a menor."*

**La diferencia:** contexto + qué datos tenés + qué querés + cómo lo querés ver.

> Y siempre, siempre: leé el código antes de ejecutarlo. Si no entendés una línea, preguntá qué hace.

---

# Qué viene en la Clase 3

**Dataset:** ~29.000 transacciones con fecha, categoría y monto

**Pregunta:** ¿Cómo evolucionó el negocio mes a mes? ¿Qué categorías crecieron?

**Herramientas nuevas:** GroupBy a escala · Series de tiempo · Promedios móviles

> De 1.000 filas que entran en una pantalla, a 29.000 que no.
> Ahí es donde Excel empieza a quedarse corto y esto empieza a valer la pena.
