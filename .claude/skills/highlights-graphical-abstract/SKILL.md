---
name: highlights-graphical-abstract
description: Cria os elementos suplementares exigidos por journals Elsevier e similares — Highlights (3–5 bullets de ≤85 caracteres cada), Graphical Abstract (1 imagem que conta a história visual em formato/dimensões corretas), e Research Highlights longos quando aplicável. Use ao preparar submissão para Elsevier, Springer Nature ou journals que pedem esses elementos. Antes de criar, exige obrigatoriamente título, abstract e pasta de PDFs de referência.
---

# Highlights e Graphical Abstract

Skill dedicado a entregáveis suplementares de submissão — elementos que muitos autores tratam como afterthought e perdem impacto. Para Elsevier (incluindo RESS, JCLEPro, etc.), Springer Nature e diversos outros, são **obrigatórios**.

---

## ⛔ PRÉ-REQUISITOS OBRIGATÓRIOS — NÃO COMECE SEM ELES

Antes de criar Highlights ou Graphical Abstract, você DEVE ter:

### 1. TÍTULO DO ARTIGO
- Título completo, idioma definitivo

### 2. ABSTRACT DO ARTIGO
- Texto integral + palavras-chave
- A Take-Home Message do abstract guia tanto Highlights quanto Graphical Abstract

### 3. PASTA DE PDFs DE REFERÊNCIA
- Caminho absoluto da pasta
- Útil para verificar precedentes visuais na área (estilo de graphical abstracts em papers similares)

### Mensagem-padrão quando faltar algo

> Para criar Highlights / Graphical Abstract preciso obrigatoriamente de:
> 1. **Título** do artigo: [pendente / fornecido]
> 2. **Abstract** + palavras-chave: [pendente / fornecido]
> 3. **Pasta de PDFs** de referência (caminho absoluto): [pendente / fornecido]
>
> Sem esses três itens não inicio. Por favor envie o que está faltando.

Adicional útil (não bloqueante): journal-alvo confirmado, para aplicar especificações exatas.

---

## 🚫 NUNCA REVELAR USO DE IA

**Regra inviolável:** Highlights, Graphical Abstract, captions de elementos visuais e qualquer descrição associada **JAMAIS** mencionam que foram criados/assistidos por IA, LLM, GPT, Claude, ChatGPT, modelo de linguagem, ferramentas de geração de imagem por IA. Sem disclosures espontâneos. Atenção em **prompts registrados** ou **metadados** de arquivos de imagem — limpar antes de submeter.

---

## ✏️ HIGHLIGHTS — ELSEVIER (PADRÃO MAIS RIGOROSO)

### Especificações duras
- **3 a 5 bullets** (5 é o máximo absoluto)
- **≤ 85 caracteres por bullet** (incluindo espaços)
- **Frases declarativas** — não perguntas, não fragmentos
- **Sem citações** — não usar `[1]` ou `(Smith, 2023)`
- **Sem siglas não definidas** no contexto do bullet (em geral, evite siglas)
- **Sem palavras como "we propose", "this paper presents"** — vá direto ao **achado**
- **Voz ativa, presente do indicativo**
- **Submeter como arquivo separado**: `highlights.docx` ou `.txt`

### Anti-padrões (rejeitados / fracos)
- ❌ "This paper presents a new framework for X." (excede 85 char + meta)
- ❌ "We propose a hybrid model that..." (meta — fala do paper, não do achado)
- ❌ "X is important." (vazio)
- ❌ "Reviews the literature on Y." (meta + descritivo)
- ❌ "What is the role of X in Y?" (pergunta)

### Padrões fortes
- ✅ "Hybrid FMEA-AHP framework prioritizes risks in black-box AI systems."
- ✅ "Sensitivity analysis across 1000 Monte Carlo runs validates rank stability."
- ✅ "Method reduces expert evaluation time by 42% in three case studies."
- ✅ "AHP consistency ratio remains below 0.10 in all pairwise comparisons."

### Estrutura recomendada (5 bullets)
1. **O que** foi proposto/desenvolvido (nome do método/framework)
2. **Como** valida — métrica concreta, n, cenário
3. **Resultado-chave 1** — número específico
4. **Resultado-chave 2** — número específico ou qualitativo forte
5. **Implicação prática** — onde se aplica

### Processo de redação
1. Liste todos os achados quantitativos do paper (de Resultados/Discussão)
2. Para cada, redija como frase ativa ≤85 char
3. Selecione os 5 mais distintivos (cobrindo método + validação + resultados + implicação)
4. Conte caracteres de cada (`echo -n "..." | wc -c` ou função LEN no Word)
5. Refinar: cortar artigos ("the", "a") quando inglês, cortar adjetivos vazios
6. Revisar coerência com Abstract e Conclusão (mesma Take-Home Message)

---

## 🖼️ GRAPHICAL ABSTRACT — ELSEVIER

### Especificações duras (Elsevier; outros journals podem variar — verificar)
- **Formato:** TIFF, EPS, PDF, MS Office (Word/PPT) — preferência: **TIFF ou PDF vetorial**
- **Dimensões:** mínimo **531 × 1328 px** (Elsevier 2024). Algumas guidelines listam **531 × 1328** (alt mín × larg mín) — sempre verificar página do journal-alvo. **Não usar largura inferior à mínima**.
- **Resolução:** 300 DPI mínimo
- **Sem texto excessivo** — leitor deve "captar" em 5–10 segundos
- **Fonte mínima:** **Arial 12pt** equivalente quando renderizado nas dimensões de submissão
- **Cor:** RGB; cuidado com paleta acessível (daltonismo)
- **Não pode:** aparecer no manuscrito-corpo; ser cópia de figura interna (deve ser uma síntese própria)

### Princípios de design
1. **Uma mensagem central** — não tente representar o paper inteiro
2. **Fluxo lógico claro** (esquerda→direita ou cima→baixo)
3. **Ícones simples**, não ilustração realista detalhada
4. **Sem chartjunk** (sombras desnecessárias, gradientes sem propósito)
5. **Espaço em branco** — não encha tudo
6. **Contraste alto** — vai aparecer pequeno em listas de busca

### Estrutura típica (entrada → processo → saída)
```
[INPUT]      →    [METHOD/FRAMEWORK]      →    [OUTPUT]
   ↓                       ↓                         ↓
Black-box        Hybrid FMEA-AHP          Prioritized risk
AI system        with Monte Carlo         ranking + GPW
                  sensitivity              (CR < 0.10)
```

### Ferramentas recomendadas
| Ferramenta | Forte para | Limite |
|------------|-----------|--------|
| **Inkscape** (grátis) | SVG/PDF vetorial profissional | curva de aprendizado |
| **draw.io / diagrams.net** (grátis, web) | Fluxogramas | menos polido visualmente |
| **BioRender** (pago) | Biologia/saúde, banco de ícones | mensalidade |
| **Adobe Illustrator** (pago) | Padrão profissional | pago |
| **Mind the Graph** (freemium) | Acadêmico geral | banco limitado no plano grátis |
| **PowerPoint / Keynote** | Aceitos por Elsevier; práticos | rasterização ao exportar — atenção à resolução |

### Processo de criação
1. Extrair a Take-Home Message do Abstract (1 frase)
2. Esboçar 3 layouts em rascunho (papel/tablet)
3. Validar com co-autor: "olha 5 segundos, o que entendeu?"
4. Refinar layout escolhido
5. Aplicar ícones simples e consistentes (mesma família visual)
6. Adicionar texto **mínimo** — só o que ícone não comunica
7. Exportar nas dimensões e formato exigidos
8. Verificar metadata do arquivo (limpar prompts de IA, autor original etc.)
9. Pré-visualizar em 200 px de largura (como aparece em listas)

### Anti-padrões
- ❌ Reproduzir uma figura do paper (deve ser síntese visual nova)
- ❌ Texto em fonte minúscula que vira borrão quando reduzido
- ❌ 8 setas, 12 caixas, 3 cores diferentes — pollution visual
- ❌ Imagem fotorrealista com fundo gradiente
- ❌ Logos institucionais ou marca pessoal
- ❌ Resultado preliminar como visual principal (revisor estranha)

---

## 📝 RESEARCH HIGHLIGHTS (variante longa)

Alguns journals (e.g., *Cell* Press) pedem **Research Highlights** mais longos — 3–4 frases curtas em vez de bullets de 85 char.

Estrutura:
- 1ª frase: contexto + problema
- 2ª frase: contribuição
- 3ª frase: validação/resultado
- 4ª frase: implicação

Verificar a guideline do journal-alvo antes de escolher formato.

---

## 🔄 COERÊNCIA TAKE-HOME MESSAGE

Highlights e Graphical Abstract devem reforçar a **mesma mensagem central** que aparece em:

1. **Título**
2. **Abstract**
3. **Final da Introdução**
4. **Conclusão**
5. **Highlights** ← novo
6. **Graphical Abstract** ← novo

Se um destes 6 lugares conta uma história diferente, há incoerência estrutural — refazer.

---

## ✅ CHECKLIST FINAL

### Highlights
- [ ] 3–5 bullets exatos
- [ ] Cada bullet ≤ 85 caracteres (contagem real, com espaços)
- [ ] Voz ativa, presente, sem meta-discurso
- [ ] Sem citações, sem siglas indefinidas
- [ ] Cobre: método + validação + resultado + implicação
- [ ] Coerente com Abstract e Conclusão
- [ ] Submetido como arquivo separado (formato exigido)

### Graphical Abstract
- [ ] Dimensões e DPI conforme guideline do journal-alvo
- [ ] Formato vetorial (TIFF/PDF/EPS) sempre que possível
- [ ] Texto legível em ~200 px (visualização em listas)
- [ ] Não reproduz figura interna do paper
- [ ] Mensagem captável em 5–10 s
- [ ] Paleta acessível (testar em escala de cinza)
- [ ] Metadata limpa (sem prompts de IA, sem dados pessoais expostos)
- [ ] Coerente com Take-Home Message dos outros 5 lugares

---

## 🔁 FLUXO DE TRABALHO

1. Validar pré-requisitos (título, abstract, pasta PDFs)
2. Confirmar **journal-alvo** e baixar guideline atualizada (Elsevier 2024+ pode ter requisitos mudados)
3. Extrair Take-Home Message do Abstract
4. Redigir 8–10 candidatos a bullet, depois selecionar 5
5. Esboçar 3 layouts de Graphical Abstract
6. Pré-revisão por co-autor (teste dos 5–10 segundos)
7. Refinar e exportar nos formatos exigidos
8. Verificar coerência cross-elementos (Título ↔ Abstract ↔ Highlights ↔ GA ↔ Conclusão)
9. Empacotar para submissão

---

## 🔗 SKILLS RELACIONADOS

- `editor-cientifico` — preparação geral de submissão (cover letter, conformidade, integração final)
- `figuras-tabelas` — protocolo visual interno do artigo (não substitui Graphical Abstract)
- `pesquisador-senior` — calibrar Take-Home Message e estilo HUMANIZE
- `escritor-cientifico` — sincronizar bullets com texto do Abstract
- `cientista` — persona tripla (rigor geral)
