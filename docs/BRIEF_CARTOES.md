# Brief — cartões de repetição espaçada do Fisiare (15/10/2026)

Cartões SM-2: frente `a` (pergunta curta e precisa), verso `b` (resposta em 1 a 3 frases com o número,
critério, parâmetro ou artigo, e a norma, diretriz ou obra de referência COM ANO que sustenta). `tema` = id de
`taxonomia.js`. Cartão sem âncora vira boato. Leia `taxonomia.js` e a seção F de
`docs/LEVANTAMENTO_FISIO_2026-10.md` (normas vigentes e o que mudou).

Regras: o que cai em prova (Decreto-Lei 938/1969 e Lei 6.316/1975, Código de Ética COFFITO 424/2013, RDC
7/2010, parâmetros de VM e critérios de desmame, VNI, gasometria, escalas e pontos de corte, graus de força,
dosimetria, marcos do desenvolvimento motor, classificações). Um fato por cartão. Sem travessão, sem emoji, sem
markdown. Nenhum número de memória; sem confirmar, não faça o cartão. Não copie texto de livro. Cota: no
máximo 4 buscas web no total.

Saída: SÓ `docs/cartoes_<slug>.json` (lista de `{"tema","a","b"}`), na quantidade e nas áreas pedidas.
Antes de terminar: `python3 -c "import json,re,sys;d=json.load(open(sys.argv[1]));t=set(re.findall(r'\"id\":\"(\w+)\"',open('taxonomia.js').read()));assert all(x['tema'] in t and re.search(r'(19|20)\d\d',x['b']) and '—' not in x['a']+x['b'] for x in d);print(len(d))" docs/cartoes_<slug>.json`
Relatório final: quantos por área e o que ficou duvidoso.
