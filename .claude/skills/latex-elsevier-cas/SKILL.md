---
name: latex-elsevier-cas
description: Protocolo de migração de artigos científicos (Word/PDF) para o template LaTeX Elsevier CAS (Complex Article Structure). Cobre escolha cas-sc vs cas-dc, frontmatter completo (título, autores com ORCID/CRediT, afiliações múltiplas), abstract/keywords/highlights/graphical abstract, citações natbib (author-year ou numeric), BibTeX com cas-model2-names.bst, figuras (PDF/PNG/TikZ), tabelas com booktabs, troubleshooting comum (overfull, references ???, BibTeX rerun). Use ao preparar manuscrito para qualquer journal Elsevier que aceite cas-sc/cas-dc (Journal of Cleaner Production, Journal of Air Transport Management, Energy, Applied Energy, etc.). Antes de aplicar, exige obrigatoriamente título, abstract e pasta de PDFs de referência.
---

# Skill: latex-elsevier-cas

## Quando Invocar

Você é especialista em migração de artigos científicos para o template LaTeX **Elsevier CAS** (Complex Article Structure). Invoque esta skill quando o usuário:

- Está submetendo a journal Elsevier que aceita cas-sc ou cas-dc
- Tem manuscrito em Word/PDF e precisa converter para LaTeX
- Precisa configurar frontmatter Elsevier (autores múltiplos, afiliações, ORCID, CRediT)
- Precisa configurar BibTeX no formato Elsevier (cas-model2-names.bst)
- Quer criar Highlights e Graphical Abstract Elsevier
- Encontra problemas de compilação no template cas-sc/cas-dc

---

## 🚨 Regras Invioláveis Herdadas

Esta skill herda das três regras do projeto:

### 1. Três Pré-requisitos Obrigatórios

Antes de iniciar qualquer migração, você DEVE ter recebido:

1. **Título** completo do artigo + idioma
2. **Abstract** integral + 3-6 palavras-chave
3. **Pasta de PDFs** de referência (caminho absoluto)

Se algum estiver ausente, recuse iniciar e solicite o item. "Envio depois" não é aceitável.

### 2. Nunca Revelar Uso de IA

Nenhum deliverable (corpo do artigo, cover letter, agradecimentos, legendas, declaração de contribuição, resposta a revisores) pode mencionar que foi escrito, assistido ou revisado por IA/LLM/GPT/Claude/ChatGPT. Remova silenciosamente qualquer menção no texto original. Exceção única: quando a IA é objeto da pesquisa.

### 3. Topic-Agnostic

Não assuma domínio (FMEA, ML, aviação, etc.). O tema é aprendido em runtime via os três pré-requisitos.

---

## 1. Escolha da Variante (cas-sc vs cas-dc)

| Variante | Layout | Quando Usar | Journals Típicos |
|---|---|---|---|
| **cas-sc** | 1 coluna | Drafts longos, journals de humanidades/biologia | Cell Reports, Heliyon |
| **cas-dc** | 2 colunas | Final submission, journals de STEM/engineering | J. Cleaner Prod., J. Air Transp. Manag., Energy, App. Energy |

**Decisão padrão**: confirme com o usuário; se o journal já está definido, busque em "Guide for Authors" qual variante é exigida.

---

## 2. Estrutura Mínima de Arquivos

```
artigo/
├── main.tex                     # arquivo principal
├── cas-dc.cls (ou cas-sc.cls)   # classe LaTeX (copiada do template)
├── cas-common.sty               # estilos compartilhados (copiada)
├── cas-model2-names.bst         # estilo bibliográfico (copiada)
├── references.bib               # base BibTeX
├── secoes/                      # uma seção por arquivo
│   ├── 01-introduction.tex
│   ├── 02-literature-review.tex
│   ├── 03-methodology.tex
│   ├── 04-results.tex
│   ├── 05-discussion.tex
│   └── 06-conclusion.tex
├── figs/                        # figuras em TikZ (.tex) ou bitmap (PDF/PNG/JPG)
├── tabelas/                     # tabelas standalone (.tex)
├── highlights.tex
├── graphical-abstract.tex
└── cover-letter.tex
```

**Por que separar em arquivos?**
- Editar/revisar é mais rápido
- Diff em git fica limpo
- Compilação parcial via `\includeonly{}` em desenvolvimento

---

## 3. Preâmbulo Padrão (`main.tex`)

```latex
\documentclass[a4paper,fleqn]{cas-dc}

% Citações author-year (padrão Elsevier)
\usepackage[authoryear,longnamesfirst]{natbib}

% Para diagramas e charts em TikZ/pgfplots
\usepackage{tikz}
\usetikzlibrary{positioning,arrows.meta,shapes.geometric,calc,fit,backgrounds}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}

% Tabelas (cas-dc já carrega booktabs, mas adicionalmente:)
\usepackage{tabularx}
\usepackage{array}

% Hyperref já é carregado por cas-dc, mas customizar cores:
\hypersetup{
  colorlinks=true,
  linkcolor=blue!70!black,
  citecolor=blue!70!black,
  urlcolor=blue!70!black
}

% Macros úteis
\def\tsc#1{\csdef{#1}{\textsc{\lowercase{#1}}\xspace}}
\tsc{AS9100}
\tsc{ICAO}

\begin{document}
```

**Opções do `\documentclass`** (todas opcionais):
- `[a4paper]` — papel A4 (padrão)
- `[fleqn]` — equações alinhadas à esquerda
- `[longmktitle]` — frontmatter de múltiplas páginas
- `[singleblind]` / `[doubleblind]` — anonimato para revisão
- `[review]` — double spacing para revisores
- `[final]` — spacing normal

---

## 4. Frontmatter Completo (Elsevier)

```latex
% ============ TÍTULO ============
\title[mode=title]{Título Principal do Artigo}

% Notas no título (opcional)
\tnotemark[1]
\tnotetext[1]{Este artigo é parte do projeto X financiado por Y.}

% ============ AUTOR(ES) ============
\author[1]{Primeiro Autor Sobrenome}[
  orcid=0000-0000-0000-0000,
  type=editor,
  role=Researcher
]
\cormark[1]
\ead{primeiro.autor@exemplo.com}
\ead[url]{https://exemplo.com/perfil}
\credit{Conceptualization, Methodology, Writing -- original draft}

\author[1,2]{Segundo Autor Sobrenome}[
  orcid=0000-0000-0000-0001
]
\ead{segundo.autor@exemplo.com}
\credit{Data curation, Formal analysis, Writing -- review \& editing}

% ============ AFILIAÇÕES ============
\affiliation[1]{
  organization={Departamento X, Universidade Y},
  addressline={Rua Z, 123},
  city={Cidade},
  postcode={00000-000},
  state={Estado},
  country={País}
}

\affiliation[2]{
  organization={Empresa W},
  city={Cidade},
  country={País}
}

% ============ AUTOR CORRESPONDENTE ============
\cortext[1]{Corresponding author}

% ============ TÍTULO/AUTORES CURTOS (cabeçalho) ============
\shorttitle{Versão curta do título}
\shortauthors{Sobrenome et~al.}

% ============ ABSTRACT ============
\begin{abstract}
Texto do abstract aqui (200-300 palavras).
\end{abstract}

% ============ GRAPHICAL ABSTRACT (opcional) ============
\begin{graphicalabstract}
\includegraphics[width=\linewidth]{figs/graphical-abstract.pdf}
\end{graphicalabstract}

% ============ HIGHLIGHTS ============
\begin{highlights}
\item Bullet 1 (max 85 caracteres incluindo espaços)
\item Bullet 2
\item Bullet 3
\item Bullet 4
\item Bullet 5
\end{highlights}

% ============ KEYWORDS ============
\begin{keywords}
Palavra1 \sep Palavra2 \sep Palavra3 \sep Palavra4
\end{keywords}

% Dispara compilação da página de título
\maketitle
```

### CRediT Roles (Contributor Roles Taxonomy)

Os 14 papéis CRediT padrão:
1. Conceptualization
2. Data curation
3. Formal analysis
4. Funding acquisition
5. Investigation
6. Methodology
7. Project administration
8. Resources
9. Software
10. Supervision
11. Validation
12. Visualization
13. Writing -- original draft
14. Writing -- review \& editing

Usar dentro de `\credit{}` separados por vírgula.

---

## 5. Corpo do Documento

### Seções e Subseções
```latex
\section{Introduction}
\label{sec:intro}
Texto...

\subsection{Background}
\label{subsec:background}
Texto...
```

### Listas
```latex
\begin{enumerate}[(a)]
  \item Item A
  \item Item B
\end{enumerate}

\begin{itemize}
  \item Bullet
\end{itemize}
```

### Equações
```latex
% Inline
A função $f(x) = x^2$ é convexa.

% Display numerada
\begin{equation}
  ROI = \frac{\text{Savings} - \text{Cost}}{\text{Cost}} \times 100\%
  \label{eq:roi}
\end{equation}

% Display não numerada
\begin{equation*}
  E = mc^2
\end{equation*}

% Múltiplas alinhadas
\begin{align}
  C_{\text{internal}} &= L_h \cdot R + S_c \cdot P_c \label{eq:internal} \\
  C_{\text{external}} &= W + S_h + R_p \label{eq:external}
\end{align}
```

### Figuras
```latex
% Figura simples
\begin{figure}[h]
  \centering
  \includegraphics[width=.9\linewidth]{figs/fig1.pdf}
  \caption{Descrição da figura.}
  \label{fig:fig1}
\end{figure}

% Figura em TikZ (input externo)
\begin{figure}[h]
  \centering
  \input{figs/fig0-conceptual-model}
  \caption{Modelo conceitual.}
  \label{fig:conceptual}
\end{figure}

% Figura larga (ocupa duas colunas em cas-dc)
\begin{figure*}[t]
  \centering
  \includegraphics[width=\linewidth]{figs/fig-wide.pdf}
  \caption{Figura que precisa ocupar largura total.}
  \label{fig:wide}
\end{figure*}
```

### Tabelas com booktabs (padrão Elsevier)
```latex
\begin{table}[h]
  \centering
  \caption{Comparação de resultados antes e depois da intervenção.}
  \label{tab:before-after}
  \begin{tabular}{lrrr}
    \toprule
    Métrica & Antes & Depois & Variação \\
    \midrule
    Training failures (\%)        & 38 & 27 & $-28\%$ \\
    Non-conformances (n)          & 17 & 11 & $-35\%$ \\
    Quality costs (USD M/year)    & 4.2 & 3.0 & $-1.2$ \\
    Customer satisfaction (0--5)  & 3.4 & 4.7 & $+38\%$ \\
    \bottomrule
  \end{tabular}
\end{table}

% Tabela larga (duas colunas em cas-dc)
\begin{table*}[t]
  \centering
  ...
\end{table*}
```

**Regras booktabs**:
- Use `\toprule`, `\midrule`, `\bottomrule` (não `\hline`)
- Use `\cmidrule(lr){2-4}` para linhas parciais
- **Evite** linhas verticais (`|`) — não-Elsevier-style
- **Evite** linhas horizontais entre cada linha de dados

### Citações natbib
```latex
\citet{Smith2024}        % Smith (2024)
\citep{Smith2024}        % (Smith, 2024)
\citep[ver][]{Smith2024} % (ver Smith, 2024)
\citep[p.~12]{Smith2024} % (Smith, 2024, p. 12)
\citeauthor{Smith2024}   % Smith
\citeyear{Smith2024}     % 2024
\citet*{Smith2024}       % nomes completos (longnamesfirst só na primeira vez)
```

### Fim do Documento
```latex
% Créditos resumidos (opcional)
\printcredits

% Bibliografia
\bibliographystyle{cas-model2-names}
\bibliography{references}

\end{document}
```

---

## 6. BibTeX (cas-model2-names.bst)

### Tipos suportados
- `@article`
- `@book`
- `@incollection`
- `@inproceedings`
- `@techreport`
- `@misc`
- `@online`
- `@phdthesis`

### Entry mínimo
```bibtex
@article{Smith2024,
  author  = {Smith, John A. and Doe, Jane B.},
  title   = {Título do artigo},
  journal = {Journal of Air Transport Management},
  volume  = {115},
  number  = {3},
  pages   = {102--115},
  year    = {2024},
  doi     = {10.1016/j.jairtraman.2024.012345},
  url     = {https://doi.org/10.1016/j.jairtraman.2024.012345}
}
```

### Convenções para Elsevier
- **DOI sempre** quando disponível
- Nomes: `Sobrenome, Nome` (vírgula antes do nome dado)
- Múltiplos autores: separar com `and` (não vírgula)
- Pages com travessão duplo: `102--115`
- Use `et~al.` (com til) ao escrever no texto, mas BibTeX gera automaticamente

---

## 7. Compilação

### Sequência padrão
```bash
pdflatex main
bibtex main
pdflatex main
pdflatex main
```

### Para projetos com TikZ pesado
Adicionar no preâmbulo:
```latex
\usetikzlibrary{external}
\tikzexternalize[prefix=tikz-cache/]
```

### Limpeza de arquivos auxiliares
```bash
rm -f *.aux *.bbl *.blg *.log *.out *.toc *.fls *.fdb_latexmk
```

---

## 8. Troubleshooting Comum

| Problema | Causa | Solução |
|---|---|---|
| Refs aparecem como `???` | BibTeX não rodou | `bibtex main` + 2× `pdflatex` |
| `Undefined control sequence \maketitle` | Falta `\maketitle` após frontmatter | Inserir antes de `\section{Introduction}` |
| Tabela transborda coluna | tabular muito larga em cas-dc | Use `table*` (duas colunas) ou `\resizebox{\linewidth}{!}{...}` |
| Figura não aparece | Path errado ou formato não suportado | Use paths relativos: `figs/x.pdf`; formatos: PDF, PNG, JPG (não EPS) |
| `Overfull \hbox` em URLs | URL não quebra linha | Use `\sloppy` localmente ou `\url{...}` ao invés de plain text |
| `Missing $ inserted` | Caractere matemático fora de math mode | Verifique `_`, `^`, `<`, `>` no texto — escape com `\_` ou `\textunderscore` |
| Frontmatter quebra layout | Muitos autores/afiliações em 1 coluna | Adicione opção `longmktitle` no `\documentclass` |
| `Package natbib Error: Bibliography not compatible` | Mistura `\cite` e `\citep` em estilo errado | Padronize: ou tudo numeric ou tudo author-year |
| Cores no PDF não imprimem | xcolor em CMYK vs RGB | Para print: `\usepackage[cmyk]{xcolor}` |

---

## 9. Checklist Final Antes de Submeter

- [ ] Compila sem erros (`pdflatex` × 2 + `bibtex` + `pdflatex` × 2)
- [ ] Nenhuma referência aparece como `???` ou `[?]`
- [ ] Todas as figuras compilam e têm `\caption{}` + `\label{}`
- [ ] Todas as tabelas usam booktabs (sem `\hline` ou `|`)
- [ ] Todas as citações têm DOI quando disponível
- [ ] Frontmatter: título, autores, ORCID, afiliações, CRediT, autor correspondente
- [ ] Abstract com 200-300 palavras
- [ ] Keywords: 3-6 termos separados por `\sep`
- [ ] Highlights: 3-5 bullets, cada ≤85 caracteres
- [ ] Graphical Abstract (se journal exige)
- [ ] Cover Letter pronto
- [ ] Sem menções a IA/LLM/Claude no texto, agradecimentos, créditos
- [ ] Sem placeholders `[NOME]`, `[ORG]`, `[EMAIL]` esquecidos
- [ ] Conferência visual do PDF final em monitor + impressão

---

## 10. Arquivos para Enviar à Elsevier

Ao submeter via Elsevier Editorial System:

1. `main.pdf` — PDF compilado (peer review)
2. `main.tex` — fonte LaTeX
3. `cas-dc.cls` (ou cas-sc.cls)
4. `cas-common.sty`
5. `cas-model2-names.bst`
6. `references.bib`
7. Pasta `figs/` com todas as figuras
8. Pasta `secoes/` com todos os `.tex`
9. `cover-letter.pdf` separado
10. (Se journal pede) `highlights.pdf` separado, `graphical-abstract.pdf` separado

---

**Skills relacionadas**: [[journal-jatm]] (para preparação específica JATM), [[figuras-tabelas]] (TikZ/pgfplots), [[editor-cientifico]] (cover letter e response to reviewers), [[highlights-graphical-abstract]] (elementos suplementares).
