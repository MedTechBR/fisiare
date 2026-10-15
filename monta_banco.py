#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta banco.js a partir de lotes-questoes/leva*.json (ordem alfabética) e valida.

Fisiare. Ver CLAUDE.md: banco.js é gerado, a fonte é a leva.

banco.js é GERADO — não editar à mão. Para mexer numa questão, edite a leva
correspondente e rode: python3 monta_banco.py
"""
import glob, json, os, subprocess, sys

RAIZ = os.path.dirname(os.path.abspath(__file__))

def main():
    banco = []
    # lotes ainda em escrita por redatores ficam de fora: um nome por linha em lotes-questoes/EM_ANDAMENTO.txt
    pend = os.path.join(RAIZ, "lotes-questoes", "EM_ANDAMENTO.txt")
    fora = set(open(pend, encoding="utf-8").read().split()) if os.path.exists(pend) else set()
    for arq in sorted(glob.glob(os.path.join(RAIZ, "lotes-questoes", "leva*.json"))):
        if os.path.basename(arq) in fora:
            print(f"  {os.path.basename(arq)}: em andamento, fora do banco"); continue
        leva = json.load(open(arq, encoding="utf-8"))
        print(f"  {os.path.basename(arq)}: {len(leva)} questões")
        banco.extend(leva)
    # mesma questão em dois cadernos (enunciado igual = mesma chave de progresso): fica a primeira e a
    # outra prova entra em fonte.tb, para a prova na íntegra continuar completa
    sys.path.insert(0, RAIZ)
    from valida_banco import chave_q
    vistas, unico, dup = {}, [], 0
    for q in banco:
        k = chave_q(q)
        if k in vistas:
            dup += 1; prim = vistas[k]
            if q.get("fonte") and prim.get("fonte"):
                tb = prim["fonte"].setdefault("tb", [])
                tb.append({"prova": q["fonte"]["prova"], "n": q["fonte"].get("n")})
            continue
        vistas[k] = q; unico.append(q)
    if dup: print(f"  {dup} questões repetidas entre cadernos: ficam uma vez, com fonte.tb")
    banco = unico
    with open(os.path.join(RAIZ, "banco.js"), "w", encoding="utf-8") as f:
        f.write("window.BANCO=")
        json.dump(banco, f, ensure_ascii=False, indent=0)
        f.write(";\n")
    print(f"banco.js gerado: {len(banco)} questões\n")
    r = subprocess.run([sys.executable, os.path.join(RAIZ, "valida_banco.py")])
    sys.exit(r.returncode)

if __name__ == "__main__":
    main()
