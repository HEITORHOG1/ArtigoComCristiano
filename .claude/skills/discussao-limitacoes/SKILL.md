---
name: discussao-limitacoes
description: Estrutura e calibra a Discussão e a seção de Limitações — interpretação dos achados, triangulação real com a literatura (não só "concorda/discorda"), implicações teóricas vs práticas, limitações como evidência de honestidade intelectual (não como pedido de desculpa), trabalhos futuros específicos. Aplica o teste "So What?" e calibra hedging à força dos dados. Use ao redigir/revisar Discussão e Limitações. Antes de iniciar, exige obrigatoriamente título, abstract e pasta de PDFs de referência.
---

# Discussão e Limitações

A Discussão é a seção mais difícil do paper — onde reviewers Q1 distinguem trabalho competente de trabalho excepcional. Limitações honestas não enfraquecem; **fortalecem**.

---

## ⛔ PRÉ-REQUISITOS OBRIGATÓRIOS — NÃO COMECE SEM ELES

Antes de redigir/revisar Discussão ou Limitações, você DEVE ter:

### 1. TÍTULO DO ARTIGO
- Título completo, idioma

### 2. ABSTRACT DO ARTIGO
- Texto integral + palavras-chave
- Necessário para amarrar a Discussão à Take-Home Message

### 3. PASTA DE PDFs DE REFERÊNCIA
- Caminho absoluto da pasta
- **Crítico para Discussão** — triangulação real exige acesso aos papers comparados

### Mensagem-padrão quando faltar algo

> Para redigir/revisar Discussão e Limitações preciso obrigatoriamente de:
> 1. **Título** do artigo: [pendente / fornecido]
> 2. **Abstract** + palavras-chave: [pendente / fornecido]
> 3. **Pasta de PDFs** de referência (caminho absoluto): [pendente / fornecido]
>
> Sem esses três itens não inicio. Por favor envie o que está faltando.

Adicional necessário: **Resultados** já redigidos ou tabela-síntese dos achados, e **Introdução** (objetivos + perguntas de pesquisa).

---

## 🚫 NUNCA REVELAR USO DE IA

**Regra inviolável:** a Discussão, a seção de Limitações e qualquer texto associado **JAMAIS** mencionam que foram escritos/assistidos/revisados por IA, LLM, GPT, Claude, ChatGPT ou modelo de linguagem. Sem disclosures, sem agradecimentos a ferramentas de IA. Exceção única: IA como objeto da pesquisa.

---

## 🎯 PRINCÍPIOS DA DISCUSSÃO Q1

1. **A Discussão responde "So What?"** — para cada achado, por que importa.
2. **Triangulação real**, não citação decorativa. Diga **por que** concorda ou diverge.
3. **Implicações teóricas E práticas** — não confundir. Audiência mista.
4. **Limitações ≠ desculpa** — são parte da metodologia honesta. Sempre acompanhadas de **mitigação** ou **direção futura**.
5. **A força das afirmações deve corresponder à força dos dados** — nem timidez nem overclaim.
6. **Não introduzir resultado novo** — Discussão interpreta o que já está em Resultados.
7. **Não repetir Resultados** — não rebobinar números; usá-los como evidência da interpretação.

---

## 📐 ESTRUTURA RECOMENDADA — DISCUSSÃO

### Parágrafo 1 — Recapitulação dirigida (NÃO repetição)
- 1ª frase: **Take-Home Message** declarada
- 2–3 frases: principais achados que sustentam a TH
- **Não** repetir números do Resultados — sintetizar interpretativamente

> Exemplo: "Our findings demonstrate that integrating AHP with FMEA yields stable risk rankings under uncertainty (Kendall's W ≥ 0.85 across all sensitivity scenarios). This stability — absent in standalone FMEA — supports the central claim that hybridization addresses, rather than merely repackages, the limitations of traditional approaches."

### Parágrafo 2–N — Interpretação por achado (1 parágrafo por finding principal)
Estrutura interna de cada parágrafo:

1. **Achado** (1 frase, sem números detalhados)
2. **Interpretação** (o que significa)
3. **Triangulação com literatura** (concorda? diverge? estende?)
4. **Implicação** (1–2 frases)

> **Exemplo:**
> "The 42% reduction in expert evaluation time aligns with prior findings in operational FMEA contexts (Smith, 2021), but extends them to AI-specific failure modes for the first time. While Smith reported similar efficiency gains in mechanical systems, the present results suggest the gain is preserved when failure modes are non-physical and non-deterministic — a transfer that prior work explicitly questioned (Jones, 2023). This indicates that the AHP weighting layer abstracts cleanly from the underlying system class, with practical implications for AI risk auditing in regulated industries."

### Triangulação real — modos
| Modo | Quando | Como dizer |
|------|--------|-----------|
| **Confirmar** | Resultados convergentes | "consistent with X (Smith, 2021), our data show..." |
| **Estender** | Mesma direção, novo escopo | "extending Smith's (2021) findings to..., we observe..." |
| **Refinar** | Mesma direção, condição diferente | "while Smith (2021) reported X under condition A, the present study suggests X holds also under condition B" |
| **Divergir** | Direção oposta | "contrary to Smith (2021), we find..." — **sempre** seguido de explicação plausível para a divergência (amostra, método, contexto) |
| **Reconciliar** | Aparente contradição | "the apparent disagreement with Smith (2021) resolves when accounting for [factor]" |

⚠️ **Não dizer simplesmente "in line with Smith (2021)"** sem explicar **em que aspecto** e **por que** importa.

### Penúltimo parágrafo — Implicações
- **Implicações teóricas** — o que adiciona ao corpus do conhecimento
- **Implicações práticas** — para profissionais, política, ferramentas
- Não confundir: teóricas falam à academia; práticas falam ao mundo

### Último parágrafo da Discussão — Ponte para Limitações ou Conclusões
Transição clara, não brusca.

---

## 📐 SEÇÃO DE LIMITAÇÕES — COMO ESCREVER

### Princípio: limitações como força, não fraqueza

**Antipadrão (defensivo, fraco):**
> "Our study has several limitations. The sample size is small, the data are self-reported, and we did not measure X."

**Padrão (honesto, forte):**
> "Several boundaries shape the interpretation of these findings. The sample (n = 47) supports detection of medium-to-large effects (d ≥ 0.5) but provides limited resolution for smaller effects; future work with larger samples could test whether [secondary hypothesis]. Self-report measures, while validated for constructs A and B, may underestimate construct C; objective measures via [method] are recommended for replication. Variable X was not measured because [reason]; its inclusion in subsequent studies could test [specific question]."

### Estrutura por limitação
Cada limitação tem 3 partes:

1. **O que é a limitação** (objetivamente)
2. **Por que existe** (decisão de desenho, restrição prática, escopo)
3. **O que isso afeta + mitigação ou direção futura**

### Categorias de limitação a considerar

| Categoria | Exemplos |
|-----------|---------|
| **Amostral** | n, representatividade, atrito, viés de seleção |
| **Metodológica** | desenho, instrumentos, não-randomização, ausência de controle |
| **Mensuração** | escalas, validade, confiabilidade, self-report, single rater |
| **Análise** | premissas violadas, poder, modelos simplificadores |
| **Generalização** | contexto, cultura, período, organização-tipo |
| **Causal** | observacional vs experimental, confoundes residuais |
| **Tecnológica** | versão de software/modelo, dados de treinamento |
| **Temporal** | período de coleta, mudanças contextuais subsequentes |
| **Geográfica/cultural** | uma região, uma cultura, idioma |
| **Replicabilidade** | dados/código não disponíveis publicamente (e por quê) |

### Quantas limitações?
- **3–6** é o range típico para Q1
- Menos que 3 → revisor desconfia (ou autor não reflete, ou paper é trivial)
- Mais que 8 → paper parece falho; melhor consolidar relacionadas

### O que NÃO contar como limitação
- "Future work could explore X" sem amarrar ao estudo atual — isso é direção futura, não limitação
- "We did not solve every aspect of Y" — escopo legítimo, não limitação
- "The literature is limited" — limitação do campo, não do estudo
- "Reviewers may want more" — não é limitação

---

## 🪞 TESTE "SO WHAT?"

Aplicar a **cada parágrafo** da Discussão. Se a resposta a "E daí?" não for imediata e específica, o parágrafo precisa de revisão.

> Achado: "AHP consistency ratio remained below 0.10 across all matrices."
> So What? "→ Validates the rigor of expert elicitation in our case studies, ensuring that the priority weights are not artifacts of inconsistent judgment. This addresses a known weakness of FMEA-based risk assessment under expert disagreement."

Se So What é vago → o achado é decorativo, considerar cortar.

---

## ⚖️ HEDGING CALIBRADO — TABELA DE FORÇA

A força da afirmação deve corresponder à força dos dados:

| Força | Quando usar | Verbo (EN / PT) |
|-------|-------------|-----------------|
| **Forte** | RCT bem-poderado, replicação independente, IC estreito | demonstrate, show, confirm / **demonstram, mostram, confirmam** |
| **Moderada** | Estudo único, observacional bom, IC razoável | indicate, reveal / **indicam, revelam** |
| **Fraca** | Dados preliminares, n pequeno, IC largo | suggest, imply / **sugerem, implicam** |
| **Muito fraca** | Especulação informada | appear, may indicate / **aparentam, podem indicar** |

⚠️ **Reviewers Q1 calibram isto rigorosamente.** Forte demais → "overclaim" → pedido de moderação. Fraca demais → "self-defeating" → pedido de fortalecimento.

---

## 🔁 TRABALHOS FUTUROS — ESPECÍFICOS, NÃO GENÉRICOS

### Antipadrão
- ❌ "More research is needed."
- ❌ "Future studies should explore this further."
- ❌ "Replication in larger samples is recommended."

### Padrão
- ✅ "A pre-registered replication with n ≥ 200 would have 90% power to detect d = 0.3, addressing the present study's limited resolution for small effects."
- ✅ "Extending the framework to streaming data scenarios — where expert elicitation is impractical — would test whether automated weighting via [specific method] preserves the rank stability observed here."
- ✅ "A multi-site implementation in healthcare settings beyond imaging (e.g., NLP for clinical notes) would clarify whether the AHP layer generalizes across modalities."

Cada direção futura responde 3 perguntas: **o quê**, **com qual método/desenho**, **para responder qual pergunta**.

---

## 🚫 ANTIPADRÕES NA DISCUSSÃO

| Antipadrão | Sintoma | Correção |
|------------|---------|----------|
| **Repetição de Resultados** | Reescrever números já apresentados | Sintetizar interpretativamente, sem rebobinar |
| **Citação decorativa** | "(Smith, 2021)" sem dizer **o que** Smith disse | Triangulação real ou cortar a citação |
| **"Our findings agree with the literature"** | Genérico | Especificar quais autores, em que aspecto |
| **Overclaim** | "Demonstrates definitively" com n pequeno | Calibrar para "suggest" / "indicate" |
| **Underclaim** | "May possibly potentially suggest" para resultado robusto | Reduzir hedging |
| **Saltos lógicos** | Achado A → conclusão Z sem ponte | Inserir interpretação intermediária |
| **Confundir teórico ↔ prático** | "Implicações teóricas: profissionais devem fazer X" | Separar audiências |
| **Ignorar resultado contrário** | Discutir só o que confirma | Discutir e explicar resultados não-significativos / inesperados |
| **Limitações como confissão** | "Unfortunately we could not..." | Reformular como decisão de desenho com mitigação |
| **Encerramento clichê** | "In conclusion, this study contributes to the field." | Frase específica que ecoa Take-Home Message |

---

## ✅ CHECKLIST FINAL

### Discussão
- [ ] 1º parágrafo abre com Take-Home Message clara
- [ ] Cada achado principal tem 1 parágrafo dedicado
- [ ] Cada parágrafo passa no teste "So What?"
- [ ] Triangulação real (não citação decorativa) — explicar concordância/divergência
- [ ] Implicações teóricas e práticas separadas
- [ ] Hedging calibrado por força dos dados
- [ ] Sem repetir números do Resultados
- [ ] Sem introduzir achado novo
- [ ] Conexão visível com perguntas de pesquisa da Introdução

### Limitações
- [ ] 3–6 limitações sólidas (não 1, não 10)
- [ ] Cada uma com: o quê + por quê + impacto/mitigação
- [ ] Tom de honestidade, não desculpa
- [ ] Nada de "future research is needed" como limitação
- [ ] Não confundir limitação com escopo legítimo

### Trabalhos futuros (se separado)
- [ ] Cada direção é específica (o quê + como + para responder o quê)
- [ ] Não são repetição das limitações
- [ ] Refletem ambição mas dentro do realista

### Coerência cross-seções
- [ ] Discussão responde às perguntas/objetivos da Introdução
- [ ] Take-Home Message ecoa Título, Abstract, Highlights, Conclusão

---

## 🔁 FLUXO DE TRABALHO

1. Validar pré-requisitos (3 + Resultados + Introdução)
2. Listar achados principais (5–8) e secundários
3. Para cada achado principal: redigir parágrafo de Discussão (4 partes: achado→interpretação→triangulação→implicação)
4. Verificar triangulação contra PDFs reais — checar **o que** o autor citado realmente disse
5. Separar implicações teóricas vs práticas
6. Listar 3–6 limitações no formato (o quê + por quê + mitigação)
7. Listar 2–4 direções futuras específicas
8. Aplicar teste "So What?" parágrafo a parágrafo
9. Calibrar hedging
10. Verificar coerência da Take-Home Message com outras seções

---

## 🔗 SKILLS RELACIONADOS

- `escritor-cientifico` — redação geral IMRAD; estrutura da Discussão dentro do template
- `revisor-critico` — auditoria da Discussão pelo checklist I-R-B-MB-E
- `pesquisador-senior` — princípios HUMANIZE + força das afirmações
- `estatistica-reporting` — interpretação correta de p-valores e effect sizes na Discussão
- `cientista` — persona tripla (rigor geral)
