---
name: revisao-sistematica-prisma
description: Conduz revisão sistemática da literatura seguindo PRISMA 2020 — formulação da pergunta (PICO/PICOC/PEO), strings de busca, critérios de inclusão/exclusão, fluxograma PRISMA, extração de dados, avaliação de risco de viés, síntese narrativa ou meta-análise, checklist 27-itens. Use quando o artigo terá uma seção de revisão sistemática ou scoping review, ou quando o trabalho inteiro é uma SLR/meta-análise. Antes de iniciar, exige obrigatoriamente título, abstract e pasta de PDFs de referência.
---

# Revisão Sistemática — PRISMA 2020

Skill para conduzir revisão sistemática da literatura ou scoping review com rigor metodológico publicável em Q1.

---

## ⛔ PRÉ-REQUISITOS OBRIGATÓRIOS — NÃO COMECE SEM ELES

Antes de qualquer trabalho, você DEVE ter:

### 1. TÍTULO DO ARTIGO
- Título completo, idioma, subtítulo

### 2. ABSTRACT DO ARTIGO
- Texto integral + palavras-chave
- Necessário para alinhar a pergunta de pesquisa da SLR ao escopo

### 3. PASTA DE PDFs DE REFERÊNCIA
- Caminho absoluto da pasta
- Pode conter os PDFs já triados pela SLR ou os PDFs-semente para construir a string de busca

### Mensagem-padrão quando faltar algo

> Para conduzir a revisão sistemática preciso obrigatoriamente de:
> 1. **Título** do artigo: [pendente / fornecido]
> 2. **Abstract** + palavras-chave: [pendente / fornecido]
> 3. **Pasta de PDFs** de referência (caminho absoluto): [pendente / fornecido]
>
> Sem esses três itens não inicio. Por favor envie o que está faltando.

Não aceite "manda depois". Confirme cada item recebido.

---

## 🚫 NUNCA REVELAR USO DE IA

**Regra inviolável:** o protocolo, a SLR e qualquer material derivado **JAMAIS** mencionam que foram escritos/assistidos/revisados por IA, LLM, GPT, Claude, ChatGPT ou modelo de linguagem. Sem disclosures, sem agradecimentos a ferramentas de IA. Exceção única: quando IA é o **objeto da pesquisa** — mesmo assim, sem autorrevelação do processo.

---

## 📐 PRISMA 2020 — VISÃO GERAL

PRISMA 2020 (Page et al., *BMJ* 2021) é o padrão internacional para reportar revisões sistemáticas. Tem **27 itens de checklist** + **fluxograma de seleção**. Adesão é frequentemente **obrigatória** em journals Q1 (BMJ, JAMA, Lancet, Cochrane, Elsevier de saúde/engenharia, etc.).

Para **scoping reviews**, use **PRISMA-ScR** (Tricco et al., *Annals* 2018).
Para **meta-análises de IPD** (individual participant data), use **PRISMA-IPD**.
Para **abstracts de SLR**, use **PRISMA-S** (search) e **PRISMA-A** (abstract).

---

## 🎯 ETAPA 1 — PERGUNTA DE PESQUISA E FRAMEWORK

Escolha o framework adequado ao tipo de pergunta:

| Framework | Uso |
|-----------|-----|
| **PICO** | Intervenção clínica (Population, Intervention, Comparison, Outcome) |
| **PICOC** | Intervenção em qualquer área (+ Context) |
| **PEO** | Pesquisa qualitativa (Population, Exposure, Outcome) |
| **SPIDER** | Estudos qualitativos/mistos (Sample, Phenomenon of Interest, Design, Evaluation, Research type) |
| **CIMO** | Pesquisa em management (Context, Intervention, Mechanism, Outcome) |
| **PCC** | Scoping review (Population, Concept, Context) |

Formato de saída:

```
## Pergunta de Pesquisa
**Tipo:** [Sistemática / Scoping / Meta-análise]
**Framework:** [PICO/PICOC/PEO/...]

- **P** (Population/Problem): [...]
- **I** (Intervention/Concept): [...]
- **C** (Comparison/Context): [...]
- **O** (Outcome): [...]

**Pergunta primária:** [pergunta única, específica, respondível]
**Perguntas secundárias:** (até 3, opcional)
```

---

## 🔎 ETAPA 2 — PROTOCOLO E PRÉ-REGISTRO

Antes de buscar:

1. **Redigir o protocolo** (idealmente seguindo PRISMA-P 2015)
2. **Pré-registrar** em uma das plataformas:
   - **PROSPERO** (saúde, métodos sociais relacionados a saúde) — gratuito
   - **OSF Registries** (genérico, qualquer área) — gratuito
   - **Research Registry** (alternativa)
   - **INPLASY** (pago/grátis dependendo)
3. **Documentar** desvios do protocolo posteriormente, com justificativa

Conteúdo mínimo do protocolo: pergunta, critérios de elegibilidade, fontes de informação, estratégia de busca, processo de seleção, extração de dados, risco de viés, métodos de síntese.

---

## 📚 ETAPA 3 — ESTRATÉGIA DE BUSCA

### 3.1 Bases de dados (mínimo 3, ideal 4–6)

**Por área:**
- **Saúde:** PubMed/MEDLINE, Embase, Cochrane CENTRAL, CINAHL, PsycINFO, Web of Science, Scopus
- **Engenharia:** Scopus, Web of Science, IEEE Xplore, ACM Digital Library, Engineering Village (Compendex), ScienceDirect
- **Ciências Sociais:** Scopus, Web of Science, PsycINFO, Sociological Abstracts, ERIC, Business Source
- **Multidisciplinar:** Google Scholar (sempre como complemento, nunca como única fonte)
- **Cinza:** OpenGrey (descontinuado, alternativas: BASE, CORE, ProQuest Dissertations)

### 3.2 String de busca (search string)

Construa a string usando:
- **Operadores booleanos:** `AND`, `OR`, `NOT`
- **Truncamento:** `*` (varia por base)
- **Aspas:** `"machine learning"` para frase exata
- **Proximidade:** `NEAR/n`, `W/n` (varia por base)
- **MeSH terms** (PubMed) ou **Emtree** (Embase) quando disponíveis
- **Filtros:** período, idioma, tipo de documento

Estrutura típica:
```
("conceito1" OR sinonimo1 OR sinonimo2)
  AND
("conceito2" OR sinonimo1 OR sinonimo2)
  AND
("conceito3" OR sinonimo1 OR sinonimo2)
```

**Exemplo (engenharia, FMEA + IA):**
```
("FMEA" OR "Failure Mode and Effects Analysis" OR "FMECA")
  AND
("artificial intelligence" OR "machine learning" OR "deep learning" OR "neural network*")
  AND
("risk" OR "reliability" OR "safety")
```

### 3.3 Adaptação por base
A string varia entre bases. Documentar **TODAS as strings** usadas, com data de execução e número de hits. Tabela:

| Base | String | Data | Hits |
|------|--------|------|------|
| Scopus | `TITLE-ABS-KEY(...)` | 2025-XX-XX | N |
| Web of Science | `TS=(...)` | 2025-XX-XX | N |
| ... | ... | ... | ... |

### 3.4 Busca complementar
- **Backward citation chasing** (referências dos incluídos)
- **Forward citation chasing** (quem citou os incluídos)
- **Hand-search** em journals-chave da área (últimos 3 anos)
- **Contato com especialistas** (opcional)

---

## 🧪 ETAPA 4 — CRITÉRIOS DE ELEGIBILIDADE

Tabela explícita de **inclusão** e **exclusão**:

| Dimensão | Inclusão | Exclusão |
|----------|----------|----------|
| Tipo de estudo | [empírico, RCT, observacional, ...] | [editorial, opinião, ...] |
| Período | [ex.: 2014–2025] | [pré-2014] |
| Idioma | [EN, PT, ES] | [outros] |
| População | [...] | [...] |
| Intervenção | [...] | [...] |
| Outcome | [pelo menos um relatado] | [não reporta] |
| Acesso | [full-text disponível] | [só abstract] |

Critérios **a priori** — definidos no protocolo, antes de olhar os resultados.

---

## 🔧 ETAPA 5 — SELEÇÃO DE ESTUDOS

### Processo em 2 fases

**Fase 1 — Title/Abstract:**
- 2 revisores independentes triam cada registro
- Tela cega quando possível
- Discordâncias resolvidas por discussão ou 3º revisor
- Reportar concordância (Cohen's kappa)

**Fase 2 — Full-text:**
- Mesmo processo, agora com texto completo
- Documentar motivo de exclusão de cada full-text excluído

### Ferramentas
- **Covidence** (pago, padrão Cochrane)
- **Rayyan** (gratuito, blinding nativo)
- **EPPI-Reviewer**
- **DistillerSR**

### Fluxograma PRISMA 2020 — números a coletar
- Records identified (por base)
- Records removed before screening (duplicates, automation tools)
- Records screened (title/abstract)
- Records excluded
- Reports sought for retrieval
- Reports not retrieved
- Reports assessed for eligibility
- Reports excluded (com motivos)
- Studies included in review
- Reports of included studies

---

## 📝 ETAPA 6 — EXTRAÇÃO DE DADOS

Formulário **piloto** primeiro (5–10 estudos), refinar, depois aplicar a todos.

Campos típicos:
- Identificação: autor(es), ano, país, journal
- Desenho do estudo
- População/contexto
- Intervenção/exposição
- Comparador
- Outcomes (primário, secundários)
- Tamanho de amostra
- Resultados-chave (com IC quando disponível)
- Fonte de financiamento
- Conflitos de interesse declarados

2 extratores independentes, conferência cruzada.

---

## ⚖️ ETAPA 7 — AVALIAÇÃO DE RISCO DE VIÉS

Use a ferramenta apropriada ao tipo de estudo:

| Tipo de estudo | Ferramenta |
|----------------|-----------|
| RCT | **RoB 2** (Cochrane, 2019) |
| Observacional não-randomizado de intervenção | **ROBINS-I** |
| Observacional de exposição | **ROBINS-E** |
| Estudos diagnósticos | **QUADAS-2** |
| Estudos de prognóstico | **QUIPS** |
| Modelos de predição | **PROBAST** |
| Reviews já existentes | **AMSTAR-2** ou **ROBIS** |
| Qualitativos | **CASP**, **JBI** |
| Mistos | **MMAT** |

Reportar avaliação por estudo + visão agregada (traffic-light plot via `robvis` em R).

---

## 🧮 ETAPA 8 — SÍNTESE

### 8.1 Síntese narrativa (sempre)
Estruturar por:
- Características dos estudos incluídos (tabela de evidência)
- Achados principais (por outcome, por subgrupo)
- Heterogeneidade (clínica, metodológica, estatística)

### 8.2 Síntese quantitativa — Meta-análise (quando apropriado)
**Pré-condições:** ≥2 estudos comparáveis, mesmo outcome, similaridade clínica/metodológica.

**Decisões:**
- Modelo: efeitos fixos vs. aleatórios (geralmente aleatórios — DerSimonian-Laird ou REML)
- Effect size: SMD (Cohen's d, Hedges' g), OR, RR, MD
- Heterogeneidade: I², τ², Cochran's Q
- Forest plot: obrigatório
- Funnel plot + teste de Egger: ≥10 estudos
- Sensitivity analysis (leave-one-out)
- Subgrupos / meta-regressão (quando justificado e pré-registrado)

**Software:**
- **R:** `metafor`, `meta`, `metaSEM`
- **Stata:** `meta` suite
- **RevMan** (Cochrane)
- **Comprehensive Meta-Analysis** (CMA, pago)

### 8.3 Síntese sem meta-análise (SWiM)
Use guidelines **SWiM** (Campbell et al., *BMJ* 2020) quando meta-análise não é viável.

---

## 📋 ETAPA 9 — CHECKLIST PRISMA 2020 (27 itens)

| # | Item | Seção |
|---|------|-------|
| 1 | Title (identifica como SLR) | Title |
| 2 | Structured abstract (PRISMA-A) | Abstract |
| 3 | Rationale | Introduction |
| 4 | Objectives (PICO/equiv) | Introduction |
| 5 | Eligibility criteria | Methods |
| 6 | Information sources | Methods |
| 7 | Search strategy (full strings) | Methods |
| 8 | Selection process | Methods |
| 9 | Data collection process | Methods |
| 10a | Data items — outcomes | Methods |
| 10b | Data items — outras variáveis | Methods |
| 11 | Risk of bias assessment | Methods |
| 12 | Effect measures | Methods |
| 13a–f | Synthesis methods | Methods |
| 14 | Reporting bias assessment | Methods |
| 15 | Certainty assessment (GRADE) | Methods |
| 16 | Study selection (numbers + flow) | Results |
| 17 | Study characteristics | Results |
| 18 | Risk of bias in studies | Results |
| 19 | Results of individual studies | Results |
| 20a–d | Results of syntheses | Results |
| 21 | Reporting biases | Results |
| 22 | Certainty of evidence | Results |
| 23a–d | Discussion | Discussion |
| 24a–c | Registration & protocol | Other |
| 25 | Support (funding) | Other |
| 26 | Competing interests | Other |
| 27 | Availability of data, code, materials | Other |

Anexar o checklist preenchido como **material suplementar**.

---

## 📊 ETAPA 10 — GRADE (CERTEZA DA EVIDÊNCIA)

Para cada outcome principal, use **GRADE** (Grading of Recommendations Assessment, Development and Evaluation):

5 domínios para **rebaixar** evidência:
1. Risk of bias
2. Inconsistency (heterogeneidade não explicada)
3. Indirectness
4. Imprecision (IC largos, n pequeno)
5. Publication bias

3 domínios para **subir** (estudos observacionais):
1. Effect size grande
2. Dose-response
3. Confounding plausível operando contra o efeito

Saída: **Summary of Findings table** (SoF) — gerada via **GRADEpro GDT** ou **R `metafor`**.

---

## 🔁 FLUXO DE TRABALHO

1. Validar pré-requisitos (título, abstract, pasta PDFs)
2. Definir pergunta + framework (PICO/PCC/etc.)
3. Redigir protocolo + pré-registrar (PROSPERO/OSF)
4. Construir e adaptar strings por base
5. Executar buscas + remover duplicatas
6. Triagem em 2 fases (title/abstract → full-text), 2 revisores
7. Extração de dados (formulário piloto)
8. Avaliação de risco de viés (ferramenta apropriada)
9. Síntese (narrativa ± meta-análise)
10. GRADE (certeza da evidência)
11. Checklist PRISMA 2020 + fluxograma
12. Redigir manuscrito seguindo PRISMA 2020 item-a-item

---

## ⚠️ ARMADILHAS COMUNS

- **Buscar só Google Scholar** — viés de cobertura, não-replicável
- **Não documentar a string** — não-replicável, reviewer rejeita
- **1 revisor único** na triagem — viés sistemático
- **Não pré-registrar** — credibilidade questionada
- **Confundir SLR com narrative review** — SLR exige todos os itens PRISMA
- **Meta-análise inadequada** — agrupar estudos incomparáveis (heterogeneidade clínica alta)
- **Ignorar grey literature** — viés de publicação

---

## 🔗 SKILLS RELACIONADOS

- `cientista` — persona tripla (rigor científico geral)
- `escritor-cientifico` — redação das seções da SLR
- `revisor-critico` — auditoria do produto final
- `reporting-guidelines` — checagem de conformidade com PRISMA e outros
- `estatistica-reporting` — meta-análise e effect sizes
- `figuras-tabelas` — fluxograma PRISMA, forest plot, traffic-light plot
