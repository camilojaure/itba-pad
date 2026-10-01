"""Genera el PDF de un deck hecho con plantilla.html.

Uso:  python3 render.py deck.html            → deck.pdf
      python3 render.py deck.html salida.pdf

Requiere Playwright con Chromium (pip install playwright && playwright install chromium).
Avisa si alguna slide se desborda (contenido que pisa el pie o se sale de la página).
"""
import asyncio, sys
from pathlib import Path
from playwright.async_api import async_playwright

CHECK = """[...document.querySelectorAll('section.s')].map((s, i) => {
  if (s.classList.contains('cover')) return [i + 1, 0];
  const top = s.getBoundingClientRect().top; let fondo = 0;
  s.querySelectorAll('*').forEach(e => {
    if (e.closest('.logo,.pg,.author-cover,.r') ) return;
    fondo = Math.max(fondo, e.getBoundingClientRect().bottom - top);
  });
  return [i + 1, Math.round(fondo)];
})"""

async def main(src, dst):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 960, 'height': 540})
        await pg.goto(Path(src).resolve().as_uri())
        await pg.wait_for_load_state('networkidle')
        await pg.wait_for_timeout(500)
        malas = [(n, h) for n, h in await pg.evaluate(CHECK) if h > 505]
        for n, h in malas:
            print(f'⚠ slide {n}: el contenido llega a {h}px (máximo 505). Recortá texto o achicá la tabla.')
        await pg.pdf(path=dst, width='960px', height='540px', print_background=True)
        await b.close()
    print(f'PDF: {dst}' + ('' if malas else ' · sin desbordes'))

if __name__ == '__main__':
    src = sys.argv[1]
    dst = sys.argv[2] if len(sys.argv) > 2 else str(Path(src).with_suffix('.pdf'))
    asyncio.run(main(src, dst))
