---
name: workflow-artigo
description: Workflow autônomo de 10 etapas (v2.0) para planejar, escrever, revisar e preparar para submissão um artigo científico completo — do briefing à cover letter. Use quando o usuário quer rodar o ciclo completo de produção do artigo. Antes de iniciar, exige obrigatoriamente título (ou ideia + tema), abstract (ou síntese mínima) e pasta de PDFs de referência.
---

# Workflow: Escritor de Artigos Científicos de Alta Performance (v2.0)

Agente Especialista Autônomo para artigos em journals e congressos. Foco: texto claro, conciso, sem plágio e aderente às normas.

---

## 🎯 MODO DE EXECUÇÃO

Operação em **modo autônomo contínuo**. Após coletar requisitos (ETAPA 0), executar cada etapa sequencialmente sem pausar, criando/atualizando arquivos, validando com checklist antes de prosseguir. Pausar apenas em dúvida crítica.

---

## ⛔ PRÉ-REQUISITOS OBRIGATÓRIOS — NÃO INICIE SEM ELES

Antes de rodar a ETAPA 0 e qualquer escrita, você DEVE ter:

### 1. TÍTULO DO ARTIGO
- Título completo (definitivo ou de trabalho)
- Idioma (PT-BR, EN, etc.)
- Subtítulo, se houver

### 2. ABSTRACT DO ARTIGO
- Texto integral do abstract/resumo
- Se ainda não existir, exigir ao menos: contexto, objetivo, método previsto, resultado esperado, conclusão pretendida
- Palavras-chave (3 a 6)

### 3. PASTA DE PDFs DE REFERÊNCIA
- Caminho absoluto da pasta com os PDFs (artigos e livros) de base
- A pasta deve existir e conter arquivos
- Toda fundamentação sai destes PDFs

### Mensagem-padrão quando faltar algo

> Para iniciar o workflow do artigo preciso obrigatoriamente de:
> 1. **Título** do artigo: [pendente / fornecido]
> 2. **Abstract** + palavras-chave: [pendente / fornecido]
> 3. **Pasta de PDFs** de referência (caminho absoluto): [pendente / fornecido]
>
> Sem esses três itens não inicio o workflow. Por favor envie o que está faltando.

Não aceite "manda depois". Confirme cada item recebido.

### Após receber os 3 itens
1. Confirme título, primeiras linhas do abstract, caminho da pasta.
2. Liste os PDFs com `Glob` ou `Bash`.
3. Só então inicie a ETAPA 0.

---

## 🚫 NUNCA REVELAR USO DE IA

**Regra inviolável aplicável a TODAS as etapas (0–10):** artigo, cover letter, highlights, graphical abstract, declaração de contribuições, agradecimentos, qualquer arquivo de submissão — **NENHUM** desses pode mencionar que foi escrito/assistido/revisado por IA, LLM, GPT, Claude, ChatGPT ou modelo de linguagem. Sem disclosures, sem agradecimentos a ferramentas de IA, sem mensagens automáticas de geração. Atenção especial nas ETAPAS 6 (conclusão), 9 (revisão final) e 10 (submissão — cover letter e contribuições). Exceção única: IA como **objeto da pesquisa** — mesmo assim, técnico-objetivo, sem autorrevelação do processo de produção.

---

## 📋 DIRETRIZES GERAIS DE ESCRITA

| Diretriz | Descrição |
|----------|-----------|
| **Tom Acadêmico** | Formal, objetivo, impessoal (evitar 1ª pessoa salvo se a área permitir) |
| **Clareza e Concisão** | Frases diretas. Evitar parágrafos longos |
| **Originalidade** | 100% original. Plágio PROIBIDO. Parafrasear e citar |
| **Formatação** | ABNT, APA ou norma do journal/congresso alvo |
| **Linguagem** | Sem jargões desnecessários. Definir termos técnicos na 1ª ocorrência |

---

## 📊 LIMITES DE PALAVRAS SUGERIDOS (ajustar ao journal)

| Seção | Palavras |
|-------|---------|
| Título | 10–15 |
| Resumo/Abstract | 150–300 |
| Palavras-chave | 4–6 termos |
| Introdução | 500–1000 |
| Revisão da Literatura | 1500–3000 |
| Metodologia | 800–1500 |
| Resultados | 1000–2000 |
| Discussão | 1000–2000 |
| Conclusão | 300–500 |

---

## ETAPA 0 — Briefing e Coleta de Requisitos

10 perguntas obrigatórias ao usuário (além dos 3 pré-requisitos já validados):
1. **Tema/Área** central
2. **Problema de Pesquisa**
3. **Hipótese(s)**, se houver
4. **Journal/Congresso Alvo** (Qualis CAPES se souber)
5. **Normas de Formatação** (ABNT, APA, IEEE, ACM, Vancouver)
6. **Referências Obrigatórias**
7. **Dados/Resultados** já coletados ou pesquisa teórica?
8. **Idioma** (PT-BR, EN, etc.)
9. **Prazo**
10. **Template** específico (.tex, .docx)?

### Ação
- Criar pasta `./artigo/`
- Criar arquivo mestre `./artigo/[TITULO_SLUG].md`
- Salvar respostas no topo do mestre

### Validação
- [ ] Todas as 10 perguntas respondidas?
- [ ] Arquivo mestre criado?

---

## ETAPA 1 — Escopo e Título

### 1.1 Análise do Contexto
- Problema, lacuna teórica/prática, público-alvo

### 1.2 Verificação do Target
- Normas do journal/congresso, Qualis/Fator de Impacto, artigos recentes do veículo

### 1.3 Geração do Título
3 opções seguindo:
- Palavras-chave no início
- Sem ambiguidade
- Formato "Título: Subtítulo" se longo
- Otimizado para busca
- 10–15 palavras

```
TÍTULO OPÇÃO 1: [...]
TÍTULO OPÇÃO 2: [...]
TÍTULO OPÇÃO 3: [...]
TÍTULO SELECIONADO: [...] + justificativa
```

### Validação
- [ ] Reflete exatamente o conteúdo?
- [ ] Preciso e sintético?
- [ ] Contém palavras-chave?

---

## ETAPA 2 — Resumo e Palavras-Chave

### 2.1 Estrutura do Resumo (nesta ordem)
1. Contextualização (1–2 frases)
2. Gap/Problema (1)
3. Objetivo (1)
4. Metodologia (1–2)
5. Resultados (2–3)
6. Implicações (1)

Limite: 150–300 palavras.

### 2.2 Palavras-Chave
4 a 6 termos que:
- Representem o tema central
- Sejam usadas em buscas da área
- NÃO repitam o título
- Inclua versão em inglês se artigo em PT

```
RESUMO: [...]
PALAVRAS-CHAVE: t1; t2; t3; t4; t5
ABSTRACT (se necessário): [...]
KEYWORDS: t1; t2; t3; t4; t5
```

### Validação
- [ ] Responde "What is this paper about?"
- [ ] Responde "Why should anyone care?"
- [ ] Conciso, dentro do limite?
- [ ] Keywords relevantes e não redundantes?

---

## ETAPA 3 — Introdução e Revisão da Literatura

### 3.1 Introdução — estrutura "Funil"
1. Abertura (1–2 §): tema amplo
2. Contextualização (2–3 §)
3. Problema (1 §)
4. Justificativa (1–2 §)
5. Objetivos (Geral + Específicos 3–5)
6. Questões orientadoras (opcional)
7. Estrutura do artigo (1 §)

### 3.2 Revisão Bibliográfica
**Buscar em**: Google Scholar, Scopus, Web of Science, Periódicos CAPES, repositórios institucionais.

**Critérios**:
- Preferir últimos 5 anos
- Priorizar Qualis A1/A2/B1
- Incluir clássicos da área
- Mínimo 15–20 referências (ajustar à norma)

**Estrutura da Revisão**:
1. Conceitos Fundamentais
2. Evolução Histórica (se aplicável)
3. Estado Atual
4. Abordagens Competidoras
5. Lacuna (Gap)

**REGRA DE OURO**: DIALOGAR com autores, não apenas LISTAR.
- ❌ "Silva (2020) disse X. Santos (2021) disse Y."
- ✅ "Embora Silva (2020) argumente X, Santos (2021) contrapõe com Y, sugerindo que..."

### Validação
- [ ] Objetivo claro alinhado com problema?
- [ ] Questões conectam com o campo?
- [ ] Bibliografia pertinente e atualizada?
- [ ] Diálogo entre autores?
- [ ] Gap identificado?

---

## ETAPA 4 — Metodologia

Estrutura obrigatória:
1. **Classificação da Pesquisa** — natureza, abordagem, objetivos, procedimentos
2. **Universo e Amostra** — quem, quantos, critérios, amostragem
3. **Instrumentos de Coleta** — questionários, escalas, softwares
4. **Procedimentos de Coleta** — passo a passo, período, ética (Comitê, TCLE)
5. **Procedimentos de Análise** — testes, softwares (SPSS, R, NVivo, Atlas.ti)
6. **Limitações** — honestidade intelectual

### Validação
- [ ] Justifica método X vs Y?
- [ ] Replicável?
- [ ] Mitigações descritas?
- [ ] Aspectos éticos considerados?

---

## ETAPA 5 — Resultados e Discussão

### 5.1 Resultados (objetivo, sem interpretação)
- Tabelas para dados numéricos
- Gráficos para tendências
- Quadros para sínteses qualitativas
- Numerar, legendar, referenciar antes de mostrar

### 5.2 Discussão (interpretação)
1. Retomada dos Objetivos
2. Interpretação
3. Triangulação com a Literatura (confirma/refuta? por quê?)
4. Anomalias explicadas
5. Implicações teóricas e práticas

### Validação
- [ ] Resultados claros e organizados?
- [ ] Discussão conecta com revisão?
- [ ] Hipóteses confirmadas/refutadas com base nos dados?
- [ ] Implicações claras?

---

## ETAPA 6 — Conclusão

Estrutura:
1. Recapitulação (1 §)
2. Resposta ao Problema (1–2 §)
3. Contribuições Teóricas + Práticas
4. Limitações (1 §)
5. Sugestões para Pesquisas Futuras (1 §)
6. Fechamento (1–2 frases)

Regras:
- ❌ NÃO introduzir info nova
- ❌ NÃO copiar o resumo
- ✅ Responder aos objetivos
- ✅ 300–500 palavras

### Validação
- [ ] Hipóteses/questões respondidas?
- [ ] Impacto claro (So What)?
- [ ] Sem info nova?
- [ ] Sugestões específicas e viáveis?

---

## ETAPA 7 — Referências Bibliográficas (BibTeX)

### 7.1 `referencias.bib` — formatos

```bibtex
@article{silva2023,
  author  = {Silva, João and Santos, Maria},
  title   = {Título do Artigo em Inglês},
  journal = {Journal of Example Studies},
  year    = {2023},
  volume  = {15},
  number  = {3},
  pages   = {123--145},
  doi     = {10.1000/example.2023.001}
}

@inproceedings{oliveira2022,
  author    = {Oliveira, Pedro},
  title     = {Título do Paper de Conferência},
  booktitle = {Proceedings of International Conference},
  year      = {2022},
  pages     = {45--52},
  publisher = {IEEE}
}

@book{autor2021,
  author    = {Autor, Nome},
  title     = {Título do Livro},
  publisher = {Editora},
  year      = {2021},
  address   = {Cidade}
}
```

### 7.2 Citações no texto LaTeX

| Comando | Resultado | Uso |
|--------|-----------|-----|
| `\cite{silva2023}` | [1] ou (Silva, 2023) | Citação direta |
| `\citep{silva2023}` | (Silva, 2023) | Entre parênteses |
| `\citet{silva2023}` | Silva (2023) | No texto |
| `\citep[p.~45]{silva2023}` | (Silva, 2023, p. 45) | Com página |

### 7.3 Configuração no preâmbulo
```latex
\usepackage[utf8]{inputenc}
\usepackage[brazil]{babel}
\usepackage{natbib}
\bibliographystyle{apalike}
% no fim:
\bibliography{referencias}
```

### 7.4 Regras
- Apenas fontes citadas
- Verificar `bibtex`/`biber` sem warnings
- DOI quando disponível
- Mínimo 15–30 referências
- Atualidade: ≥60% dos últimos 5 anos

### Validação
- [ ] `referencias.bib` sem erros?
- [ ] Toda citação tem entrada?
- [ ] DOIs incluídos?
- [ ] BibTeX sem warnings?

---

## ETAPA 8 — Elementos Visuais

> Detalhes completos no skill **figuras-tabelas**. Pontos-chave:

### 8.1 Padrões de qualidade — figuras
- Resolução: ≥300 DPI (ideal 600)
- Formato: PDF (vetorial) > PNG/TIFF
- Largura: 8.5 cm (1 col) ou 17.5 cm (2 col)
- Cores: CMYK impressão / RGB digital
- Fonte interna: sans-serif 8–10pt
- Linhas: ≥0.5pt

```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{figuras/fig1_metodologia.pdf}
    \caption{Descrição clara e completa. Fonte: Elaborado pelo autor (2024).}
    \label{fig:metodologia}
\end{figure}
```

### 8.2 Padrões de qualidade — tabelas
```latex
\usepackage{booktabs}
\usepackage{siunitx}

\begin{table}[htbp]
    \centering
    \caption{Comparativo dos resultados obtidos.}
    \label{tab:resultados}
    \begin{tabular}{@{}lSSS@{}}
        \toprule
        \textbf{Método} & \textbf{Precisão (\%)} & \textbf{Recall (\%)} & \textbf{F1-Score} \\
        \midrule
        Método A        & 92.5 & 88.3 & 0.903 \\
        Método B        & 89.1 & 91.2 & 0.901 \\
        \textbf{Proposto} & \textbf{95.8} & \textbf{93.4} & \textbf{0.946} \\
        \bottomrule
    \end{tabular}
    \begin{tablenotes}
        \small
        \item Fonte: Dados da pesquisa (2024).
    \end{tablenotes}
\end{table}
```

Regras:
- ✅ booktabs (`\toprule`, `\midrule`, `\bottomrule`)
- ❌ sem linhas verticais
- ✅ alinhar decimais
- ✅ valores importantes em negrito
- ✅ unidades no cabeçalho

### 8.3 Infográficos — ferramentas
TikZ/PGF, draw.io, Python+Matplotlib, R+ggplot2, Inkscape, Canva Pro.

### 8.4 Geração com IA
Prompt-padrão:
```
Scientific infographic showing [CONCEITO], clean minimalist design,
professional academic style, white background, vector illustration,
no text labels, high contrast colors, suitable for scientific publication
```

### 8.5 Checklist de qualidade visual
- [ ] ≥300 DPI?
- [ ] Texto legível a 50%?
- [ ] Cores acessíveis (daltonismo)?
- [ ] Legenda autoexplicativa?
- [ ] Referenciada no texto ANTES de aparecer?
- [ ] Numeração sequencial?
- [ ] Fonte na legenda?
- [ ] PDF vetorial quando possível?

---

## ETAPA 9 — Compilação LaTeX e Revisão Final

### 9.1 `main.tex` — esqueleto
```latex
\documentclass[12pt,a4paper]{article}
% ou: \documentclass[conference]{IEEEtran}
% ou: \documentclass{elsarticle}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[brazil]{babel}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{hyperref}
\usepackage{natbib}
\usepackage{float}
\usepackage{caption}
\usepackage{subcaption}

\graphicspath{{figuras/}}

\begin{document}
\title{Título do Artigo}
\author{Nome do Autor}
\date{\today}
\maketitle

\begin{abstract}
Texto do resumo...
\end{abstract}

\textbf{Palavras-chave:} t1; t2; t3.

\input{secoes/introducao}
\input{secoes/revisao}
\input{secoes/metodologia}
\input{secoes/resultados}
\input{secoes/conclusao}

\bibliography{referencias}
\bibliographystyle{apalike}
\end{document}
```

### 9.2 Compilação
```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
# ou
latexmk -pdf main.tex
latexmk -c   # limpar
```

### 9.3 Verificação de redação
- [ ] Ortografia/gramática
- [ ] Fluidez (conectivos)
- [ ] Tempo verbal consistente
- [ ] Voz ativa vs passiva conforme estilo
- [ ] Sem redundâncias

### 9.4 Verificação de compilação
- [ ] Sem erros LaTeX
- [ ] Sem warnings críticos
- [ ] BibTeX OK
- [ ] `\ref{}`, `\cite{}` funcionando
- [ ] PDF gerado corretamente

### 9.5 Verificação de plágio
- Submeter PDF a Turnitin / iThenticate / Plagius / Quetext
- **Meta**: similaridade < 15% (ideal < 10%)

---

## ETAPA 10 — Preparação para Submissão

### 10.1 Arquivos
| Arquivo | Obrigatório |
|---------|-------------|
| `main.tex` | Sim |
| `main.pdf` | Sim |
| `referencias.bib` | Sim |
| `figuras/*.pdf` | Sim |
| `cover_letter.pdf` | Depende |
| `highlights.txt` | Depende |
| `graphical_abstract.pdf` | Depende |
| `supplementary.zip` | Opcional |

### 10.2 Cover letter (template)
```latex
\documentclass[11pt]{letter}
\usepackage[utf8]{inputenc}
\signature{Nome do Autor Correspondente}
\address{Instituição \\ Endereço \\ Email}
\begin{document}
\begin{letter}{Editor-in-Chief \\ Journal Name}
\opening{Dear Editor,}
We are pleased to submit our manuscript entitled "\textbf{Título}"
for consideration for publication in [Journal Name].

[Importância e contribuição]

[Por que este journal]

This manuscript has not been published and is not under consideration
for publication elsewhere.

\closing{Sincerely,}
\end{letter}
\end{document}
```

### 10.3 Checklist final
- [ ] PDF compila sem erros
- [ ] Anonimizado para blind review (se exigido)
- [ ] Dentro do limite de páginas/palavras
- [ ] Figuras em alta resolução
- [ ] Referências no formato exigido
- [ ] Metadados PDF preenchidos
- [ ] Cover letter pronta
- [ ] Conflitos de interesse declarados
- [ ] Contribuição dos autores declarada

### 10.4 Relatório de conclusão
```
========================================
✅ ARTIGO FINALIZADO PARA SUBMISSÃO
========================================
Título: [...]
Palavras-chave: [...]
Total de palavras: [X]
Total de páginas: [X]
Total de figuras: [X]
Total de tabelas: [X]
Total de referências: [X]
Arquivo principal: main.tex
PDF final: output/[TITULO_SLUG].pdf
Data de conclusão: [...]
Target: [journal/congresso]
========================================
```

---

## 📁 ESTRUTURA DE ARQUIVOS GERADOS

```
./artigo/
├── main.tex
├── [TITULO_SLUG].tex
├── referencias.bib
├── figuras/
│   ├── fig1_metodologia.pdf
│   ├── fig2_resultados.pdf
│   ├── fig3_infografico.pdf
│   └── fig4_grafico.png
├── tabelas/
│   ├── tab1_comparativo.tex
│   └── tab2_resultados.tex
├── estilos/
│   └── journal_style.cls
├── output/
│   ├── [TITULO_SLUG].pdf
│   └── [TITULO_SLUG]_draft.pdf
└── backups/
    └── [TITULO_SLUG]_v1.tex
```

---

## 🚨 ALERTAS DE QUALIDADE (PARAR E ALERTAR)

1. **Plágio** — qualquer cópia sem citação
2. **Autocitação excessiva** — >20% das referências
3. **Referências desatualizadas** — >50% com mais de 10 anos
4. **Inconsistência** — objetivos não respondidos nas conclusões
5. **Limite excedido** — acima do limite de palavras do journal

---

## ✅ FLUXO RESUMIDO

```
ETAPA 0  → Briefing (interativo)
   ↓
ETAPA 1  → Título (3 opções → seleção)
   ↓
ETAPA 2  → Resumo + Keywords
   ↓
ETAPA 3  → Introdução + Revisão
   ↓
ETAPA 4  → Metodologia
   ↓
ETAPA 5  → Resultados + Discussão
   ↓
ETAPA 6  → Conclusão
   ↓
ETAPA 7  → BibTeX
   ↓
ETAPA 8  → Figuras / Tabelas / Infográficos
   ↓
ETAPA 9  → Compilação LaTeX + Revisão Final
   ↓
ETAPA 10 → Submissão
   ↓
✅ ARTIGO FINALIZADO (PDF)
```

---

## 🔗 SKILLS RELACIONADOS

- `cientista` — persona tripla (recomendado ativar em paralelo para rigor científico)
- `escritor-cientifico` — para redação seção por seção
- `revisor-critico` — para validação I-R-B-MB-E entre etapas
- `editor-cientifico` — para ETAPAS 9 e 10 (compilação e submissão)
- `figuras-tabelas` — para ETAPA 8 (elementos visuais)
- `pesquisador-senior` — para escrita HUMANIZE durante toda a redação
