# Regras da *Production* e conformidade deste artigo

Conferido em 06/11/2026 em <https://prod.org.br/instructions> e na chamada da seção temática (<https://ijcieom.org/2027/call-for-papers.html>). **Refazer a conferência no dia do envio** (regra permanente do Heitor: nenhum artigo se fecha sem reler as regras do veículo).

**Revista:** *Production*, ABEPRO. ISSN 0103-6513 (impresso) e 1980-5411 (online). Scopus, SciELO, DOAJ. Sem taxa de submissão nem de publicação; CC BY 4.0; inglês; duplo-cego; fluxo contínuo. Submissão pelo ScholarOne: <https://mc04.manuscriptcentral.com/prod-scielo>.

**Base do texto (06/11/2026):** o artigo original (`ArtigoExemplo/Paper Training - 15 Nov 2025.pdf`), restaurado por pedido do Heitor ("não remover o que foi escrito"). Ver `PENDENCIAS.md`.

Legenda: **OK** = cumprido; **PENDENTE** = depende de conteúdo ou de decisão; **CONFERIR** = fazer no dia do envio.

## 1. Manuscrito

| Regra | Situação em 06/11/2026 |
|---|---|
| Artigo original ou revisão sistemática; não aceita *case reports* | OK no enquadramento: estudo de caso com métodos mistos, perguntas de pesquisa, desenho em três fases e ameaças à validade. "A Case Study on" saiu do título |
| Ordem: Abstract, Keywords, Introduction, Methods, Results, Discussions, Conclusions, References | OK. A revisão de literatura do original virou 1.1 a 1.5 |
| Seções numeradas a partir da Introduction | OK |
| 4.000 a 8.000 palavras, contando as referências (não há limite de páginas) | **PENDENTE:** 8.342 pelo `pdftotext`, sem os avisos vermelhos (06/11/2026, depois das correções da revisão). O número muda quando as 22 referências inexistentes forem resolvidas; se continuar acima, condensar 3.1 e 3.2 numa tabela (`PENDENCIAS.md`, seção 4). CONFERIR no Word |
| Título com até 15 palavras | OK: 14 (o título do original sem "A", "for" e "A Case Study on") |
| Resumo com até 250 palavras, nas cinco partes rotuladas | OK: cerca de 220, com o conteúdo do resumo original |
| 3 a 5 palavras-chave que não repitam o título | OK: training evaluation; AS9100; cost of quality; human factors; cleaner production |
| Arquivo .docx ou LaTeX; até 3 MB | OK: pacote LaTeX; PDF de prova com 1,9 MB e figuras com 1,7 MB |
| A4; margens de 2,5 cm; Times 12 (10 em tabelas e figuras); espaço 1,5; sem recuo; justificado; uma coluna | OK. Tabelas, legendas e notas em 10 pt (`\footnotesize`; até 06/11/2026 estavam em 10,95 pt) |
| Figuras no corpo, logo depois da primeira citação | OK (`[H]`) |
| Figuras em JPEG, com 300 dpi ou mais, legenda e fonte | Figs. 1 a 5: OK (400 dpi; setas, rótulos e cores corrigidos em 06/11/2026, fiéis ao original). Figs. 6 a 8: imagens **originais** com 115, 137 e 164 dpi. **PENDENTE:** gráfico ou planilha de origem |
| Tabelas como tabelas, não como imagem; abreviaturas e fonte abaixo de cada tabela e figura | OK |
| Sem notas de rodapé; equações numeradas; SI; ponto decimal | OK |
| APA, com todos os autores na lista, DOI quando houver e sem fontes de difícil acesso | Estilo OK. **PENDENTE:** 22 referências do original não existem (bases e web; em vermelho); 1 citação do original sem entrada (ANAC, 2018); 6 frases citam fontes reais que não trazem o que o texto diz (avisos vermelhos) |
| Sem autores, afiliações nem copyright no arquivo | OK: sem bloco de autores; nome da empresa trocado no exemplo do gêmeo digital; o pacote recusa nomes dos autores, UCP, Petrópolis e GE no corpo. A autocitação em terceira pessoa "(Pereira et al., 2017)" é permitida |
| Declaração de ética com aprovação e consentimento, ou isenção justificada | **PENDENTE (D4):** o estudo tem participantes (questionários, entrevistas pareadas, grupo focal) |
| Conflito de interesse declarado | OK, sem nomes no manuscrito |
| Financiamento com a frase padrão | OK; confirmar com os autores |
| Declaração de uso de IA, se houve uso (regra 46) | Decisão dos autores (D7) |
| Sem preprint | OK |

## 2. Arquivos e passos do ScholarOne

| Item | Arquivo | Situação |
|---|---|---|
| Main Document | `submissao-scholarone/manuscript.tex` | PENDENTE: a versão de envio só é gerada sem nenhuma pendência. O rascunho (`--rascunho`) compila do zero só com `pdflatex`: 26 páginas, zero erros, nenhuma fonte Type 3 |
| Figuras | oito `.jpg` | Figs. 6 a 8 em baixa resolução (ver acima) |
| Carta de apresentação | `ENVIO-SCHOLARONE/02-cover-letter/cover-letter.txt` | Rascunho alinhado ao original; resolver os colchetes |
| Agreement form | `ENVIO-SCHOLARONE/03-formularios/latex/01-Agreement-form.pdf` | Preenchido com o título novo. Falta data, telefone e assinaturas. O formulário declara autorização do comitê de ética (D4) |
| Declaration of Conflict of Interest | `.../02-Conflict-of-Interest.pdf` | Preenchido; faltam assinaturas e datas |
| Open Science Compliance Form | `.../03-Open-Science-Compliance-Form.pdf` | Preenchido; faltam as duas escolhas de revisão aberta |
| Parecer do comitê de ética | "Supplemental File NOT for Review" | PENDENTE (D4) |

## 3. Seção temática (se D2 = temática)

- **Prazo:** 30/11/2026.
- **Calendário:** primeira decisão em 17/01/2027; decisão final em 21/04/2027.
- **Apresentação presencial obrigatória** no IJCIEOM, PUC-Rio, de 14 a 16/06/2027.
- **Tópicos da chamada em que o artigo se encaixa:** "Sustainability & social impact", "Human-centricity and organizational change", "Performance frameworks & interventions", "Empirical modelling, case research, mixed methods".
