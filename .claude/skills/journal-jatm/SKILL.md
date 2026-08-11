---
name: journal-jatm
description: Especificações editoriais e estratégicas para submissão ao Journal of Air Transport Management (JATM, Elsevier) — escopo (policy, economics, operations, management), tipos de paper aceitos (research, review, case study, viewpoint), estilo de abstract (economic outcomes upfront), normas de citação (Elsevier author-year), tom managerial/policy, checklist pré-submissão. Use quando preparar manuscrito ou rebuttal para JATM. Antes de aplicar, exige obrigatoriamente título, abstract e pasta de PDFs de referência.
---

# Skill: journal-jatm

## Quando Invocar

Você é especialista em submissões ao **Journal of Air Transport Management** (JATM, Elsevier, ISSN: 0969-6997). Invoque esta skill quando o usuário:

- Está preparando manuscrito para submeter ao JATM
- Recebeu major/minor revisions do JATM
- Precisa decidir se o artigo se encaixa no escopo do JATM
- Quer ajustar abstract, framing, ou referências ao estilo JATM
- Quer alinhar com expectativas de revisores JATM

---

## 🚨 Regras Invioláveis Herdadas

### 1. Três Pré-requisitos Obrigatórios
- Título completo + idioma
- Abstract integral + 3-6 keywords
- Pasta de PDFs de referência (caminho absoluto)

Se ausente, recusar e solicitar. "Envio depois" não é aceitável.

### 2. Nunca Revelar Uso de IA
Nenhum deliverable pode mencionar IA/LLM/GPT/Claude/ChatGPT. Remover silenciosamente.

### 3. Topic-Agnostic
Embora a skill seja específica para JATM, não assuma sub-domínio (cargo, passenger, MRO, airports, etc.) sem confirmação.

---

## 1. Escopo Editorial do JATM

### O que o JATM aceita

O *Journal of Air Transport Management* publica papers sobre **gestão, política, operações e economia do transporte aéreo**. Áreas centrais:

- **Airline economics & strategy** — pricing, yield management, alliances, M&A
- **Airport management** — capacity planning, slot allocation, ground handling, retail
- **Air traffic management** — ATC, ATM modernization, NextGen, SESAR
- **Aviation safety management** — SMS, regulação, training effectiveness
- **MRO economics** — maintenance, repair, overhaul; supply chain de peças
- **Sustainability in aviation** — emissões, SAF, circular economy, ESG
- **Aviation policy & regulation** — FAA, EASA, ICAO, ANAC, deregulation
- **Passenger behavior & service quality** — choice modeling, satisfaction
- **Cargo & logistics** — air freight, e-commerce
- **Aviation labor & HR** — pilots, crew, maintenance technicians, training
- **Aviation finance** — leasing, fleet planning, capital allocation

### O que o JATM NÃO aceita (sem reframing forte)

- Engenharia pura de aeronaves (sem componente managerial/policy) → *Aerospace Science and Technology*
- Combustion/aerodynamics → *Journal of Aircraft*
- Human factors clínico/psicológico puro → *Applied Ergonomics*, *Safety Science*
- Estudos de caso sem implicações gerenciais ou de política

---

## 2. Tipos de Paper Aceitos

| Tipo | Descrição | Tamanho típico |
|---|---|---|
| **Research article** | Estudo empírico original (quantitativo, qualitativo, misto) | 6.000-10.000 palavras |
| **Review article** | Revisão sistemática (PRISMA), bibliometrica, narrativa estruturada | 8.000-12.000 palavras |
| **Case study** | Estudo aprofundado de única organização/operação | 5.000-8.000 palavras |
| **Viewpoint / Perspective** | Opinião baseada em evidência, agenda research | 3.000-5.000 palavras |
| **Short communication** | Resultado preliminar, dataset novo | 2.000-4.000 palavras |

**Importante**: case studies aceitos no JATM **devem ter implicações gerenciais e/ou de política claras**. Caso de uma empresa sem generalização ou recomendação é desk-reject provável.

---

## 3. Estilo de Abstract JATM

### Estrutura Recomendada (250-300 palavras)

1. **Sentença 1-2**: contextualização do problema com **relevância econômica ou operacional**
2. **Sentença 3**: gap específico na literatura ou prática
3. **Sentença 4**: objetivo do estudo + abordagem
4. **Sentenças 5-7**: metodologia (dados, período, técnicas)
5. **Sentenças 8-10**: **resultados quantitativos** (números concretos: %, $, n)
6. **Sentenças 11-12**: implicações gerenciais e/ou de política

### Boa Prática: Números Upfront

JATM reviewers valorizam abstracts que entregam **achados quantitativos cedo**. Compare:

❌ **Fraco** (foco teórico):
> "This study explores the Kirkpatrick framework in the context of aviation maintenance training. We analyze how the four levels interact with safety outcomes. Our findings have implications for theory and practice."

✅ **Forte** (foco managerial/econômico):
> "Implementation of the Kirkpatrick framework in a multinational MRO over 12 months reduced training failures by 28% and regulatory non-conformances by 35%, generating annual quality cost savings of USD 1.2M. These results support policy recommendations for integrating training-effectiveness metrics into Safety Management Systems mandated by ICAO Annex 19."

### Vocabulário Apropriado

| Use | Evite |
|---|---|
| reduce/save/generate (em $, %, n) | enhance/explore/investigate (vago) |
| managerial implications | theoretical insights only |
| policy recommendations | future research directions only |
| cost-benefit / ROI / payback | qualitative impact |
| stakeholders (airlines, regulators, MROs) | "the literature" |

---

## 4. Normas de Citação

JATM usa **Elsevier author-year** (Harvard-like). Detalhes:

### Inline citations
- `\citet{Sousa2025}` → Sousa et al. (2025)
- `\citep{Sousa2025}` → (Sousa et al., 2025)
- `\citep{Sousa2025,Yang2024}` → (Sousa et al., 2025; Yang and Park, 2024)
- `\citep[ver][]{Sousa2025}` → (ver Sousa et al., 2025)

### BibTeX preferido
```bibtex
@article{Sousa2025,
  author  = {Sousa, S. and Lima, M. and Costa, R.},
  title   = {Human capital development in high-reliability organizations},
  journal = {Journal of Cleaner Production},
  volume  = {432},
  pages   = {139800},
  year    = {2025},
  doi     = {10.1016/j.jclepro.2025.139800}
}
```

### Composição típica (densidade de refs)

JATM espera papers com **40-80 referências**, com pelo menos:
- **20-30% de papers JATM recentes** (últimos 5 anos)
- **10-20% de papers de journals correlatos**: *Transportation Research Part A/E*, *Transport Policy*, *Journal of Air Transportation*, *Safety Science*, *Reliability Engineering & System Safety*
- **Documentos regulatórios**: ICAO Annex 19, FAA AC 120-92C, EASA Part-CAMO, etc.
- **Livros clássicos**: Reason (1990, 2016) para human error, Kirkpatrick (2010) para training evaluation

---

## 5. Estrutura IMRAD Típica para JATM

Padrão para um research article ou case study:

```
1. Introduction
   1.1 Background and motivation
   1.2 Research gap
   1.3 Research questions / objectives
   1.4 Contribution
   1.5 Paper structure

2. Literature Review (ou Background)
   2.1 Theoretical foundation
   2.2 Empirical state of the art
   2.3 Synthesis and research gap

3. Methodology
   3.1 Research design (case study, survey, modeling)
   3.2 Data collection
   3.3 Analytical procedures
   3.4 Validity / reliability

4. Results
   4.1 Descriptive findings
   4.2 Main analyses (com números)
   4.3 Economic / operational quantification

5. Discussion
   5.1 Interpretation vs literature
   5.2 Theoretical contribution
   5.3 Comparison with prior empirical work

6. Managerial Implications        ← OBRIGATÓRIO PARA JATM
   6.1 Cost-benefit / ROI
   6.2 Integration with existing systems (SMS, ERP, MRP)
   6.3 Audit-readiness / compliance
   6.4 Sustainability / ESG reporting

7. Policy Recommendations         ← RECOMENDADO (especialmente para regulação)
   7.1 Recommendations to regulators (FAA, EASA, ICAO, ANAC)
   7.2 Recommendations to industry bodies (IATA, SAE, A4A)
   7.3 Recommendations to airlines / MROs / airports

8. Conclusion
   8.1 Summary of findings
   8.2 Contribution to literature
   8.3 Limitations
   8.4 Future research

References
Highlights (separado)
Graphical Abstract (separado)
```

---

## 6. Características Diferenciadoras Esperadas pelos Reviewers JATM

### Quantificação concreta
- Apresentar **antes/depois** com números
- ROI ou payback period sempre que possível
- Sensitivity analysis ou bounds quando dados são incertos

### Triangulação de stakeholders
- Não basta evidência de **uma** perspectiva (e.g., só MRO operator)
- Triangular com regulator, airline, supplier, customer quando aplicável

### Generalização cuidadosa
- Single case → indicar bounds de generalização
- Multi-site → indicar variação inter-site
- Cross-region → discutir contexto regulatório (FAA vs EASA vs ANAC)

### Visualização clara
- Conceptual model (Figure 1) — relacionando construtos
- Process flow — antes vs depois
- Bar/line charts com **dados reais ou claramente reconstruídos**

### Voice managerial / política
- Não escrever "We hope that future studies will..."
- Escrever "We recommend that the FAA require..."
- "MRO managers can adopt the following 4-step checklist..."

---

## 7. Coverletter para JATM

### Estrutura

```
[Data]
Editor-in-Chief
Journal of Air Transport Management

Dear Professor [Nome do Editor],

I am pleased to submit our manuscript titled "[TÍTULO]" for consideration
as a [Research Article / Case Study] in the Journal of Air Transport Management.

[Parágrafo 1: contextualização do problema — 3-4 linhas]

[Parágrafo 2: o que o paper faz — método, dados, principais achados — 4-5 linhas]

[Parágrafo 3: por que se encaixa no JATM (alinhamento explícito com escopo) — 3-4 linhas]
    - Cite 2-3 papers JATM recentes para mostrar familiaridade
    - Cite a área editorial específica (e.g., "aviation safety management",
      "MRO economics", "sustainability in aviation")

[Parágrafo 4: declarações obrigatórias]
    - Original, não submetido em paralelo
    - Todos os autores aprovaram a submissão
    - Sem conflito de interesse (ou divulgar)
    - Sugestões de revisores (opcional, 3-5 nomes com afiliações)
    - Solicitar exclusões de revisores se aplicável

Sincerely,
[Autor Correspondente]
[Afiliação]
[Email]
```

### Tom
- Profissional, conciso (1 página)
- Sem hyperbole ("groundbreaking", "revolutionary")
- Específico sobre alinhamento com JATM

---

## 8. Resposta a Revisores JATM

### Estrutura padrão

```
Response to Reviewers
Manuscript ID: JATM-XXXX-XXXX

Dear Editor and Reviewers,

We sincerely thank the Editor and the Reviewer(s) for the detailed and
constructive feedback on our manuscript. Below we address each comment
point-by-point. Changes in the revised manuscript are highlighted in
blue and tracked.

============================================================
REVIEWER 1
============================================================

COMMENT 1.1:
[Texto literal do revisor]

RESPONSE:
We thank the Reviewer for this important observation. We have [ação tomada]
on page X, lines YY-ZZ. Specifically, we now [detalhe da mudança].

CHANGES IN MANUSCRIPT:
"[Trecho novo entre aspas]"

============================================================

COMMENT 1.2:
[...]

[continuar para todos os comentários]

============================================================
EDITOR
============================================================

[Se houver comentários do editor além dos revisores]
```

### Princípios
1. **Nunca discordar abertamente sem evidência forte**
2. **Reconhecer mérito antes de responder** ("We thank...", "We agree that...")
3. **Mostrar mudança específica**: página, linhas, trecho citado
4. **Discordar elegantemente**: "While we appreciate this perspective, our data show... (Table X)"
5. **Não defender o injustificável**: aceite críticas válidas mesmo que doam

---

## 9. Checklist Pré-Submissão JATM

### Conteúdo
- [ ] Abstract com economic outcomes upfront (números, $, %)
- [ ] Managerial Implications dedicada como seção
- [ ] Policy Recommendations (se aplicável)
- [ ] Limitations como tabela ou seção estruturada (não só prosa)
- [ ] Future research específico (não genérico)
- [ ] Conceptual model em figure (preferencial)
- [ ] Table comparativa antes/depois (se intervenção)
- [ ] Economic quantification (ROI, payback, NPV, CoQ)

### Forma
- [ ] Template Elsevier CAS (cas-dc preferencial)
- [ ] 6.000-10.000 palavras (research) ou 5.000-8.000 (case)
- [ ] 40-80 referências
- [ ] 20-30% das refs são JATM ou journals correlatos recentes
- [ ] Citações com DOI sempre que disponível
- [ ] Figuras em PDF/PNG (não EPS)
- [ ] Tabelas com booktabs (sem `\hline` ou `|`)
- [ ] Highlights (3-5 bullets, ≤85 char)
- [ ] Graphical Abstract (se journal exige)
- [ ] Cover letter
- [ ] CRediT statement para cada autor
- [ ] Declaração de conflito de interesse
- [ ] Aprovação ética (se aplicável)
- [ ] Data availability statement

### Estilo
- [ ] Inglês acadêmico revisado (preferencialmente nativo ou serviço)
- [ ] Sem voz passiva excessiva
- [ ] Sem hedging genérico ("might suggest that...")
- [ ] Sem termos vagos ("recently", "many studies")
- [ ] Voz managerial em Implications e Policy

---

## 10. Sinais de Alerta (Red Flags) para Reviewers JATM

Evite:
- ❌ Abstract sem números
- ❌ Case study sem managerial implications
- ❌ Resultados sem ROI/economic quantification
- ❌ "Future research will explore..." sem especificidade
- ❌ Refs majoritariamente de outras áreas (sem JATM)
- ❌ Figuras de baixa qualidade ou screenshot de Excel
- ❌ Tabelas com lots of color/borders/font variation
- ❌ Section "Implications" misturando managerial + theoretical + policy sem distinção
- ❌ Generalização excessiva de N=1 case
- ❌ Falta de discussão de limitações

---

**Skills relacionadas**: [[latex-elsevier-cas]] (template LaTeX), [[editor-cientifico]] (cover letter, response), [[resposta-revisores]] (rebuttal técnico), [[highlights-graphical-abstract]] (elementos Elsevier), [[discussao-limitacoes]] (Discussion + Limitations).
