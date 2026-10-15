#!/bin/bash
# Cópia de teste do Fisiare com Firebase de mentira (nunca publicar a cópia).
# Uso: bash docs/prepara_teste.sh <pasta-destino>   e depois: python3 <pasta>/servir.py 8752
set -e
SRC="$(cd "$(dirname "$0")/.." && pwd)"; DST="$1"; [ -n "$DST" ] || { echo "uso: $0 <destino>"; exit 1; }
rm -rf "$DST"; mkdir -p "$DST"
rsync -a --exclude .git --exclude provas-reais --exclude docs "$SRC/" "$DST/"
cp ~/Documents/Claude/_mtsync/fake-firebase.js "$DST/"
for f in _mttokens.css _mtacesso.js _mtvoltar.js; do
  [ -f "$SRC/../MedTech/site/$f" ] && cp "$SRC/../MedTech/site/$f" "$DST/" || curl -sf "https://medtechbr.com.br/$f" -o "$DST/$f" || true
done
python3 - "$DST/index.html" <<'PY'
import sys,re
p=sys.argv[1];s=open(p,encoding="utf-8").read()
s=s.replace('<script src="mtsync.js','<script src="fake-firebase.js"></script>\n<script src="mtsync.js',1)
s=s.replace('navigator.serviceWorker.register("sw.js")','Promise.reject("sem SW no teste")',1)
open(p,"w",encoding="utf-8").write(s)
PY
echo "pronto: $DST"
