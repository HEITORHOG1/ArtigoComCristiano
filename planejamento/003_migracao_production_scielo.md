# 003. Migração do artigo Kirkpatrick para a revista *Production* (ABEPRO, SciELO)

Criado em 06/11/2026. Documento de trabalho: atualizar a tabela de fases a cada sessão.

Decisão de partida (Heitor, 06/11/2026): publicar na *Production*, submissão pelo ScholarOne <https://mc04.manuscriptcentral.com/prod-scielo>, usando como modelo o kit já montado para o artigo B em `G:\Projetos\Dissertacao\001-Doutorado\artigos\Production-ABEPRO-secao-tematica-2027\`. A pasta `IJCIEOM-2027-Springer-PROMS\`, indicada primeiro, é a versão de conferência (Springer `llncs`) e não serve de molde; o molde certo é a pasta da *Production*, ao lado dela.

## 0. Situação em uma página

1. **O formato é a parte fácil.** O kit do artigo B já resolve tudo o que a *Production* exige de forma: preâmbulo (A4, 2,5 cm, Times 12, espaço 1,5, sem recuo), APA 7, figuras JPEG, pacote LaTeX de arquivo único que o conversor antigo do ScholarOne aceita, formulários em PDF e o roteiro do sistema. Adaptar leva de dois a três dias.
2. **O conteúdo não pode ir como está, para revista nenhuma.** O parecer de 11/08/2026 (`002_parecer_pre_submissao.html`) concluiu "não submeter nesta versão", e nada mudou desde então (último commit em 11/08/2026; nenhum arquivo de `artigo/` alterado depois). Hoje, conferido em 06/11/2026: as 15 referências que o parecer não encontrou no Crossref continuam citadas **47 vezes** em `secoes/` e `tabelas/`, inclusive `Pereira2017`, que sustenta o custo de USD 189.500 por reclamação de garantia e, com ele, o modelo econômico inteiro.
3. **A *Production* acrescenta duas exigências que o JATM não cobrava assim:** (a) não aceita *case reports*, então o artigo tem de se apresentar como pesquisa empírica de caso (artigo original), com pergunta, desenho e ameaças à validade; (b) exige a declaração de ética no manuscrito **e** a cópia do parecer do comitê de ética no sistema, e o `main.tex` ainda traz "[Institution Ethics Committee] under protocol No. [X]".
4. **Prazo.** A seção temática do IJCIEOM na *Production* fecha em **30/11/2026** (24 dias). O fluxo contínuo não tem prazo. Proposta: trabalhar desde já nas frentes que não dependem de ninguém (bibliografia e formato) e decidir a rota em **20/11/2026** (seção 4).

## Status

| Data | Fase | O que foi feito |
|---|---|---|
| 06/11/2026 | D8 | Tag git `jatm-r1-2026-05` na versão JATM; pasta `artigo-production/` criada; `CLAUDE.md` atualizado |
| 06/11/2026 | **F3 concluída** | Formato da *Production* completo em `artigo-production/`: seções na ordem da revista (mapa da seção 6), resumo estruturado (210 palavras), título com 13 palavras, palavras-chave, tabelas com notas de abreviaturas e fonte, oito figuras em JPEG a 400 dpi (legenda da Fig. 6 e rótulo da Fig. 7 corrigidos), APA 7, versão cega, declarações, pacote do ScholarOne testado em rascunho (19 páginas, zero erros, sem Type 3, 2,4 MB), três formulários preenchidos e compilados, carta em rascunho. Bibliografia: só 5 entradas verificadas (Boyd e Stolzer corrigido pelo Crossref; FAA AC 120-92D conferida no site da FAA; Kirkpatrick 2006); as 15 sem registro aparecem em vermelho no texto. O que falta está em `artigo-production/PENDENCIAS.md` |
| 06/11/2026 | **Base trocada para o original** | Pedido do Heitor: "está faltando muita coisa do original, referências principalmente; adaptar, mas não remover o que foi escrito". O texto de `artigo-production/` voltou a ser o artigo original (`ArtigoExemplo/Paper Training - 15 Nov 2025.pdf`) inteiro: quatro perguntas de pesquisa, revisão 2.1 a 2.5, três fases, coleta por nível, AS9100 e CAR detalhados, processo, os quatro níveis, custo da qualidade, discussão e conclusão do original. Gráficos 6 a 8 = imagens originais (os "reconstruídos" do JATM tinham outros valores). Referências: todas as do original no `refs.bib`; verificação no Crossref e no OpenAlex: 11 existem (corrigidas), 23 não localizadas (em vermelho, mantidas). Números que só a versão JATM tinha (78→86 %, κ, α, IC, parâmetros de custo) saíram do texto e estão guardados em pastas `_NAO-USAR`. Título do original reduzido a 14 palavras. Cerca de 7.900 palavras, 26 páginas, zero erros; o pacote de envio recusa enquanto houver referência em vermelho |
| 06/11/2026 | D1 | Respondida: o artigo **não** está no JATM |
| 06/11/2026 | **Rodada das skills** | Pedido do Heitor: "é só você rodar as skills". Rodaram `workflow-artigo`, `anti-vicios-ia`, `revisor-critico` (com `discussao-limitacoes`, `estatistica-reporting`, `reporting-guidelines` e `figuras-tabelas`, numa revisão independente) e `editor-cientifico`, além da verificação das referências. Resultados: frases mais curtas (média de 28,9 para 22,7 palavras); linguagem causal ajustada ao desenho; contradições desfeitas; Figs. 1 a 5 corrigidas. Referências: **22 do original não existem** (bases e web); o relatório da EASA e a circular da FAA, conferidos nos PDFs, não trazem os números atribuídos a eles; 4 citações reais entraram (IATA 2009, Buriak & Ayars, Jung et al., Yücel & Ayvaz). Texto com 8.342 palavras, acima do limite de 8.000. Detalhes em `artigo-production/RELATORIO-SKILLS-2026-11-06.md`; o que falta, em `PENDENCIAS.md` |
| | F1, F2, D2, D4, D6, D7 | Abertas (ver `artigo-production/PENDENCIAS.md`) |

## 1. Ficha

| Item | Valor |
|---|---|
| Revista | *Production*, ABEPRO. ISSN 0103-6513 (impresso) e 1980-5411 (online). Scopus, SciELO, DOAJ. Sem taxa de submissão nem de publicação; CC BY 4.0; inglês; duplo-cego; fluxo contínuo |
| Submissão | ScholarOne, <https://mc04.manuscriptcentral.com/prod-scielo> |
| Tipo | Artigo original. A revista aceita artigos originais e revisões sistemáticas e recusa explicitamente "case reports, brief communications letters, simple literature reviews, and technical reports" |
| Título atual | *A Kirkpatrick-based Framework for Integrating Safety and Sustainability in Aviation Maintenance: A Case Study on Waste Reduction and Resource Efficiency* (**20 palavras; limite 15**) |
| Autores | José Cristiano Pereira (UCP e GE Aviation; correspondente no JATM) e Heitor Oliveira Gonçalves (UCP) |
| Origem | Revisão *major* do JATM (10 comentários de um revisor, `ArtigoExemplo/Comments for Air Transport Management.pdf`); versão LaTeX `cas-dc` em `artigo/` |
| Tamanho hoje | ~8.500 palavras antes das referências no PDF (inclui o texto das figuras TikZ) + 478 nas referências; seções em `secoes/` somam ~6.100 |
| Pré-requisitos das skills | Título e abstract: `artigo/main.tex`. Pasta de PDFs: `ArtigoExemplo/` (flexibilização registrada no plano 001). Para a F1 será preciso uma pasta com os PDFs das fontes reais (`artigo-production/referencias-pdf/`) |

## 2. Por que o formato não vem primeiro

Os achados do parecer que continuam abertos e que qualquer revista vai encontrar:

| Bloco | Problema | Onde |
|---|---|---|
| Bibliografia | 15 das 20 referências citadas sem registro no Crossref; 8 DOIs resolvem para artigos alheios ao tema; 3 com metadados errados (Boyd 2015 está no *J. of Aviation Technology and Engineering* 5(1); a circular de SMS é a AC 120-92D; a 3ª edição de Kirkpatrick é de 2006, Berrett-Koehler) | `references.bib`; 47 citações em 9 arquivos |
| Números da introdução | USD 90 bi de mercado MRO, 12 a 18 % dos acidentes, multiplicador de 3 a 7 vezes, USD 189.500 por reclamação e "fewer than 20% go beyond Level 2" (a lacuna) citam entradas inexistentes | `01-introduction.tex` |
| Figuras × texto | Fig. 7: seis notas abaixo de 70 (71,4 %), o texto diz três (86 %); Fig. 6: três sessões abaixo de 8, o texto diz duas; Fig. 8 × Tabela 1 na satisfação (4,64 × 4,7; baseline "n.a." × barras pré); os fontes das três figuras de dados dizem "values reconstructed", a metodologia diz "no values were synthesised or imputed" | `figs/fig8`, `fig9`, `fig10`; `04-results.tex`; `table1` |
| Estatística | Intervalos de confiança incompatíveis com contagens plausíveis; teste errado para taxas (z e qui-quadrado em vez de razão de taxas de Poisson); ganho do Nível 2 com n = 21 é ruído (p = 0,52); nenhum denominador informado | `03-methodology.tex`, `04-results.tex` |
| Economia | Custo de qualidade cai 28,57 %, o mesmo número da taxa de falha reexpresso em dólares; payback usa custo recorrente como investimento; ROI definido e nunca calculado; VPL pedido pelo revisor e ausente | `04-results.tex`, `table3` |
| Sustentabilidade | Título promete redução de resíduo e eficiência de recursos; nenhum kg, kWh ou kgCO2e é medido | título, abstract, 4.6 |
| Ética | Placeholders no PDF; consentimento de técnicos observados pelos próprios supervisores, com acesso ao ERP condicionado à prova | `main.tex` |

O que o parecer elogiou e deve sobreviver: a tese (eficácia de treinamento ligada a custo da qualidade e a indicadores ESG em MRO), a seção 3.3 sobre ameaças à validade, a tabela de limitações, a declaração de conflito de interesse e a prosa.

## 3. Decisões que travam o trabalho (F0)

| # | Decisão | Quem | Por que trava | Recomendação |
|---|---|---|---|---|
| D1 | **Situação no JATM.** A revisão R1 foi enviada? O manuscrito ainda está aberto no sistema da Elsevier? | Cristiano (correspondente no JATM) | O formulário de autoria da *Production* declara que o trabalho não está em avaliação em outro lugar | Se estiver aberto, retirar por escrito antes de submeter e guardar a confirmação do JATM |
| D2 | **Rota:** seção temática (prazo 30/11/2026) ou fluxo contínuo | Heitor e Cristiano | Define o calendário inteiro | Decidir em 20/11 (seção 4) |
| D3 | **Dados brutos da instalação:** notas dos 21 participantes, escores das 10 sessões, respostas de satisfação, ciclos de auditoria e constatações por ano, tarefas de manutenção, saídas de treinamento, eventos de observação, horas de retrabalho, sucata e garantias com valor unitário do ERP | Cristiano | Sem eles a F2 não fecha e o artigo não vai | Pedir hoje; incluir no pedido o prazo da revisão de confidencialidade da GE, que o próprio manuscrito diz ter havido e que terá de se repetir com números novos |
| D4 | **Ética:** existe parecer de CEP com número de protocolo? | Cristiano | A revista exige a declaração no texto e a cópia do parecer no sistema ("Supplemental File NOT for Review") | Se existir, anexar. Se não existir, não há aprovação retroativa: consultar o CEP da UCP sobre dispensa pela Res. CNS 510/2016, art. 1º, parágrafo único (por exemplo, inciso V, banco de dados agregados sem identificação individual) [Média: conferir o texto da resolução e o entendimento do CEP]. A *Production* aceita isenção declarada e justificada. A frase "All participants provided informed consent" só fica se for fato |
| D5 | **Sustentabilidade:** medir o mínimo (kg de sucata evitada, horas de retrabalho, kgCO2e do frete expresso, todos deriváveis do ERP) ou realinhar título e abstract | Heitor e Cristiano | Decide o título (seção 7) e a seção 3.6 | Medir, se D3 trouxer os dados; a seção temática fala em circularidade, reparo e impacto social, e o artigo ganha encaixe |
| D6 | **Lista de autores e correspondente** | Heitor e Cristiano | A revista não deixa incluir nem retirar autor depois da submissão | Fechar antes da F6. Se o correspondente for o Heitor, a conta do ScholarOne já existe (artigo B) |
| D7 | **Regra 46 (uso de IA).** A declaração negativa exigida pelo JATM não tem equivalente na *Production* e sai do manuscrito. A revista pede a seção "Artificial Intelligence Use Statement" sempre que houver uso de IA no texto | Autores | É declaração dos autores | Mesma condução do artigo B: decisão explícita dos autores; nenhum texto entra sem ela e nenhuma declaração falsa entra |
| D8 | **Onde mora a nova versão** | (proposta) | Evita estragar a versão JATM | Marcar o estado atual com a tag git `jatm-r1-2026-05`, criar `artigo-production/` na raiz e atualizar a lista de pastas do `CLAUDE.md`. `artigo/` fica congelado |

## 4. Rotas e calendário

| | Seção temática do IJCIEOM | Fluxo contínuo |
|---|---|---|
| Prazo | 30/11/2026; envio planejado em 28/11 (dois dias de folga) | Nenhum; meta sugerida 18/12/2026 |
| Encaixe | Tópicos da chamada (lidos em 06/11/2026): "Sustainability & social impact", "Human-centricity and organizational change", "Performance frameworks & interventions", "Empirical modelling, case research, mixed methods", "Decision-support validated in real contexts". Nenhum tópico fala de treinamento, segurança, manutenção ou aviação | Escopo geral da revista (engenharia de produção e gestão de operações) |
| Obrigações | Apresentação presencial no IJCIEOM, PUC-Rio, 14 a 16/06/2027, por ao menos um autor | Nenhuma |
| Calendário | Primeira decisão 17/01/2027; R1 até 14/02/2027; decisão final 21/04/2027. Se recusado na primeira decisão, pode ir à trilha regular do IJCIEOM até 14/02/2027 (anais, não revista) | Prazos da revista |
| Observação | O artigo B dos mesmos autores vai para a mesma seção; a chamada não limita artigos por autor na *Production* (o limite de dois por correspondente é da trilha regular) | |

**Ponto de decisão em 20/11/2026.** Fica a rota temática se, até essa data, D1 e D4 estiverem resolvidos, os dados de D3 estiverem em mãos e a F1 estiver concluída. Faltando qualquer um, segue o fluxo contínuo, sem pressa artificial: o mérito do artigo depende dos números da F2.

## 5. Fases

Datas da rota temática. No fluxo contínuo valem a mesma ordem e os mesmos critérios.

| Fase | Período | Depende de | Entregável | Critério de pronto |
|---|---|---|---|---|
| F0 Decisões | 06 a 10/11 | autores | D1 a D8 respondidas e registradas neste arquivo | Nenhuma linha da seção 3 em aberto, salvo D2, que fecha em 20/11 |
| F1 Bibliografia | 07 a 17/11 | nada | Planilha afirmação → fonte para as 47 citações; `references.bib` refeito com BibTeX exportado do registro da editora ou do Crossref (nunca digitado); PDFs em `referencias-pdf/`; `scripts/validar_crossref.py` que consulta `api.crossref.org/works/<doi>` e falha em qualquer divergência de título, periódico, volume ou ano | Zero entrada sem registro; cada afirmação da introdução com fonte real ou retirada; 3 metadados corrigidos; entradas "Author, A." e `JATMnew*` apagadas; artigos da própria *Production* sobre treinamento, custo da qualidade ou MRO citados onde couber, só se verificados |
| F2 Dados e estatística | 10 a 20/11 | D3, D4, D5 | `dados/*.csv` com os registros; `scripts/analise.py` que gera as tabelas `.tex` e as figuras de dados; texto de Métodos e Resultados refeito | Nenhum número digitado à mão. Taxas como razão de taxas de Poisson com IC exato (aceitando os que cruzam 1); denominadores publicados; Nível 2 dito como indistinguível de ruído se for o caso; α de Cronbach e κ com n e IC; software declarado. Economia com fração de atribuição α (α = 1 e α = 0,5), custo único separado do recorrente, payback só sobre o único, ROI calculado, VPL de três anos com taxa declarada, sensibilidade por parâmetro (tornado) no lugar do ±25 % uniforme. Figuras 6, 7 e 8 plotando os registros, ou metodologia descrevendo com exatidão o que foi agregado |
| F3 Formato *Production* | 09 a 13/11 | D8 | `artigo-production/` com o mapa da seção 6, preâmbulo do artigo B, tabelas com nota de fonte e abreviaturas, 8 figuras TikZ em JPEG a 600 dpi, versão cega | Compila; `pdftotext` limpo (checagens do `CLAUDE.md`); ainda **não submissível**, porque herda o conteúdo antigo até F1 e F2 entrarem |
| Ponto de decisão | 20/11 | F1, D1, D3, D4 | Rota escolhida (seção 4) | Registrada aqui |
| F4 Texto | 20 a 24/11 | F1, F2 | Título (≤ 15 palavras), resumo nas cinco partes, palavras-chave, introdução reancorada em gestão de operações, discussão calibrada, carta de apresentação | Afirmações no nível de associação, sem "demonstrating that", "confirm", "delivers", "prevented"; recomendações de política como agenda para piloto em vários sítios, presas à tabela de limitações; os escores de *Mastery* 5,2 e 4,0 tratados como achado; comparação com a literatura com números; carta coerente com a declaração de conflito |
| F5 Validação | 24 a 26/11 | F4 | Relatório de conformidade (seção 8) com todas as linhas OK | Crossref verde; 4.000 a 8.000 palavras com referências contadas no Word; resumo ≤ 250; PDF ≤ 3 MB; `pdffonts` sem Type 3; nenhum identificador de autor; instruções da revista relidas no dia; skills `revisor-critico`, `estatistica-reporting` e `anti-vicios-ia` rodadas e achados tratados |
| F6 Pacote e formulários | 25 a 27/11 | F5, D6 | `ENVIO-SCHOLARONE/` (seção 10) | `manuscript.tex` compila do zero só com `pdflatex` e reproduz o `main.pdf`; Agreement e declaração de conflito assinados pelos autores (gov.br, um PDF por formulário); Open Science Form com a justificativa de confidencialidade; parecer de ética ou dispensa em PDF |
| F7 Submissão | 28/11 | F6 | Submissão no ScholarOne, passos B0 a B7 do roteiro do artigo B | Número do manuscrito registrado aqui; "View PDF Proof" conferido contra o `manuscript.pdf` |

## 6. Mapa de seções: JATM → *Production*

Ordem obrigatória da revista: Abstract, Keywords, Introduction, Methods, Results, Discussions, Conclusions, References, com numeração a partir da Introduction.

| Hoje (`artigo/`) | Na *Production* (`artigo-production/secoes/`) | Observação |
|---|---|---|
| Abstract (JATM, 256 palavras, remete à "Section 4") | `00-resumo.tex`: Paper aims; Originality; Research method; Main findings; Implications for theory and practice | Até 250 palavras com os rótulos; autossuficiente; IC no próprio resumo |
| Highlights, graphical abstract, `\credit`, bloco de autores, `\shorttitle` | saem | A *Production* não pede highlights nem resumo gráfico; autores e CRediT vão só no sistema |
| Keywords (8) | 3 a 5, sem repetir termos do título | Fecham junto com o título (seção 7) |
| `01-introduction` + `02-literature-review` + 4.1 e 4.2 (que são revisão) | `01-introducao.tex`: 1 Introduction; 1.1 Kirkpatrick em indústrias de alto risco; 1.2 AS9100, SMS e sustentabilidade | Revisão crítica, com fontes em tensão, não catálogo; lacuna refeita com fontes reais |
| `03-methodology` + 4.3 (a intervenção) | `02-metodos.tex`: 2.1 desenho e contexto (pesquisa empírica de caso, sítio único); 2.2 intervenção, com os componentes enumerados (o condicionamento do ERP à prova declarado como cointervenção); 2.3 dados, medidas e denominadores (definição de *training failure*); 2.4 análise estatística; 2.5 modelo de custo da qualidade; 2.6 ameaças à validade | O parágrafo sobre *selection* é refeito; entram regressão à média, efeito de testagem e atrito |
| 4.4 a 4.6 | `03-resultados.tex`: 3.1 Nível 1; 3.2 Nível 2; 3.3 Nível 3; 3.4 Nível 4 (segurança e conformidade); 3.5 resultado econômico; 3.6 sustentabilidade (só o que foi medido) | Tabelas e figuras de dados geradas pela F2 |
| `05-discussion` + `06-managerial-implications` + `07-policy-recommendations` + `09-limitations` + `table2` | `04-discussoes.tex`: 4.1 interpretação; 4.2 comparação com a literatura; 4.3 implicações gerenciais; 4.4 agenda regulatória; 4.5 limitações (tabela) | 06 e 07 condensados; o público é de engenharia de produção, não só de transporte aéreo |
| `08-conclusion` | `05-conclusoes.tex` | Responde às perguntas de pesquisa com os números novos |
| Funding, AI declaration, Ethics, Competing interest, Data availability | `06-declaracoes.tex`: Conflict of interest; Funding; Ethics statement; Data availability | Conflito sem identificar autor nem empresa na versão cega (por exemplo, "One author is employed by the company that operates the host facility; the company reviewed the manuscript for confidentiality only"); nome completo só no formulário e no sistema. Financiamento com a frase padrão da revista, se confirmado que não houve: "This research did not receive external funding or support." Declaração de IA conforme D7 |
| Mapeamento Kirkpatrick → AS9100 → SMS → sustentabilidade, hoje escrito de três formas | Uma tabela canônica em 2.1 ou 1.2, citada nos outros lugares; Fig. 0 alinhada a ela | Achado do parecer (cláusulas 6.1, 7.1, 8.1.1 e 9 divergem entre seções) |

Tabelas: nota abaixo de cada uma com as abreviaturas (mesmo já definidas no texto) e a fonte ("Source: the authors" ou "Source: facility records, 2023–2024"), corpo em 10 pt, feitas como tabela (nunca imagem). Figuras: JPEG ≥ 300 dpi (o kit gera 600), legenda, fonte e abreviaturas, logo depois do parágrafo que as cita (`[H]`). Sem notas de rodapé. Ponto decimal; unidades SI.

## 7. Título, resumo e palavras-chave

O título fecha depois de D5. Duas propostas dentro de 15 palavras:

| Se D5 = medir resíduo | Se D5 = realinhar |
|---|---|
| *A Kirkpatrick-Based Framework Linking Aircraft Maintenance Training to Safety, Quality Costs and Waste* (13 palavras) | *Evaluating Aircraft Engine Maintenance Training with the Kirkpatrick Model: Safety and Cost-of-Quality Outcomes* (13 palavras) |

"A Case Study on..." sai do título nas duas: além do limite de palavras, ajuda a não ler o artigo como *case report*. As palavras-chave não podem repetir termos do título; por exemplo, com a primeira proposta, "Safety management systems" e "Aerospace quality management" ficam de fora. Exemplo a conferir no fechamento: *AS9100; Human factors; Cleaner production; MRO; Mixed methods*.

## 8. Orçamento de palavras

A revista conta de 4.000 a 8.000 palavras **incluindo as referências**, como o Word conta. Figuras em JPEG não entram na contagem; texto de tabela entra.

| Parte | Hoje (aprox.) | Meta |
|---|---|---|
| Resumo | 256 | ≤ 250 |
| 1 Introduction (com 1.1 e 1.2) | ~1.560 + revisão de 4.1 e 4.2 | 1.300 |
| 2 Methods | ~1.160 + intervenção de 4.3 | 1.400 (cresce com denominadores e análise) |
| 3 Results | ~1.370 menos 4.1 a 4.3 | 1.300 |
| 4 Discussions (com implicações, agenda, limitações) | ~1.610 | 1.300 |
| 5 Conclusions | ~425 | 300 |
| Declarations | ~250 | 200 |
| Tabelas | ~400 | 500 |
| Referências (25 a 35 entradas em APA) | 478 (20 entradas) | ~850 |
| **Total** | **~8.900** | **~7.400**, com folga de 600 |

Se passar: cortar primeiro 4.3 e 4.4 (implicações e agenda), depois 1.1; nunca Methods e Results.

## 9. Conformidade com as instruções da revista

Conferido em 06/11/2026 em <https://prod.org.br/instructions>. Refazer no dia do envio (regra permanente do Heitor: nenhum artigo se fecha sem reler as regras do veículo).

| Regra | Situação hoje | Fase |
|---|---|---|
| Artigo original; sem *case report* | Precisa do enquadramento de pesquisa empírica de caso | F4 |
| Ordem das seções e numeração | Fora (seções 6, 7 e 9 extras; Literature Review separada) | F3 |
| 4.000 a 8.000 palavras com referências | ~8.900: acima | F3 a F5 |
| Título ≤ 15 palavras | 20: acima | F4 |
| Resumo ≤ 250 palavras em cinco partes rotuladas | 256, não estruturado | F4 |
| 3 a 5 palavras-chave, sem repetir o título | 8, repetem o título | F4 |
| `.docx` ou LaTeX; ≤ 3 MB | LaTeX via pacote de arquivo único | F6 |
| A4, margens 2,5 cm, Times 12 (10 em tabelas e figuras), espaço 1,5, recuo zero, justificado, uma coluna | `cas-dc`, duas colunas | F3 |
| Figuras JPEG ≥ 300 dpi com legenda e fonte; abreviaturas abaixo de tabelas e figuras | TikZ e pgfplots; sem notas de fonte | F3 |
| Sem notas de rodapé; equações numeradas; SI e ponto decimal | Conferir | F3 |
| APA; todos os autores na lista (sem "et al." nas referências); DOI quando houver; evitar teses e fontes de difícil acesso | natbib com `cas-model2-names`; bibliografia inválida | F1, F3 |
| Duplo-cego: sem autores, afiliações nem copyright no arquivo | Autores, GE Aviation e UCP no `main.tex` | F3 |
| Declaração de ética no manuscrito; parecer do CEP no sistema | Placeholders | D4, F6 |
| Conflito de interesse declarado; formulário assinado por todos | Declarado no manuscrito; carta do JATM contradiz | F3, F6 |
| Financiamento com a frase padrão | Frase do JATM | F3 |
| Uso de IA (regra 46) | Declaração negativa do JATM | D7 |
| Sem preprint; crédito a versão anterior em anais, se houver | Não há | OK |
| Agreement form, Open Science Compliance Form, Declaration of Conflict of Interest | A preparar | F6 |
| Autores fixos após a submissão | A fechar | D6 |

## 10. O que reaproveitar do artigo B

Copiar da pasta `Production-ABEPRO-secao-tematica-2027\`; nunca editar a pasta original.

| Arquivo do artigo B | Uso aqui | Adaptação |
|---|---|---|
| `main.tex` (preâmbulo) | Base do novo `main.tex` | Título, bibliografia, chave `\versaocega` |
| `secoes/06-declaracoes.tex` | Modelo das declarações | Conflito existente, ética real, dados confidenciais |
| `scripts/preparar_production.py`, etapa 3 | TikZ → PDF isolado → JPEG 600 dpi (`pdftoppm`) | Lista com as 8 figuras; descartar as etapas das tabelas do B |
| `scripts/pacote_scholarone.py` | Junta tudo num `manuscript.tex`, apaga comentários, escreve as citações em APA 7 no próprio arquivo (pandoc com `apa.csl`), troca fontes por Type 1, compila numa pasta limpa só com `pdflatex` e compara com o `main.pdf` | `FIGURAS`, `BIBS_CEGA` e `IDENTIFICADORES` (acrescentar GE, Cristiano, Pereira fora da lista de referências, Petr, UCP, Heitor) |
| `scripts/csl/apa.csl` | Estilo APA 7 do pacote | Igual (licença CC BY-SA 3.0) |
| `ENVIO-SCHOLARONE/03-formularios/latex/*.tex` | Agreement, conflito de interesse e Open Science em PDF com células largas para o carimbo do gov.br | Título, dois autores, quadro de autor com conflito |
| `PASSO-A-PASSO-SUBMISSAO.md`, partes B e C | Roteiro do ScholarOne (B0 a B7) e pós-envio | Igual; a parte A muda (decisões deste artigo) |
| `REGRAS-DO-VEICULO.md` | Checklist item por item | Refeito para este artigo a partir da seção 9 |

Fontes no novo `main.tex`: `newtxtext,newtxmath` (Times, como o template da revista). O ajuste de fontes do `CLAUDE.md` vale só para o `cas-dc`; as checagens de `pdftotext` (ligaduras, `??`, glifos, placeholders) continuam valendo depois de cada compilação.

## 11. Pacote do ScholarOne

| Arquivo | Designação no sistema |
|---|---|
| `manuscript.tex` | Main Document |
| 8 figuras `.jpg` | Arquivo suplementar de LaTeX (ou "Image"), conforme o menu |
| Agreement form assinado (PDF) | Agreement form |
| Open Science Compliance Form | Open Science Compliance Form (dados confidenciais: justificar) |
| Declaration of Conflict of Interest assinada por todos | Declaration of Conflict of Interest |
| Parecer do CEP ou documento de dispensa | Supplemental File NOT for Review |
| Carta de apresentação | Campo Cover Letter: escopo, relevância teórica e prática, objetivos, método, resultados e contribuição; seção temática, se D2 |

## 12. Riscos

| Risco | Sinal | Plano B |
|---|---|---|
| Dados brutos indisponíveis | D3 sem resposta até 20/11 | Não submeter. Números reconstruídos não entram apresentados como registros |
| Sem aprovação ética nem dispensa | D4 | Não submeter enquanto não houver caminho que a revista aceite |
| Revisão de confidencialidade da GE demorar | D3 | Pedir junto com os dados; rota de fluxo contínuo |
| Mesa ler o artigo como *case report* ou fora do escopo | Triagem | Pergunta de pesquisa e desenho explícitos; ancorar em custo da qualidade e operações centradas no humano; citar a própria *Production* |
| Passar de 8.000 palavras | F4 | Cortes da seção 8 |
| Prazo temático apertado | 20/11 | Fluxo contínuo |
| Conversor do ScholarOne falhar | Prova em PDF | O pacote já foi provado no artigo B; o log "TeX Processor Log" mostra a causa |

## 13. Regras para todo o trabalho

- **Zero invenção.** Nenhum número, referência ou DOI de memória. Números só de `dados/` gerados por script; referências só com registro conferido no Crossref ou na editora, com PDF na pasta.
- **Dados ditos como são.** Registro é registro; agregado ou reconstruído é dito assim no texto e na legenda.
- **Cegueira.** Nada de nome, afiliação, GE, Petrópolis ou autocitação em primeira pessoa no manuscrito; o vínculo do autor aparece de forma neutra e completa só nos formulários e no sistema.
- **Coerência entre documentos.** Manuscrito, carta, formulários e dados digitados no sistema dizem a mesma coisa sobre conflito, financiamento, ética e dados.
- **Não tocar** em `artigo/` (versão JATM congelada na tag) nem na pasta do artigo B.
- **Validar o PDF** depois de cada compilação, com as checagens do `CLAUDE.md`.
- **Ao fechar cada fase,** perguntar ao Heitor quais skills de validação rodar.

## 14. Fontes consultadas em 06/11/2026

- Instruções aos autores: <https://prod.org.br/instructions>
- Chamada da seção temática: <https://ijcieom.org/2027/call-for-papers.html>
- Kit do artigo B: `REGRAS-DO-VEICULO.md`, `LEIA-ME.md`, `PASSO-A-PASSO-SUBMISSAO.md`, `ENVIO-SCHOLARONE/LEIA-ME.md`, `main.tex`, `scripts/`
- Parecer pré-submissão: `planejamento/002_parecer_pre_submissao.html` (11/08/2026)
- Plano anterior: `planejamento/001_migracao_artigo_jatm.md`
