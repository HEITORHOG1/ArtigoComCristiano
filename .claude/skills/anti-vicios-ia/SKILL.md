---
name: anti-vicios-ia
description: Escaneia texto científico para detectar e remover vícios típicos de IA (travessão/em-dash em excesso, "vale ressaltar", "delve into", "tapestry", regra de três mecânica, hedging exagerado, transições genéricas como "Furthermore"/"Moreover"/"Ademais", clichês de abertura/fechamento). Use em texto já escrito (próprio ou IA-assistido) antes de submeter, especialmente quando preocupado com detectores tipo Turnitin AI ou GPTZero. Antes de aplicar, exige obrigatoriamente título, abstract e pasta de PDFs de referência.
---

# Anti-Vícios de IA — `@anti-vicios-ia`

Skill dedicado a **caçar e remover** padrões textuais que delatam escrita gerada/assistida por IA. Diferente de `pesquisador-senior` (que orienta a redação desde o início), este skill atua **depois** do texto pronto, em modo auditoria-e-limpeza.

---

## ⛔ PRÉ-REQUISITOS OBRIGATÓRIOS — NÃO COMECE SEM ELES

Antes de auditar/reescrever, você DEVE ter:

### 1. TÍTULO DO ARTIGO
- Título completo, idioma, subtítulo

### 2. ABSTRACT DO ARTIGO
- Texto integral + palavras-chave
- Necessário para preservar a Take-Home Message ao reescrever

### 3. PASTA DE PDFs DE REFERÊNCIA
- Caminho absoluto da pasta
- Necessária para verificar que termos técnicos no texto **existem nas fontes** (caça alucinações de IA, não só estilo)

### Mensagem-padrão quando faltar algo

> Para auditar e remover vícios de IA preciso obrigatoriamente de:
> 1. **Título** do artigo: [pendente / fornecido]
> 2. **Abstract** + palavras-chave: [pendente / fornecido]
> 3. **Pasta de PDFs** de referência (caminho absoluto): [pendente / fornecido]
>
> Sem esses três itens não inicio. Por favor envie o que está faltando.

Não aceite "manda depois". Confirme cada item recebido.

### Após receber os 3 itens
1. Confirme título, abstract, caminho da pasta.
2. Liste os PDFs com `Glob` ou `Bash`.
3. Peça o **texto a auditar** (arquivo ou colado).
4. Pergunte o **idioma do texto** (PT-BR, EN, outro).
5. Só então comece a auditoria.

---

## 🚫 REGRA INVIOLÁVEL — JAMAIS REVELAR USO DE IA

**Em hipótese alguma** o texto entregue, cover letter, agradecimentos, ou qualquer parte do material pode mencionar:

- "este artigo foi escrito/auxiliado/revisado por IA / LLM / GPT / Claude / ChatGPT / inteligência artificial"
- "com assistência de ferramentas de IA"
- "usando modelo de linguagem"
- "este texto foi gerado por..."
- Agradecimentos a ferramentas de IA
- Disclosures de uso de IA em metodologia, exceto se o **uso da IA for o objeto da pesquisa em si**

Se o usuário fornecer texto bruto que contenha essas menções, **remova-as silenciosamente**. Se forem essenciais ao escopo (ex: estudo sobre IA), reescreva técnico-objetivo sem autorrevelação do processo de produção.

**Por quê:** o usuário foi explícito — o material deve ser indistinguível como trabalho humano. Nenhum disclosure não solicitado.

---

## 🎯 OBJETIVO

Reduzir a "assinatura de IA" do texto preservando:
- Conteúdo técnico
- Citações reais
- Estrutura científica
- Take-Home Message
- Voz do autor

Sem introduzir erros gramaticais artificiais (não é "humanizar piorando").

---

## 🚩 CATÁLOGO DE VÍCIOS — PORTUGUÊS

### 1. Pontuação suspeita

| Vício | Sinal | Como tratar |
|-------|-------|-------------|
| **Travessão (—) em excesso** | Mais de 1–2 travessões por parágrafo | Trocar por vírgula, parênteses ou ponto-e-vírgula. Travessão fica só onde dá pausa enfática real. |
| **Travessão substituindo dois pontos** | "O método foi simples — coletamos os dados..." | Trocar por dois pontos: "O método foi simples: coletamos..." |
| **Reticências sem necessidade** | "...explorar o tema..." | Cortar. Reticências em texto científico são raras. |
| **Aspas duplas em termos comuns** | "abordagem", "framework" | Remover. Aspas só pra termos técnicos novos ou citação literal. |

### 2. Vocabulário-marcador

Palavras que detectores estatísticos (e revisores experientes) flagam imediatamente:

- **"vale ressaltar"** → deletar a frase inteira ou trocar por "Note-se que" (raro)
- **"é importante notar"** / **"é importante destacar"** → deletar; o ponto importante deve falar por si
- **"em síntese"** / **"em suma"** → trocar por "portanto" ou cortar
- **"outrossim"** → nunca usar; é sinal claro de autotradução IA
- **"ademais"** → trocar por "além disso" ou cortar
- **"por conseguinte"** → trocar por "logo" ou "assim"
- **"nesse sentido"** / **"nesse contexto"** → frequentemente vazio, cortar
- **"de fato"** / **"com efeito"** → cortar (raro humano usar tanto)
- **"robusto"** / **"robusta"** → checar se é técnico (estatística robusta) ou retórico ("método robusto") — no segundo caso, trocar por "consistente" ou cortar
- **"profundo"** / **"profunda"** ("análise profunda", "discussão profunda") → cortar adjetivo
- **"abrangente"** ("revisão abrangente") → checar; muitas vezes vazio
- **"intricado"** / **"intrincado"** → trocar por "complexo" e justificar
- **"navegar pelo"** ("navegar pelos desafios") → traduzir literalmente do inglês AI; reescrever
- **"explorar"** ("este artigo explora") → trocar por verbo concreto ("analisa", "compara", "testa")
- **"mergulhar"** ("mergulhar no tema") → cortar metáfora; ir direto

### 3. Transições genéricas

| Vício | Substituir por |
|-------|----------------|
| "Furthermore," / "Moreover," | conector contextual ("Apesar disso", "Embora", "Como consequência") ou ponto final + nova frase |
| "Ademais," / "Além disso," (em excesso) | conector específico ou cortar |
| "Por outro lado," (em excesso) | "Em contraste,", "Diferentemente," ou cortar |
| "Em primeiro lugar... em segundo lugar..." | cortar a numeração; deixar a lógica conduzir |
| "Diante do exposto," | cortar; vai direto ao ponto |
| "Posto isto," | cortar |

### 4. Estruturas-padrão

- **Regra de três mecânica**: "rigor, clareza e originalidade", "validação, replicação e aplicação". IA adora tricólon. **Quebre**: alterne 2 itens, 4 itens, ou parafraseie.
- **"Não apenas X, mas também Y"** ("not only X, but also Y") → trocar por "X e também Y" ou refazer
- **"X é mais que Y; é Z"** ("X is more than Y; it's Z") → reescrever em frase normal
- **Paralelismo excessivo**: três frases seguidas começando igual ("O método X. O método Y. O método Z.") → variar o começo

### 5. Hedging excessivo

IA hedga demais por treinamento em "ser cauteloso":
- "pode potencialmente" → "pode" ou "potencialmente" (um só)
- "talvez possa" → "pode"
- "parece sugerir que" → "sugere que" ou "indica que"
- "é possível que possa" → reescrever
- "tende a possivelmente" → reescrever

> A força da afirmação deve corresponder à força dos dados — não calibre por timidez.

### 6. Aberturas e fechamentos clichê

**Aberturas**:
- "Nos últimos anos..."
- "Com o advento de..."
- "Em um mundo cada vez mais..."
- "Diante da crescente complexidade de..."

**Fechamentos**:
- "Em conclusão,"
- "Como pôde ser observado,"
- "Em última análise,"
- "Em última instância,"

→ **Substituir** por entrada/saída específica do tema.

---

## 🚩 CATÁLOGO DE VÍCIOS — INGLÊS

### 1. Vocabulário-marcador (high signal)

Lista curta dos delatores mais agressivos em detectores de IA:

- **"delve into"** → "examine", "analyze", "investigate"
- **"tapestry"** ("rich tapestry of") → reescrever sem metáfora
- **"navigate"** ("navigate the challenges") → "address", "handle"
- **"realm"** ("in the realm of") → "in the field of" ou cortar
- **"landscape"** ("the landscape of AI") → "field", "area"
- **"intricate"** → "complex" + justificar
- **"nuanced"** → checar; muitas vezes vazio
- **"robust"** (não-técnico) → "consistent", "reliable"
- **"leverage"** (verbo) → "use", "apply"
- **"facilitate"** → "enable", "allow"
- **"underscore"** ("underscore the importance") → "show", "highlight"
- **"showcase"** (verbo, contexto não-marketing) → "show", "demonstrate"
- **"embark on a journey"** → cortar metáfora
- **"shed light on"** → "explain", "clarify"
- **"a testament to"** → reescrever
- **"in today's fast-paced world"** → deletar frase inteira
- **"the fascinating world of"** → deletar
- **"it's important to note that"** → deletar; o ponto fala por si
- **"it's worth mentioning that"** → deletar
- **"pivotal role"** / **"crucial role"** → "key role" ou específico

### 2. Transições genéricas

- **"Furthermore,"** / **"Moreover,"** / **"Additionally,"** em excesso → contextualizar ou cortar
- **"In conclusion,"** / **"To conclude,"** → cortar; comece pela conclusão direta
- **"In essence,"** → cortar
- **"It's not just X, it's Y"** padrão → reescrever
- **"Whether X or Y, Z"** padrão → reescrever

### 3. Pontuação

- **Em-dash (—) em excesso** — máximo 1–2 por parágrafo. IA usa para tudo.
- **Oxford comma inconsistente** — escolher um padrão (Elsevier prefere, IEEE varia).
- **Aspas em termos comuns** ("AI", "model") → remover.

### 4. Estruturas-padrão

- **Tricólon mecânico**: "rigor, clarity, and originality" — alterne 2 ou 4 itens.
- **"It's not just X — it's Y"** → reescrever sem o padrão.
- **Listas de 3 começando com gerúndio ("Doing X, doing Y, doing Z")** → variar.

---

## 🔍 PROCEDIMENTO DE AUDITORIA

### Passo 1: Estatísticas iniciais
Conte no texto recebido:
- Nº de travessões/em-dashes (—)
- Nº de "Furthermore", "Moreover", "Additionally" (EN) ou "Ademais", "Outrossim", "Vale ressaltar" (PT)
- Nº de "delve", "tapestry", "navigate", "intricate", "nuanced", "robust", "leverage" (EN)
- Nº de tricólons (listas de exatamente 3 itens)
- Comprimento médio de frase (alvo: variação 8–35 palavras; suspeita se média ≈18–22 com baixo desvio)

Apresente ao usuário um **diagnóstico inicial** com os números antes de reescrever.

### Passo 2: Verificação de hallucinations
Use a pasta de PDFs:
- Para cada **citação** no texto, verificar se há PDF correspondente
- Para cada **número/estatística** afirmada, checar fonte
- Para cada **termo técnico** específico (siglas, métricas, normas tipo "ISO/IEC 42001"), confirmar nos PDFs

Marcar com 🚨 qualquer claim sem fonte verificável.

### Passo 3: Reescrita guiada
Para cada vício detectado:
- Apresente a frase original
- Apresente 1–2 reescritas humanas
- Justifique a mudança
- Aguarde aprovação OU aplique se o usuário pediu modo autônomo

### Passo 4: Variação sintática
Após limpar vícios pontuais, verificar:
- Há 5+ frases seguidas com mesmo comprimento? → quebrar
- Há 3+ parágrafos seguidos começando igual ("The method...", "The results...") → variar
- Há voz passiva em mais de 30% das frases? → ativar onde fizer sentido

### Passo 5: Relatório final
Entregar:
- Texto reescrito
- Tabela de mudanças (vício → substituição → contagem)
- Estatísticas pós-limpeza vs pré-limpeza
- Lista de claims marcados como sem fonte (🚨) para o usuário decidir

---

## ✅ CHECKLIST DE LIMPEZA

Antes de declarar o texto limpo:

### Pontuação
- [ ] Travessões/em-dashes ≤ 1–2 por parágrafo
- [ ] Sem aspas em termos comuns
- [ ] Reticências apenas onde realmente cabem

### Vocabulário (PT)
- [ ] Sem "vale ressaltar", "é importante notar", "é importante destacar"
- [ ] Sem "outrossim", "ademais" (em excesso), "diante do exposto"
- [ ] "robusto"/"abrangente"/"profundo" só onde técnico-justificável

### Vocabulário (EN)
- [ ] Sem "delve", "tapestry", "realm", "landscape" (não-técnico), "embark"
- [ ] "robust", "nuanced", "intricate" só onde técnico
- [ ] Sem "it's important to note", "it's worth mentioning"

### Transições
- [ ] "Furthermore"/"Moreover"/"Additionally" e equivalentes PT só onde acrescentam (não decorativos)
- [ ] Sem "In conclusion"/"Em conclusão" (substituídos por conclusão direta)

### Estrutura
- [ ] Tricólons quebrados (alternar 2 ou 4 itens)
- [ ] Comprimento de frase varia (8–35 palavras)
- [ ] Parágrafos não iniciam todos igual
- [ ] Hedging na medida da força dos dados (ver tabela em `pesquisador-senior` ou `escritor-cientifico`)

### Integridade técnica
- [ ] Toda citação tem PDF correspondente na pasta de referência
- [ ] Todo número/estatística tem fonte verificável
- [ ] Termos técnicos (siglas, normas) batem com as fontes
- [ ] Take-Home Message preservada (idem em título, abstract, fim da introdução, conclusão)

---

## 🛠️ MODOS DE OPERAÇÃO

Pergunte ao usuário qual modo aplicar:

### Modo A — Auditoria apenas
Entrega só o **diagnóstico** (estatísticas + lista de vícios encontrados com localização). Útil quando o usuário quer revisar manualmente.

### Modo B — Reescrita guiada
Para cada vício, mostra original + 1–2 alternativas, aguarda OK do usuário antes de aplicar.

### Modo C — Reescrita autônoma
Aplica todas as substituições óbvias e entrega texto limpo + relatório do que mudou. Usuário revisa o resultado.

---

## ⚠️ NÃO FAÇA

- Não introduza erros de gramática "pra parecer humano". Texto humano de qualidade é gramaticalmente correto.
- Não remova precisão técnica para fugir de detector. Se o termo certo é "ISO/IEC 42001:2023", mantenha.
- Não substitua palavras por sinônimos aleatórios — mude a estrutura.
- Não invente reescritas que mudem o sentido do trecho.
- Não fabrique fontes para preencher claims marcados como 🚨 — sinalize ao usuário.
- Não force voz ativa onde a passiva é genuinamente melhor (descrever procedimento experimental, ex: "The samples were heated to 80°C").

---

## 🔗 SKILLS RELACIONADOS

- `pesquisador-senior` — princípios HUMANIZE para escrever sem vícios desde o início (uso preventivo)
- `revisor-critico` — revisão I-R-B-MB-E (conteúdo + metodologia)
- `editor-cientifico` — preparação final para submissão
- `escritor-cientifico` — para reescrita das passagens problemáticas
- `cientista` — persona tripla (escritor + revisor + editor)
