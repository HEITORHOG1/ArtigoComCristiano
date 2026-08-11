---
name: estatistica-reporting
description: Audita e orienta o reporting estatístico do artigo — escolha do teste, premissas (normalidade, homocedasticidade, independência), tamanho de efeito (Cohen's d, Hedges' g, η², r, OR, RR), intervalos de confiança, correção para múltiplas comparações (Bonferroni, BH/FDR), análise de poder, regressão (assumptions checking), reporte de software, interpretação além do p-valor. Use quando o artigo tem análise quantitativa empírica. Antes de iniciar, exige obrigatoriamente título, abstract e pasta de PDFs de referência.
---

# Estatística e Reporting Estatístico

Skill para garantir rigor estatístico publicável em Q1. Reviewers estatísticos matam papers em: ausência de effect size, p-hacking suspeito, premissas não checadas, correção ausente para múltiplas comparações, interpretação errada de p > 0.05.

---

## ⛔ PRÉ-REQUISITOS OBRIGATÓRIOS — NÃO COMECE SEM ELES

Antes de auditar/orientar análise estatística, você DEVE ter:

### 1. TÍTULO DO ARTIGO
- Título completo, idioma

### 2. ABSTRACT DO ARTIGO
- Texto integral + palavras-chave

### 3. PASTA DE PDFs DE REFERÊNCIA
- Caminho absoluto da pasta

### Mensagem-padrão quando faltar algo

> Para auditar/orientar análise estatística preciso obrigatoriamente de:
> 1. **Título** do artigo: [pendente / fornecido]
> 2. **Abstract** + palavras-chave: [pendente / fornecido]
> 3. **Pasta de PDFs** de referência (caminho absoluto): [pendente / fornecido]
>
> Sem esses três itens não inicio. Por favor envie o que está faltando.

Adicional necessário: **dados ou descrição do desenho** (n, variáveis, escalas), **hipóteses** (se houver), **software** usado.

---

## 🚫 NUNCA REVELAR USO DE IA

**Regra inviolável:** seção de Métodos estatísticos, código, output, tabelas e qualquer descrição **JAMAIS** mencionam que foram preparados/auditados por IA, LLM, GPT, Codex, ChatGPT ou modelo de linguagem. Sem disclosures, sem agradecimentos a ferramentas de IA. Atenção especial em **comentários de código** e **scripts compartilhados** (limpar antes de commit).

---

## 🎯 PRINCÍPIOS-CHAVE

1. **p < 0.05 não é descoberta** — é uma **decisão**. Reportar effect size + IC sempre.
2. **"Significativo" é palavra perigosa** — diga "estatisticamente significativo" sempre, e considere se a magnitude é praticamente relevante.
3. **Premissas precedem testes** — testar antes de aplicar.
4. **Múltiplas comparações exigem correção** — Bonferroni, Holm, FDR/BH.
5. **Pré-especificar análises primárias** — análises post hoc são exploratórias, marcar como tal.
6. **n pequeno ≠ p alto** — pode haver efeito real subdetectado. Reporte poder.
7. **Distribuição de p valores em múltiplos testes deve ser checada** — se todos p ≈ 0.04, suspeitar p-hacking.

---

## 📊 ESCOLHA DO TESTE — ÁRVORE DE DECISÃO

### Comparação de 2 grupos
| Cenário | Teste paramétrico | Teste não-paramétrico |
|---------|-------------------|------------------------|
| 2 grupos independentes | t de Student (independente) | Mann-Whitney U |
| 2 grupos pareados | t pareado | Wilcoxon signed-rank |
| Variâncias muito diferentes | Welch's t | Mann-Whitney U |

### Comparação de >2 grupos
| Cenário | Paramétrico | Não-paramétrico |
|---------|-------------|------------------|
| Independentes | ANOVA one-way | Kruskal-Wallis |
| Pareados / repetidas | ANOVA repeated-measures | Friedman |
| Múltiplos fatores | ANOVA factorial | ART (Aligned Rank Transform) |

### Pós-hoc (após ANOVA significativa)
- **Tukey HSD** (todos vs todos)
- **Dunnett** (todos vs controle)
- **Bonferroni** (poucas comparações pré-especificadas)
- **Games-Howell** (variâncias desiguais)
- **Dunn** (após Kruskal-Wallis)

### Associação entre variáveis
| Tipo | Teste |
|------|-------|
| Contínua × contínua, linear | Correlação de Pearson |
| Contínua × contínua, monotônica | Spearman / Kendall tau |
| Categórica × categórica | Chi-quadrado, Fisher exact (n pequeno) |
| Contínua × categórica binária | Point-biserial / t test |
| Concordância entre avaliadores | Cohen's kappa, Krippendorff's alpha, ICC |

### Modelagem
| Outcome | Modelo |
|---------|--------|
| Contínuo | Regressão linear (OLS); GLS se heterocedástico |
| Binário | Regressão logística |
| Contagem | Poisson; binomial negativa se overdispersion |
| Tempo até evento | Cox proportional hazards; Kaplan-Meier descritivo |
| Hierárquico/clustered | Linear mixed models, GEE |
| Não-linear | GAM, regressão polinomial |

---

## 🧪 PREMISSAS — CHECAR ANTES DE INTERPRETAR

### Normalidade
- **Shapiro-Wilk** (n ≤ 50, mais sensível)
- **Kolmogorov-Smirnov** (n maior; menos potente)
- **Anderson-Darling**
- **Visual:** Q-Q plot + histograma — frequentemente mais útil que teste formal
- ⚠️ Com n grande (>200), Shapiro detecta desvios irrelevantes

### Homocedasticidade (igualdade de variâncias)
- **Levene's test** (robusto a não-normalidade)
- **Bartlett** (assume normalidade)
- **Brown-Forsythe** (Levene com mediana)

### Independência dos resíduos
- **Durbin-Watson** (autocorrelação em séries temporais / regressão)
- Inspeção de resíduos × ordem de coleta

### Linearidade (regressão)
- Resíduos × fitted plot (sem padrão)
- Component+Residual plots

### Multicolinearidade (regressão múltipla)
- **VIF** (Variance Inflation Factor) — alarme em VIF > 5; crítico em VIF > 10
- Tolerância = 1/VIF

### Outliers e pontos influentes (regressão)
- **Cook's distance** > 1 (alarme); > 4/n (atenção)
- **Leverage** (valores > 2k/n com k = preditores)
- **Studentized residuals** > |3|

---

## 📏 EFFECT SIZES — REPORTAR SEMPRE

p-valor sozinho **não é suficiente**. Effect size diz **quanto**.

### Diferenças de média
| Nome | Quando | Interpretação |
|------|--------|---------------|
| **Cohen's d** | 2 grupos independentes | 0.2 small, 0.5 medium, 0.8 large |
| **Hedges' g** | Cohen's d com correção para n pequeno | mesma escala que d |
| **Glass's Δ** | Quando se quer usar SD do controle apenas | mesma escala |
| **Cliff's delta** | Não-paramétrico | -1 a +1; \|0.147\| small, \|0.33\| medium, \|0.474\| large |

### ANOVA
| Nome | Interpretação |
|------|---------------|
| **η² (eta-squared)** | 0.01 small, 0.06 medium, 0.14 large |
| **η²_p (partial eta-squared)** | mesma referência |
| **ω² (omega-squared)** | menos enviesado que η² em n pequeno |

### Correlação
| Nome | Interpretação (Cohen) |
|------|------------------------|
| **r de Pearson** | 0.10 small, 0.30 medium, 0.50 large |
| **ρ de Spearman** | mesma referência aproximada |
| **r²** | proporção de variância explicada |

### Categóricas / Logística
| Nome | Interpretação |
|------|---------------|
| **OR (Odds Ratio)** | reportar com IC 95% |
| **RR (Risk Ratio / Relative Risk)** | preferível a OR para outcomes comuns |
| **HR (Hazard Ratio)** | sobrevida |
| **NNT (Number Needed to Treat)** | clínica |
| **Cramer's V** | Chi-quadrado em tabelas r×c |
| **Phi (φ)** | Chi-quadrado em 2x2 |

### Sempre acompanhar effect size de **IC 95%**.

---

## 🎚️ CORREÇÃO PARA MÚLTIPLAS COMPARAÇÕES

Sem correção, fazer 20 testes a α=0.05 → ~64% de chance de pelo menos um falso positivo.

| Método | Controla | Quando usar |
|--------|----------|-------------|
| **Bonferroni** | FWER (Family-Wise Error Rate) | Poucas comparações (≤10), pré-especificadas |
| **Holm-Bonferroni** | FWER | Sequential, mais potente que Bonferroni |
| **Hochberg** | FWER | Step-up, se testes independentes |
| **BH / FDR (Benjamini-Hochberg)** | FDR (False Discovery Rate) | Muitas comparações (genômica, neuroimaging) |
| **Tukey HSD** | FWER | Pós-hoc ANOVA, todos pares |
| **Dunnett** | FWER | Pós-hoc ANOVA, vs controle |

Reportar: **número total de testes**, método de correção, **p ajustado** (q-valor para FDR).

---

## 🔌 PODER ESTATÍSTICO E TAMANHO DE AMOSTRA

Antes da coleta — calcular **n necessário** para detectar effect size esperado com poder 80% (convencional) e α 5%:

- **G*Power** (gratuito) — desktop, todos os testes principais
- **R: `pwr` package** — `pwr.t.test()`, `pwr.anova.test()`, `pwr.r.test()`, etc.
- **Stata `power`** suite

Reportar:
- Effect size esperado (de literatura ou piloto)
- α e poder usados
- n calculado
- Justificativa para qualquer desvio

Para estudo já feito com p > 0.05 — reportar **post-hoc power** é controverso (muitos estatísticos desaconselham); preferir **IC 95%** do effect size para mostrar "ausência de efeito" vs "evidência inconclusiva".

---

## 🚩 INTERPRETAÇÃO — ARMADILHAS COMUNS

### "p > 0.05 significa que não há efeito" — **ERRADO**
- Pode haver efeito real, com poder insuficiente
- Reportar IC 95%: se inclui valores praticamente relevantes, é **inconclusivo**, não "ausente"

### "p < 0.05 significa efeito grande" — **ERRADO**
- p mede evidência **contra H0**, não magnitude
- Com n grande, qualquer diferença trivial dá p < 0.001

### Comparar p-valores — **ERRADO**
- "p = 0.04 em A e p = 0.06 em B → A tem efeito, B não" — comparação inválida
- Só comparar effect sizes com IC

### "Resultados marginalmente significativos" (p ≈ 0.06) — **ANTIPADRÃO**
- Pré-especificou α = 0.05 → mantenha. Resultado é não-significativo. Discuta poder.

### Reportar só p-valor exato sem teste — **INSUFICIENTE**
- Reportar: estatística do teste (t, F, χ², U, etc.), df, n, p, effect size, IC

---

## 📝 PADRÃO DE REPORTE — APA/Q1

### Teste t
> *t*(48) = 2.43, *p* = 0.019, *d* = 0.70, 95% CI [0.12, 1.27]

### ANOVA
> *F*(2, 87) = 6.84, *p* = 0.002, η²_p = 0.14

### Regressão linear
> Para cada unidade adicional de X, Y aumentou em β = 0.42 unidades (95% CI [0.21, 0.63], *p* < 0.001), com R² = 0.36 (R²_adj = 0.34) explicando 36% da variância.

### Regressão logística
> OR = 2.15 (95% CI [1.34, 3.45], *p* = 0.001)

### Correlação
> *r*(98) = 0.42, *p* < 0.001, 95% CI [0.24, 0.57]

### Chi-quadrado
> χ²(2, *N* = 200) = 11.6, *p* = 0.003, Cramer's *V* = 0.24

### Sobrevida
> HR = 0.65 (95% CI [0.48, 0.89], *p* = 0.007)

---

## 🛠️ SOFTWARE — REPORTAR VERSÃO

Sempre reportar software, versão e pacotes-chave:

> Statistical analyses were performed in R v4.3.2 (R Core Team, 2023) using packages `lme4` v1.1-35 and `emmeans` v1.10.

Para reprodutibilidade total: **`sessionInfo()`** ou **`session_info()`** (renv) anexar como suplementar.

### Recomendados
| Software | Notas |
|----------|-------|
| **R** | Padrão acadêmico; reprodutibilidade via `renv`/Docker |
| **Python** | `scipy`, `statsmodels`, `pingouin`, `scikit-learn` |
| **Stata** | Padrão em economia/saúde |
| **JASP / jamovi** | Alternativas point-and-click open-source |
| **SPSS** | Comum em saúde/social, menos transparente |
| **GraphPad Prism** | Bom para gráficos, limitado para análise complexa |

### Disclosure
- Código deve estar disponível (GitHub, OSF, Zenodo) para reprodutibilidade
- Sementes (`set.seed()`) reportadas

---

## 📋 CHECKLIST DE AUDITORIA ESTATÍSTICA

Antes de submeter:

### Planejamento
- [ ] Análises primárias **pré-especificadas** (idealmente registradas)
- [ ] Cálculo de tamanho de amostra documentado e justificado
- [ ] Hipóteses a priori distinguidas de análises exploratórias

### Premissas
- [ ] Normalidade testada (Shapiro-Wilk + Q-Q plot) **ou** justificado uso de não-paramétrico/robusto
- [ ] Homocedasticidade testada (Levene)
- [ ] Independência verificada (DW para regressão)
- [ ] Linearidade (regressão)
- [ ] Multicolinearidade (VIF para regressão múltipla)
- [ ] Outliers/influentes identificados e tratados (com justificativa)

### Análise principal
- [ ] Teste apropriado ao desenho e variáveis
- [ ] Effect size reportado **sempre** (não apenas p-valor)
- [ ] IC 95% reportado **sempre**
- [ ] Estatística do teste, df, n reportados
- [ ] p-valor exato (não "p < 0.05") salvo p < 0.001

### Múltiplas comparações
- [ ] Total de testes contado
- [ ] Método de correção declarado e aplicado
- [ ] p ajustado (q-valor para FDR) reportado

### Interpretação
- [ ] p > 0.05 não interpretado como "ausência de efeito" sem qualificação
- [ ] Magnitude prática avaliada (não só estatística)
- [ ] Resultados negativos não escondidos

### Reprodutibilidade
- [ ] Software + versão + pacotes reportados
- [ ] Sementes (seeds) reportadas
- [ ] Código disponível em repositório
- [ ] Dados disponíveis (ou justificada restrição)

### Visualização
- [ ] Gráficos com IC ou erro padrão visível
- [ ] Não usar barras quando dotplot/boxplot é mais informativo
- [ ] Cor acessível (daltonismo)

---

## ⚠️ ARMADILHAS / SINAIS DE p-HACKING

Reviewers atentos suspeitam quando:

- Vários testes com p entre 0.04 e 0.05
- Outcomes "secundários" virando primários sem justificativa
- Subgrupos analisados ad hoc sem correção
- Outliers removidos sem critério a priori
- Trocas de teste estatístico após resultado inicial não-significativo
- Diferentes "doses" de cutoff até dar significância

→ Pré-registro + análises pré-especificadas + reporte transparente das decisões matam isso.

---

## 🔁 FLUXO DE TRABALHO

1. Validar pré-requisitos (3 + tipo de dado + software)
2. Mapear tipo de variáveis e desenho
3. Recomendar testes apropriados (árvore de decisão)
4. Verificar premissas
5. Executar testes + effect sizes + IC + correção para múltiplas
6. Auditar interpretação no rascunho
7. Verificar conformidade com guideline aplicável (CONSORT/STROBE/etc.)
8. Recomendar visualização adequada (cair no skill `figuras-tabelas` ou `discussao-limitacoes` para limitações estatísticas)

---

## 🔗 SKILLS RELACIONADOS

- `reporting-guidelines` — itens estatísticos das guidelines (CONSORT, STROBE, TRIPOD)
- `revisao-sistematica-prisma` — meta-análise e effect sizes em SLR
- `figuras-tabelas` — visualização estatística (forest plot, ROC, Bland-Altman)
- `discussao-limitacoes` — limitações estatísticas (poder, generalização)
- `revisor-critico` — auditoria geral
- `cientista` — persona tripla (rigor geral)
