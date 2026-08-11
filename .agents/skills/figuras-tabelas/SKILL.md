---
name: figuras-tabelas
description: Protocolo obrigatório para inclusão e criação de figuras e tabelas em artigos científicos e dissertações — quando incluir, como descrever, formato LaTeX padrão (booktabs), nomenclatura, integração com RQs/SQs, checklist de qualidade visual. Use sempre que estiver redigindo, revisando ou planejando elementos visuais. Antes de aplicar, exige obrigatoriamente título, abstract e pasta de PDFs de referência.
---

# Diretrizes para Figuras e Tabelas — Protocolo Visual

Aplica-se a artigos científicos e dissertações.

---

## ⛔ PRÉ-REQUISITOS OBRIGATÓRIOS — NÃO COMECE SEM ELES

Antes de propor ou criar qualquer figura/tabela, você DEVE ter:

### 1. TÍTULO DO ARTIGO
- Título completo, idioma, subtítulo se houver

### 2. ABSTRACT DO ARTIGO
- Texto integral + palavras-chave
- Necessário para identificar quais conceitos demandam visualização

### 3. PASTA DE PDFs DE REFERÊNCIA
- Caminho absoluto da pasta com PDFs (artigos e livros) que servirão de fonte de inspiração para padrões visuais e dados a tabelar

### Mensagem-padrão quando faltar algo

> Para propor/criar figuras e tabelas preciso obrigatoriamente de:
> 1. **Título** do artigo: [pendente / fornecido]
> 2. **Abstract** + palavras-chave: [pendente / fornecido]
> 3. **Pasta de PDFs** de referência (caminho absoluto): [pendente / fornecido]
>
> Sem esses três itens não inicio. Por favor envie o que está faltando.

Não aceite "manda depois". Confirme cada item recebido.

### Após receber os 3 itens
1. Confirme título, abstract e caminho da pasta.
2. Liste os PDFs com `Glob` ou `Bash` (servem como inspiração visual).
3. Só então proponha figuras/tabelas.

---

## 🚫 NUNCA REVELAR USO DE IA EM CAPTIONS/LEGENDAS

Em legendas, fontes, notas de rodapé de tabelas, descrições de figuras, prompts de geração de imagem registrados no artigo: **JAMAIS** mencionar que foi gerado/assistido por IA, LLM, GPT, Codex, ChatGPT ou modelo de linguagem. A "Fonte" padrão é "Elaborado pelo autor" ou citação de PDF real. Sem "gerado por IA generativa", sem "criado com auxílio de modelo".

---

## 🧭 REGRA FUNDAMENTAL

- **SEMPRE** incluir figuras e tabelas quando apropriado para ilustrar conceitos
- **NUNCA** deixar seções apenas com texto quando elementos visuais podem enriquecer o conteúdo
- **MAXIMIZAR** o uso de recursos visuais para melhor compreensão

---

## 🖼️ PROTOCOLO PARA FIGURAS

### Quando incluir figuras
- Diagramas de arquitetura de framework
- Fluxogramas de processos metodológicos
- Esquemas conceituais
- Gráficos de resultados e análises
- Ilustrações de estruturas hierárquicas
- Diagramas de modos de falha (FMEA, etc.)

### Descrição obrigatória ao identificar necessidade de figura
Ao propor uma figura, SEMPRE forneça os 5 elementos:

1. **Localização exata** — "Figura X.Y deve aparecer na seção X.Y.Z"
2. **Descrição detalhada** — elementos que devem constar
3. **Propósito** — como contribui para o entendimento
4. **Estilo** — tipo de diagrama/gráfico mais adequado
5. **Referência no texto** — como será mencionada

### Formato de solicitação de figura

```
FIGURA NECESSÁRIA:
- Localização: Seção X.Y.Z
- Título: "Figura X.Y - [Título descritivo]"
- Descrição: [Descrição detalhada dos elementos]
- Propósito: [Como contribui para o entendimento]
- Referência no texto: "conforme ilustrado na Figura X.Y"
```

---

## 📊 PROTOCOLO PARA TABELAS

### Quando criar tabelas
- Comparações entre metodologias
- Critérios de avaliação
- Matrizes de comparação pareada (AHP)
- Resultados de estudos de caso
- Classificação de riscos por categoria
- Índices de consistência (CR)
- Dados de validação de framework

### Criação automática
- **SEMPRE** criar tabelas em LaTeX quando identificar necessidade
- **USAR** formato acadêmico padrão com caption e label
- **INCLUIR** fonte quando baseada em dados dos PDFs
- **REFERENCIAR** no texto antes de apresentar a tabela

### Estrutura padrão de tabela LaTeX

```latex
\begin{table}[htbp]
\centering
\caption{Título descritivo da tabela}
\label{tab:identificador}
\begin{tabular}{|c|c|c|}
\hline
\textbf{Coluna 1} & \textbf{Coluna 2} & \textbf{Coluna 3} \\
\hline
Dados & Dados & Dados \\
\hline
\end{tabular}
\source{Fonte: Elaborado pelo autor baseado em [referência]}
\end{table}
```

---

## 📂 EXEMPLOS DE APLICAÇÃO (do projeto base FMEA-AHP)

### Figuras típicas
1. **Arquitetura do Framework FMEA-AHP** — Capítulo 4, integração das metodologias
2. **Fluxograma do Processo de Priorização** — Capítulo 3, etapas do framework
3. **Estrutura Hierárquica AHP** — Capítulo 2, organização de critérios

### Tabelas típicas
1. **Comparação FMEA vs Métodos Tradicionais** — Capítulo 2 (Eficácia, Aplicabilidade, Limitações)
2. **Matriz de Comparação AHP** — Capítulo 4 (Severidade, Probabilidade, Detectabilidade)
3. **Resultados dos Estudos de Caso** — Capítulo 6 (Riscos, Priorização, CR)

> Estes exemplos são do contexto do projeto-base. Adapte ao tema do artigo em questão.

---

## 🧰 INSTRUÇÕES DE COMPORTAMENTO

### Para figuras
1. **Identificar oportunidades** de ilustração em cada seção
2. **Descrever detalhadamente** para criação externa
3. **Referenciar adequadamente** no texto
4. **Numerar sequencialmente** por capítulo

### Para tabelas
1. **Criar automaticamente** em LaTeX
2. **Usar dados dos PDFs** quando disponível
3. **Manter formatação consistente**
4. **Incluir caption e fonte**

### Integração texto-visual
- **Sempre mencionar** figuras e tabelas no texto antes de apresentá-las
- **Usar referências cruzadas** (Figura X.Y, Tabela X.Y)
- **Explicar** o que o leitor deve observar
- **Conectar** com o argumento principal

---

## 🎯 INTEGRAÇÃO COM RQs / SQs

### Figuras e tabelas para cada RQ
- **RQ1 (Adaptação FMEA):** Diagramas de modos de falha de IA, taxonomias de riscos
- **RQ2 (Integração AHP):** Estruturas hierárquicas, matrizes de comparação pareada
- **RQ3 (Eficácia):** Gráficos comparativos, tabelas de validação
- **RQ4 (Validação):** Fluxogramas Delphi, tabelas de consistência CR

### Conexão com Search Questions
- **SQ1:** Tabelas comparativas de adaptações FMEA existentes
- **SQ2:** Diagramas de integração AHP com outras metodologias
- **SQ3:** Tabelas de métricas de eficácia na literatura
- **SQ4:** Fluxogramas de métodos de validação

> Adapte os exemplos acima quando o artigo tratar de outro tema. O princípio é: cada RQ deve ter pelo menos 1 figura ou 1 tabela que ajude a respondê-la.

---

## ✅ VERIFICAÇÃO OBRIGATÓRIA

Antes de finalizar qualquer seção:

- [ ] Há oportunidades para figuras?
- [ ] Há dados que podem ser tabelados?
- [ ] Todas as figuras/tabelas estão referenciadas no texto?
- [ ] As descrições são claras e completas?
- [ ] A numeração está correta?
- [ ] Conecta com as RQs e SQs definidas?
- [ ] Segue o fluxo metodológico obrigatório?

---

## 📚 FONTES DE INSPIRAÇÃO

Consulte sempre os PDFs disponíveis na pasta de referência fornecida pelo usuário para:
- Exemplos de tabelas de comparação
- Estruturas de dados para tabelar
- Conceitos que podem ser ilustrados
- Padrões de apresentação visual
- Elementos visuais que respondam às RQs

---

## 🎨 DIAGRAMAS E FLUXOGRAMAS EM TIKZ

Para journals que exigem figuras vetoriais de alta qualidade (Elsevier, IEEE, ACM, Springer Nature), **prefira TikZ** sobre bitmap (PNG/JPG screenshot). TikZ produz PDFs vetoriais que escalam sem perda.

### Quando usar TikZ
- Diagramas conceituais (relação entre construtos)
- Fluxogramas de processo (Before/After)
- Modelos hierárquicos (organograma, taxonomia)
- Arquiteturas (sistemas, frameworks, pipelines)
- Mapas mentais
- Estruturas de dados (árvores, grafos)

### Bibliotecas essenciais

```latex
\usepackage{tikz}
\usetikzlibrary{
  positioning,        % posicionamento relativo (right=of, below=of)
  arrows.meta,        % setas modernas com flexibilidade
  shapes.geometric,   % retângulos, losangos, círculos, paralelogramos
  shapes.misc,        % shapes adicionais
  calc,               % cálculos com coordenadas
  fit,                % fit nodes em torno de grupos
  backgrounds,        % background layer
  decorations.pathmorphing  % linhas com efeitos
}
```

### Template: Diagrama hierárquico (top-down)

```latex
\begin{tikzpicture}[
    every node/.style={font=\small\sffamily},
    box/.style={
        rectangle, rounded corners=3pt,
        draw=blue!60, fill=blue!10, thick,
        minimum width=3.5cm, minimum height=0.9cm,
        align=center
    },
    arrow/.style={-{Stealth[length=2.5mm]}, thick, blue!60}
]
  \node[box] (top) {Top Level};
  \node[box, below left=0.8cm and 0.2cm of top] (left) {Branch A};
  \node[box, below right=0.8cm and 0.2cm of top] (right) {Branch B};
  \node[box, below=0.8cm of left] (a1) {Sub A1};
  \node[box, below=0.8cm of right] (b1) {Sub B1};

  \draw[arrow] (top) -- (left);
  \draw[arrow] (top) -- (right);
  \draw[arrow] (left) -- (a1);
  \draw[arrow] (right) -- (b1);
\end{tikzpicture}
```

### Template: Fluxograma de processo (left-to-right)

```latex
\begin{tikzpicture}[
    node distance=1cm and 1.5cm,
    every node/.style={font=\small\sffamily},
    start/.style={
        ellipse, draw=green!60, fill=green!15, thick,
        minimum width=1.5cm, minimum height=0.8cm
    },
    step/.style={
        rectangle, rounded corners=3pt,
        draw=blue!60, fill=blue!10, thick,
        minimum width=2.5cm, minimum height=0.9cm,
        align=center
    },
    decision/.style={
        diamond, draw=orange!70, fill=orange!15, thick, aspect=2,
        align=center
    },
    arrow/.style={-{Stealth[length=2mm]}, thick}
]
  \node[start] (s) {Start};
  \node[step, right=of s] (p1) {Identify\\Needs};
  \node[step, right=of p1] (p2) {Plan\\Training};
  \node[decision, right=of p2] (d) {Approved?};
  \node[step, right=of d] (p3) {Execute};
  \node[start, right=of p3] (e) {End};

  \draw[arrow] (s) -- (p1);
  \draw[arrow] (p1) -- (p2);
  \draw[arrow] (p2) -- (d);
  \draw[arrow] (d) -- node[above] {Yes} (p3);
  \draw[arrow] (p3) -- (e);
  \draw[arrow] (d) |- node[near start, left] {No} ++(0,-1.5) -| (p1);
\end{tikzpicture}
```

### Template: Modelo conceitual com camadas

```latex
\begin{tikzpicture}[
    every node/.style={font=\small\sffamily, align=center},
    layer/.style={
        rectangle, rounded corners=4pt,
        draw=black!30, thick,
        minimum width=12cm, minimum height=1.5cm
    },
    item/.style={
        rectangle, rounded corners=2pt,
        draw=black!50, fill=white, thick,
        minimum width=2.2cm, minimum height=0.7cm
    }
]
  \node[layer, fill=blue!10]   (l1) at (0, 4.5) {};
  \node[layer, fill=green!10]  (l2) at (0, 3.0) {};
  \node[layer, fill=orange!10] (l3) at (0, 1.5) {};
  \node[layer, fill=red!10]    (l4) at (0, 0.0) {};

  \node[anchor=west, font=\bfseries] at (l1.west) {Layer 1};
  \node[anchor=west, font=\bfseries] at (l2.west) {Layer 2};
  \node[anchor=west, font=\bfseries] at (l3.west) {Layer 3};
  \node[anchor=west, font=\bfseries] at (l4.west) {Layer 4};

  \foreach \i/\name in {0/A, 1/B, 2/C, 3/D} {
    \node[item] at ({\i*2.5-1.5}, 4.5) {Item \name};
    \node[item] at ({\i*2.5-1.5}, 3.0) {Sub \name};
  }
\end{tikzpicture}
```

### Boas práticas TikZ
- **Use `\input{figs/figX.tex}`** para isolar cada figura em arquivo próprio
- **Padronize cores** com `\definecolor{}` no preâmbulo
- **Padronize estilos** com chave `every X/.style={}`
- **Use grids invisíveis** com `\draw[help lines]` durante o desenvolvimento, depois remova
- **Evite cores muito saturadas** — prefira tons pastel com `fill=blue!10`
- **Mantenha sans-serif** (`\sffamily`) para consistência com Elsevier

---

## 📈 CHARTS EM PGFPLOTS

Para gráficos de barras, linhas, dispersão — **prefira pgfplots** sobre exportar PNG de Excel/Python. Pgfplots produz vetorial, fonte casa com o texto, alta qualidade editorial.

### Setup

```latex
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usepgfplotslibrary{groupplots}  % para charts agrupados
\usetikzlibrary{patterns}        % padrões para gráficos B&W friendly
```

### Template: Bar chart simples

```latex
\begin{tikzpicture}
\begin{axis}[
    ybar,
    width=10cm, height=6cm,
    bar width=18pt,
    ylabel={Score},
    symbolic x coords={T1, T2, T3, T4, T5, T6, T7, T8, T9, T10},
    xtick=data,
    ymin=0, ymax=10,
    nodes near coords,
    nodes near coords align={vertical},
    nodes near coords style={font=\tiny},
    enlarge x limits=0.08,
    every axis plot/.append style={
        fill=blue!50, draw=blue!70
    }
]
\addplot coordinates {
    (T1, 9.8) (T2, 9.7) (T3, 9.5) (T4, 9.5)
    (T5, 9.0) (T6, 9.0) (T7, 9.5) (T8, 9.6)
    (T9, 9.4) (T10, 9.8)
};
\end{axis}
\end{tikzpicture}
```

### Template: Grouped bar chart (comparação Before/After)

```latex
\begin{tikzpicture}
\begin{axis}[
    ybar=4pt,
    width=12cm, height=7cm,
    bar width=14pt,
    ymin=0,
    ylabel={Value},
    symbolic x coords={Metric1, Metric2, Metric3, Metric4, Metric5},
    xtick=data,
    legend pos=north east,
    legend style={font=\small, draw=none},
    enlarge x limits=0.15,
    nodes near coords,
    nodes near coords style={font=\tiny, /pgf/number format/precision=1}
]
\addplot[fill=red!50, draw=red!70]
    coordinates {(Metric1,38) (Metric2,17) (Metric3,4.2) (Metric4,3.4) (Metric5,10)};
\addplot[fill=green!50, draw=green!70]
    coordinates {(Metric1,27) (Metric2,11) (Metric3,3.0) (Metric4,4.7) (Metric5,7)};
\legend{Before, After}
\end{axis}
\end{tikzpicture}
```

### Template: Bar chart com threshold horizontal

```latex
\begin{tikzpicture}
\begin{axis}[
    ybar,
    width=12cm, height=6cm,
    bar width=10pt,
    ylabel={Final Grade},
    ymin=0, ymax=100,
    xtick={1,...,21},
    xticklabel style={font=\tiny},
    extra y ticks={70},
    extra y tick labels={Pass},
    extra y tick style={
        ytick style={draw=none},
        yticklabel style={anchor=west, xshift=2pt, font=\small, color=green!60!black}
    }
]
\addplot[fill=blue!50, draw=blue!70]
    coordinates {
        (1,65) (2,85) (3,92) (4,98) (5,100)
        (6,72) (7,75) (8,68) (9,70) (10,73)
        (11,68) (12,82) (13,69) (14,71) (15,68)
        (16,70) (17,69) (18,75) (19,71) (20,72)
        (21,93)
    };
\draw[green!60!black, thick, dashed] (axis cs:0,70) -- (axis cs:22,70);
\end{axis}
\end{tikzpicture}
```

### Paletas de cores Elsevier-friendly

```latex
% Paleta sequencial azul
\definecolor{elsB1}{HTML}{08306B}
\definecolor{elsB2}{HTML}{2171B5}
\definecolor{elsB3}{HTML}{6BAED6}
\definecolor{elsB4}{HTML}{C6DBEF}

% Paleta categórica acessível (ColorBrewer Set2)
\definecolor{elsC1}{HTML}{66C2A5}
\definecolor{elsC2}{HTML}{FC8D62}
\definecolor{elsC3}{HTML}{8DA0CB}
\definecolor{elsC4}{HTML}{E78AC3}
\definecolor{elsC5}{HTML}{A6D854}
```

### Print-friendly (preto-e-branco)

Adicione patterns ao invés de cores quando o journal pede preto-e-branco:

```latex
\addplot[pattern=north east lines, pattern color=black, draw=black] coordinates {...};
\addplot[pattern=horizontal lines, pattern color=black, draw=black] coordinates {...};
```

---

## ⚠️ TRANSPARÊNCIA METODOLÓGICA EM CHARTS RECONSTRUÍDOS

Quando os **dados brutos não estão disponíveis** e você precisa reconstruir um chart a partir de **agregados publicados** (médias, percentuais, totais), é OBRIGATÓRIO:

### 1. Indicar na caption
> **Fig. X**: Distribuição de scores de treinamento (n=10 sessões). *Valores reconstruídos a partir de agregados publicados no relatório interno; não representam dados individuais brutos.*

### 2. Indicar na Methodology
Em uma nota de rodapé ou na seção 3.2 (Data Analysis):

> "Visualizações apresentadas nas Figuras X-Y foram reconstruídas a partir de estatísticas agregadas (médias e percentuais) reportadas pela facility nos relatórios de qualidade Q1-Q4. Dados individuais não foram disponibilizados por motivos de confidencialidade."

### 3. Limitar tipos de chart aceitáveis quando dados são agregados
- **OK**: bar chart de médias, line chart de tendências, pizza de proporções
- **NÃO OK**: box plot, violin plot, scatter plot individual, histogram detalhado
  (esses exigem dados brutos)

### 4. Linguagem honesta no texto
- ✅ "A facility reported a reduction of 28% in training failures"
- ❌ "We observed a reduction of 28%..." (implica que você teve acesso ao raw)

---

## 🔗 SKILLS RELACIONADOS

- `cientista` — persona tripla completa
- `escritor-cientifico` — para integrar referências cruzadas no texto
- `revisor-critico` — para auditoria visual das figuras/tabelas
- `workflow-artigo` — fluxo completo (ETAPA 8 cobre elementos visuais)
- `latex-elsevier-cas` — integração com template Elsevier CAS
- `journal-jatm` — expectativas específicas de visualização para JATM
