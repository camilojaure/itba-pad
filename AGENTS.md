# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

## Project Overview

This is the course material for **PAD (Programación para el Análisis de Datos)**, a 6-week module of ITBA's Fintech Master's program. The audience is finance/banking professionals (not engineers): they know Excel and SQL but have no prior Python experience. The pedagogical approach is problem-first, AI-assisted ("vibe coding"), delivered entirely in Google Colab — no local environment setup required.

There are no build, lint, or test commands. Everything runs in cloud Jupyter notebooks.

## Class Structure (from Clase 2 onwards)

Every class follows the same three-block shape. Announce it explicitly to students — knowing what to expect lowers the anxiety of people who don't come from programming.

| Block | What happens | Time |
|---|---|---|
| **1 · Teoría** | The business problem first. Colab closed. | ~35 min |
| **2 · Práctica guiada** | Work through a notebook together, step by step. | ~85 min |
| **3 · Práctica individual** | They solve a second notebook alone, with Gemini as copilot. | ~45 min |

**Saving a copy (softened from Clase 4 on):** students open the notebooks from the GitHub/Colab links, so nobody overwrites anybody. `Archivo → Guardar una copia en Drive` (named `Clase{N}_{Guiada|Individual}_TuNombre`) is only needed to keep their own work and finish the individual practice at home. Mention it in one sentence; no need to verify hand by hand.

## Course Directory Layout

Each class lives in its own directory (`Clase 1/` through `Clase 6/`) and contains:
- `README.md` — objectives, materials table, teacher guidance
- `Guion_Clase_N.md` — full teaching script with timings and delivery notes (teacher only)
- `Deck_Outline_Clase_N.md` — slide outline; `Deck_Clase_N_PARA_GAMMA.md` is the paste-ready version
- Notebooks (`.ipynb`) and a `data/` folder

**Deck principle:** the deck must NOT mirror the notebook. Code lives in the notebook; slides carry business concepts, reading criteria, and class structure. If a slide can be replaced by "look at cell 12", it doesn't belong.

**Class progression:**
| Class | Topic | Dataset(s) |
|-------|-------|-----------|
| 1 | Conceptual intro — data-to-decision cycle, Colab, AI as copilot | (none) |
| 2 | Churn as a business definition + basic Pandas — load, filter, describe, viz | `clientes.csv` |
| 3 | Aggregation & time series — GroupBy, pivot, datetime, rolling | `transacciones.csv` |
| 4 | Joins — merging multiple tables, relational model | `clientes.csv`, `tarjetas.csv`, `transacciones.csv` |
| 5 | Data quality — nulls, duplicates, outliers, normalization | `transacciones_sucias.csv` |
| 6 | Exam — novel dataset, integrates all prior skills | `portafolio_prestamos.csv` |

## Unified Dataset (Fictional Argentine Fintech)

All datasets represent the same fictional company and share keys for joins:

```
clientes (cliente_id) — 1,000 records
  Fields: cliente_id, nombre, edad, provincia, segmento, antiguedad_años,
          balance_ars, cant_productos, cliente_activo (bool), churn
  Segments: Premium, Retail, PyME, Joven
  Provinces: Buenos Aires, CABA, Córdoba, Santa Fe, Mendoza, Entre Ríos, Tucumán

tarjetas (tarjeta_id → cliente_id) — 2,110 records
  Fields: tarjeta_id, cliente_id, tipo_tarjeta, limite_credito, fecha_emision, activa
  50 clients have no card at all (so the LEFT JOIN lesson shows something)

transacciones (transaccion_id → tarjeta_id, cliente_id) — 28,956 clean / 29,825 dirty
  Fields: transaccion_id, tarjeta_id, cliente_id, fecha, monto_ars, categoria, tipo, aprobada
  Categories: Supermercado, Restaurant, Combustible, Viajes, Entretenimiento,
              Salud, Indumentaria, Servicios, E-commerce, Transferencia
  Period: Jan–Dec 2024 (monthly time-series)
  45 clients have a card but never transacted

portafolio_prestamos (prestamo_id → cliente_id) — 800 records (Clase 6 exam only)
  Fields: prestamo_id, cliente_id, tipo, monto_otorgado, tasa_anual, plazo_meses,
          fecha_otorgamiento, estado, provincia
  States: Al día, 30 días mora, 60 días mora, 90+ días mora, Cancelado
```

### Generators — regenerate, don't hand-edit

`datasets/generar_clientes.py` and `datasets/generar_transacciones.py` produce the four main CSVs. Both are deterministic (fixed seed) and must be run in that order, from inside `datasets/`. The originals (pre-August 2026) had every column independent of every other, so no analysis in the course found any signal — segments were indistinguishable, `Joven` clients averaged 47 years old, and churned customers behaved exactly like retained ones. Do not reintroduce that: any new column must be generated *as a consequence* of the customer profile.

**Signal the generators guarantee** (the exercises depend on it):

- Segments have coherent profiles: Joven ≈ 23 years old, ~1.2 years tenure, ~$46k median balance; Premium ≈ 52, ~8.5 years, ~$1.66M
- Churn is driven by segment, tenure, product count and balance: Joven 37.9% · Retail 18.1% · PyME 11.9% · Premium 7.2% (global 19.9%)
- **Ranking by churn rate is the exact inverse of ranking by balance at risk** — Premium $29.6M > Retail $19.7M > PyME $18.9M > Joven $5.9M. This is the punchline of Clase 2
- `balance_ars` is lognormal: mean is 3.3× the median (the mean-vs-median lesson)
- Tucumán shows 31.1% churn on only 45 clients — the small-base trap
- Within Retail, churned customers have shorter tenure (3.3 vs 4.5 years); within Joven the effect vanishes because everyone has ~1.2 years — a variable with no variance explains nothing
- Credit limits and spend scale with segment; churned customers stop transacting months before leaving
- Rejection rate: Joven ~10% vs Premium ~2.5%
- Category spend hierarchy, débito/crédito profiles, nominal growth through 2024, December peak, Viajes seasonal in January and July, E-commerce the fastest-growing category Q1→Q4, Friday/Saturday the heaviest days

`transacciones_sucias.csv` is the intentionally degraded version: ~7% nulls in `monto_ars`, ~5% in `categoria`, ~4% in `fecha`, ~3% exact duplicate rows, zero/negative/outlier amounts, and text inconsistencies in `categoria` and `tipo`. The `tipo` variants are restricted to those Clase 5's cleaning code actually resolves (strip + lower + replace `credito`/`credit`).

**`portafolio_prestamos.csv` has NOT been regenerated** and still has the flat-signal problem. It is also referenced by the Clase 6 exam answer key, so regenerating it means regenerating the exam.

### Notebooks load data from GitHub

Notebooks read from `https://raw.githubusercontent.com/camilojaure/itba-pad/main/datasets/`. **Changes to a CSV only reach students after pushing to GitHub.** The per-class `data/` folders are local copies and should be kept in sync.

## Notebook Structure Convention

**Guided practice notebook:**
1. Header + the "save your own copy to Drive" ritual
2. Setup — imports (`pandas`, `matplotlib`, `seaborn`) + styling
3. The five moves of any analysis: cargar → explorar → filtrar → medir → ver
4. A business case that closes with a recommendation in three bullets

**Individual practice notebook:**
1. Header + copy ritual + rules (Gemini for syntax, never for judgement)
2. 10 exercises ordered by difficulty, each with an empty code cell and a `**Lectura:**` cell for the business reading
3. A capstone challenge requiring integration

**Solutions notebook** (teacher only, never shared): solved code plus the expected business reading and grading criteria for each exercise.

## Teaching Principles

- **Problem-first**: start with the business question, not the Python syntax
- **Decision-oriented**: each analysis closes with "what should the manager do?"
- **AI-assisted**: Gemini is the primary in-Colab assistant; ask it for syntax, never for business judgement
- **No memorization**: students prompt AI for syntax, focus on problem framing
- All content and comments in notebooks are in **Spanish** (rioplatense)
- Currency is **ARS** (Argentine Peso); geography is Argentine provinces
