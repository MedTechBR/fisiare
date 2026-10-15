/* Fisiare — taxonomia do conteúdo de Fisioterapia.

   Fonte primária: Anexo III do ENARE multiprofissional (Edital 04/2026, igual às edições 2024/25 e
   2025/26): 12 tópicos de conhecimentos comuns (SUS, PNSP, NR 32, bioética) e os itens 8.1 a 8.14 de
   Fisioterapia; e o Anexo do Edital nº 3 da EBSERH 2024 (FGV), Grupo 7 Fisioterapia (métodos de
   avaliação e tratamento, provas de função muscular, cinesiologia, marcha, recursos, órteses e próteses,
   áreas neuro, ortopedia, cardio, pneumo, ginecologia e obstetrícia, geriatria, ética). Título de
   especialista do COFFITO: as especialidades entram pelas áreas abaixo.

   `peso` = incidência esperada numa prova de 100 questões (soma 100). ids curtos, sem hífen
   (o valida_leituras.py casa a área com \w+). */

window.TAXONOMIA=[
{"id":"sus","nome":"SUS: legislação e políticas de saúde","matriz":"Conhecimentos comuns","peso":8,"sub":[
 "Constituição Federal e o direito à saúde","Lei 8.080/1990 e Decreto 7.508/2011","Lei 8.142/1990 e controle social",
 "Política Nacional de Atenção Básica","Redes de Atenção à Saúde","Política Nacional de Humanização",
 "Financiamento e gestão do SUS","Políticas de equidade e populações vulneráveis","Educação permanente em saúde"]},

{"id":"coletiva","nome":"Epidemiologia, vigilância e saúde do trabalhador","matriz":"Conhecimentos comuns","peso":5,"sub":[
 "Indicadores de saúde","Vigilância epidemiológica e notificação compulsória","Vigilância sanitária e ambiental",
 "Saúde do trabalhador e ergonomia","Sistemas de informação em saúde","Estudos epidemiológicos e bioestatística"]},

{"id":"seguranca","nome":"Segurança do paciente e biossegurança","matriz":"Conhecimentos comuns","peso":4,"sub":[
 "Metas internacionais e PNSP","Higiene das mãos","Precauções padrão e específicas",
 "Infecções relacionadas à assistência","Biossegurança e NR 32","Notificação de incidentes",
 "Prevenção de quedas e de lesão por pressão"]},

{"id":"etica","nome":"Ética, legislação profissional e pesquisa","matriz":"Exercício profissional","peso":5,"sub":[
 "Decreto-Lei 938/1969 e Lei 6.316/1975","Código de Ética e Deontologia da Fisioterapia",
 "Resoluções do COFFITO","Especialidades e parâmetros assistenciais","Prontuário e registro",
 "Bioética e direitos do paciente","Prática baseada em evidências e pesquisa","Trabalho em equipe multiprofissional"]},

{"id":"aps","nome":"Fisioterapia na atenção primária e saúde funcional","matriz":"Exercício profissional","peso":6,"sub":[
 "Fisioterapia na APS e eMulti","Promoção da saúde e prevenção","CIF e funcionalidade",
 "Vigilância dos distúrbios cinesiofuncionais","Atenção domiciliar e reabilitação na comunidade",
 "Pessoa com deficiência e Rede de Cuidados","Populações vulneráveis"]},

{"id":"bases","nome":"Anatomia, cinesiologia e biomecânica","matriz":"Bases","peso":6,"sub":[
 "Anatomia funcional","Cinesiologia e biomecânica","Análise da marcha","Fisiologia muscular e do exercício",
 "Controle e aprendizagem motora","Postura e equilíbrio"]},

{"id":"avaliacao","nome":"Avaliação e diagnóstico cinético-funcional","matriz":"Bases","peso":6,"sub":[
 "Anamnese e exame físico","Provas de função muscular e goniometria","Escalas e testes funcionais",
 "Diagnóstico cinético-funcional","Exames complementares","Testes ortopédicos especiais"]},

{"id":"recursos","nome":"Recursos terapêuticos","matriz":"Bases","peso":6,"sub":[
 "Eletroterapia","Termoterapia e crioterapia","Fototerapia e laser","Ultrassom terapêutico",
 "Cinesioterapia e exercício terapêutico","Hidroterapia","Terapia manual e massoterapia",
 "Órteses, próteses e tecnologia assistiva"]},

{"id":"respiratoria","nome":"Fisioterapia respiratória","matriz":"Cardiorrespiratória","peso":8,"sub":[
 "Fisiologia e mecânica respiratória","Gasometria arterial","Espirometria e função pulmonar",
 "Higiene brônquica e reexpansão pulmonar","Oxigenoterapia","DPOC, asma e bronquiectasias",
 "Reabilitação pulmonar","Pré e pós-operatório"]},

{"id":"uti","nome":"Terapia intensiva e ventilação mecânica","matriz":"Cardiorrespiratória","peso":9,"sub":[
 "Modos ventilatórios","Ajuste e mecânica do sistema respiratório","Ventilação não invasiva e alto fluxo",
 "Desmame e extubação","SDRA e ventilação protetora","Mobilização precoce e fraqueza adquirida",
 "Via aérea artificial e traqueostomia","Paciente neurocrítico"]},

{"id":"cardio","nome":"Fisioterapia cardiovascular","matriz":"Cardiorrespiratória","peso":5,"sub":[
 "Fisiologia cardiovascular e eletrocardiograma","Reabilitação cardiovascular","Teste de esforço e prescrição de exercício",
 "Insuficiência cardíaca","Pós-operatório de cirurgia cardíaca","Doença vascular periférica e linfedema"]},

{"id":"neuro","nome":"Fisioterapia neurofuncional","matriz":"Neuro e musculoesquelética","peso":8,"sub":[
 "Acidente vascular cerebral","Traumatismo cranioencefálico e lesão medular","Doença de Parkinson e distúrbios do movimento",
 "Esclerose múltipla e doenças neuromusculares","Neuropatias periféricas","Avaliação neurológica e escalas",
 "Abordagens terapêuticas em neurologia","Reabilitação vestibular"]},

{"id":"orto","nome":"Traumato-ortopedia, reumatologia e esporte","matriz":"Neuro e musculoesquelética","peso":8,"sub":[
 "Coluna vertebral","Membro superior","Membro inferior","Fraturas e pós-operatório ortopédico",
 "Doenças reumáticas","Lesões esportivas","Amputação e protetização","Dor crônica"]},

{"id":"pediatria","nome":"Pediatria e neonatologia","matriz":"Ciclos de vida","peso":6,"sub":[
 "Desenvolvimento motor típico","Paralisia cerebral","Neuropediatria e síndromes genéticas",
 "Fisioterapia respiratória pediátrica","UTI neonatal e prematuridade","Ventilação neonatal e pediátrica"]},

{"id":"mulher","nome":"Saúde da mulher e uroginecologia","matriz":"Ciclos de vida","peso":4,"sub":[
 "Gestação e puerpério","Assoalho pélvico e incontinência","Câncer de mama e linfedema","Dor pélvica e disfunções sexuais"]},

{"id":"idoso","nome":"Gerontologia","matriz":"Ciclos de vida","peso":3,"sub":[
 "Envelhecimento e avaliação funcional","Quedas e fragilidade","Sarcopenia e osteoporose","Demências e declínio funcional"]},

{"id":"onco","nome":"Oncologia, queimados, dermatofuncional e paliativos","matriz":"Ciclos de vida","peso":3,"sub":[
 "Fisioterapia oncológica","Queimados","Dermatofuncional","Cuidados paliativos"]}
];

/* Cenário — onde o atendimento acontece muda a conduta certa. */
window.CENARIOS=[
 {"id":"aps","nome":"Atenção primária e comunidade"},
 {"id":"amb","nome":"Ambulatório e reabilitação"},
 {"id":"enf","nome":"Enfermaria"},
 {"id":"uti","nome":"UTI"},
 {"id":"ger","nome":"Gestão e vigilância"}
];

/* Competência — o que a questão cobra de você. */
window.COMPETENCIAS=[
 {"id":"base","nome":"Bases anatômicas e fisiológicas"},
 {"id":"aval","nome":"Avaliação e diagnóstico cinético-funcional"},
 {"id":"cond","nome":"Conduta e plano terapêutico"},
 {"id":"tec","nome":"Recurso e técnica"},
 {"id":"norma","nome":"Legislação, ética e normas"}
];

/* Nível de profundidade. Os `id` seguem os do ClínicaMed (o código do app os referencia). */
window.NIVEIS=[
 {"id":"r1","nome":"Essencial","desc":"O que o fisioterapeuta não pode errar no atendimento."},
 {"id":"r2","nome":"Intermediário","desc":"Conduta e raciocínio de nível de concurso e residência."},
 {"id":"r3","nome":"Avançado","desc":"Nuance de diretriz e de parâmetro; profundidade de especialista."},
 {"id":"tit","nome":"Nível prova de título","desc":"Questão de especialidade, no formato das provas de título do COFFITO."}
];
