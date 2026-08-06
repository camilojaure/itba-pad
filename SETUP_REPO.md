# Cómo publicar el repo (5 minutos, una sola vez)

Todo está preparado para el repo `camilojaure/itba-pad`. Si vas a usar otro nombre de
usuario o de repo, cambialo primero (ver el último punto).

## 1. Crear el repo en GitHub

En github.com → **New repository**:

- Nombre: `itba-pad`
- Visibilidad: **Public** ← obligatorio. Si es privado, las URLs de los datasets
  devuelven 404 y a los alumnos no les carga nada.
- No tildes "Add a README" — ya hay uno acá.

## 2. Subir todo

Desde una terminal, parada en esta carpeta:

```bash
cd "/Users/camilojaureguiberry/Documents/Work/ITBA/PAD"

git init
git add .
git commit -m "Curso PAD - Maestría en Fintech ITBA 2026"
git branch -M main
git remote add origin https://github.com/camilojaure/itba-pad.git
git push -u origin main
```

Antes de pushear, corré `git status` y mirá la lista. El `.gitignore` ya excluye
los guiones de clase, los deck outlines, el analítico, las soluciones y la clave del
examen. Si ves alguno de esos archivos en la lista de "to be committed", frená.

## 3. Verificar que funciona

Abrí en el navegador:

```
https://raw.githubusercontent.com/camilojaure/itba-pad/main/datasets/clientes.csv
```

Si ves el CSV en texto plano, ya está: los notebooks van a cargar solos. Si ves un 404,
o el repo quedó privado o el nombre no coincide.

Después probá un badge de Colab del README, ejecutá la primera celda y confirmá que
carga el dataset.

## 4. Si usás otro nombre de repo

La URL aparece en tres lugares. Buscá y reemplazá `camilojaure/itba-pad`:

- `README.md` — badges de Colab y ejemplo de carga
- `Clase 2..6/*.ipynb` — la constante `DATOS` arriba de cada celda de carga
- Este archivo

```bash
grep -rl "camilojaure/itba-pad" . --include=*.ipynb --include=*.md
```

---

## Dos cosas a tener en cuenta

**Clase 1 depende de un repo ajeno.** El notebook de churn lee de
`raw.githubusercontent.com/YBI-Foundation/Dataset/...`, que no controlás vos. Funciona hoy,
pero si esa gente lo borra o lo renombra, la demo de la primera clase se cae. Cuando puedas,
bajá ese CSV y subilo a `datasets/` para no depender de terceros.

**Las soluciones están ignoradas a propósito.** Los `Soluciones_Clase_*.ipynb` no se
publican mientras el `.gitignore` los liste. Para liberarlas al cierre del curso, borrá esa
línea del `.gitignore` y hacé commit.
