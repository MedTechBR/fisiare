#!/bin/bash
# Publica o Fisiare: valida tudo e PARA no primeiro erro (nada de "| grep" mascarando código de saída).
# Uso: bash docs/publica.sh "mensagem do commit"
set -euo pipefail
cd "$(dirname "$0")/.."
MSG="${1:?mensagem do commit}"
EXC=(); while read -r f; do [ -n "$f" ] && EXC+=(":(exclude)lotes-questoes/$f"); done < lotes-questoes/EM_ANDAMENTO.txt
for h in leituras/*.html; do b=$(basename "$h" .html); case "$b" in _*) continue;; esac; [ -f "leituras/_entradas_$b.json" ] || EXC+=(":(exclude)$h"); done
python3 monta_extras.py
python3 monta_leituras.py
python3 gera_indice.py >/dev/null
PRONTAS=$(for e in leituras/_entradas_*.json; do b=${e#leituras/_entradas_}; echo "${b%.json}.html"; done)
python3 valida_leituras.py $PRONTAS | tail -1
python3 docs/confere_links_cruzados.py | tail -1
python3 docs/confere_origem.py $(cat lotes-questoes/EM_ANDAMENTO.txt) > /tmp/fi_origem.txt || { echo "divergências de origem (ver /tmp/fi_origem.txt)"; tail -1 /tmp/fi_origem.txt; }
python3 monta_banco.py > /tmp/fi_banco.txt; grep -E 'gerado|repetidas' /tmp/fi_banco.txt
python3 valida_html.py
python3 bump.py
git add -A -- . ${EXC[@]+"${EXC[@]}"}
git -c user.name="MedTechBR" -c user.email="matheusparente1@gmail.com" commit -q -m "$MSG

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
git push -q
git log --oneline | head -1
