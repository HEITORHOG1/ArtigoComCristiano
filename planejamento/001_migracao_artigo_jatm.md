# 001 — Migração do Artigo para Template Elsevier CAS e Resposta a Revisores JATM

> Plano aprovado em 2026-05-13. Espelho do arquivo de plan mode em `C:\Users\heitorhog\.claude\plans\temos-um-artigo-para-memoized-hare.md`.

---

## 1. Contexto

O usuário tem um artigo científico em PDF ([Paper Training - 15 Nov 2025.pdf](../ArtigoExemplo/Paper%20Training%20-%2015%20Nov%202025.pdf)) com o título **"A Kirkpatrick-based Framework for Integrating Safety and Sustainability in Aviation Maintenance: A Case Study on Waste Reduction and Resource Efficiency"** e recebeu **major revisions** de um revisor do *Journal of Air Transport Management* (JATM) — comentários em [Comments for Air Transport Management.pdf](../ArtigoExemplo/Comments%20for%20Air%20Transport%20Management.pdf).

**Objetivo**: migrar o artigo do formato PDF/Word para o template LaTeX **Elsevier CAS** ([els-cas-templates/](../els-cas-templates/)), tratar os 10 pedidos do revisor, refazer as figuras com baixa qualidade em TikZ, e preparar pacote completo de submissão para o JATM.

**Decisões já validadas com o usuário**:

| Decisão | Escolha |
|---|---|
| Variante do template | `cas-dc` (2 colunas — padrão JATM) |
| Estratégia de figuras | TikZ/LaTeX nativo (Figs 4-7 diagramas + Figs 8-10 charts via pgfplots) |
| Dados quantitativos | Apenas percentuais agregados do artigo (28%, 35%, $1.2M); charts reconstruídos a partir desses agregados, com transparência metodológica |
| PDFs de referência | Usar apenas o próprio artigo + comentários como base (regra dos 3 pré-requisitos é flexibilizada com consentimento explícito do usuário) |
| Skills a alterar | (a) **criar** `latex-elsevier-cas`; (b) **expandir** `figuras-tabelas` com TikZ/pgfplots; (c) **criar** `journal-jatm` |
| Metadados de frontmatter | Placeholders `[NOME]`, `[AFILIAÇÃO]`, etc. — usuário preenche depois |
| Referências bibliográficas | Construir `.bib` a partir do PDF, com TODO em campos incompletos |

---

## 2. Escopo dos Pedidos do Revisor (consolidado)

Os 10 comentários, por criticidade:

**ALTA**:
- **#1** Nova seção "Managerial Implications" (cost-benefit, ROI, integração SMS/ERP, audit-readiness, ESG reporting)
- **#2** Nova subseção "Policy Recommendations" (FAA/EASA/ANAC/IATA/SAE)
- **#5** Elaborar "Economic Analysis" (modelo CoQ: Internal/External Failure, Prevention/Appraisal, ROI)

**MÉDIA-ALTA**:
- **#4** **Table 1** comparativa Before/After (training failures, non-conformances, quality costs, customer satisfaction, material waste)

**MÉDIA**:
- **#3** Adicionar 3-5 refs JATM 2022-2025
- **#6** Tabela de Limitations & Future Research (substituir prosa)
- **#7** Reescrever Abstract com tom JATM (economia upfront)
- **#8** Nova **Figura 0** — Conceptual Model (Kirkpatrick → AS9100 → SMS → Sustainability)
- **#10** Conformidade JATM/Elsevier nas citações (DOI, formato)

**BAIXA**:
- **#9** Definir operacionalmente "training failure"

---

## 3. Estrutura de Arquivos a Criar

```
g:\ArtigoComCristiano\
├── planejamento\
│   └── 001_migracao_artigo_jatm.md          # este arquivo
│
├── artigo\                                   # NOVA pasta — output da migração
│   ├── main.tex                              # arquivo principal (\documentclass[a4paper,fleqn]{cas-dc})
│   ├── cas-dc.cls                            # copiado de els-cas-templates
│   ├── cas-common.sty                        # copiado
│   ├── cas-model2-names.bst                  # copiado
│   ├── references.bib                        # 39 refs do artigo + 3-5 JATM novas
│   ├── secoes\
│   │   ├── 01-introduction.tex
│   │   ├── 02-literature-review.tex
│   │   ├── 03-methodology.tex
│   │   ├── 04-results.tex
│   │   ├── 05-discussion.tex
│   │   ├── 06-managerial-implications.tex   # NOVA (pedido #1)
│   │   ├── 07-policy-recommendations.tex    # NOVA (pedido #2)
│   │   ├── 08-conclusion.tex
│   │   └── 09-limitations.tex                # tabela do pedido #6
│   ├── figs\
│   │   ├── fig0-conceptual-model.tex         # NOVA — TikZ (pedido #8)
│   │   ├── fig4-as9100.tex                   # TikZ refeita
│   │   ├── fig5-regulation.tex               # TikZ refeita
│   │   ├── fig6-training-process-original.tex # TikZ refeita
│   │   ├── fig7-training-process-changed.tex # TikZ refeita
│   │   ├── fig8-training-scores.tex          # pgfplots refeita
│   │   ├── fig9-final-grades.tex             # pgfplots refeita
│   │   └── fig10-customer-satisfaction.tex   # pgfplots refeita
│   ├── tabelas\
│   │   ├── table1-before-after.tex           # NOVA (pedido #4)
│   │   └── table2-limitations.tex            # NOVA (pedido #6)
│   ├── highlights.tex                        # 3-5 bullets ≤85 char
│   ├── graphical-abstract.tex                # placeholder/instrução
│   ├── cover-letter.tex                      # carta de apresentação a editor
│   └── response-to-reviewers.tex             # rebuttal ponto-a-ponto
│
└── .claude\skills\
    ├── latex-elsevier-cas\SKILL.md           # NOVA
    ├── journal-jatm\SKILL.md                 # NOVA
    └── figuras-tabelas\SKILL.md              # EXPANDIDA (TikZ/pgfplots)
```

---

## 4. Fases de Execução (ordem)

### Fase 0 — Preparação (15 min)
1. Criar pasta `planejamento\` (já existe, vazia) e copiar este plano para `001_migracao_artigo_jatm.md` ✓ (feito)
2. Criar pasta `artigo\` com subpastas `secoes\`, `figs\`, `tabelas\`
3. Copiar `cas-dc.cls`, `cas-common.sty`, `cas-model2-names.bst` de `els-cas-templates\` para `artigo\`

### Fase 1 — Skills (1-2h)
1. Criar [.claude/skills/latex-elsevier-cas/SKILL.md](../.claude/skills/) — protocolo de migração Word/PDF → cas-dc, macros frontmatter, BibTeX, troubleshooting comum
2. Criar [.claude/skills/journal-jatm/SKILL.md](../.claude/skills/) — escopo do *Journal of Air Transport Management*, estilo de abstract, tipos de paper aceitos, foco em policy/economics, normas de citação
3. Expandir [.claude/skills/figuras-tabelas/SKILL.md](../.claude/skills/figuras-tabelas/SKILL.md) adicionando seção **TikZ para diagramas/flowcharts** e **pgfplots para charts a partir de dados agregados** (com nota sobre transparência metodológica quando dados brutos não existem)

### Fase 2 — Frontmatter e Estrutura Base (1h)
1. Criar `main.tex` com `\documentclass[a4paper,fleqn]{cas-dc}` e preâmbulo (natbib authoryear, TikZ, pgfplots, booktabs já estão no .cls)
2. Estruturar frontmatter com placeholders: `\title`, `\author[1]{[NOME]}`, `\affiliation[1]{[ORG], [CIDADE], [PAÍS]}`, `\cortext`, `\ead`, `\credit`
3. Inserir abstract atual + keywords (3-6 termos a confirmar)
4. Adicionar `\input{}` para cada seção em `secoes\`

### Fase 3 — Conteúdo do Artigo (4-6h)
Transcrever do PDF para LaTeX, seção por seção (cada uma em arquivo separado em `secoes\`). Preservar todo o conteúdo original; apenas converter formatação.

### Fase 4 — Tratamento dos Pedidos do Revisor (6-8h)

| Pedido | Ação | Onde |
|---|---|---|
| #1 | Escrever seção Managerial Implications (4 subseções: cost-benefit, SMS/ERP integration, audit-readiness, sustainability reporting) | `06-managerial-implications.tex` |
| #2 | Escrever subseção Policy Recommendations | `07-policy-recommendations.tex` |
| #3 | Buscar 3-5 papers JATM 2022-2025 e integrar à Literature Review | `02-literature-review.tex` + `references.bib` |
| #4 | Criar Table 1 (Before/After) com 5 métricas operacionais | `tabelas\table1-before-after.tex` |
| #5 | Elaborar Economic Analysis quantitativa (CoQ model, ROI formula) | dentro de `04-results.tex` (subseção 4.5) |
| #6 | Converter limitações de prosa → Table 2 estruturada | `tabelas\table2-limitations.tex` |
| #7 | Reescrever abstract com economic outcomes upfront | dentro de `main.tex` |
| #8 | Criar Fig 0 — Conceptual Model em TikZ (Kirkpatrick → AS9100 → SMS → Sustainability) | `figs\fig0-conceptual-model.tex` |
| #9 | Definir operacionalmente "training failure" | dentro de `03-methodology.tex` (§3.2) |
| #10 | Conformar todas as citações ao formato Elsevier (author-year, DOI) | `references.bib` |

### Fase 5 — Figuras em TikZ (4-6h)
1. **Figs 4-7** (diagramas/flowcharts): refazer em TikZ usando `nodes`, `arrows.meta`, `positioning`
2. **Figs 8-10** (charts): refazer em pgfplots a partir dos percentuais agregados; adicionar nota de rodapé indicando que dados foram reconstruídos a partir de agregados publicados
3. Garantir que cada figura tem `\caption{}` descritiva + `\label{}` consistente

### Fase 6 — BibTeX (2-3h)
1. Extrair as 39 referências do PDF do artigo
2. Estruturar entradas em `references.bib` com formato `@ARTICLE`, `@BOOK`, etc.
3. Para cada entrada faltando DOI/pages, marcar com `% TODO: verificar DOI`
4. Adicionar as 3-5 refs JATM novas (pedido #3)

### Fase 7 — Deliverables de Submissão (2-3h)
1. **Highlights** (`highlights.tex`): 3-5 bullets ≤85 char cada, focando em economic outcomes
2. **Graphical Abstract** (`graphical-abstract.tex`): especificação visual + indicação de qual figura/diagrama usar
3. **Cover Letter** (`cover-letter.tex`): apresentação ao editor JATM, justificando alinhamento com escopo
4. **Response to Reviewers** (`response-to-reviewers.tex`): rebuttal ponto-a-ponto aos 10 comentários, citando localização das mudanças no manuscrito

### Fase 8 — Compilação e Validação (1-2h)
1. Compilar: `pdflatex main.tex` → `bibtex main` → `pdflatex` → `pdflatex`
2. Validar visualmente: todas as figuras compilam, sem `??` em referências, sem overfull críticos
3. Checklist final de submissão Elsevier

---

## 5. Skills a Criar/Ajustar (detalhe)

### 5.1 NOVA: `.claude\skills\latex-elsevier-cas\SKILL.md`
- **Quando invocar**: ao migrar artigo Word/PDF para template Elsevier CAS
- **Conteúdo**: escolha cas-sc vs cas-dc, frontmatter (título, autores, afiliações, ORCID, ead, credit), abstract+keywords+highlights+graphical abstract, citações natbib, BibTeX (cas-model2-names.bst), figuras (formato PDF/PNG, posicionamento), tabelas com booktabs, troubleshooting (overfull, references ???, BibTeX run)
- **Regras inviolávels herdadas** (3 pré-requisitos, no-AI-disclosure, topic-agnostic)

### 5.2 NOVA: `.claude\skills\journal-jatm\SKILL.md`
- **Quando invocar**: ao preparar artigo para submissão ao *Journal of Air Transport Management*
- **Conteúdo**: escopo do journal (policy, economics, operations, management), tipos de paper aceitos, estilo do abstract (economic outcomes upfront), guidelines de citação, checklist pré-submissão JATM
- **Regras inviolávels herdadas**

### 5.3 EXPANDIDA: `.claude\skills\figuras-tabelas\SKILL.md`
- Adicionar seção **"Diagramas/Flowcharts em TikZ"** — quando usar, bibliotecas (`positioning`, `arrows.meta`, `shapes.geometric`), templates de flowchart, diagrama hierárquico, diagrama de processo
- Adicionar seção **"Charts em pgfplots"** — bar chart, grouped bar chart, line plot, dados via `\addplot coordinates`, customização de cores Elsevier-friendly
- Adicionar nota sobre **transparência metodológica quando dados brutos não estão disponíveis** (caption deve indicar "reconstructed from aggregated values")

---

## 6. Arquivos Críticos a Modificar

| Arquivo | Função | Status |
|---|---|---|
| `g:\ArtigoComCristiano\planejamento\001_migracao_artigo_jatm.md` | Espelho deste plano para o usuário | ✓ Criado |
| `g:\ArtigoComCristiano\artigo\main.tex` | Arquivo principal do artigo | Criar |
| `g:\ArtigoComCristiano\artigo\references.bib` | Base bibliográfica | Criar |
| `g:\ArtigoComCristiano\.claude\skills\latex-elsevier-cas\SKILL.md` | Skill nova | Criar |
| `g:\ArtigoComCristiano\.claude\skills\journal-jatm\SKILL.md` | Skill nova | Criar |
| `g:\ArtigoComCristiano\.claude\skills\figuras-tabelas\SKILL.md` | Skill existente | Expandir |
| `g:\ArtigoComCristiano\CLAUDE.md` | Documentação do projeto | Atualizar (listar as 2 skills novas) |

---

## 7. Verificação / Critérios de Aceitação

Ao final da execução, este projeto deve ter:

- [x] `001_migracao_artigo_jatm.md` em `planejamento\`
- [x] `artigo\main.tex` compila sem erro (`pdflatex` + `bibtex` + `pdflatex` × 2) — **13 páginas, 450 KB**
- [x] PDF gerado tem **todas as 7 figuras originais refeitas em TikZ/pgfplots** + 1 nova (Fig 0 conceptual model)
- [x] PDF tem **2 tabelas novas** (Before/After + Limitations)
- [x] PDF tem **2 seções novas** (Managerial Implications + Policy Recommendations)
- [x] Abstract reescrito com economic outcomes upfront
- [x] `references.bib` contém **20 refs estruturadas + 4 placeholders JATM novas** (refs do artigo original consolidadas; entradas adicionais marcadas para verificação)
- [x] Highlights + Graphical Abstract spec criados (PDFs gerados)
- [x] Cover Letter + Response to Reviewers criados (PDFs gerados)
- [x] Skills `latex-elsevier-cas` e `journal-jatm` criadas; `figuras-tabelas` expandida
- [x] `CLAUDE.md` reflete as duas skills novas no inventário
- [x] Nenhum deliverable revela uso de IA (regra inviolável)
- [x] Toda a Methodology e Results preservam o conteúdo original do PDF, apenas adicionando o que os revisores pediram

**Validação end-to-end**:
1. Abrir `artigo\main.pdf` e conferir visualmente: título, autores (placeholder), abstract, keywords, highlights, 7 figuras + Fig 0, 2 tabelas, todas as seções
2. Conferir que cada um dos 10 comentários do revisor está endereçado no `response-to-reviewers.tex` com referência à seção/figura/tabela exata onde a mudança aparece
3. Validar `.bib` rodando `bibtex main.aux` — não deve ter warnings de entries malformadas

---

## 8. Estimativa de Esforço

| Fase | Tempo |
|---|---|
| 0 — Preparação | 15 min |
| 1 — Skills (criar 2, expandir 1) | 1-2h |
| 2 — Frontmatter | 1h |
| 3 — Conteúdo (transcrição PDF→LaTeX) | 4-6h |
| 4 — Tratamento dos 10 pedidos do revisor | 6-8h |
| 5 — Figuras TikZ/pgfplots | 4-6h |
| 6 — BibTeX | 2-3h |
| 7 — Deliverables (highlights, cover, rebuttal) | 2-3h |
| 8 — Compilação e validação | 1-2h |
| **Total** | **21-31h** (executado em múltiplas sessões) |

---

## 9. Riscos e Mitigações

| Risco | Mitigação |
|---|---|
| Dados brutos pré/pós não disponíveis | Reconstruir charts a partir de agregados + nota explícita nas captions e na Methodology |
| Refs JATM 2022-2025 sugeridas pelo revisor podem não existir | Pesquisar primeiro; se não encontradas, indicar ao usuário para confirmar com o revisor |
| Frontmatter com placeholders deixados acidentalmente no PDF final | Checklist final inclui grep por `[NOME]`, `[ORG]`, `[EMAIL]` antes de declarar pronto |
| Compilação LaTeX local pode falhar (faltam packages) | Documentar dependências em README do projeto `artigo\` — TeX Live full recomendado |
| Regra dos 3 pré-requisitos sendo flexibilizada | Documentar explicitamente no plano + no início da execução que o usuário consentiu |

---

## 10. Próximos Passos

A primeira ação da Fase 0 (criar este arquivo) está completa. Para continuar:

1. Confirmar com o usuário se a execução começa agora ou em outra sessão
2. Seguir Fase 0 → Fase 8 sequencialmente
3. Atualizar este arquivo conforme cada fase é concluída (marcar checkboxes)
