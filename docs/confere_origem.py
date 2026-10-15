#!/usr/bin/env python3
"""Confere cada questão de prova real das levas (lotes-questoes/leva1*.json) contra a candidata extraída do
caderno (provas-reais/cand_*.json): mesma (prova, n) -> alternativas e gabarito idênticos e enunciado igual
a menos de espaços. Existe porque redatores em paralelo dividem o scratchpad e já sobrescreveram rascunhos
uns dos outros. Uso: python3 docs/confere_origem.py   (sai com 1 se houver divergência)"""
import json, glob, os, re, sys
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
norm = lambda s: re.sub(r"\s+", " ", s).strip()
cand = {}
for f in glob.glob(os.path.join(R, "provas-reais", "cand_*.json")):
    for q in json.load(open(f, encoding="utf-8")):
        fo = q["fonte"]; cand[(fo["banca"], fo["prova"], fo["n"])] = q
erros = 0; n = 0; sem = 0
ignora = set(sys.argv[1:])
for f in sorted(glob.glob(os.path.join(R, "lotes-questoes", "leva1*.json"))):
    if os.path.basename(f) in ignora: continue
    for q in json.load(open(f, encoding="utf-8")):
        fo = q.get("fonte") or {}
        c = cand.get((fo.get("banca"), fo.get("prova"), fo.get("n")))
        n += 1
        if not c: sem += 1; continue
        prob = []
        if q["gab"] != c["gab"]: prob.append(f"gab {q['gab']}≠{c['gab']}")
        if [norm(a) for a in q["alts"]] != [norm(a) for a in c["alts"]]: prob.append("alts")
        if norm(q["q"]) != norm(c["q"]) and norm(c["q"]) not in norm(q["q"]): prob.append("q")
        if prob:
            erros += 1; print(os.path.basename(f), fo.get("prova"), fo.get("n"), prob)
print(f"{n} questões reais conferidas, {erros} divergentes, {sem} sem candidata de origem")
sys.exit(1 if erros else 0)
