# Clase 4 — Joins: combinando fuentes de datos

**Tipo:** Teórico-práctica | **Duración:** 3 horas

## Objetivo

Que el alumno entienda por qué los datos de una empresa viven repartidos y qué valor hay en cruzarlos,
y que pueda unir tres tablas con `merge`, predecir cuántas filas tienen que salir, elegir entre `inner` y `left`
y armar una tabla con una fila por cliente.

## Estructura

| Bloque | Qué pasa | Tiempo |
|---|---|---|
| Apertura | Recap de la Clase 3 y las dos preguntas abiertas | 10 min |
| **1 · Teoría** | Datos repartidos, modelo relacional, vista 360, lo que no matchea, el error silencioso. Colab cerrado | 25 min |
| **2 · Práctica guiada** | Resolvemos `Clase_4_Practica_Guiada.ipynb` juntos | 75 min |
| — | Corte | 10 min |
| **3 · Práctica individual** | Resuelven `Clase_4_Practica_Individual.ipynb` solos, con Gemini | 50 min |
| Cierre | Puesta en común de los ejercicios 3, 5 y 7 | 10 min |

## Contenido

**Negocio**
- Por qué los datos viven repartidos: cada sistema nació para operar
- Claves y cardinalidad (uno a muchos): cuántas filas deberían salir
- La vista 360 del cliente
- Lo que no matchea es un hallazgo
- El error silencioso: filas que se multiplican

**Técnico**
- `pd.merge` con `on`, `how` (`inner` / `left`) y `validate`
- Encontrar lo que no matchea: `.isna()` después de un left, `indicator=True`
- Resumir antes de unir: `groupby` → `merge`, `fillna`
- `pd.concat` para apilar

## Materiales

| Archivo | Descripción | ¿Se comparte? |
|---------|-------------|---|
| `Clase_4_Practica_Guiada.ipynb` | Recorrido que se hace en clase (8 pasos + recomendación) | Sí |
| `Clase_4_Practica_Individual.ipynb` | 10 ejercicios con celda de lectura de negocio + desafío | Sí |
| `Soluciones_Clase_4.ipynb` | Soluciones, lectura esperada, criterios y tabla de números del dataset | **No — solo docente** |
| `Guion_Clase_4.md` | Guión completo, tiempos con hora de reloj y notas de dictado | Solo docente |
| `Deck_Clase_4_PARA_GAMMA.md` | Fuente del deck (14 tarjetas) | Solo docente |
| `Prompts_Gamma_Clase_4.md` | Prompts, tarjeta por tarjeta, para editar el deck en Gamma | Solo docente |
| `Deck_Outline_Clase_4.md` | Outline largo (22 slides), previo al rediseño | Solo docente |
| `Clase_4_Joins.ipynb` | Versión vieja, todo en una notebook. Reemplazada | No |
| `data/` | Copias locales de `clientes`, `tarjetas` y `transacciones` | Se descargan solas desde el repo |

## Relación entre tablas

```
clientes (cliente_id) ──< tarjetas (tarjeta_id, cliente_id) ──< transacciones (transaccion_id, tarjeta_id, cliente_id)
```

- 1.000 clientes · 2.110 tarjetas · 28.956 transacciones
- 50 clientes sin tarjeta · 45 con tarjeta y sin transacciones

## Para el docente

1. **El Paso 6 de la guiada es el remate y arranca a las 20:30 a más tardar.** Responde la pregunta abierta de la Clase 3:
   los clientes que operan bajan de 781 a 727, pero los que se quedan suben de 675 a 727. Toda la caída son clientes que se estaban yendo.
2. **El Paso 3 (el balance que da $25.693M en vez de $693M)** es el error del día. Preguntar cuál está bien antes de explicarlo.
3. **Ejercicio 8:** el 77% de churn con tarjeta inactiva es para desconfiar, no para celebrar.

El detalle completo, con tiempos y frases de dictado, está en `Guion_Clase_4.md`.
