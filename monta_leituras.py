#!/usr/bin/env python3
"""Gera leituras.js a partir de leituras/_entradas_*.json (um por leitura, escrito pelo redator).
Os sidecars FICAM (são a fonte do índice). GRUPOS define a ordem; leitura de área sem grupo vai a "Outras"."""
import json, glob, os
RAIZ = os.path.dirname(os.path.abspath(__file__))
GRUPOS = [("Exercício profissional e SUS", ["etica", "sus", "coletiva", "seguranca", "aps"]),
          ("Bases e recursos", ["bases", "avaliacao", "recursos"]),
          ("Cardiorrespiratória e terapia intensiva", ["respiratoria", "uti", "cardio"]),
          ("Neuro e musculoesquelética", ["neuro", "orto"]),
          ("Ciclos de vida", ["pediatria", "mulher", "idoso", "onco"])]
ent = [e for f in sorted(glob.glob(os.path.join(RAIZ, "leituras", "_entradas_*.json"))) for e in json.load(open(f, encoding="utf-8"))]
esc = lambda s: json.dumps(str(s), ensure_ascii=False)
out = ["/* GERADO por monta_leituras.py a partir de leituras/_entradas_*.json: não editar à mão.\n"
       "   `area` liga a leitura ao tema do banco; itens com `grupo` são separadores; `min` em ~80 palavras/min. */\nwindow.LEITURAS=["]
usadas = set()
for nome, areas in GRUPOS + [("Outras", None)]:
    ls = [e for e in ent if (areas is None and e["f"] not in usadas) or (areas and e["area"] in areas)]
    ls.sort(key=lambda e: (areas.index(e["area"]) if areas else 0, e["t"]))
    if not ls: continue
    out.append(f'\n {{grupo:{esc(nome)}}},')
    for e in ls:
        usadas.add(e["f"])
        out.append(f' {{f:{esc(e["f"])}, tipo:{esc(e["tipo"])}, area:{esc(e["area"])}, min:{int(e["min"])},\n  t:{esc(e["t"])},\n  s:{esc(e["s"])}}},')
out.append("];\n")
open(os.path.join(RAIZ, "leituras.js"), "w", encoding="utf-8").write("\n".join(out))
print(f"leituras.js: {len(usadas)} leituras")
