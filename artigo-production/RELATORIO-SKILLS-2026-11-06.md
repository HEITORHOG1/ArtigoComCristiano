# Rodada das skills no manuscrito (06/11/2026)

Pedido do Heitor: "é só você rodar as skills: /workflow-artigo e /anti-vicios-ia e as skills de artigos que temos, e de referências". O manuscrito é o de `artigo-production/`, com o texto do original restaurado.

## Pré-requisitos das skills

| Item | Situação |
|---|---|
| Título | *Kirkpatrick-Based Framework Integrating Safety and Sustainability in Aviation Maintenance: Waste Reduction and Resource Efficiency* (inglês, 14 palavras) |
| Resumo e palavras-chave | `secoes/00-resumo.tex`: resumo estruturado; palavras-chave *training evaluation; AS9100; cost of quality; human factors; cleaner production* |
| Pasta de PDFs | `referencias-pdf/` **estava vazia**. Recebeu os 5 PDFs abertos das referências verificadas: FAA AC 120-92D, EASA ASR 2025, Boyd & Stolzer, Leveson e Shunko et al. (manuscrito dos autores). Faltam 6, que são livros ou artigos pagos e precisam vir do Cristiano |

## O que cada skill fez

| Skill | O que foi feito | Resultado |
|---|---|---|
| `anti-vicios-ia`, com `pesquisador-senior` e `escritor-cientifico` | Diagnóstico com `scripts/auditar_estilo.py` e reescrita autônoma (Modo C), sem retirar ideia, número ou citação | Ver a tabela "Antes e depois" |
| `revisor-critico`, `discussao-limitacoes`, `estatistica-reporting`, `reporting-guidelines` e `figuras-tabelas` | Revisão independente, por um agente que não participou da redação | Nota geral **R** (revisão necessária), com 4 achados que bloqueiam o envio, 14 importantes e 10 menores. O que não depende dos autores foi aplicado; o resto está em `PENDENCIAS.md` |
| Referências: passo 2 da `anti-vicios-ia`, etapa 7 da `workflow-artigo` e fontes da `revisor-critico` | Busca na web das 23 referências não localizadas e das 4 citações sem entrada; conferência, nos PDFs, das frases que citam as 11 verificadas | 22 não existem; 1 achada com outro título; 3 citações sem entrada identificadas; 6 frases não batem com a fonte real (detalhes em `PENDENCIAS.md`) |
| `editor-cientifico` | Conferência das regras da *Production* (`REGRAS-DO-VEICULO.md`) | Formato OK, inclusive a letra de 10 pt em tabelas, legendas e notas (corrigida). Pendentes: limite de palavras, referências, ética |
| `workflow-artigo` | Checklist das etapas 0 a 10 sobre o artigo existente | Ver a tabela "Etapas" |
| Não se aplicam | `latex-elsevier-cas` e `journal-jatm` (a revista não é mais Elsevier nem o JATM); `highlights-graphical-abstract` (a *Production* não pede); `resposta-revisores` (ainda não há pareceres); `revisao-sistematica-prisma` (o artigo não é revisão sistemática) | — |

## Antes e depois (estilo)

Contagem do `scripts/auditar_estilo.py`, aproximada, sobre o texto das seções:

| Medida | Antes | Depois |
|---|---|---|
| Média de palavras por frase | 28,9 | 22,7 |
| Desvio-padrão do tamanho das frases | 15,8 | 9,8 |
| Frases com mais de 35 palavras | 58 | 26 |
| Marcadores de estilo (*robust*, *not only… but also*, *foster*, *synergy*, *serves as*, *critical* retórico etc.) | 39 | 17 |
| Travessões e transições como *Furthermore* e *Moreover* | 0 | 0 |

As listas de três itens não foram quebradas de propósito. Quase todas são conteúdo (cláusulas, categorias, itens de questionário), e quebrá-las exigiria tirar itens.

## Mudanças no manuscrito

- **Estilo:**
  - frases longas divididas;
  - intensificadores trocados;
  - siglas definidas na primeira vez (AI, EEG, fNIRS, IoT);
  - o LMS com um nome só;
  - os dois parágrafos-lista da Discussão viraram listas numeradas.
- **Afirmações calibradas ao desenho do estudo** (caso único, antes e depois, sem grupo de controle): *yielded*, *preventing*, *strengthened*, *confirmed*, *show*, *drives*, *safeguards*, *applies* e *correlate with* passaram a *associated with*, *suggest*, *can*, *was designed to* e equivalentes.
- **Contradições desfeitas:**
  - a Discussão dizia que o tempo de atendimento melhorou, mas a Fig. 8 mostra que foi das notas mais baixas, numa pesquisa do início do ano;
  - o 28% aparecia como "errors" num lugar e como "training failures" em outro;
  - o método dizia que o caso não era controlável pelos pesquisadores, mas a Introdução diz que os autores implantaram o modelo.
- **Fontes:**
  - frases ajustadas ao que Leveson, FAA, Boyd & Stolzer, Shunko, Pereira e Oschman de fato dizem;
  - o "15% e 57%" foi corrigido pela fonte real (IATA, 2009, com dados de 2008);
  - entraram Buriak & Ayars (2019), Jung et al. (2019) e Yücel & Ayvaz (2019);
  - avisos vermelhos onde a fonte conferida não traz o número.
- **Método:**
  - rótulo de estudo de caso intervencionista;
  - nova ameaça à validade (quem implantou também avaliou);
  - avisos com os dados que faltam.
- **Tabela 2:** duas limitações novas (amostras pequenas; sem medida anterior nos Níveis 1, 2 e 4) e duas células corrigidas.
- **Figuras 1 a 5:** corrigidas (ver `PENDENCIAS.md`, seção 5), mais fiéis ao original.
- **Estrutura:** subtítulo próprio para as lacunas de pesquisa (1.5); a antiga 1.5 virou 1.6.

## Etapas da `workflow-artigo`

| Etapa | Situação |
|---|---|
| 0 Briefing | Respostas no plano `planejamento/003_migracao_production_scielo.md`. Prazo: 30/11/2026 se for a seção temática (D2) |
| 1 Título | OK: 14 palavras, palavras-chave no início. A revisão sugere ajuste (D8) |
| 2 Resumo e palavras-chave | OK: cinco partes rotuladas, cerca de 220 palavras; as palavras-chave não repetem o título |
| 3 Introdução e revisão | Estrutura OK. **Falha no critério "bibliografia pertinente":** a maior parte da revisão se apoia em referências inexistentes |
| 4 Método | Fases, instrumentos e ameaças à validade OK. Faltam datas, amostragem, grupo focal, codificação e ética |
| 5 Resultados e discussão | Faltam a linha de base, os resultados do Nível 3 e a triangulação com fontes reais |
| 6 Conclusão | Responde às quatro RQs, sem informação nova |
| 7 Referências | `biber` sem avisos; toda citação tem entrada. **22 inexistentes** |
| 8 Figuras e tabelas | Figs. 1 a 5 a 400 dpi e corrigidas; Figs. 6 a 8 abaixo de 300 dpi |
| 9 Compilação | 0 erros, 0 linhas estouradas, 26 páginas, só fontes Type 1, sem ligadura quebrada |
| 10 Submissão | **Não pronto.** Alertas da skill: limite de palavras excedido (8.342 de 8.000) e referências inexistentes |

## Relatório de conclusão (etapa 10)

```text
========================================
ARTIGO: NAO PRONTO PARA SUBMISSAO
========================================
Titulo: Kirkpatrick-Based Framework Integrating Safety and Sustainability in
        Aviation Maintenance: Waste Reduction and Resource Efficiency
Palavras-chave: training evaluation; AS9100; cost of quality; human factors;
                cleaner production
Total de palavras: 8.342 sem avisos vermelhos (limite 8.000 com referencias)
Total de paginas: 26 (main.pdf); 27 no pacote do ScholarOne
Figuras: 8 | Tabelas: 2
Referencias na lista: 36 (15 conferidas; 21 inexistentes citadas no texto)
Avisos vermelhos no texto: 30
Alvo: Production (ABEPRO, SciELO), ScholarOne prod-scielo
Data: 06/11/2026
========================================
```
