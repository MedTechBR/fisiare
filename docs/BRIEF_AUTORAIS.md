# Brief — questões AUTORAIS do Fisiare (15/10/2026)

Fisiare = app de estudo de Fisioterapia (`~/Documents/Claude/fisiare/`): residência multiprofissional
(ENARE/FGV), concursos de fisioterapeuta (EBSERH) e título de especialista do COFFITO. O banco é quase todo de
provas reais; autoral só cobre o que não tem caderno público (o título do COFFITO não publica caderno). Esta rodada é a AMOSTRA que o
Matheus vai aprovar antes de escalar ("não gere 500 antes de eu ver 10"): qualidade máxima, não volume.

## Antes de escrever
- Leia `taxonomia.js` (áreas, `sub`, cenários, competências, níveis) e as seções E e F de
  `docs/LEVANTAMENTO_FISIO_2026-10.md` (formato do título COFFITO, normas vigentes e o que mudou) e o Anexo I
  do edital COFFITO 2026 (`provas-reais/txt/coffito2026_anexoI_conteudos_referencias.raw`: conteúdo e
  bibliografia por especialidade).
- Leia 10 questões reais do ENARE para pegar o tom da banca: `provas-reais/txt/enare2025_fisio_tipo1.raw`.
  NÃO copie nem parafraseie questão real: a sua é original, sobre outro ponto ou outro caso.

## Formato (lista JSON; chaves nesta ordem)
`q, alts, gab, tema, sub, cenario, comp, nivel, base, coment, porAlt` (sem `fonte`: ausência = autoral).
- `q`: caso clínico ou situação de serviço curta e concreta (idade, setor, dados), terminando em pergunta
  direta. Pelo menos metade das questões em caso clínico. Evite "assinale a INCORRETA"/"exceto" (no máximo 1 em 10).
- `alts`: 5 alternativas (A–E, como o COFFITO e o ENARE), sem letra na frente.
  Todas plausíveis para quem estudou pouco; o distrator erra por CONTEÚDO (prazo trocado, norma antiga, parâmetro
  fora da faixa, conduta de outra categoria profissional, valor de corte errado), nunca por vagueza.
- `gab`: índice 0-based. Distribua as posições (nunca a mesma em mais de 30% do seu arquivo).
- `tema`/`sub`: ids e nomes EXATOS de `taxonomia.js`. `cenario`: aps, amb, enf, uti, ger.
  `comp`: base, aval, cond, tec, norma. `nivel`: r1, r2, r3, tit.
- `base`: a norma, manual ou diretriz que sustenta a resposta, com NÚMERO e ANO (4 dígitos), versão vigente.
  Ex.: "Resolução COFFITO 424/2013 (Código de Ética)", "Decreto-Lei 938/1969, art. 3º", "RDC ANVISA 7/2010,
  art. 14", "Recomendações Brasileiras de Ventilação Mecânica (AMIB/SBPT) 2013", "GOLD 2026".
- `coment`: 300 a 900 caracteres, explica por que a correta está certa e o raciocínio, citando o artigo,
  número ou critério decisivo e a fonte. Tom de manual, frases diretas.
- `porAlt`: uma frase por alternativa, na MESMA ordem de `alts`, cada uma com mais de 20 caracteres; a da
  correta começa com "Correta: ", as outras dizem por que estão erradas.

## Viés de tamanho (o validador mede)
Distratores entre ~85% e ~115% do tamanho da correta. A correta deve ser a alternativa mais longa em 18 a 26%
das suas questões (o acaso daria ~20%; nem mais, nem bem menos). Sem "sempre/nunca/apenas" concentrado nos
distratores e "pode/geralmente" só na correta.

## Escrita
Sem travessão (—, –); sem emoji; sem markdown; sem "é importante ressaltar". Acentuação completa em todas as
alternativas. Nenhum número, dose, prazo ou artigo de memória: confira na fonte primária. Na dúvida, escolha
outro ponto para a questão.

## Operação
- Escreva em partes (5 questões por vez, acrescentando ao arquivo).
- Cota: no máximo 6 buscas web (WebSearch + WebFetch) no trabalho inteiro. Use antes os textos já baixados
  em `provas-reais/txt/`.
- Escreva SÓ o seu arquivo `lotes-questoes/leva<NNN>-<slug>.json`. Não edite banco.js nem outros arquivos;
  não rode monta_banco.py.
- Antes de terminar, rode e corrija até passar:
```
python3 -c "
import json,sys,collections
d=json.load(open(sys.argv[1]));L=0;pos=collections.Counter()
for x in d:
  a=x['alts'];g=x['gab'];c=len(a[g]);pos[g]+=1
  assert len(x['porAlt'])==len(a) and x['porAlt'][g].startswith('Correta: '), x['q'][:60]
  assert 300<=len(x['coment'])<=900 and any(ch.isdigit() for ch in x['base']), x['q'][:60]
  assert '—' not in x['q']+x['coment']+''.join(a+x['porAlt']) and '–' not in x['coment']
  assert all(0.85*c<=len(t)<=1.15*c for j,t in enumerate(a) if j!=g), ('tamanho', x['q'][:60])
  if c>max(len(t) for j,t in enumerate(a) if j!=g): L+=1
print(len(d),'questões; correta mais longa',round(L/len(d)*100),'%; posições',dict(pos))
assert 0.15<=L/len(d)<=0.30 and max(pos.values())<=0.3*len(d)+1
" lotes-questoes/leva<NNN>-<slug>.json
```
- Relatório final: questões por área, fontes conferidas (com URL) e qualquer ponto que ficou duvidoso.
