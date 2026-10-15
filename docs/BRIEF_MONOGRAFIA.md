# Brief para escrever uma leitura (monografia) do Fisiare (versão 15/10/2026)

Fisiare é a plataforma de estudo de **Fisioterapia** do MedTech (`~/Documents/Claude/fisiare/`, irá ao ar em
medtechbr.com.br/fisiare/). É irmã do Enfermare, do ClínicaMed e do CirurgiaMed e herda deles a arquitetura e o
formato das leituras. Público: fisioterapeuta que presta a **residência multiprofissional** (ENARE/FGV,
residências de universidades e secretarias), **concursos de fisioterapeuta** (EBSERH e secretarias) e o
**título de especialista do COFFITO** (Res. COFFITO 630/2025). O dono é o Matheus, médico, que exige textos de
**nível monografia**, comparáveis à norma e à diretriz, não resumo de cursinho.

## Modelos (só leitura, NÃO edite nada lá)
Leia antes de escrever, em `~/Documents/Claude/clinicamed/leituras/`: `choque.html` (monografia de diretriz),
`parada-cardiaca.html` (monografia com fluxogramas). Copie a estrutura e o cabeçalho. O CSS/JS das leituras
já existe aqui em `leituras/_leitura.css` e `leituras/_leitura.js`.

## Fontes
Normas e diretrizes PRIMÁRIAS vigentes em outubro de 2026, conferidas na fonte (nome + número + ano). O
levantamento já feito está em `docs/LEVANTAMENTO_FISIO_2026-10.md` (leia a seção F inteira: Decreto-Lei
938/1969, Lei 6.316/1975, Código de Ética Res. COFFITO 424/2013 com arts. 37 e 39 revogados pelo CADE, título
Res. 630/2025 e RQE 627/2025, RDC 7/2010 na UTI, VM AMIB/SBPT 2013 e orientações práticas 2025, GOLD 2026,
GINA 2026, AHA 2025, reabilitação cardiovascular SBC 2020, e os itens marcados "a conferir"). Textos já
baixados em `provas-reais/txt/` (editais, Anexo III do ENARE, Anexo I do COFFITO 2026 com bibliografia por
especialidade, GOLD 2026). Para o resto: legislação no planalto.gov.br e bvsms.saude.gov.br, resoluções no
coffito.gov.br, manuais do Ministério da Saúde e da ANVISA, diretrizes de sociedades (AMIB, SBPT, SBC, ASSOBRAFIR).
**Nunca escreva número, dose, prazo, corte ou classificação de memória.** Se não confirmou, não escreva o
número e anote "a conferir" no relatório. Quando uma norma substituiu outra que ainda aparece em prova (Res. COFFITO 377/2010 → 630/2025; RPE → RQE;
GOLD ABCD → ABE; III Consenso de VM 2007 → recomendações 2013), ensine as duas e diga o que mudou.
Livros de fisioterapia (Kisner, Kendall, Sarmento, West, Umphred, O'Sullivan) têm direito autoral: não copie
texto, tabela nem figura. Pode citar a obra e o raciocínio.

## Regras de conteúdo
1. **Tamanho:** 4.000–6.000 palavras. Conte com `sed 's/<[^>]*>/ /g' arquivo.html | wc -w`.
2. **Abra com a base:** a primeira seção depois do sumário é "Visão geral", que explica o tema do zero para
   quem chega sem base (o público é amplo, do recém-formado ao especialista). Depois aprofunde.
3. **Fisioterapia de verdade:** o foco é o que o fisioterapeuta avalia, decide e faz, com parâmetros (ajuste
   do ventilador, critérios de desmame, carga e intensidade de exercício, dosimetria de eletro e laser, escalas
   e pontos de corte), o limite da atuação (diagnóstico cinético-funcional, não nosológico) e o que a norma
   exige. Mostre como a banca cobra (FGV gosta de caso clínico com conduta e de "assinale a correta" sobre
   parâmetro e diretriz).
4. Classificação de evidência ou força de recomendação só **transcrita da fonte**, em `table.rec`.
5. Português do Brasil, prosa técnica e direta.
6. **Escrita (o Matheus reprova "cara de IA"):** sem travessão (— ou –) em prosa, título e legenda; sem emoji;
   sem "é importante ressaltar / vale destacar / neste contexto / não é X, é Y"; sem frase-aforismo de
   fechamento; títulos e h2 são **substantivos** ("Modos ventilatórios", não "Modos: a arte de ventilar"); o dek diz o que o texto cobre e por qual fonte. Negrito com parcimônia.

## Estrutura do HTML
```html
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Título</title>
<link rel="stylesheet" href="_leitura.css?v=1"><script src="_leitura.js?v=1"></script>
<div class="wrap">
<p class="kicker">Área · NN min · Fonte ANO · monografia</p>
<h1>Título</h1>
<p class="dek">O que o texto cobre e por qual fonte.</p>
<nav class="toc"><b>Sumário</b><ol><li><a href="#id">Seção</a></li>…</ol></nav>
<h2 id="visao">Visão geral</h2>
…
<h2 id="armadilhas">Erros frequentes</h2>
<h2 id="autoteste">Perguntas de revisão</h2>
<a class="vaiQuestoes" href="../index.html?area=AREA#questoes">Treinar questões de …</a>
<footer><b>Fontes primárias</b><ol><li>Citação completa com número, ano e URL.</li></ol></footer>
</div>
```
h2 **sem numeração**, todo h2 com id e no sumário na mesma ordem e texto. Componentes (em `_leitura.css`):
`table.rec`, `table.criterio`, `div.rolagem>table`, `div.cx chave|armadilha|fonte|nota`, `div.ancora`
(Questão-âncora com `<details>`), `div.compara`, `div.dose`, `ol.passos`, `<details><summary>` no autoteste.

**Fluxogramas (mínimo 2):**
```html
<div class="fluxo"><div class="leg"><b>Fluxograma 1</b>Legenda curta</div>
<pre class="mermaid">
flowchart TD
  A["Rótulo entre aspas"] --> B{"Pergunta?"}
  B -->|"sim"| C["Ação"]
</pre></div>
```
Rótulos entre aspas, `<br/>` para quebra, sem parênteses ou vírgula fora das aspas, `flowchart TD`, no máximo
3 nós lado a lado.

**Figuras:** nunca copie imagem de livro, manual, PDF ou web (direito autoral; app público e pago). Esquema
simples pode ser **SVG inline** desenhado por você: fonte `-apple-system,system-ui,sans-serif`, cores
`var(--ink)`, `var(--ink2)`, `var(--brand)`, `var(--linha)`, `var(--ok)`, `var(--err)`; texto de SVG não quebra
linha: quebre à mão e confira que nada vaza do viewBox.

## Operação
- **Escreva por seções:** crie o arquivo com cabeçalho + primeira seção e acrescente uma seção por vez
  (até ~900 palavras por acréscimo). Nunca um Write gigante.
- **Cota: no máximo 6 buscas web (WebSearch + WebFetch somados)** para a leitura inteira. Prefira os textos já
  baixados e fontes oficiais conhecidas.
- Rascunhos só em `/private/tmp/claude-501/-Users-matheusparente/24edeac6-15cd-4c88-8b50-83646c37609c/scratchpad/mono-<slug>/`.
- Escreva SÓ `leituras/<slug>.html` e `leituras/_entradas_<slug>.json`:
  `[{"f":"<slug>.html","tipo":"AMIB/SBPT 2013 · monografia","area":"uti","min":60,"t":"Título","s":"Resumo de duas a quatro linhas, igual ao dek."}]`
  `min` = palavras ÷ 80. `area` é um id de `taxonomia.js`.
- Ao fim: `python3 valida_leituras.py` (0 erros no seu arquivo).
- **Não toque** em `leituras.js`, `index.html`, `CLAUDE.md`, `sw.js`, `banco.js`, nem em nada de outros apps.
  Não rode `bump.py`, não faça commit nem push.
- Relatório final curto: arquivo, palavras, fluxogramas, fontes usadas com ano, e tudo que ficou "a conferir".
