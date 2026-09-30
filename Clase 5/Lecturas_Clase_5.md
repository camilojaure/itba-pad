# Lecturas — Clase 5: Datos reales = datos sucios

**Programación para el Análisis de Datos · Maestría en Fintech · ITBA · 2026**

Qué leer para acompañar la clase. Las dos primeras son de la bibliografía obligatoria y están disponibles gratis en la web.

---

## Bibliografía obligatoria

**1. McKinney, W. (2022). *Python for Data Analysis* (3ra ed.). O'Reilly. — Capítulo 7: *Data Cleaning and Preparation***
🔗 https://wesmckinney.com/book/data-cleaning.html

- **Leer:** 7.1 *Handling Missing Data* (nulos: `isna`, `dropna`, `fillna`) y de 7.2 *Data Transformation*, las secciones
  *Removing Duplicates* y *Detecting and Filtering Outliers*
- **Opcional:** 7.4 *String Manipulation* (el `str.strip`, `str.lower` y compañía que usamos para normalizar texto)
- Es la versión web oficial y gratuita de la 3ra edición, escrita por el creador de pandas

**2. VanderPlas, J. *Python Data Science Handbook*. O'Reilly. — *Handling Missing Data***
🔗 https://jakevdp.github.io/PythonDataScienceHandbook/03.04-missing-values.html

- Explica cómo representa pandas los datos faltantes (`NaN`, `None`) y por qué una suma "ignora" los nulos sin avisar
- **Opcional:** [*Vectorized String Operations*](https://jakevdp.github.io/PythonDataScienceHandbook/03.10-working-with-strings.html), para normalizar texto
- La versión web gratuita corresponde a la 1ra edición; el capítulo es el mismo en la 2da (2023)

---

## Complementaria (si querés ir más allá)

**3. Peng, R. D. y Matsui, E. (2015). *The Art of Data Science*. Leanpub. — Capítulo 4: *Exploratory Data Analysis***
🔗 https://leanpub.com/artofdatascience

- El checklist de exploración (leer los datos, mirar la estructura, validar contra una fuente externa) de donde sale la idea de
  "diagnóstico antes que limpieza". El libro es pago en Leanpub

**4. Wickham, H. (2014). *Tidy Data*. Journal of Statistical Software, 59(10).**
🔗 https://www.jstatsoft.org/article/view/v059i10

- El artículo clásico sobre cómo tiene que estar organizada una tabla para poder analizarla. Gratuito. Los ejemplos están en R,
  pero las ideas valen para cualquier herramienta

**5. Documentación de pandas: *Working with missing data***
🔗 https://pandas.pydata.org/docs/user_guide/missing_data.html

- La referencia oficial, para consultar cuando Gemini te sugiere una función que no conocés

---

**Para la clase no hace falta leer todo.** Si tenés tiempo para una sola cosa, que sea la sección 7.1 de McKinney.
