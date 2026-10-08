"""Gera header.svg (matrix + pixel art) e footer.svg (space invaders).
Uso: python assets/gen.py   -> sobrescreve assets/header.svg e assets/footer.svg
"""
import random
from pathlib import Path

OUT = Path(__file__).parent
random.seed(7)  # determinístico: regenerar não muda o SVG à toa

GREEN, BRIGHT, BG = "#00ff41", "#d4ffd9", "#020a04"

# Fonte 5x7 só com as letras necessárias
FONT = {
    "C": ["01111", "10000", "10000", "10000", "10000", "10000", "01111"],
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "I": ["11111", "00100", "00100", "00100", "00100", "00100", "11111"],
    "X": ["10001", "10001", "01010", "00100", "01010", "10001", "10001"],
    "E": ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
    "T": ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
}
LOCK = [
    "00111100", "01000010", "01000010", "01000010", "11111111",
    "11111111", "11100111", "11100111", "11110111", "11111111",
]
INVADER = [  # dois frames, 11x8
    ["00100000100", "00010001000", "00111111100", "01101110110",
     "11111111111", "10111111101", "10100000101", "00011011000"],
    ["00100000100", "10010001001", "10111111101", "11101110111",
     "11111111111", "01111111110", "00100000100", "01000000010"],
]
GLYPHS = "01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホ"


def pixels(rows, x0, y0, size, cls=""):
    c = f' class="{cls}"' if cls else ""
    return "".join(
        f'<rect x="{x0 + x * size}" y="{y0 + y * size}" width="{size}" height="{size}"{c}/>'
        for y, row in enumerate(rows) for x, b in enumerate(row) if b == "1"
    )


def text_pixels(word, x0, y0, size):
    out = []
    for i, ch in enumerate(word):
        out.append(pixels(FONT[ch], x0 + i * 6 * size, y0, size))
    return "".join(out)


def header(w=960, h=300):
    col_w, n_chars = 16, 24
    rain = []
    for i in range(w // col_w):
        dur = random.uniform(4, 10)
        delay = -random.uniform(0, dur)
        chars = []
        for j in range(n_chars):
            op = round((j + 1) / n_chars, 2)
            fill = BRIGHT if j == n_chars - 1 else GREEN
            chars.append(f'<tspan x="{i * col_w + 8}" dy="16" fill="{fill}" '
                         f'fill-opacity="{op}">{random.choice(GLYPHS)}</tspan>')
        rain.append(f'<text class="drop" style="animation-duration:{dur:.1f}s;'
                    f'animation-delay:{delay:.1f}s">{"".join(chars)}</text>')

    size = 10
    word = "CAIXETA"
    word_w = (len(word) * 6 - 1) * size
    lock_w = 8 * size
    total = lock_w + 30 + word_w
    x0 = (w - total) // 2
    wx = x0 + lock_w + 30
    name = text_pixels(word, wx, 80, size)
    lock = pixels(LOCK, x0, 80, size)

    tagline = "$ whoami → matheus caixeta reis :: iam · segurança · automação"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Matheus Caixeta Reis — IAM, Segurança da Informação e Automação">
<style>
  .drop {{ font: 14px "MS Gothic","Noto Sans Mono CJK JP","Osaka",monospace; animation: fall linear infinite; }}
  @keyframes fall {{ from {{ transform: translateY(-{n_chars * 16}px) }} to {{ transform: translateY({h}px) }} }}
  .name rect {{ fill: {GREEN}; }}
  .ghost-r rect {{ fill: #ff0055; }} .ghost-c rect {{ fill: #00e5ff; }}
  .ghost-r, .ghost-c {{ opacity: 0; mix-blend-mode: screen; }}
  .ghost-r {{ animation: gr 5s steps(1) infinite; }} .ghost-c {{ animation: gc 5s steps(1) infinite; }}
  @keyframes gr {{ 0%,86%,100% {{ opacity:0; transform:none }} 87% {{ opacity:.9; transform:translate(-6px,2px) }} 89% {{ opacity:.9; transform:translate(4px,-3px) }} 91% {{ opacity:0 }} }}
  @keyframes gc {{ 0%,86%,100% {{ opacity:0; transform:none }} 87% {{ opacity:.9; transform:translate(6px,-2px) }} 89% {{ opacity:.9; transform:translate(-4px,3px) }} 91% {{ opacity:0 }} }}
  .name {{ animation: boot 1.2s steps(6), jitter 5s steps(1) infinite 1.2s; filter: drop-shadow(0 0 6px {GREEN}); }}
  @keyframes boot {{ 0% {{ opacity:0 }} 30% {{ opacity:1 }} 45% {{ opacity:.2 }} 60%,100% {{ opacity:1 }} }}
  @keyframes jitter {{ 0%,86%,92%,100% {{ transform:none }} 88% {{ transform:translateX(3px) skewX(-8deg) }} 90% {{ transform:translateX(-2px) }} }}
  .lock rect {{ fill: {GREEN}; }} .lock {{ animation: pulse 2.4s ease-in-out infinite; filter: drop-shadow(0 0 6px {GREEN}); }}
  @keyframes pulse {{ 50% {{ opacity: .55 }} }}
  .tag {{ font: 600 17px "JetBrains Mono","Cascadia Code",Consolas,monospace; fill: {GREEN}; }}
  .cover {{ fill: {BG}; animation: uncover 4s steps(40); }}
  @keyframes uncover {{ 0%,25% {{ transform: translateX(-{w}px) }} 100% {{ transform: translateX(0) }} }}
  .cursor {{ fill: {GREEN}; animation: blink 1s steps(1) infinite; }}
  @keyframes blink {{ 50% {{ opacity: 0 }} }}
  @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
</style>
<defs>
  <pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="2" fill="#000" fill-opacity=".35"/></pattern>
  <radialGradient id="vig" cx="50%" cy="50%" r="70%"><stop offset="55%" stop-color="#000" stop-opacity="0"/><stop offset="100%" stop-color="#000" stop-opacity=".85"/></radialGradient>
</defs>
<rect width="{w}" height="{h}" fill="{BG}"/>
<g opacity=".45">{"".join(rain)}</g>
<rect x="{x0 - 40}" y="56" width="{total + 80}" height="118" fill="{BG}" fill-opacity=".82" stroke="{GREEN}" stroke-width="2" stroke-dasharray="10 6"/>
<g class="lock">{lock}</g>
<g class="ghost-r">{name}</g><g class="ghost-c">{name}</g>
<g class="name">{name}</g>
<text class="tag" x="{w // 2}" y="226" text-anchor="middle">{tagline}</text>
<rect class="cover" x="{w}" y="200" width="{w}" height="40"/>
<rect class="cursor" x="{w // 2 + 330}" y="211" width="10" height="20"/>
<rect width="{w}" height="{h}" fill="url(#scan)"/>
<rect width="{w}" height="{h}" fill="url(#vig)"/>
</svg>'''


def footer(w=960, h=150):
    size, cols, gap = 4, 8, 64
    row_w = (cols - 1) * gap + 11 * size
    x0 = (w - row_w) // 2
    colors = ["#00ff41", "#00e5ff", "#ff0055"]
    rows = []
    for r, color in enumerate(colors):
        y = 18 + r * 38
        f0 = "".join(f'<use href="#i0" x="{x0 + c * gap}" y="{y}"/>' for c in range(cols))
        f1 = "".join(f'<use href="#i1" x="{x0 + c * gap}" y="{y}"/>' for c in range(cols))
        rows.append(f'<g fill="{color}"><g class="f0">{f0}</g><g class="f1">{f1}</g></g>')
    ship = ["00000100000", "00001110000", "00001110000", "01111111110", "11111111111", "11111111111"]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Space invaders em pixel art">
<style>
  .fleet {{ animation: march 6s steps(12) infinite alternate; }}
  @keyframes march {{ from {{ transform: translateX(-90px) }} to {{ transform: translateX(90px) }} }}
  .f0 {{ animation: frame .8s steps(1) infinite; }} .f1 {{ animation: frame .8s steps(1) infinite reverse; }}
  @keyframes frame {{ 0% {{ opacity:1 }} 50% {{ opacity:0 }} }}
  .ship {{ animation: patrol 4s ease-in-out infinite alternate; }}
  @keyframes patrol {{ from {{ transform: translateX(-200px) }} to {{ transform: translateX(200px) }} }}
  .shot {{ animation: shoot 1s linear infinite; }}
  @keyframes shoot {{ from {{ transform: translateY(0); opacity:1 }} to {{ transform: translateY(-90px); opacity:0 }} }}
  @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
</style>
<defs><g id="i0">{pixels(INVADER[0], 0, 0, size)}</g><g id="i1">{pixels(INVADER[1], 0, 0, size)}</g></defs>
<rect width="{w}" height="{h}" fill="{BG}"/>
<g class="fleet" filter="drop-shadow(0 0 3px #00ff41)">{"".join(rows)}</g>
<g class="ship" fill="{GREEN}">{pixels(ship, w // 2 - 22, h - 26, 4)}<rect class="shot" x="{w // 2 - 2}" y="{h - 40}" width="4" height="10"/></g>
</svg>'''


if __name__ == "__main__":
    (OUT / "header.svg").write_text(header(), encoding="utf-8")
    (OUT / "footer.svg").write_text(footer(), encoding="utf-8")
    for f in ("header.svg", "footer.svg"):
        s = (OUT / f).read_text(encoding="utf-8")
        assert s.startswith("<svg") and s.rstrip().endswith("</svg>") and "<script" not in s
        print(f, len(s), "bytes")
