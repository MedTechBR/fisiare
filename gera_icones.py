#!/usr/bin/env python3
"""Ícones do Fisiare: coluna vertebral (quatro vértebras em leve curva), na cor da marca (#0B7A64),
   sobre papel claro. Gera icons/icon-180.png, icon-192.png, icon-512.png e icon-maskable-512.png.
   Quadrado cheio, sem canto transparente (o macOS emoldura ícone 'any' com transparência).
   O mesmo desenho está no SVG do logotipo do cabeçalho (index.html, VERTEBRAS)."""
from PIL import Image, ImageDraw

MARCA = (11, 122, 100, 255)
PAPEL = (250, 250, 248, 255)
# (centro x, centro y, largura, altura) na grade de 24; de cima (cervical) para baixo (lombar)
VERTEBRAS = [(12.9, 4.4, 6.4, 3.2), (12.0, 9.0, 7.6, 3.4), (11.6, 13.9, 8.8, 3.6), (12.3, 19.0, 10.0, 3.8)]

def icone(tam, maskable=False):
    S = 4 * tam                                  # desenha grande e reduz (antisserrilhado)
    im = Image.new("RGBA", (S, S), PAPEL)
    d = ImageDraw.Draw(im)
    esc = (0.56 if maskable else 0.80) * S / 24  # o desenho mora numa grade de 24
    off = (S - 24 * esc) / 2
    P = lambda x, y: (off + x * esc, off + y * esc)
    for cx, cy, w, h in VERTEBRAS:
        d.rounded_rectangle([P(cx - w / 2, cy - h / 2), P(cx + w / 2, cy + h / 2)], radius=1.3 * esc, fill=MARCA)
    return im.resize((tam, tam), Image.LANCZOS).convert("RGB")

for tam in (180, 192, 512):
    icone(tam).save(f"icons/icon-{tam}.png")
icone(512, maskable=True).save("icons/icon-maskable-512.png")
print("ícones gerados")
