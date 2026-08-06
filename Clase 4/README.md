# Clase 4 — Joins: combinando fuentes de datos

**Tipo:** Teórico-práctica | **Duración:** 3 horas

## Objetivo
Que el alumno pueda unir múltiples tablas relacionadas y construir una tabla analítica completa para responder preguntas de negocio.

## Contenido
- Por qué existen múltiples tablas (modelo relacional básico)
- Tipos de join: inner, left, right, outer — con analogía visual
- `pd.merge()` y `pd.concat()`
- Joins en cadena: unir 3 tablas paso a paso
- Análisis sobre la tabla combinada

## Materiales
| Archivo | Descripción |
|---------|-------------|
| `Clase_4_Joins.ipynb` | Notebook con código guiado + 10 ejercicios |
| `data/clientes.csv` | 1.000 clientes |
| `data/tarjetas.csv` | 1.534 tarjetas (los clientes pueden tener más de una) |
| `data/transacciones.csv` | ~29.000 transacciones |

## Relación entre tablas
```
clientes (cliente_id) ──< tarjetas (cliente_id / tarjeta_id) ──< transacciones (tarjeta_id)
```

## Para el docente
El diagrama de relación entre tablas es clave para que entiendan el modelo antes de escribir código. Dibujalo en pantalla antes de empezar. El ejercicio 10 (clientes valiosos en riesgo) es el cierre ideal.
