---
name: reporting-guidelines
description: Identifica e aplica reporting guidelines da rede EQUATOR conforme tipo de estudo — CONSORT (RCT), STROBE (observacional), PRISMA (revisão sistemática), TRIPOD (modelos de predição), ARRIVE (animal), CARE (caso clínico), SPIRIT (protocolo), MDAR (life sciences), STARD (diagnóstico), AGREE (guidelines), SQUIRE (melhoria de qualidade). Use no início do projeto (planejamento) e antes da submissão (auditoria de conformidade). Antes de iniciar, exige obrigatoriamente título, abstract e pasta de PDFs de referência.
---

# Reporting Guidelines — Conformidade EQUATOR

Skill para identificar a guideline de reporting apropriada ao tipo de estudo e auditar conformidade. Q1 journals frequentemente exigem o checklist preenchido como suplementar — não enviar = desk-reject.

---

## ⛔ PRÉ-REQUISITOS OBRIGATÓRIOS — NÃO COMECE SEM ELES

Antes de aplicar reporting guidelines, você DEVE ter:

### 1. TÍTULO DO ARTIGO
- Título completo, idioma

### 2. ABSTRACT DO ARTIGO
- Texto integral + palavras-chave
- Necessário para inferir tipo de estudo se ainda não for explícito

### 3. PASTA DE PDFs DE REFERÊNCIA
- Caminho absoluto da pasta

### Mensagem-padrão quando faltar algo

> Para aplicar reporting guidelines preciso obrigatoriamente de:
> 1. **Título** do artigo: [pendente / fornecido]
> 2. **Abstract** + palavras-chave: [pendente / fornecido]
> 3. **Pasta de PDFs** de referência (caminho absoluto): [pendente / fornecido]
>
> Sem esses três itens não inicio. Por favor envie o que está faltando.

Adicional necessário (perguntar): **tipo de estudo** (RCT, observacional, SLR, modelo preditivo, etc.) e **journal-alvo** (alguns exigem guidelines específicas).

---

## 🚫 NUNCA REVELAR USO DE IA

**Regra inviolável:** o checklist preenchido, materiais suplementares e qualquer arquivo da submissão **JAMAIS** mencionam que foram preenchidos/auditados por IA, LLM, GPT, Claude, ChatGPT ou modelo de linguagem. Sem disclosures, sem agradecimentos a ferramentas de IA.

---

## 🌐 EQUATOR NETWORK

A rede **EQUATOR** (Enhancing the QUAlity and Transparency Of health Research) — `equator-network.org` — mantém a coleção autoritativa de reporting guidelines. Há mais de 500 catalogadas. Para tipos de estudo fora da saúde (engenharia, ciências sociais), também há equivalentes — abaixo as principais.

---

## 🗺️ MAPA RÁPIDO — ESCOLHA DA GUIDELINE

| Tipo de estudo | Guideline | Versão atual |
|----------------|-----------|--------------|
| **Ensaio clínico randomizado** | CONSORT 2010 + extensions | CONSORT 2010 |
| **Estudo observacional** (cohort, case-control, cross-sectional) | STROBE | STROBE 2007 (atualização em curso) |
| **Revisão sistemática / meta-análise** | PRISMA | PRISMA 2020 |
| **Scoping review** | PRISMA-ScR | 2018 |
| **Modelo de predição (diagnóstico/prognóstico)** | TRIPOD / TRIPOD+AI | TRIPOD+AI 2024 |
| **Estudo diagnóstico (acurácia)** | STARD | STARD 2015 |
| **Pesquisa qualitativa** | SRQR ou COREQ | — |
| **Caso clínico / série** | CARE | CARE 2013 |
| **Protocolo de RCT** | SPIRIT | SPIRIT 2013 (extensions) |
| **Protocolo de SLR** | PRISMA-P | PRISMA-P 2015 |
| **Melhoria de qualidade** | SQUIRE 2.0 | 2015 |
| **Pesquisa animal pré-clínica** | ARRIVE 2.0 | 2020 |
| **Life sciences (manuscript-level)** | MDAR | MDAR Framework |
| **Guidelines clínicas** | AGREE II / AGREE-REX | — |
| **Estudos econômicos em saúde** | CHEERS | CHEERS 2022 |
| **Big data / EHR studies** | RECORD | RECORD 2015 |
| **AI/ML em saúde — estudos de intervenção** | CONSORT-AI / SPIRIT-AI | 2020 |
| **AI/ML em saúde — predição** | TRIPOD+AI | 2024 |
| **AI/ML em saúde — protocolos diagnósticos** | STARD-AI / DECIDE-AI | em desenvolvimento |
| **Estudos de coorte com EHR** | RECORD | 2015 |

Para áreas fora da saúde (engenharia, computação, ciências sociais): pode não haver guideline EQUATOR formal — neste caso, seguir conventions do journal-alvo + adaptação dos princípios STROBE/PRISMA.

---

## 📐 CONSORT 2010 — RCTs

### Estrutura (25 itens em 6 seções)
1. **Title and abstract** (1a–1b): identificar como RCT no título; abstract estruturado
2. **Introduction** (2a–2b): contexto + objetivos/hipóteses
3. **Methods** (3–12): trial design, participants, interventions, outcomes, sample size, randomization, blinding, statistical methods
4. **Results** (13–19): participant flow (CONSORT diagram), recruitment, baseline data, numbers analyzed, outcomes/estimation, ancillary analyses, harms
5. **Discussion** (20–22): limitations, generalisability, interpretation
6. **Other** (23–25): registration, protocol, funding

### Anexar
- **CONSORT diagram** (4-block flowchart)
- **CONSORT checklist** (`consort-statement.org`) preenchido
- **Trial registration ID** (ClinicalTrials.gov, ISRCTN, etc.) — pré-registrado **antes** do enrollment do 1º paciente

### Extensões importantes
- **CONSORT-AI** (2020) para RCTs com AI
- **CONSORT cluster** (2012) para cluster trials
- **CONSORT pragmatic** (2008)
- **CONSORT non-inferiority** (2012)

---

## 📐 STROBE — OBSERVACIONAIS

### Estrutura (22 itens)
- Title and abstract (1)
- Introduction (2–3): background, objectives
- Methods (4–12): study design, setting, participants, variables, data sources, bias, study size, quantitative variables, statistical methods
- Results (13–17): participants, descriptive data, outcome data, main results, other analyses
- Discussion (18–21): key results, limitations, interpretation, generalisability
- Other (22): funding

### Variantes
- **STROBE-cohort, STROBE-case-control, STROBE-cross-sectional** — colunas separadas no checklist para diferenças
- **STROBE-MR** (Mendelian randomization)
- **STROBE-AMS** (antimicrobial stewardship)
- **STROBE-Vet**

### Anexar
- Checklist STROBE preenchido (`strobe-statement.org`)
- Flow diagram de participantes (recomendado, não obrigatório)

---

## 📐 PRISMA 2020 — REVISÕES SISTEMÁTICAS

Detalhado no skill `revisao-sistematica-prisma`. 27 itens + flow diagram. Anexar:
- PRISMA 2020 checklist preenchido
- PRISMA flow diagram
- Search strategy completa (PRISMA-S) — todas as bases, datas, hits

---

## 📐 TRIPOD+AI — MODELOS DE PREDIÇÃO

TRIPOD+AI (2024) é a atualização de TRIPOD para modelos de IA/ML. **Críticos:**
- Reportar dataset (origem, splits, preprocessamento)
- Hiperparâmetros e processo de seleção
- Métricas (calibração + discriminação): AUC, Brier score, ECE, calibration plot
- Validação interna (cross-validation, bootstrap) **e** externa
- Análise de fairness (subgrupos)
- Interpretabilidade (SHAP, LIME, etc.)
- Disponibilidade de código + modelo

---

## 📐 STARD 2015 — ESTUDOS DIAGNÓSTICOS

30 itens. Foco em:
- Index test e reference standard claramente definidos
- Flow diagram (recrutamento, exclusões)
- 2x2 table (TP, FP, TN, FN)
- Sensibilidade, especificidade, PPV, NPV com IC 95%
- Curva ROC + AUC

---

## 📐 ARRIVE 2.0 — PESQUISA ANIMAL

Essential 10 + Recommended Set:
- Espécie, cepa, sexo, idade
- Sample size justification
- Randomização e blinding
- Critérios de inclusão/exclusão e atrito
- Cuidados éticos (3Rs, comitê)
- Conditions de housing

Sem ARRIVE preenchido, journals como *PLOS ONE*, *Nature*, *eLife* desk-rejeitam.

---

## 📐 CARE 2013 — RELATOS DE CASO

13 itens. Estrutura: timeline visual obrigatório, anonimização, perspectiva do paciente (quando possível).

---

## 📐 SPIRIT 2013 — PROTOCOLOS DE RCT

33 itens. Antes de começar o trial — registrar o protocolo. Crítico:
- PICO bem definido **a priori**
- Sample size com poder estatístico
- Análise estatística pré-especificada
- Plano de monitoramento de segurança

Para outras áreas (não-saúde): adaptar princípios.

---

## 📐 MDAR — LIFE SCIENCES MANUSCRIPT FRAMEWORK

MDAR (Materials Design Analysis Reporting) — adotado por *Nature*, *Cell*, *Science*, *PLOS*. Requer reporte de:
- Reagent identification (RRIDs)
- Experimental design
- Statistical analysis
- Data and code availability
- Ethics (human, animal, environmental)

Submetido como **MDAR Reporting Summary** (PDF padronizado).

---

## 🔁 FLUXO DE TRABALHO

### Modo planejamento (antes do estudo)
1. Validar pré-requisitos (título, abstract, pasta PDFs)
2. Confirmar **tipo de estudo** com o usuário
3. Identificar guideline aplicável (mapa acima)
4. Baixar checklist atualizado (sempre da fonte oficial: equator-network.org)
5. Listar itens **obrigatórios pré-coleta** (sample size, registration, ethics, randomização)
6. Construir o protocolo seguindo a guideline (e pré-registrar quando aplicável)

### Modo auditoria (antes da submissão)
1. Validar pré-requisitos
2. Confirmar tipo de estudo + guideline aplicada
3. Para cada item da guideline: marcar **OK / Parcial / Faltando**, com localização (Seção X.Y) ou indicação clara de ausência
4. Apontar **Faltando** ao usuário, com sugestão de onde inserir
5. Apontar **Parcial** com sugestão de melhoria
6. Verificar conformidade com requisitos do **journal-alvo** (algumas exigem extensions específicas)
7. Preencher checklist oficial em formato exigido pelo journal
8. Anexar como **suplementar**

---

## 📋 CHECKLIST DE CONFORMIDADE (META)

Antes de submeter:
- [ ] Tipo de estudo identificado e guideline correta selecionada
- [ ] Versão atual da guideline confirmada (não usar versão obsoleta)
- [ ] Checklist baixado da fonte oficial (equator-network.org ou domínio do consórcio)
- [ ] Cada item endereçado no manuscrito ou justificado se omitido
- [ ] Flow diagram criado quando aplicável (CONSORT, PRISMA, STARD)
- [ ] Pré-registro citado quando aplicável (ClinicalTrials.gov, OSF, PROSPERO)
- [ ] Extensions aplicáveis identificadas (e.g., CONSORT-AI, STROBE-MR)
- [ ] Disponibilidade de dados/código declarada (item comum em todas)
- [ ] Conflitos de interesse, funding, contribuições — declarados (item comum)
- [ ] Ethics statement (IRB/CEP) presente quando humanos/animais

---

## ⚠️ ARMADILHAS COMUNS

- **Aplicar guideline errada** (ex.: CONSORT em estudo observacional) — desk-reject
- **Versão desatualizada** (ex.: CONSORT 2001 quando 2010 é o atual)
- **Checklist apenas marcado, sem mostrar onde no texto** — reviewer não consegue verificar
- **Esquecer extension** quando o estudo é cluster RCT, AI-RCT, etc.
- **Ignorar exigência específica do journal** que vai além da guideline
- **Pré-registro pós-fato** (registrar depois de coletar dados é contraproducente — sinal de p-hacking para reviewers atentos)
- **Ethics statement vago** ("Approved by local committee" sem ID nem instituição) — pedido de revisão certo

---

## 🔗 SKILLS RELACIONADOS

- `revisao-sistematica-prisma` — PRISMA 2020 detalhado
- `estatistica-reporting` — itens estatísticos das guidelines (effect sizes, IC, poder)
- `editor-cientifico` — empacotamento de checklists como suplementar
- `revisor-critico` — auditoria geral
- `cientista` — persona tripla (rigor geral)
