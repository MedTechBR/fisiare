#!/usr/bin/env python3
"""Reaproveita o editorial de questões que o Enfermare já comentou (mesmo texto, mesmas alternativas e mesmo
gabarito), mapeando cenário e competência para os ids do Fisiare. Só para as áreas comuns às duas taxonomias
(sus, coletiva, seguranca, etica) e com `sub` existente aqui. Comentário que fala de enfermagem fica de fora
(vai para o redator).
Uso: python3 docs/reaproveita_enfermare.py <cand.json> <prefixo-de-id> <leva-saida.json> <pendentes-saida.json>"""
import json, glob, re, sys, os
cand, pref, saida, pend = sys.argv[1:5]
norm = lambda t: re.sub(r'\W+', '', (t or '').lower())
tax = open(os.path.join(os.path.dirname(__file__), '..', 'taxonomia.js'), encoding='utf-8').read()
subs = {}
for m in re.finditer(r'\{"id":"(\w+)".*?"sub":\[(.*?)\]\}', tax, re.S):
    subs[m.group(1)] = set(re.findall(r'"([^"]+)"', m.group(2)))
CEN = {"aps": "aps", "enf": "enf", "emg": "enf", "cc": "enf", "uti": "uti", "ger": "ger"}
COMP = {"aval": "aval", "cuid": "cond", "tec": "tec", "calc": "tec", "norma": "norma"}
enf = {}
for f in sorted(glob.glob(os.path.expanduser('~/Documents/Claude/enfermare/lotes-questoes/leva*.json'))):
    for q in json.load(open(f, encoding='utf-8')):
        enf.setdefault(norm(q['q']) + '|' + norm(''.join(q['alts'])), q)
ok, resto = [], []
for x in json.load(open(cand, encoding='utf-8')):
    if not x['id'].startswith(pref): continue
    e = enf.get(norm(x['q']) + '|' + norm(''.join(x['alts'])))
    if (e and e['gab'] == x['gab'] and e['tema'] in subs and e.get('sub') in subs[e['tema']]
            and not re.search(r'enferm', e['coment'] + ''.join(e['porAlt']), re.I)):
        f = dict(x['fonte']); f.pop('id', None)
        ok.append({"q": x['q'], "alts": x['alts'], "gab": x['gab'], "tema": e['tema'], "sub": e['sub'],
                   "cenario": CEN[e['cenario']], "comp": COMP[e['comp']], "nivel": e['nivel'], "base": e['base'],
                   "coment": e['coment'], "porAlt": e['porAlt'], "fonte": f})
    else:
        resto.append(x)
json.dump(ok, open(saida, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(resto, open(pend, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'{len(ok)} reaproveitadas → {saida}; {len(resto)} para o redator → {pend}')
