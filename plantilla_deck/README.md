# Plantilla de deck — formato propio

Los decks del curso se arman en HTML y se exportan a PDF. No hace falta Gamma ni PowerPoint.
La Clase 5 fue la primera hecha así (`Clase 5/materiales/deck.html`).

## Archivos

| Archivo | Qué es |
|---|---|
| `plantilla.html` | Estilos y un ejemplo de cada layout. Se copia y se completa |
| `itba_logo.png` | Logo para la portada y el pie |
| `render.py` | Genera el PDF y avisa si alguna slide se desborda |

## Cómo armar un deck nuevo

1. Copiar `plantilla.html` e `itba_logo.png` a `Clase N/materiales/` (la plantilla queda como `deck.html`)
2. Cambiar el `<title>` y la portada. Borrar los layouts que no se usen y duplicar los que sí
3. `python3 render.py "Clase N/materiales/deck.html" "Clase N/PAD-Clase-N-Tema.pdf"`
4. Mirar el PDF y subirlo a Blackboard (carpeta *Presentaciones / contenidos* del módulo)

## Lo que es fijo en todas las slides

- **Pie automático:** logo ITBA abajo a la izquierda y **Camilo Jaureguiberry | número** abajo a la derecha
- **Portada:** el nombre abajo a la izquierda, el logo grande en el panel celeste de la derecha
- Lo agrega el script al final de la plantilla, a partir de `data-autor` y `data-logo` en `<body>`. No escribirlo a mano
- Tipografía Nunito Sans (títulos en peso 300) · 960 × 540 · fondo blanco

## Layouts disponibles

| Layout | Para qué |
|---|---|
| Portada | Pregunta de la clase + nombre del curso + tema |
| Agenda | Tabla con hora de reloj; los tres bloques en negrita |
| Tabla + nota | Un concepto en tabla y la idea fuerza en la nota amarilla |
| Bullets + nota | Hasta 5 bullets con etiqueta en negrita |
| Dos cifras | Contrastar dos números grandes |
| Grilla de tarjetas | "Para llevarse", mapa de ejercicios |
| Pase a la notebook | Nombre de la notebook, recorrido en chips, recordatorio de la copia |
| Cierre | Próxima clase y la frase con la que se van |

## Reglas de contenido

- **El deck no repite la notebook.** El código vive en la notebook; las slides llevan el problema de negocio,
  el criterio de lectura y la estructura de la clase. Si una slide se puede reemplazar por "miren la celda 12", sobra
- **Una idea por slide.** La nota amarilla es esa idea, en una o dos líneas
- **Números reales.** Toda cifra sale de correr el código sobre los datasets del curso
- **Unas 15 slides** por clase: portada, agenda, dónde estamos, la pregunta del día, 6 a 8 de teoría,
  herramientas, pase a la guiada, pase a la individual, para llevarse y próxima clase
- Español rioplatense, sin emojis
