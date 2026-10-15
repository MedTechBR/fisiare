# Fisiare — plataforma de estudo de Fisioterapia

Criado em 15/10/2026 a pedido do Matheus: "seguindo o mesmo molde das outras plataformas de estudo, faça uma de
fisioterapia, utilizando predominantemente questões existentes de concursos / processos seletivos. Inclua no
medtech na área de multi". Nome escolhido por ele entre opções (Fisioterapia + ENARE). É um **fork do Enfermare**
(`~/Documents/Claude/enfermare/`), que é fork do CirurgiaMed e do ClínicaMed: mesma arquitetura, camada viva, motor
de conta (mtsync), erratas (mterrata), sinalização (mtsinal), defesas. **Leia o CLAUDE.md do Enfermare** (e, por
ele, os do CirurgiaMed e do ClínicaMed) para o que é comum: chave por conteúdo, Fisher-Yates, viés de tamanho,
`bump.py`, `.nojekyll`, `servir.py` com charset, escrita sem cara de IA, formato das leituras, erratas. Aqui fica
só o que é PRÓPRIO.

## Público e linha de produto (decisão dele, 15/10/2026)
- Três públicos no mesmo banco: **residência multiprofissional em Fisioterapia** (ENARE/FGV e residências de
  universidades e secretarias), **concursos de fisioterapeuta** (EBSERH, FGV, IBADE, Selecon, Marinha) e
  **título de especialista do COFFITO**.
- **Separado, com login**: conta MedTech e sync automático como os apps de estudo. À venda na linha **MedTech
  Multi** (com Enfermare, FarmaUTI, Banca ENARE Farmácia e SOS Farmácia): produto `fisiare` no `planos.json` com
  `publico:"fisioterapia"`, mesmo preço dos outros (R$ 49,90/mês ou R$ 397/ano), Mercado Pago. Internamente segue
  a linha `provas`. Não pôr cross-link para apps médicos dentro do app.
- Banco **predominantemente de provas reais** (pedido dele). Autoral só onde não há caderno público: título do
  COFFITO (amostra `leva301-autorais-titulo.json`, aguardando aprovação dele antes de escalar).

## Provas (conferidas na fonte em 15/10/2026; URLs em docs/LEVANTAMENTO_FISIO_2026-10.md)
- **ENARE multiprofissional, Fisioterapia** (FGV): 100 q, A–E, 5 h; q1–20 gerais (idênticas às de todas as
  profissões, já comentadas no Enfermare e reaproveitadas) e q21–100 Fisioterapia. Corte 50% no Edital 04/2026.
  2024/25 só tem caderno Tipo 1 público (anuladas 1, 43, 68); 2026/27 anulou a q52 do Tipo 1.
- **EBSERH 2024** (FGV): só q16–60 entram (15 políticas + 30 específicas). **EBSERH 2023** (IBFC): 8 cadernos de
  Fisioterapeuta (geral, cardiovascular, respiratória, mulher, terapia intensiva, UTI adulto, neo, pediátrica):
  q21–30 SUS comuns aos 8 (uma cópia + `fonte.tb`), q41–60 específicas, todas diferentes.
- Residências: HCPA, UFCSPA, UFPA 2023–2026, UNICAMP 2026, UERJ 2022–2026 (4 alternativas), SES-PE 2023–2026
  (2025 anulada e reaplicada: só a reaplicação vale). Concursos: FGV (Canaã, FHEMIG, MPES, Nova Iguaçu, SES-MT),
  IBADE, Selecon, Marinha CP-CSM 2021–2025 (cadernos escaneados).
- **Título (COFFITO)**: Res. COFFITO 630/2025 (revogou a 377/2010); certame nacional pelo IADES, 50 q A–E, 4 h,
  on-line, mínimo 70%, depois títulos. 2025 publicou só gabarito; **o Edital 1/2026 promete o caderno em
  07/12/2026** (prova em 06/12): baixar nesse dia e trocar a amostra autoral por questões reais.

## Normas que o banco precisa refletir (out/2026) — seção F do levantamento
Decreto-Lei 938/1969 e Lei 6.316/1975; Código de Ética Res. COFFITO 424/2013 com **arts. 37 e 39 revogados (CADE)**;
título 630/2025 e **RQE** (627/2025, ex-RPE); RDC ANVISA 7/2010: fisioterapia 1:10 leitos em 18 h (a RDC 26/2012
mudou só a enfermagem); VM pelas recomendações AMIB/SBPT 2013 + orientações práticas 2025 (J Bras Pneumol
2025;51(1):e20240255); GOLD 2026 (1 exacerbação moderada já escalona); GINA 2026 (O2 se SpO2 < 92%); AHA 2025;
reabilitação cardiovascular SBC 2020. A conferir no DOU: telefisioterapia 619/2025 x 516/2020; paliativos
660/2026 x 539/2021; parâmetros assistenciais 387/2011 + 444/2014.

## O que mudou em relação ao Enfermare
- Identidade: verde-petróleo **#0B7A64** (escuro #6FD6BF), família de verdes e azuis-esverdeados na camada viva
  (contraste AA medido), ícone de coluna vertebral (`gera_icones.py`, mesmo desenho no SVG do cabeçalho).
  Prefixo `fi_`, caches `fi-vN`/`fi-fontes-v1`/`fi-livros-v1`, IndexedDB `fi-db`, app id `fisiare` no mtsync,
  mtsinal e mterrata, porta local 8751 (teste com Firebase falso: 8752).
- Taxonomia: 17 áreas a partir do Anexo III do ENARE (itens 8.1–8.14) e do Grupo 7 da EBSERH 2024 (ids: sus,
  coletiva, seguranca, etica, aps, bases, avaliacao, recursos, respiratoria, uti, cardio, neuro, orto,
  pediatria, mulher, idoso, onco). `matriz:"Conhecimentos comuns"` (sus, coletiva, seguranca) define o bloco de
  gerais do simulado. Cenários aps/amb/enf/uti/ger; competências base/aval/cond/tec/norma.
- Simulado: `enare` (100 q, 5 h, 20 gerais + 80, 50%), `ebserh` (45 q, 3 h, 15 + 30, 50%), `coffito` (50 q, 4 h,
  70%, sem SUS/vigilância), `integra` (caderno real inteiro), `livre`.
- Aba **Casos** (`pratica.js`): raciocínio clínico fisioterapêutico em etapas (avaliação, diagnóstico
  cinético-funcional, objetivos, conduta com parâmetros, reavaliação), espelho C/H/A de 5,0.
- Turma desligada (sem função de backend `fisiare`). Sinalização e erratas precisam de `fisiare` na lista
  `APPS` de `MedTech/backend/functions/sinal.js` e deploy (ele roda o `.command`); a venda precisa do produto no
  `MedTech/backend/functions/planos.json` e do deploy-backend.

## Estado em 15/10/2026 (fi-v3, no ar em medtechbr.com.br/fisiare/, repo MedTechBR/fisiare)
2.274 questões: 2.234 de prova real (ENARE 2024–2026, EBSERH 2023 IBFC 8 cargos e 2024 FGV, SES-PE 2023–2026,
HCPA, UFCSPA, UFPA 2023–2026, UNICAMP 2026, UERJ 2022–2026, FGV municipais/estaduais, IBADE, Selecon, Marinha
2021–2025) + 40 autorais de AMOSTRA do título COFFITO (leva301, aguardando aprovação). 234 repetidas entre
cadernos ficam uma vez com `fonte.tb`. ~8% das reais descartadas na triagem (motivos em
provas-reais/relatorios/*.json). Editorial de questões idênticas às do Enfermare reaproveitado por
`docs/reaproveita_enfermare.py`. 9 leituras (ética, VM, desmame/VNI, respiratória, cardio, AVC, recursos,
ortopedia, pediatria/neo) passaram por dois conferentes; 154 cartões; 8 casos. Comentários do ENARE auditados.
À venda na linha Multi (site 56b099f + 596e9fc, _mtauth v46, _mtacesso v14).
Pendências: deploy do backend (sinal.js, conteudo.js e planos.json já editados em MedTech/backend/functions) para
erratas/sinalização/curador do Fisiare; baixar o caderno do COFFITO em 07/12/2026; "a conferir" que sobrou nas
leituras (grau AAP 2014 na bronquiolite, tabela de Houghton 2010, texto das Portarias 665/2012 e 800/2015).

## Fluxo de publicação
`bash docs/publica.sh "msg"` (para no primeiro erro). Lotes em escrita: um nome por linha em
`lotes-questoes/EM_ANDAMENTO.txt` (fora do banco e do commit). Leitura sem `_entradas_<nome>.json` fica fora do
índice e do commit. Cartões/casos: novo arquivo SEMPRE no fim de ORDEM_CARTOES/ORDEM_CASOS (SM-2 por índice).
Numeração das levas: 1NN = provas reais, 3NN = autorais.

## Teste local
`bash docs/prepara_teste.sh <scratchpad>/teste-fi` (cópia com `fake-firebase.js` e sem SW) e o preview
`fisiare-teste` (porta 8752) do `.claude/launch.json`; no console:
`await __fake.auth.signInWithEmailAndPassword('x@exemplo.com')`.

## Briefs dos redatores (docs/)
BRIEF_EXTRACAO (cadernos → `provas-reais/cand_*.json`), BRIEF_REAIS (triagem e comentário → leva1NN),
BRIEF_AUTORAIS (amostra de título → leva3NN), BRIEF_MONOGRAFIA (leituras), BRIEF_CASOS (`docs/casos_a.json` →
pratica.js), BRIEF_CARTOES (`docs/cartoes_*.json` → flash.js; SM-2 por índice: só acrescentar no fim).
`docs/extracao/gabgeo.py` aceita números de até 3 dígitos desde 15/10 (perdia a linha 81–100 do ENARE).
