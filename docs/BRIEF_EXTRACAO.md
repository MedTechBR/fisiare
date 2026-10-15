# Brief — extração de provas reais para o Fisiare (15/10/2026)

Fisiare = app de estudo de FISIOTERAPIA (`~/Documents/Claude/fisiare/`), fork do Enfermare
(`~/Documents/Claude/enfermare/`, que já extraiu milhares de questões por este método). Você extrai
questões VERBATIM de cadernos oficiais públicos já baixados em `provas-reais/` (texto em `provas-reais/txt/`:
`.txt` = pdftotext -layout, `.raw` = modo simples). Referência de método (só leitura): `~/Documents/Claude/enfermare/docs/PROVAS_REAIS.md`, `~/Documents/Claude/enfermare/provas-reais/relatorios/extracao_*.md`
e os scripts de `docs/extracao/` (vieram do CirurgiaMed via Enfermare; `gabgeo.py` lê gabarito FGV pela geometria com PyMuPDF).
PyMuPDF (`import fitz`) e pdftotext existem na máquina.

## Saída (só estes arquivos)
1. `provas-reais/cand_<sufixo>.json`: lista de `{"id","q","alts","gab","fonte"}`.
   - `id`: `<prova>-<NN>` (ex.: `en25-fis-07`).
   - `q`: enunciado completo, verbatim (junte as linhas quebradas, desfaça hifenização de fim de linha,
     preserve parágrafos com \n quando houver texto-base, tabela em linhas "Coluna: valor" se precisar).
   - `alts`: as alternativas verbatim, SEM a letra "(A)"/"A)" na frente. 5 ou 4 conforme o caderno.
   - `gab`: índice 0-based do gabarito OFICIAL DEFINITIVO (ou retificado), do MESMO tipo de caderno.
   - `fonte`: `{"banca":..., "ano": <ano de APLICAÇÃO>, "prova": ..., "n": <número da questão no caderno>,
     "parte": "gerais"|"especificas"|"politicas"|...}`.
2. `provas-reais/relatorios/extracao_<sufixo>.md`: tabela por prova (URL do caderno e do gabarito, que estão em
   `docs/LEVANTAMENTO_FISIO_2026-10.md`; extraídas; descartadas e por quê) + peculiaridades e armadilhas.

## Regras
- DESCARTE: anulada; questão que depende de imagem/figura/gráfico que não vira texto; texto truncado irrecuperável.
  Registre cada descarte com o motivo.
- Ler gabarito pela POSIÇÃO (geometria), não por texto corrido, e conferir por um segundo método. Sinal de parser
  quebrado: distribuição de letras absurda ou divergência entre os dois métodos.
- Conferência obrigatória antes de terminar, por script: contagem contínua 1..N, número de alternativas certo em
  todas, nenhuma alternativa vazia ou idêntica a outra, nenhum "(A)" sobrando, nenhum número de página/rodapé/
  cabeçalho ("ENARE", "Tipo 1", "Página", nome do cargo) colado no enunciado, distribuição do gabarito. Abra 5 questões ao acaso
  e compare com o PDF (renderize a página com fitz se precisar ver).
- Cuidado com o bug herdado: não apague linhas que são só número (dados de tabela, doses, idades).
- Não edite nada fora dos dois arquivos de saída. Não use a web (os PDFs já estão aqui). Não rode monta_banco.py.
- Resumo final: por prova, extraídas/descartadas, e qualquer dúvida de gabarito ou de texto.
