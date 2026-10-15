#!/usr/bin/env python3
"""Gera flash.js (de docs/cartoes_*.json) e pratica.js (de docs/casos_*.json).

flash.js: o progresso SM-2 é por ÍNDICE. A ordem é a de ORDEM_CARTOES; arquivo novo entra SEMPRE no fim
da lista, nunca no meio, e cartão publicado não se apaga nem se move (corrige-se no lugar)."""
import json, os, re
RAIZ = os.path.dirname(os.path.abspath(__file__))
ORDEM_CARTOES = ["cartoes_a.json", "cartoes_b.json"]
ORDEM_CASOS = ["casos_a.json"]
def le(n): return json.load(open(os.path.join(RAIZ, "docs", n), encoding="utf-8"))
tax = set(re.findall(r'"id":"(\w+)"', open(os.path.join(RAIZ, "taxonomia.js"), encoding="utf-8").read()))
cart = [c for n in ORDEM_CARTOES for c in le(n)]
assert all(c["tema"] in tax for c in cart)
cab = open(os.path.join(RAIZ, "flash.js"), encoding="utf-8").read().split("window.FLASH=")[0]
open(os.path.join(RAIZ, "flash.js"), "w", encoding="utf-8").write(cab + "window.FLASH=" + json.dumps(cart, ensure_ascii=False, indent=0) + ";\n")
casos = [c for n in ORDEM_CASOS for c in le(n)]
assert len({c["id"] for c in casos}) == len(casos)
for c in casos: assert c["area"] in tax and abs(sum(i["peso"] for i in c["espelho"]) - 5) < 1e-6, c["id"]
open(os.path.join(RAIZ, "pratica.js"), "w", encoding="utf-8").write(
 "/* Casos clínicos de Fisioterapia, em etapas, com espelho C/H/A de 5,0. GERADO por\n"
 "   monta_extras.py a partir de docs/casos_*.json: não editar à mão. Brief: docs/BRIEF_CASOS.md. */\n"
 "window.PRATICA=" + json.dumps(casos, ensure_ascii=False, indent=1) + ";\n")
print(f"flash.js: {len(cart)} cartões · pratica.js: {len(casos)} casos")
