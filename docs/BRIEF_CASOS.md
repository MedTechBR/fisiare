# Brief — Casos clínicos de Fisioterapia (aba "Casos", `pratica.js`) — 15/10/2026

A aba reproduz o raciocínio do atendimento fisioterapêutico num caso que chega por etapas: avaliação
cinético-funcional, diagnóstico cinético-funcional (com a linguagem da CIF quando couber), objetivos, conduta
com parâmetros e reavaliação. O aluno lê a abertura, escreve o que faria em cada etapa, recebe os dados
seguintes e, no fim, escreve o plano e se corrige por um espelho com pesos. Leia antes `taxonomia.js` e a
seção F de `docs/LEVANTAMENTO_FISIO_2026-10.md`. Veja o formato num exemplo (só leitura):
`~/Documents/Claude/enfermare/pratica.js`.

## Formato de cada caso (objeto JSON; chaves nesta ordem)
`id` ("caso-<slug>"), `titulo` (substantivo, sem dois-pontos), `area` (id de taxonomia.js), `cenario`
(aps, amb, enf, uti, ger), `tempo` (minutos sugeridos: 15 a 25), `abertura` (setor, paciente, dados
iniciais e o que se pede), `etapas` (3 a 5 objetos `{n, tarefa, entrega}`: `tarefa` = o que o aluno deve dizer
naquela etapa; `entrega` = os dados que chegam DEPOIS que ele cumpre a etapa; a última `entrega` pode ser
"Encerramento do caso."), `espelho` (8 a 12 itens `{eixo, item, peso}`).
- `eixo`: C = avaliação e raciocínio (diagnóstico cinético-funcional); H = conduta, técnica e parâmetros;
  A = segurança, critérios de interrupção, ética e registro. Use os três eixos. Pesos em décimos; a soma dos
  pesos de cada caso é EXATAMENTE 5,0.
- Cada item é uma ação ou decisão verificável ("Ajusta volume corrente de 6 mL/kg de peso predito e mantém
  pressão de platô até 30 cmH2O"), não uma qualidade vaga. Item com número, parâmetro, escala ou norma cita a
  fonte e o ano entre parênteses.
- Mostre o limite da atuação: o que é do fisioterapeuta, o que é decisão compartilhada com a equipe, o que
  exige o médico.

## Casos a escrever (8, um por linha)
1. Paciente em ventilação mecânica com SDRA moderada: ajuste protetor e titulação de PEEP (uti, uti)
2. Desmame: teste de respiração espontânea e extubação com risco de falha, VNI ou alto fluxo pós-extubação (uti, uti)
3. DPOC exacerbada na enfermaria e encaminhamento à reabilitação pulmonar (respiratoria, enf)
4. AVC isquêmico subagudo com hemiparesia: avaliação, escalas e plano de reabilitação (neuro, amb)
5. Pós-operatório de reconstrução do LCA: progressão por critérios até o retorno ao esporte (orto, amb)
6. Prematuro de 30 semanas na UTI neonatal com desconforto respiratório em CPAP (pediatria, uti)
7. Incontinência urinária de esforço no pós-parto: avaliação do assoalho pélvico e treino muscular (mulher, amb)
8. Idoso com quedas de repetição na atenção primária: avaliação de risco e programa de exercícios (idoso, aps)

## Escrita e rigor
Sem travessão (—, –), sem emoji, sem markdown, sem "é importante ressaltar". Nenhum número, parâmetro, carga
ou prazo de memória: confira na fonte primária (diretriz, norma, consenso). Cota: no máximo 6 buscas web
(WebSearch + WebFetch) no total.

## Saída
Escreva SÓ `docs/casos_a.json` (lista JSON dos 8 casos). Não edite pratica.js nem outros arquivos.
Antes de terminar rode e corrija até passar:
```
python3 -c "
import json;d=json.load(open('docs/casos_a.json'));import re
tax=set(re.findall(r'\"id\":\"(\w+)\"',open('taxonomia.js').read()))
for c in d:
  assert c['area'] in tax and abs(sum(i['peso'] for i in c['espelho'])-5.0)<1e-6, c['id']
  assert {i['eixo'] for i in c['espelho']}=={'C','H','A'} and 3<=len(c['etapas'])<=5, c['id']
  assert '—' not in json.dumps(c,ensure_ascii=False), c['id']
print(len(d),'casos ok')"
```
Relatório final: casos, fontes conferidas com URL e o que ficou "a conferir".
