# Fisioterapia: levantamento de provas e normas (Brasil)

Data da pesquisa: 15/10/2026. Usei 10 buscas web (WebSearch) e 1 WebFetch, 11 das 40 permitidas. O resto saiu por `curl` direto nos servidores oficiais: listagens de diretório, JSON embutido, API do WordPress e índice CDX do Wayback, este só para descobrir nomes de arquivo. Nenhum PDF veio de cópia arquivada ou de cursinho.

Pasta: `/private/tmp/claude-501/-Users-matheusparente/24edeac6-15cd-4c88-8b50-83646c37609c/scratchpad/fisio-provas/`
- `pdf/`: 161 PDFs (148 MB), sendo 78 cadernos de prova e 83 gabaritos, editais, comunicados e normas.
- `txt/`: `pdftotext -layout` em `.txt` e modo simples em `.raw`, um par para cada PDF.
- `txt/enare_fisio_topicos_2026.txt`: os 14 tópicos de Fisioterapia do ENARE, já limpos.
- `txt/gabaritos_imagem_transcritos.txt`: os 4 gabaritos que só existem como imagem, transcritos uma vez. Precisam de uma 2ª leitura.
- `aux/`: páginas HTML das listagens, imagens renderizadas e arquivos intermediários. Não é entrega.

Legenda: **[oficial]** é documento da banca ou do órgão. **[secundária]** é compilador de normas, imprensa ou blog, e não serve como fonte primária.

Também copiei para cá, sem baixar de novo, arquivos que o Enfermare já tinha:
- gabaritos e editais do ENARE;
- gabarito e edital da EBSERH 2024;
- cadernos e gabaritos multi da HCPA e da UFCSPA, que trazem todas as profissões num PDF só;
- cadernos Selecon e IBADE e os gabaritos Selecon, IBADE e FGV;
- gabaritos finais da Marinha;
- gabarito da HCFMUSP;
- comunicado 005/2025 da SES-PE.

---

## A) ENARE: Residência em Área Profissional da Saúde, Fisioterapia (FGV)

### A.1 Estrutura (conferida nos cadernos e nos gabaritos definitivos)

| | 2024/2025 | 2025/2026 | 2026/2027 |
|---|---|---|---|
| Prova | 20/10/2024 | 19/10/2025 | 13/09/2026 (tarde) |
| Questões | 100, A–E | 100, A–E | 100, A–E |
| Divisão | q1–20 Conhecimentos Gerais + q21–100 Específicos | igual | igual |
| Duração e corte | 5 h; mínimo de 40 pontos, mais análise curricular de 10% | 5 h; 40% | 5 h; **50%** (item 9.6) |
| Tipos de caderno de Fisioterapia publicados | **só o Tipo 1** (código FISIOTT01) | 4 | 4 |
| Anuladas em Fisioterapia (definitivo) | Tipo 1: **1, 43, 68** | **nenhuma** | 1 por tipo: T1 q52, T2 q47, T3 q68, T4 q65 |

- Estrutura, edital e corte são os mesmos da Enfermagem. Ver o levantamento do Enfermare, seção A.1.
- **As q1–20 são idênticas entre as profissões.** Em 2026, o gabarito das q1–20 do Tipo 1 é o mesmo em Enfermagem, Fisioterapia, Farmácia e Nutrição: `EAACBACDEDADDCBECAEA`. Essas 20 questões já estão no banco do Enfermare. Para o app novo valem só as q21–100.
- Os cadernos têm texto extraível, e o script achou 100 alternativas (A) a (E) em cada um.
  - As imagens dos cadernos ficam só na capa e na contracapa. Em 2025 há imagens pequenas na pág. 2 (instruções).
  - Não achei questão que dependa de figura, mas vale conferir durante a extração.

| Edição | Caderno (URL oficial) | Gabarito definitivo | Arquivo local |
|---|---|---|---|
| 2026/27 [oficial] | base `https://enare2026.conhecimento.fgv.br`. T1 `/docs/32fa57ca8c6881438dadfe28c6f34fb8.pdf?v=e7b0c4fa`, T2 `/docs/32fa57ca8c6881689461ee4c9c2dd247.pdf?v=2300ee53`, T3 `/docs/32fa57ca8c6881688443ccbd0a0022b0.pdf?v=e65c9a48`, T4 `/docs/32fa57ca8c688154932ee923a804c65c.pdf?v=0df9a3f3`. Lista no JSON embutido da [página Provas](https://enare2026.conhecimento.fgv.br/provas/) | `/docs/32fa57ca8c68815597a3e7f90baee852-definitivo.pdf?v=caa07b1d`, bloco "Fisioterapia - N - Turno Tarde" | `enare2026_fisio_tipo1..4.pdf`, `enare2026_multi_gab_definitivo.pdf` |
| 2025/26 [oficial] | `https://storage.googleapis.com/website-enare-2025/assets/provas/res-multi/multi-fisioterapia-cns007-tipo-{1,2,3,4}.pdf` (bucket listável) | `.../assets/provas/gabaritos/enare2025-multiprofissional-gabaritos-definitivos.pdf` | `enare2025_fisio_tipo1..4.pdf`, `enare2025_multi_gab_definitivo.pdf` |
| 2024/25 [oficial] | `https://mapa-vagas-enare-ebserh.conhecimento.fgv.br/provas-gabaritos/multiuni/Provas/FISIOTERAPIA%20(FISIOTT01).pdf`. A página só lista o Tipo 1, e os nomes testados para o Tipo 2 dão 404 | `.../multiuni/ENARE2024%20Gabarito%20Definitivo%20-%20Multi_Uniprofissional.pdf`, bloco "FISIOTERAPIA (FISIOTT01) - PROVA TIPO 1" | `enare2024_fisio_tipo1.pdf`, `enare2024_multi_gab_definitivo.pdf` |

Também estão em `pdf/`: os Anexos III de 2024, 2025 e 2026 e os editais multi das três edições.

### A.2 Conteúdo programático de Fisioterapia (Anexo III): igual nas três edições

Comparei os três anexos. O texto é o mesmo; em 2026 os subitens 8.11.1–8.11.3 viraram 8.12–8.14.
- [Anexo III 2026](https://enare2026.conhecimento.fgv.br/docs/36fa57ca8c6880cbb9cdca4ab9636daf.pdf?v=363f342b) [oficial]
- `txt/enare_fisio_topicos_2026.txt`

**8. FISIOTERAPIA**
- 8.1 A Fisioterapia e o aspecto biopsicossocial das coletividades humanas.
- 8.2 Saúde funcional na APS em todas as fases do ciclo da vida e em populações vulneráveis.
- 8.3 Vigilância dos distúrbios cinesiofuncionais.
- 8.4 **Ventilação mecânica invasiva e não invasiva.**
- 8.5 Avaliação funcional e atendimento do paciente crítico e não crítico.
- 8.6 Programas e políticas públicas de saúde e a Fisioterapia.
- 8.7 Métodos de avaliação funcional em fisioterapia cardiorrespiratória, neurofuncional e musculoesquelética do adulto; diagnóstico cinético-funcional.
- 8.8 Recursos e técnicas nas afecções respiratórias, cardiovasculares, traumato-ortopédicas, neurológicas, reumatológicas e oncológicas.
- 8.9 Análise e interpretação de exames complementares.
- 8.10 Ética, deontologia e prática baseada em evidências.
- 8.11 Habilidades e atitudes das DCN da graduação passíveis de prova teórica. Entram aqui 8.12, 8.13 e 8.14:
  - 8.12 Avaliação fisioterapêutica: anamnese, exame físico, avaliação cinesiofuncional.
  - 8.13 Comunicação com o paciente e com a equipe.
  - 8.14 Intervenções: eletrotermoterapia, cinesioterapia, drenagem linfática, terapias respiratórias.

**Conhecimentos gerais (item 1, comum a todas as profissões):** os mesmos 12 itens de SUS, RAS, PNAB, PNEPS, PNH, PNVS, bioética, PNSP, equipe multiprofissional e NR 32. Ver a seção A.2 do levantamento do Enfermare.

Peso para a taxonomia: a lista é curta e genérica. A cobrança real nos cadernos é muito cardiorrespiratória e de terapia intensiva (VM, VNI, desmame, gasometria), seguida de neurofuncional, traumato-ortopedia, saúde da mulher e pediatria/neonatologia. A taxonomia pode partir dos editais da EBSERH e da COFFITO (seções B.3 e E).

---

## B) EBSERH: Fisioterapeuta

### B.1 EBSERH 2024 (Concurso 01/2024, Edital nº 03, Área Assistencial), FGV, prova em 16/03/2025 [oficial]

- **Um caderno único, o "Grupo 7 – Fisioterapia" (turno da manhã)**, vale para os 8 cargos:
  - Fisioterapeuta;
  - Especialista em Fisioterapia Cardiovascular;
  - Especialista em Terapia Intensiva, em quatro versões: geral, Neonatologia, Pediatria e Adulto;
  - Especialista em Saúde da Mulher;
  - Especialista em Fisioterapia Respiratória.
- 60 questões A–E, 4 h, mínimo de 30 pontos.
- Distribuição: LP q1–10 (0,4), Legislação EBSERH q11–15, Políticas Públicas q16–30 e **Específicos q31–60 (1,2 ponto cada)**.
- **Comuns:** as q1–30 são as mesmas do caderno de Enfermagem (Grupo 4, manhã), com gabarito idêntico no Tipo 1. Já estão no Enfermare. Só as **q31–60 (30 questões)** são de Fisioterapia.
- Gabarito definitivo: **nenhuma anulada** em Fisioterapia, nos tipos 1 a 4.

| Caderno | Gabarito definitivo | Arquivo |
|---|---|---|
| `https://conhecimento.fgv.br/sites/default/files/concursos/grupo-7-fisioterapiae3cnsgp07-tipo-{1,2,3,4}.pdf` | `https://conhecimento.fgv.br/sites/default/files/concursos/ebserrhassistencial2024_gabarito_definitivo.pdf`, seção "Grupo - Fisioterapia - TIPO 1..4" | `ebserh2024_fisio_grupo7_tipo1..4.pdf`, `ebserh2024_assist_gab_definitivo.pdf`, `ebserh2024_edital3_assistencial.pdf` |

**Conteúdo do Grupo 7 (Anexo VII do edital)**, em 9 itens:
1. Métodos e técnicas de avaliação, tratamento e procedimentos.
2. Provas de função muscular.
3. Cinesiologia e biomecânica.
4. Análise da marcha.
5. Exercícios terapêuticos e treinamento funcional.
6. Hidro, massoterapia, mecanoterapia, crioterapia, eletroterapia e termoterapia superficial e profunda: indicações, contraindicações, técnicas e efeitos.
7. Órteses e próteses.
8. Anatomia, fisiologia, fisiologia do exercício, fisiopatologia, semiologia e procedimentos em:
   - neurologia e neuropediatria;
   - ortopedia e traumatologia;
   - cardiologia e pneumologia;
   - ginecologia e obstetrícia;
   - geriatria.
9. Ética profissional.

O texto está em `txt/ebserh2024_edital3_assistencial.txt`, linhas 6718–6724.

### B.2 EBSERH 2023 (Concurso 01/2023, Edital nº 03), IBFC, prova em dez/2023 [oficial]

- Servidor oficial: `fs.ibfc.org.br`. O link sumiu da página do concurso, mas os arquivos continuam no ar. É o mesmo caminho usado no Enfermare.
  - Caderno: `https://fs.ibfc.org.br/arquivos/2317/caderno_area_assistencial_outghw/pdf/CADERNO_IBFC_<cód>.pdf`. A lista de cargos está no JS de `.../caderno_area_assistencial_outghw/`.
  - Gabarito definitivo pós-recurso: `https://fs.ibfc.org.br/arquivos/2317/AGabarito_pierw%C3%A7assistencialsf/pdf/GABARITO_DEFINITIVO_ASS_IBFC_<cód>.pdf`.
- Estrutura: 60 questões A–E.
  - q1–10 Português, q11–20 Raciocínio Lógico, **q21–30 Legislação SUS**, q31–40 Legislação EBSERH, **q41–60 Conhecimentos Específicos**.
- **Comuns:** as q1–40 se repetem nos 8 cadernos e são as mesmas da Enfermagem 2023. O gabarito das q21–30 é `CBEADCAEDB`, igual ao do Enfermare.
- **As 20 específicas são diferentes em todos os 8 cargos**: comparei os textos e nenhuma se repete.

| Cód | Cargo | Anuladas (específicas) | Arquivos |
|---|---|---|---|
| 165 | Fisioterapeuta | — | `ebserh2023_fisio_165_fisio_caderno.pdf` / `_gabdef.pdf` |
| 166 | Esp. Fisioterapia Cardiovascular | 43 | `..._166_cardio_...` |
| 167 | Esp. Fisioterapia Respiratória | 49 | `..._167_resp_...` |
| 168 | Esp. Fisioterapia na Saúde da Mulher | — | `..._168_mulher_...` |
| 169 | Esp. Terapia Intensiva | 49, 55, 58 | `..._169_uti_...` |
| 170 | Esp. Terapia Intensiva, Adulto | 41, 52 | `..._170_uti_adulto_...` |
| 171 | Esp. Terapia Intensiva, Neonatologia | 43 | `..._171_uti_neo_...` |
| 172 | Esp. Terapia Intensiva, Pediatria | — | `..._172_uti_ped_...` |

- Total: 160 específicas, menos 8 anuladas, dá **152**.
- As anuladas saíram do `pdftotext -layout`, onde o asterisco aparece na grade. Na extração, refazer a leitura por geometria, como no Enfermare.
- Não procurei retificação posterior do definitivo de Fisioterapia. A de Enfermagem (Edital nº 20/2024) não toca nestes cargos, mas vale abrir o edital 20 inteiro.

### B.3 Depois de 2024
- Igual à Enfermagem: não há concurso nacional novo da EBSERH com prova para fisioterapeuta.
- **EBSERH 2019 (IBFC):** só existe gabarito preliminar público. Fica fora, pelo mesmo motivo que na Enfermagem.

---

## C) Residências com caderno público de Fisioterapia

| Instituição / edição | Formato | Caderno [oficial] | Gabarito [oficial] | Anuladas | Arquivo local |
|---|---|---|---|---|---|
| **UFPA (CEPS), Multi 2026** (prova em 02/11/2025) | 50 q A–E: 15 SUS + 35 específicas | `https://www.ceps.ufpa.br/images/conteudo/residencia/Multiprofissional%202026/provas%20gabaritos/Prova/Prova_Fisioterapia.pdf` | `.../Multiprofissional%202026/provas%20gabaritos/GabaritoDefinitivo/Gabarito%20Definitivo_Fisioterapia.pdf` | 12 | `ufpa2026_multi_prova_fisio.pdf`, `ufpa2026_multi_gab_def_fisio.pdf` |
| UFPA Multi 2025 | igual | `.../Multiprofissional%202025/provas%20gabaritos/PROVA%20DE%20FISIOTERAPIA.pdf` | `.../definitivo/GABARITO%20DEFINITIVO%20DE%20FISIOTERAPIA.pdf` | 7, 9, 50 | `ufpa2025_*` |
| UFPA Multi 2024 | igual | `.../Multiprofissional%202024/provas%20gabaritos/6-PROVA%20DE%20FISIOTERAPIA.pdf` | `.../definitivo/GABARITO_DEFINITIVO_DE_FISIOTERAPIA.pdf` | 30 | `ufpa2024_*` |
| UFPA Multi 2023 | igual | `.../Multiprofissional%202023/provas%20gabaritos/PROVA%20DE%20FISIOTERAPIA.pdf` | `.../definitivo/7GABARITO%20DEFINITIVO%20DE%20FISIOTERAPIA.pdf` | 3, 5, 31 | `ufpa2023_*` |
| **UNICAMP (COREMU/FCM/COMVEST) 2026**, Programa em Fisioterapia Hospitalar (61) e "Compromisso Social" (62) | 40 q A–D: q1–20 parte geral, comum a todos os programas, + q21–40 específicas; mais dissertativas | `https://portal.fcm.unicamp.br/wp-content/uploads/sites/58/2025/11/61-PROGRAMA-EM-FISIOTERAPIA-HOSPITALAR.pdf` e `.../62-PROGRAMA-EM-FISIOTERAPIA-HOSPITALAR-COMPROMISSO-SOCIAL.pdf`. **Os dois cadernos são idênticos** (99,9% das palavras) | `.../Gabarito-provas-objetivas-2026-1.pdf` (13/11/2025, com anulações), pág. 15 | 19 (geral) | `unicamp2026_fisio_61_*.pdf`, `unicamp2026_fisio_62_*.pdf`, `unicamp2026_multi_gabarito_13nov2025.pdf` |
| **HCPA (FUNDMED) 2025**, 1º edital | 40 q A–D; q1–~15 SUS comum a todas as categorias; Fisioterapia nas págs. 39–46 do PDF | `https://fundmed.org.br/website/wp-content/uploads/2025/04/HCPA-PROCESSO-SELETIVO-PARA-RESIDENCIA-MULTIPROFISSIONAL-2025-1o-EDITAL.pdf` | `.../2025/04/HCPA-GABARITO-MULTI-2025-1o-EDITAL.pdf` (**imagem**, pág. 2) | 20 | `hcpa2025_multi_prova.pdf`, `hcpa2025_multi_gabarito.pdf` |
| HCPA 2025 suplementar | 25 q A–D, págs. 20–25 | `.../2025/04/HCPA-PROCESSO-SELETIVO-SUPLEMENTAR-PARA-RESIDENCIAS-MULTIPROFISSIONAIS-2025.pdf` | `.../HCPA-GABARITO-MULTI-2025-SUPLEMENTAR-1.pdf` (**imagem**) | 18 | `hcpa2025supl_*` |
| HCPA 2024 | 40 q A–D, págs. 37–45 | `.../2024/04/2024-HCPA-Residencia-Multi-e-Uni.pdf` | `.../2024-HCPA-Residencia-Multi-e-Uni-GABARITO.pdf` | 40; a q37 foi alterada para A | `hcpa2024_*` |
| HCPA 2022 | 40 q A–D, págs. 37–45 | `.../2024/04/2022-HCPA-Residencia-Multi-e-Uni.pdf` | `...-GABARITO.pdf` | 21 | `hcpa2022_*` |
| HCPA 2023 | — | **O PDF publicado não tem o caderno de Fisioterapia.** Ele traz Física Médica 2022 duplicada no lugar | O gabarito existe e tem bloco FISIOTERAPIA; a q40 foi anulada | — | só `hcpa2023_multi_gabarito.pdf` |
| **UFCSPA (FUNDMED) 2025** | 40 q A–D, págs. 32–43; q1–15 comum | `.../2025/04/UFCSPA-PROCESSO-SELETIVO-PARA-RESIDENCIA-MULTIPROFISSIONAL-2025.pdf` | `.../UFCSPA-GABARITO-MULTI-2025-1o-EDITAL.pdf` (**imagem**) | 13 (comum), 16 | `ufcspa2025_*` |
| UFCSPA 2025 suplementar | 40 q A–D (caderno só de Fisioterapia) | `.../2025/04/UFCSPA-PROCESSO-SELETIVO-SUPLEMENTAR-PARA-RESIDENCIAS-MULTIPROFISSIONAL-2025.pdf` | `.../UFCSPA-GABARITO-MULTI-2025-SUPLEMENTAR.pdf`: **só PRELIMINAR**, em imagem | ? | `ufcspa2025supl_*` |
| UFCSPA 2024 suplementar | 40 q A–D (só Fisioterapia) | `.../2024/04/2024-UFCSPA-Residencia-Multi-e-Uni-Suplementar.pdf` | `...-Suplementar-GABARITO.pdf` | 30 | `ufcspa2024supl_*` |
| UFCSPA 2023 | 40 q A–D, págs. 31–41 | `.../2024/04/2023-UFCSPA-Residencia-Multi-e-Uni.pdf` | `...-GABARITO.pdf` | 31; a q28 foi retificada para B | `ufcspa2023_*` |
| UFCSPA 2022 | 40 q A–D, págs. 33–44 | `.../2024/04/2022-UFCSPA-Residencia-Multi-e-Uni.pdf` | `...-GABARITO.pdf` | 38, 39; q11 e q27 retificadas para D | `ufcspa2022_*` |
| **UERJ (CEPUERJ), Residência Saúde, Uniprofissional Fisioterapia** 2022–2026 | 25 q **A–D**: q1–5 SUS + q6–25 Fisioterapia. Há também uma prova discursiva por programa, que não baixei | página `https://www.cepuerj.uerj.br/concursos2.php?concurso=S00270&ano=AAAA`, com os links num `<select>`. URLs exatas em `aux/` e na lista abaixo | "Uniprofissional" pós-recurso (2022, 2025, 2026). Em 2023 e 2024, só o arquivo "Gabarito", sem o rótulo pós-recurso | 2026: q25. Demais: nenhuma | `uerj20NN_fisio_uni_prova.pdf`, `uerj20NN_uni_gab*.pdf` |
| **SES-PE (IAUPE/UPENET), Residência Multi** 2023–2026 | 50 q A–E. Hospitalar (cad. 53): q1–20 gerais (iguais à Enfermagem) + **q21–50 específicas**. Atenção Básica (73): q1–30 gerais + **q31–50**. Saúde Coletiva (86) e Interiorização (173) **repetem as q31–50 da AB**; em 2026 a Interiorização repete 45 das 50 da AB. Regionalização (183/173): caderno próprio | ver abaixo | ver abaixo | ver abaixo | `sespe20NN_*` |

Notas da UERJ:
- Em 2026 há três PDFs, um por programa: Cardiorrespiratória/TI, Neuro-Ortopédica e Pediatria/Neonatologia. **As 25 objetivas são idênticas** nos três, e o gabarito é uma linha só.
- Nenhuma questão se repete entre os anos.
- Na página da CEPUERJ, o parâmetro `ano` é o ano da edição: as provas de `ano=2026` foram aplicadas em nov/2025. Os arquivos locais seguem a edição.
- A "Saúde do Idoso – Fisioterapia" é só discursiva (4–5 questões) e ficou fora.

SES-PE, por edição [oficial, `https://www.upenet.com.br/`]. A lista completa de URLs está em `/private/tmp/.../scratchpad/fisio-scripts/sespe_lista.txt`.
- **2026** (`concursos/2026/26_RED_MULTI/`), prova em 11/01/2026:
  - cadernos 53, 73, 173 e 86 em `provas-e-gab/PROVAS/...`;
  - gabaritos definitivos multicategoria em `provas-e-gab/GABARITOS DEFINITIVOS/`;
  - **Saúde Coletiva Regionalização (183) foi ANULADA e reaplicada em 01/02/2026** (Comunicado nº 002). Use `Reaplic/PROVAS/183 ...` e o "GABARITO DEFINITIVO PERFIL SAUDE COLETIVA REGIONALIZACAO REAPLICACAO". O original anulado ficou como `sespe2026_183_screg_fisio_original_ANULADA.pdf`;
  - anuladas: 53 nenhuma, 73 nenhuma, 173 q4, 86 q7 e q23, 183-reaplicação q6 e q34.
- **2025** (`concursos/25_REDMULT/`):
  - **as quatro provas de Fisioterapia de 22/12/2024 foram ANULADAS** (Comunicado nº 005, por recursos) e reaplicadas em 12/01/2025;
  - valem os cadernos `Reaplicacao/Provas/CADERNO 53|73|86|173 ...` e os definitivos `GABARITOS/Definitivos/Reaplicacao/...`;
  - Hospitalar: há um "REPUBLICADO 2025.2" que **troca a q50 de D para E**, e o arquivo local é `sespe2025_gab_hosp_fisio_repub.pdf`;
  - anuladas: 53 q6 e q35; 73, 86 e 173 nenhuma;
  - **o caderno 73 (AB) reaplicado é escaneado, sem texto**, e precisa de OCR.
- **2024** (`concursos/24_Resid_Mult/`):
  - cadernos de Hospitalar, AB e SC em `Provas-e-gabaritos/PROVAS/...`, mais a Regionalização reaplicada (`Provas-e-gabaritos-reaplicacao/`, gabarito com caderno 173);
  - gabaritos: Hospitalar definitivo, e AB e SC "republicados 31/01/2024";
  - anuladas: Hospitalar q25; AB q3, q28 e q34; SC q34; Regionalização q40.
- **2023** (`concursos/23_Resid_Mult/Provas_Gab/`):
  - cadernos `53_HOSPITALAR FISIOTERAPIA 2023.pdf`, `73_...` e `86_...`;
  - gabaritos definitivos 221228 (Hospitalar) e 221227 (AB e SC);
  - anuladas: Hospitalar q15, q23, q30, q31 e q45; AB q4, q7, q25, q30 e q43; SC q43.

**Não achei, ou não serve:**
- **HCFMUSP 2026**: o gabarito tem bloco de Fisioterapia (opções 004, 007, 015, 020, 024, 028, 031 e 033), mas o caderno não está público. Arquivo `hcfmusp2026_multi_gabaritos.pdf`; a API de mídia do site não respondeu.
- **ESP-CE**: a RIS-ESP/CE seleciona pelo **ENARE**, segundo um edital de matrícula ENARE 2025/26 publicado pela ESP-CE ([ce.gov.br](https://www.ce.gov.br/esp/wp-content/uploads/sites/84/2026/01/Edital_Enare_Resmulti.pdf)). Logo, o ENARE já cobre o Ceará.
- **UEL (residência em Fisioterapia)**: publica só gabaritos provisório e definitivo de 2023 a 2025 (`sites.uel.br/proppg/wp-content/uploads/...FISIOTERAPIA-NOV-2025-DEFINITIVO.pdf`). Não achei caderno na mídia do site.
- **UFES** (`concursos.ufes.br/residenciaemsaude`): o servidor não respondeu (conexão recusada).
- **ESP-PB COREMU 2026** e **CMMG**: apareceram na busca só com gabarito; não segui.
- Não procurei: UNIFESP, USP/FUVEST, UFRJ, UFSC e UFMG. A HCFMUSP faz a própria seleção; FUVEST e UNIFESP não apareceram com caderno multi na Enfermagem.

---

## D) Concursos de fisioterapeuta com caderno e gabarito oficiais

### D.1 Militares

| Força | Situação | Arquivos |
|---|---|---|
| **Marinha, CP-CSM-S (Quadro de Apoio à Saúde), Fisioterapia** [oficial] | 50 q A–E por ano; uso a prova AMARELA. **Os cadernos são escaneados (sem texto) e exigem OCR**, como na Enfermagem. O gabarito final é um PDF único com todas as áreas; o bloco "Fisioterapia" está nas colunas AMARELA/ROSA ou AZUL. Anuladas na amarela: 2021 q1; 2022 nenhuma; 2023 q3, q9 e q36; 2024 q2 e q11; 2025 q39 e q42. **2026: o caderno saiu (zip), mas o gabarito final ainda não** | `marinha2021..2026_fisio_amarela.pdf`, `marinha2021..2025_gab_final.pdf` |
| Exército, EsFCEx | **Não tem Fisioterapia.** Os gabaritos de 2020 e 2025 listam só as áreas 001–042 de QC/Saúde, sem Fisioterapia | — |
| Aeronáutica, EAOAP (CIAAR) | **Não verificado.** O site `www2.fab.mil.br/ciaar` responde 403 (Cloudflare) ao curl. O Enfermare só leu a FAB pelo Chrome. Fica como lacuna | — |

URLs da Marinha [oficial]: base `https://assets.marinha.mil.br/sspm/sites/www.marinha.mil.br.sspm/files/provas/`.
- Arquivos por ano:
  - 2025: `CSM-S-FISIOTERAPIA_AMARELA.pdf`
  - 2024: `CP-CSM-S-2024_FISIOTERAPIA_AMARELA.pdf`
  - 2023: `CP-CSM-S_FISIOTERAPIA_AMARELA.pdf`
  - 2022: `CP-CSM-S_FISIOTERAPIA_PROVA%20AMARELA.pdf`
  - 2021: `Fisioterapia%20Amarela.pdf`
  - 2026: `CSM-S%202026%20%7C%20Fisioterapia.zip`
- Também existem 2011–2017. Peguei os nomes de arquivo num snapshot do Wayback da página `marinha.mil.br/sspm/csm/quadro-apoio-a-saude_princ`, porque a página está atrás de Cloudflare. Os PDFs vieram do servidor `assets.marinha.mil.br`.
- Os gabaritos estão em `.../files/arquivo/gabaritos/` (mesmos arquivos do Enfermare).

### D.2 Concursos civis (FGV, IBADE, Selecon)

Todos têm gabarito definitivo ou final [oficial].

| Concurso | Caderno | Gabarito | Questões; parte de Fisioterapia | Anuladas | Arquivo |
|---|---|---|---|---|---|
| FGV, FHEMIG 2023, AGAS Fisioterapeuta I (CNS114) | `conhecimento.fgv.br/sites/default/files/concursos/analista-de-gestao-e-assistencia-a-saude-agas-fisioterapeuta-nivel-icns114-tipo-1.pdf` | `.../gabarito-definitivo-fhemig-retificado-01.11.2023.pdf` | 45 A–E; específicas ≈ q30–45 | 6 (geral) | `fgv_fhemig2023_fisio_cns114_tipo1.pdf`, `fgv_fhemig2023_gab_def.pdf` |
| FGV, FHEMIG 2023, Fisioterapeuta Respiratório III (CNS115) | `...-fisioterapeuta-respiratorio-nivel-iiicns115-tipo-1.pdf` | mesmo | 45 A–E; ≈ q30–45 | 6, 40 | `fgv_fhemig2023_fisioresp_cns115_tipo1.pdf` |
| FGV, SES-MT 2023/24, Fisioterapeuta (CNS319) | `.../cns319-fisioterapeuta-cns319-tipo-1.pdf` | `.../gabarito-definitivo-ses-mt-v2.pdf` | 80 q **A–D**; Legislação do SUS ≈ q37–46; específicas ≈ q47–80 | 30, 31, 40, 53, 55 | `fgv_sesmt2024_*` |
| FGV, Pref. Canaã dos Carajás (Edital 01/2024, prova em 23/03/2025), Fisioterapeuta (CNS203) | `.../fisioterapeutacns203-tipo-1.pdf` | `.../prefcanaa202401_gabarito_definitivo-compilado-23.03_0.pdf` | 60 A–E; Módulo II, específicas ≈ q31–60 | nenhuma | `fgv_canaa2025_*` |
| FGV, MPES 2026, Agente Técnico – Fisioterapeuta (CNS120) | `.../agente-tecnico-fisioterapeuta-cns120-tipo-1.pdf` | `.../gabarito-definitivo-mpes-servidor-31082026.pdf` | 60 A–E; específicas ≈ q22–60 | nenhuma | `fgv_mpes2026_*` |
| FGV, SMS Nova Iguaçu, Fiscal Sanitário – Fisioterapia (CNS012) | `.../fiscal-sanitario-fisioterapia-cns012-tipo-1.pdf` | `.../gabarito-definitivo-smsnovaiguacu.pdf` | 40 A–E; quase tudo é vigilância sanitária, Fisioterapia ≈ q33–40 | 34, 35 | `fgv_novaiguacu_*` (pouco útil) |
| IBADE, Pref. Joinville 2024, Fisioterapeuta (0066) | zip `ibade.selecao.site/arquivo.php?file=edital/1/76/2795187e8b294a40c7151ecd0b775437.zip` (`SUPERIOR/0066- FISIOTERAPEUTA/... Tipo 1.pdf`) | `ibade.selecao.site/arquivo.php?file=edital/1/76/01707c9e604166ad0a43f2a4bb611d7a.pdf` (final, 05/06/2024) | 50 A–E; específicas q31–50 | 1, 8, 11, 17, 20, 31 | `ibade_joinville2024_*` |
| IBADE, Pref. Recife 2024, Fisioterapeuta 20 h (S10) e 30 h (S11) | zip `.../edital/1/69/01919fca55b1cfdae66aa3d118840daf.zip` | `.../edital/1/69/1ca836fac7a1127bed8d03c1e3221fec.pdf` (final, 25/04/2024) | 50 A–E cada; q1–25 comuns (S10 = S11); específicas q26–50, diferentes entre S10 e S11 | S10: 3; S11: 3, 30, 33 | `ibade_recife2024_fisio20h_*`, `..._fisio30h_*`, `ibade_recife2024_gab_final_demais.pdf` |
| Selecon, Hemominas 2025, Analista – Fisioterapeuta (512) | PDF do nível superior, págs. 96–104 (`anexos.cdn.selecao.net.br/uploads/746/concursos/49/anexos/72701fcf-abef-4db5-a878-1afbb2dd48c0.pdf`) | `.../concursos/49/anexos/33f2e67f-f97e-4170-9ff4-c45dc085f00d.pdf` (definitivo) | 60 A–D; Saúde Pública q11–20 + específicas q31–60 | 16 | `selecon_hemominas2025_*` |
| Selecon, Pref. Primavera do Leste-MT 2023, Fisioterapeuta (426) | PDF do nível superior, págs. 137–143 (`.../concursos/19/anexos/gnTj113msITvn5qKSyAX5yb2fi4L8pHkxsrCaUa9.pdf`) | arquivo "gabarito final retificado 19/11" baixado pelo Enfermare (`selecon_primavera2023_gab_final_retif_1911.pdf`); a URL exata não ficou registrada | 50 A–D; específicas q31–50 | nenhuma | `selecon_primavera2023_*` |
| Selecon, Pref. Campo Verde-MT 2023, Fisioterapeuta (403) | PDF do nível superior, págs. 15–20 | gabarito final retificado (`selecon_campoverde2023_gab_final_retif_sup.pdf`); a URL exata não ficou registrada | 40 A–D; específicas q21–40 | 16 (geral) | `selecon_campoverde2023_*` |

Não varri:
- outras FGV com Fisioterapia (as páginas de SJC, Macaé, Caraguatatuba e SES-TO não têm caderno de fisio);
- AOCP, que não publica caderno;
- Cebraspe, IDECAN e IBFC municipais.

O Instituto AOCP segue sem caderno na página pública, como no Enfermare.

---

## E) Título de especialista em Fisioterapia

**Mudança importante:** o título de Especialista Profissional em Fisioterapia **é concedido pelo COFFITO** por certame público nacional. As sociedades (ASSOBRAFIR etc.) são entidades credenciadas, e as páginas de "prova de título" da ASSOBRAFIR (certames 2021–2024) só mostram resultado, mediante CPF.

| Certame | Formato | Caderno público? | Arquivos |
|---|---|---|---|
| **COFFITO, Certame Público nº 1/2025** (IADES), prova on-line em 30/11/2025 [oficial] | 1ª fase objetiva on-line com **50 questões A–E, 4 h, eliminatória, mínimo de 70% (35 pontos)**. 2ª fase: títulos e experiência (10 pontos, mínimo 7). Requisito: 48 meses de registro no CREFITO. Taxa R$ 50. **Foram 18 especialidades de Fisioterapia com gabarito:** 101 Acupuntura, 102 Respiratória, 103-1/2/3 Neurofuncional (infância e adolescência, adulto e idoso, vestibular), 104 Osteopatia, 105 Quiropraxia, 107 Esportiva, 108 do Trabalho, 109 Dermatofuncional, 110 Saúde da Mulher, 111 Oncologia, 112-1/2/3 Terapia Intensiva (neo, pediatria, adulto), 114 Cardiovascular, 115 Gerontologia, 116 Reumatologia | **Gabarito oficial público, caderno não.** Os "Gabaritos oficiais" de 26/12/2025 trazem anuladas marcadas com `*` (ex.: 101 com 7 anuladas, 102 com 1). O edital (item 9.1) diz que o caderno seria divulgado com o gabarito preliminar, mas ele não está entre os arquivos da pasta `upload/1362`. Vi a lista pelo CDX do Wayback e baixei 25 arquivos do servidor IADES: nenhum é caderno. Provavelmente ficou só na área do candidato | `coffito2025_edital01_titulo_especialista.pdf` (`iades.com.br/inscricao/upload/1362/2025100181112630.pdf`), `coffito2025_gab_oficial_fisio.pdf` (`.../1362/20251226125342375.pdf`), `coffito2025_gab_preliminar_a.pdf` (`.../1362/20251130214642972.pdf`), comunicados |
| **COFFITO, Edital nº 1/2026** (IADES), **inscrições de 08/10 a 25/11/2026, prova on-line em 06/12/2026** [oficial] | Mesmo formato: 50 q A–E, 4 h, 70%. A prova tem **5 dimensões**: 1) Normas gerais e regulamentação profissional; 2) Conhecimentos básicos da especialidade; 3) Prática baseada em evidências; 4) Prática específica da especialidade; 5) Outras questões relevantes. São 20 especialidades de Fisioterapia; entram **106 Traumato-Ortopédica** e **113 Aquática**. Base: Res. COFFITO 627/2025, 630/2025 e 631/2025 | **O edital promete "gabarito preliminar e caderno de questões" em 07/12/2026** (item 9.1) no site do IADES. É a primeira chance real de caderno de título de Fisioterapia; vale um lembrete para baixar no dia | `coffito2026_edital01_titulo_especialista.pdf` (`iades.com.br/inscricao/upload/1378/202610071049598.pdf`), **`coffito2026_anexoI_conteudos_referencias.pdf`** (31 págs., conteúdo e bibliografia por especialidade: `.../1378/20261007103621695.pdf`), `coffito2026_cronograma.pdf`. Página: `iades.com.br/inscricao/ProcessoSeletivo.aspx?id=6cd9442b26` |

**Conclusão para o produto:**
- Até dez/2026, questão de título é **autoral**. O modelo é o formato COFFITO: 50 q A–E, 4 h, 70%, e as 5 dimensões.
- A bibliografia sai do Anexo I de 2026.
- ABRAFIN, SONAFE, ABRAFITO, ABFO e afins não são mais a via do título. Não procurei editais próprios delas.

---

## F) Normas e diretrizes que o banco precisa refletir (out/2026)

| Tema | Situação em out/2026 | Fonte |
|---|---|---|
| **Profissão** | **Decreto-Lei 938/1969**, que regula a profissão; ver art. 3º (atividade privativa). **Lei 6.316/1975**, que cria o COFFITO e os CREFITOs. Pelo meu conhecimento, a **Lei 8.856/1994** fixa a jornada de 30 h semanais (não conferi nesta sessão). | Leis federais (planalto.gov.br); não baixadas |
| **Código de Ética** | **Res. COFFITO 424/2013** (Fisioterapia; a TO tem a 425/2013), vigente. **Armadilha:** os **arts. 37 e 39** (honorários) estão **revogados por decisão do CADE** (PA 08700.003473/2021-16). Questão antiga que cobra "valor mínimo de honorários" está desatualizada. | [COFFITO, página da Res. 424](https://www.coffito.gov.br/nsite/?p=3187) [oficial] |
| **Título de especialista** | **Res. COFFITO 630/2025** (30/07/2025) regulamenta o título em Fisioterapia e **revoga a Res. 377/2010**. A **Res. 627/2025** cria o **RQE** (Registro de Qualificação de Especialista), que substitui o RPE; a **Res. 636/2025** muda a numeração do RQE. A Res. 603/2025 credencia as entidades de especialidade. Questão antiga sobre "Res. 377" ou "RPE" está desatualizada. | edital COFFITO 2025/2026 [oficial]; textos em [normasbrasil 630](https://www.normasbrasil.com.br/norma/resolucao-630-2025_483613.html), [627](https://www.normasbrasil.com.br/norma/resolucao-627-2025_483584.html), [636](https://www.normasbrasil.com.br/norma/resolucao-636-2025_486433.html) [secundária] |
| **Especialidade Terapia Intensiva** | **Res. COFFITO 402/2011**, ainda citada no conteúdo da especialidade 112-3 (alteração do edital de 03/11/2025). | alteração do edital 1/2025 [oficial] |
| **Parâmetros assistenciais** | **Res. COFFITO 387/2011, alterada pela 444/2014**. Não achei revogação, e protocolos da EBSERH de 2025 ainda a citam. Não conferi no site do COFFITO (lento). | [normasbrasil 444](https://www.normasbrasil.com.br/norma/resolucao-444-2014_275977.html) [secundária] |
| **UTI: RDC ANVISA 7/2010** | Art. 13: **fisioterapeuta coordenador**, especialista em TI ou em área ligada ao paciente grave, no máximo 2 UTI. Art. 14, IV: **fisioterapeutas, no mínimo 1 para cada 10 leitos ou fração, nos turnos matutino, vespertino e noturno, perfazendo 18 h diárias**. Art. 22: evolução registrada pela fisioterapia **em cada turno**. A **RDC 26/2012** mudou só a enfermagem (enfermeiro 1:10, técnico 1:2); **a fisioterapia não mudou**. Armadilha: "fisioterapia 24 h" não é exigência da RDC (há projetos de lei, sem lei federal que eu tenha confirmado). | [RDC 7/2010 (BVS)](https://bvsms.saude.gov.br/bvs/saudelegis/anvisa/2010/res0007_24_02_2010.html), [RDC 26/2012](https://bvsms.saude.gov.br/bvs/saudelegis/anvisa/2012/rdc0026_11_05_2012.html) [oficial] |
| **Telefisioterapia** | **Res. COFFITO 619/2025** (DOU de 09/07/2025). As fontes **divergem** sobre se revoga a 516/2020 (teleconsulta da pandemia): a ABMES diz que não revoga nada, um blog diz que revoga. **Conferir no DOU.** | [ABMES](https://abmes.org.br/legislacoes/detalhe/5208/resolucao-coffito-n-619) [secundária] |
| **Cuidados paliativos** | Pela imprensa, as **Res. COFFITO 660 e 661/2026** (24/08/2026) tratam da atuação em cuidados paliativos, e a 660 **revoga a 539/2021**. Não li o texto oficial. | [acritica.net](https://acritica.net/saude/coffito-resolucoes-cuidados-paliativos-fisioterapia-terapia-ocupacional/) [secundária] |
| **Limites de atuação** | Notícia do CREMERS (11/07/2022): a 1ª Turma do STJ derrubou trechos de normas do COFFITO que autorizavam "diagnosticar, prescrever exames, dar alta" sem médico. A notícia não diz as resoluções nem o processo. Tema que dá questão polêmica: o banco deve usar "diagnóstico cinesiológico-funcional" e evitar afirmar autonomia diagnóstica nosológica. | [CREMERS](https://cremers.org.br/mais-uma-vitoria-do-cremers-stj-derruba-resolucoes-que-ampliavam-atuacao-de-fisioterapeutas-e-terapeutas-ocupacionais) [secundária, parte interessada] |
| **Ventilação mecânica** | Base: **Recomendações Brasileiras de VM 2013** (AMIB/SBPT; J Bras Pneumol 2014;40(4):327-363 e 40(5):458-486). **Novo:** **"Orientações práticas de VM baseadas em evidências"**, declaração conjunta AMIB/SBPT, **J Bras Pneumol 2025;51(1):e20240255**: 38 tópicos e 75 especialistas, feita por revisões de escopo e não como diretriz GRADE. Não li o texto integral. | [PMC11796564](https://pmc.ncbi.nlm.nih.gov/articles/PMC11796564) [secundária: indexador, artigo oficial da sociedade] |
| **DPOC: GOLD 2026** | Publicado em 10/11/2025. **1 exacerbação moderada já basta para escalonar o tratamento** (critérios A/B/E ajustados); seção nova de **atividade de doença**; algoritmos separam tratamento inicial e de seguimento; capítulos de exacerbação e multimorbidade reescritos; vacinas (VSR, influenza) atualizadas; figura de biológicos. Armadilha: questões antigas usam ABCD (2017–2022) ou o limiar de ≥2 exacerbações moderadas. | `pdf/gold2026_key_changes.pdf` ([goldcopd.org](https://goldcopd.org/wp-content/uploads/2025/11/KEY-CHANGES-GOLD-2026-10Nov2025.pdf)) [oficial] |
| **Asma: GINA 2026** | Publicado em 05/05/2026. 4 fluxogramas novos de crise (APS e emergência, por faixa etária). **Com sinais de anafilaxia, adrenalina antes do broncodilatador.** **O2 só se SpO2 < 92%**, com alvo superior de 95% em adultos e crianças maiores. ICS-formoterol entra como opção na crise leve. Afasta-se ainda mais do SABA isolado. Só li resumos. | [ginasthma.org](https://ginasthma.org/2026-gina-strategy-report/) [oficial, não baixado]; [Guideline Central](https://www.guidelinecentral.com/insights/may-2026-gina-asthma-guideline-spotlight/) [secundária] |
| **RCP: AHA 2025** | Diretrizes AHA 2025 de RCP e ACE: cadeia de sobrevivência única, engasgo com 5 golpes nas costas mais 5 compressões abdominais, fim do termo "rescue breaths". Conferido no levantamento do Enfermare. | [Highlights AHA 2025](https://cpr.heart.org/-/media/CPR-Files/2025-documents-for-cpr-heart-edits-posting/Resuscitation-Science/252500_Hghlghts_2025ECCGuidelines.pdf) [oficial] |
| **Reabilitação cardiovascular** | Vigente no Brasil: **Diretriz Brasileira de Reabilitação Cardiovascular 2020** (SBC; Arq Bras Cardiol 2020;114(5):943-987; errata de 2021 na versão inglesa: intensidade de 50–80%). **Novo:** a **ESC publicou em set/2026 a primeira diretriz dedicada à reabilitação cardíaca**; só li reportagem. | [PMC8387006](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8387006/) [secundária: indexador]; [Afya](https://portal.afya.com.br/cardiologia/esc-2026-nova-diretriz-reforca-importancia-da-reabilitacao-cardiaca) [secundária] |
| **Reabilitação pulmonar** | Pelo meu conhecimento, a referência segue sendo o ATS/ERS Statement 2013 e a ATS Clinical Practice Guideline 2023. **Não conferi nesta sessão.** | — |
| **CIF** | OMS, 2001. Pelo meu conhecimento, o COFFITO adotou a CIF pela Res. 370/2009 e o CNS pela Res. CNS 452/2012. **Não conferi nesta sessão.** | — |
| **DCN da graduação** (o ENARE cobra no item 8.11) | Continua a **Res. CNE/CES 4/2002**. Há proposta de DCN nova (Parecer Técnico CNS 161/2017, Res. CNS 559/2017), mas não achei homologação pelo MEC. | [Res. CNE/CES 4/2002 (ABMES)](https://abmes.org.br/public/arquivos/legislacoes/res_ces_cne_04_190202.pdf) [secundária]; [Res. CNS 559/2017](https://www.gov.br/conselho-nacional-de-saude/pt-br/acesso-a-informacao/atos-normativos/resolucoes/2017/resolucao-no-559.pdf) [oficial] |

**Armadilhas de norma revogada ou desatualizada nas questões antigas** (para a triagem do BRIEF_REAIS):
1. Res. COFFITO 377/2010 (título): revogada pela 630/2025. O RPE virou RQE (627/2025).
2. Código de Ética 424/2013: arts. 37 e 39 (honorários) revogados (CADE). Questão que cobra "honorário mínimo" ou "referencial obrigatório" está errada hoje.
3. GOLD: classificação ABCD e limiar de ≥2 exacerbações estão superados (GOLD 2023: ABE; GOLD 2026: 1 exacerbação moderada).
4. GINA: SABA isolado como alívio no degrau 1 está superado desde 2019. O2 com alvo de 93–95% virou "< 92% para indicar" em 2026.
5. AHA 2020 → 2025 (cadeia única, engasgo).
6. VM: consenso de 2013 ainda é a base, mas há orientação prática de 2025. Questão que cita "III Consenso (2007)" é antiga.
7. RDC 7/2010: a fisioterapia segue 1:10 em 18 h. Cuidado com questões que trazem a proporção de enfermagem pré-2012 (1:8).
8. Telefisioterapia: 516/2020 x 619/2025 (situação a confirmar).
9. Cuidados paliativos: 539/2021 x 660/2026 (a confirmar no DOU).

---

## Inventário (`pdf/`, 161 arquivos)

Todos têm texto extraível, **exceto**:
- **Marinha 2021–2026**: cadernos escaneados, precisam de OCR.
- **SES-PE 2025, caderno 73 reaplicado**: escaneado.
- **Gabaritos em imagem**: HCPA 2025 (e suplementar) e UFCSPA 2025 (e suplementar). Transcrição em `txt/gabaritos_imagem_transcritos.txt`.

| Grupo | Cadernos | Gabaritos e outros |
|---|---|---|
| ENARE | 9 (2024 T1; 2025 T1–4; 2026 T1–4) | 3 definitivos, 3 Anexos III, 3 editais |
| EBSERH 2024 FGV | 4 (Grupo 7, T1–4) | definitivo e edital |
| EBSERH 2023 IBFC | 8 (cód. 165–172) | 8 definitivos |
| UFPA | 4 (2023–2026) | 4 definitivos |
| UNICAMP 2026 | 2 (idênticos) | 1 |
| HCPA (FUNDMED) | 4 PDFs multi com Fisioterapia (2022, 2024, 2025, 2025 suplementar) | 5 (inclui o de 2023, sem caderno) |
| UFCSPA (FUNDMED) | 5 (2022, 2023, 2024 suplementar, 2025, 2025 suplementar) | 5 (o de 2025 suplementar é preliminar) |
| UERJ | 7 (2022–2025; 2026 em 3 cópias idênticas) | 5 |
| SES-PE | 17 (2023: 3; 2024: 4; 2025 reaplicação: 4; 2026: 6, incluindo o 183 anulado) | 16, mais 2 comunicados de anulação |
| Marinha | 6 (2021–2026) | 5 finais |
| FGV municipais e estaduais | 6 | 5 |
| IBADE | 3 | 2 |
| Selecon | 3 PDFs multi-cargo | 3 |
| COFFITO (título) | 0 | editais 2025 e 2026, Anexo I de 2026, cronograma, gabarito oficial e preliminar de 2025, 2 comunicados |
| Normas | — | `gold2026_key_changes.pdf` |
| HCFMUSP 2026 | 0 | gabarito |

---

## Quantas questões de Fisioterapia aproveitáveis

Conta **só a parte específica de Fisioterapia**, já sem as anuladas e as duplicadas entre cadernos. Os blocos gerais e de SUS do ENARE, EBSERH, HCPA, UFCSPA e UNICAMP são os mesmos da Enfermagem e já estão no Enfermare.

| Fonte | Específicas aproveitáveis (aprox.) |
|---|---|
| ENARE 2024–2026 (Tipo 1) | 237 (3 × 80, menos 3 anuladas) |
| EBSERH 2024 | 30 |
| EBSERH 2023 (8 cargos) | 152 |
| UFPA 2023–2026 | ~137 (4 × 35, menos 3 anuladas; mais 60 de SUS, 2025 e 2026 provavelmente já no Enfermare) |
| UNICAMP 2026 | 20 |
| HCPA 2022, 2024, 2025 e 2025 suplementar | ~85 (25 por prova, menos as anuladas; o suplementar tem menos) |
| UFCSPA 2022, 2023, 2024 suplementar e 2025 | ~95, mais ~25 do 2025 suplementar (só gabarito preliminar) |
| UERJ 2022–2026 | 99 (5 × 20, menos 1) |
| SES-PE 2023–2026 | ~230 (Hospitalar 30 + AB 20 + Regionalização ~20–30 por ano; SC e Interiorização repetem a AB) |
| Marinha 2021–2025 | 242 (5 × 50, menos 8), **depende de OCR**; 2026 sem gabarito |
| FGV (FHEMIG ×2, SES-MT, Canaã, MPES, Nova Iguaçu) | ~140 |
| IBADE (Joinville, Recife ×2) | ~67 |
| Selecon (Hemominas, Primavera, Campo Verde) | ~70 |
| **Total** | **≈ 1.600 específicas de Fisioterapia com gabarito oficial.** Com o descarte de ~10% na triagem (gabarito com norma revogada, dependência de figura, duas respostas), devem sobrar **≈ 1.400–1.450** |

Formato misto:
- **A–E**: ENARE, EBSERH, UFPA, SES-PE, Marinha, FGV (menos SES-MT) e IBADE.
- **A–D**: HCPA, UFCSPA, UNICAMP, UERJ, SES-MT e Selecon.

O banco precisa de `n_alternativas` por questão.

## Lacunas, sem rodeios
- **Título de especialista:** não há caderno público. O COFFITO 2025 publicou só gabarito. O de 2026 promete o caderno para 07/12/2026.
- **ENARE 2024/25:** só o Tipo 1 de Fisioterapia está publicado (é o único que importa para o banco).
- **HCPA 2023:** o PDF oficial não tem o caderno de Fisioterapia; o gabarito existe.
- **UFCSPA 2025 suplementar:** só gabarito preliminar.
- **UERJ 2023 e 2024:** gabarito sem o rótulo "pós-recurso".
- **Aeronáutica (EAOAP):** não verificada (Cloudflare). **Exército:** não tem Fisioterapia.
- **Marinha 2026:** sem gabarito final.
- **Sem cadernos:** HCFMUSP 2026, UEL e ESP-PB (só gabarito). UFES fora do ar. Não procurei UNIFESP, USP, UFRJ, UFSC nem UFMG.
- **Não conferido no texto oficial:**
  - Res. COFFITO 619/2025: se revoga ou não a 516/2020.
  - Res. 660 e 661/2026.
  - Situação atual da 387/444 no site do COFFITO.
  - Lei 8.856/1994, Res. 370/2009 (CIF) e diretrizes de reabilitação pulmonar: citadas de memória, sem conferência.
- **Anuladas:** saíram de parsing de texto, e as da EBSERH 2023 do asterisco no layout. Antes de extrair, conferir por um segundo método, como no Enfermare.
