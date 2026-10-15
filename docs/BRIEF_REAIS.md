# Brief — questões de prova real para o Fisiare (15/10/2026)

Você recebe um lote de questões extraídas VERBATIM de cadernos oficiais públicos de Fisioterapia (ENARE
multiprofissional/FGV, concursos EBSERH 2023/IBFC e 2024/FGV, título de especialista do COFFITO, residências
como HCPA, UFCSPA, UFPA, UNICAMP, UERJ e SES-PE, concursos FGV, IBADE, Selecon e Marinha). O gabarito (`gab`,
índice 0-based) é o OFICIAL DEFINITIVO e já foi conferido contra o PDF. Seu trabalho: triar e escrever os
campos editoriais. O app é de estudo de FISIOTERAPIA (residência, concursos, título de especialista).
Leia antes `taxonomia.js` e a seção de normas de `docs/LEVANTAMENTO_FISIO_2026-10.md` (normas e diretrizes
vigentes em out/2026 e o que mudou; textos já baixados em `provas-reais/txt/`).

## 1. Triagem — INCLUIR ou DESCARTAR
Quase tudo entra, inclusive SUS, políticas públicas, bioética, NR 32 e pesquisa. DESCARTE (registre o motivo) só:
- o gabarito oficial contraria a norma ou diretriz VIGENTE hoje (out/2026) de um jeito que ensinaria errado
  (ex.: parâmetro de ventilação, critério de desmame ou de reabilitação que uma diretriz nova mudou; resolução do
  COFFITO revogada). Diga qual norma e o que mudou. Questão que cita norma antiga NÃO é descartada só por isso se
  o gabarito continua correto no conteúdo: explique no `coment` a norma nova;
- texto truncado/embaralhado ou dependente de figura ausente;
- mais de uma resposta defensável.
Na dúvida razoável sobre o gabarito, MANTENHA (é o oficial) e explique a controvérsia no `coment`.

## 2. Campos de cada questão incluída
- `q` e `alts`: COPIE EXATAMENTE. Única exceção: artefato evidente de extração (hífen de quebra, espaço
  duplo). Nunca reescreva. `gab`: NUNCA altere.
- `tema`: um id de `taxonomia.js`. Use `sub` EXATO da lista daquela área (o mais próximo).
  Dicas: Lei 8.080/8.142, PNAB, RAS, humanização, equidade, educação permanente → sus; indicadores,
  vigilância, notificação, saúde do trabalhador, ergonomia → coletiva; PNSP, IRAS, precauções, NR 32 →
  seguranca; Decreto-Lei 938/1969, Lei 6.316/1975, Código de Ética, resoluções COFFITO, bioética, pesquisa e
  estatística de artigo → etica; NASF/eMulti, CIF, promoção, visita domiciliar → aps; anatomia, cinesiologia,
  marcha, fisiologia do exercício → bases; testes, escalas, goniometria, prova de função muscular, exames →
  avaliacao; eletro, termo, foto, US, cinesioterapia, hidro, terapia manual, órteses → recursos; mecânica
  respiratória, gasometria, espirometria, higiene brônquica, O2, DPOC, reabilitação pulmonar → respiratoria;
  VM, VNI, desmame, SDRA, mobilização na UTI → uti; reabilitação cardíaca, IC, pós-op cardíaco → cardio;
  AVC, TCE, lesão medular, Parkinson, neuromusculares → neuro; ortopedia, reumatologia, esporte, amputados →
  orto; desenvolvimento motor, PC, UTI neo → pediatria; gestação, assoalho pélvico → mulher; envelhecimento,
  quedas → idoso; oncologia, queimados, dermatofuncional, paliativos → onco.
- `cenario`: aps, amb, enf, uti, ger. `comp`: base (anatomia, fisiologia, biomecânica), aval (avaliação e
  diagnóstico cinético-funcional), cond (conduta e plano terapêutico), tec (recurso e técnica, parâmetros),
  norma (legislação, ética, normas). `nivel`: r1, r2, r3 (residência e concurso costumam ser r1/r2;
  especialidade fina, r3; questão do título do COFFITO, `tit`).
- `base`: norma, manual ou diretriz que sustenta a resposta, com NÚMERO e ANO (4 dígitos), versão VIGENTE.
  Ex.: "Lei 8.080/1990, art. 7º", "Resolução COFFITO 424/2013 (Código de Ética), art. 9º", "Portaria GM/MS
  2.436/2017 (PNAB)", "Diretrizes Brasileiras de Ventilação Mecânica (AMIB/SBPT) 2013", "GOLD 2026".
  Para conteúdo de livro-texto (anatomia, cinesiologia, eletroterapia) cite a obra de referência com ano de
  edição que você tenha certeza de que existe. Não invente número nem ano: em dúvida, confira.
- `coment`: 150 a 800 caracteres, explica POR QUE a oficial está certa e o raciocínio, citando o artigo,
  critério, parâmetro ou número decisivo e a fonte. Tom de manual, frases diretas.
- `porAlt`: uma frase por alternativa, na MESMA ordem de `alts`, cada uma com mais de 20 caracteres. A da
  correta começa com "Correta: ". As demais dizem por que estão erradas.
- `fonte`: copie o objeto recebido. Remova o campo `id` (ele só serve ao relatório).

Escrita (coment e porAlt): **sem travessão (—, –)**; sem emoji; sem "é importante ressaltar"; sem markdown.
Rigor: número, parâmetro, dose, artigo só conferidos (fonte + ano). Nada de memória.

## 3. Saída
Escreva DOIS arquivos (e só eles):
1. `lotes-questoes/leva<NNN>-reais-<sufixo>.json`: lista das incluídas com as chaves
   q, alts, gab, tema, sub, cenario, comp, nivel, base, coment, porAlt, fonte (nesta ordem).
2. `provas-reais/relatorios/<sufixo>.json`: `{"incluidas": N, "descartadas": [{"id":..., "motivo":...}], "discutiveis": [{"id":..., "porque":...}]}`.

Antes de terminar rode e corrija o que falhar:
`python3 -c "import json,re;t=open('taxonomia.js').read();d=json.load(open('<arquivo da leva>'));assert all(len(x['porAlt'])==len(x['alts']) and x['porAlt'][x['gab']].startswith('Correta: ') and 150<=len(x['coment'])<=800 and re.search(r'(19|20)\d\d',x['base']) and '\"'+x['sub']+'\"' in t and '—' not in x['coment']+''.join(x['porAlt']) for x in d);print(len(d))"`
Não edite banco.js, leituras nem outros arquivos. Não rode monta_banco.py.
Cota: no máximo 5 buscas web (WebSearch + WebFetch) no lote inteiro; prefira os textos já baixados.
Resumo final: incluídas, descartadas por motivo, e todo gabarito oficial que você achou discutível mas manteve.
