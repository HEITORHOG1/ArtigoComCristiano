# Artigo Kirkpatrick: versão da *Production* (ABEPRO, SciELO)

Criada em 06/11/2026 a partir da versão JATM (`../artigo/`, congelada na tag git `jatm-r1-2026-05`). Plano: `../planejamento/003_migracao_production_scielo.md`. Molde de formato e de envio: kit do artigo B em `G:\Projetos\Dissertacao\001-Doutorado\artigos\Production-ABEPRO-secao-tematica-2027\` (copiado, nunca editado).

**Base do texto (desde 06/11/2026):** o **artigo original** (`../ArtigoExemplo/Paper Training - 15 Nov 2025.pdf`), restaurado inteiro no formato da revista, por pedido do Heitor ("não remover o que foi escrito"). Da versão JATM ficou só o que não contradiz o original.

**Estado (06/11/2026, depois da rodada das skills):** formato da revista completo e testado; conteúdo com 30 avisos em vermelho no PDF. O principal: 22 referências do original não existem (bases e web), e o texto passou de 8.000 palavras. Ver `PENDENCIAS.md` e `RELATORIO-SKILLS-2026-11-06.md`. **Não enviar** antes de zerar `PENDENCIAS.md`.

## Arquivos

| Caminho | O que é |
|---|---|
| `main.tex` | Preâmbulo no formato da revista e `\input` das seções; sem texto |
| `secoes/00-resumo.tex` a `06-declaracoes.tex` | Abstract estruturado e palavras-chave; Introduction; Methods; Results; Discussions; Conclusions; Declarations |
| `tabelas/tab1-results-by-level.tex`, `tab3-limitations.tex` | Tabela 1 (resultados por nível, só com números do original) e Tabela 2 (limitações) |
| `tabelas/_jatm-NAO-USAR/` | Tabelas da versão JATM com números que não estão no original (guardadas, fora do texto) |
| `figs-tikz/` | TikZ do modelo conceitual e dos quatro diagramas (redesenho fiel das Figs. 4 a 7 do original) |
| `figs-tikz/_reconstrucoes-jatm-NAO-USAR/` | Gráficos "reconstruídos" da versão JATM, com valores diferentes dos originais (guardados, fora do texto) |
| `figuras-originais/` | Os três gráficos de dados do original (Figs. 8 a 10), extraídos do PDF sem alteração |
| `figuras/` | Oito JPEG gerados (não editar à mão) |
| `refs.bib` | Todas as referências do original. 15 conferidas: as 11 de antes, Yücel & Ayvaz e três citações do original que não tinham entrada. 22 inexistentes, mantidas com os dados do original e marcadas (`keywords = {naolocalizada}`, saem em vermelho) |
| `verificacao-referencias/` | Script e resultado da busca de cada referência do original no Crossref e no OpenAlex (06/11/2026); a busca na web está no `RELATORIO-SKILLS-2026-11-06.md` |
| `referencias-pdf/` | PDFs das fontes conferidas, que são o pré-requisito das skills: 5 abertos (FAA, EASA, Boyd & Stolzer, Leveson, Shunko). Faltam os 6 livros e artigos pagos. Os PDFs ficam fora do git (`.gitignore` da pasta) |
| `scripts/auditar_estilo.py` | Diagnóstico de estilo por seção (tamanho das frases, marcadores, voz passiva); só lê |
| `RELATORIO-SKILLS-2026-11-06.md` | O que cada skill fez na rodada de 06/11/2026, com antes e depois |
| `scripts/gerar_figuras.py` | TikZ → JPEG a 400 dpi; imagens originais → JPEG sem alteração |
| `scripts/pacote_scholarone.py` | Gera o pacote de envio (arquivo único, APA escrita no `.tex`, só `pdflatex`) |
| `scripts/csl/apa.csl` | Estilo APA 7 usado pelo pandoc (licença CC BY-SA 3.0) |
| `ENVIO-SCHOLARONE/` | Carta, formulários e dados para digitar no sistema |
| `REGRAS-DO-VEICULO.md` | Checklist das regras da revista |
| `PENDENCIAS.md` | O que falta, por fase e por responsável |

Mapa do original para esta versão:
- **Introduction** = 1 Introduction + 2.1 a 2.5 Literature Review (como 1.1 a 1.6; o parágrafo das lacunas ganhou subtítulo próprio, 1.5);
- **Methods** = 3 Methodology, mais a definição de *training failure*, o modelo de custo e as ameaças à validade (da versão JATM);
- **Results** = 4.1 a 4.4 e o impacto no custo da qualidade;
- **Discussions** = Discussion of Results, mais as implicações gerenciais e a agenda regulatória (da versão JATM);
- **Conclusions** = 10 Conclusion, mais a tabela de limitações (da versão JATM).

Saíram highlights, resumo gráfico, bloco de autores, CRediT e a declaração de IA do JATM.

## Compilar

```text
python scripts/gerar_figuras.py            # so quando mudar alguma figura em figs-tikz/
pdflatex main && biber main && pdflatex main && pdflatex main
```

Depois de cada compilação, as checagens do `CLAUDE.md` da raiz: `pdftotext main.pdf -` sem ligaduras quebradas, sem `??`, sem glifo corrompido. (A palavra "findings" casa com o padrão "ndings" do `CLAUDE.md`: é falso positivo.) Fontes: `pdffonts main.pdf` só com Type 1. O ajuste de fontes do `CLAUDE.md` vale para o `cas-dc`; aqui a Times vem do `newtx`.

## Gerar o pacote de envio

```text
python scripts/pacote_scholarone.py --rascunho   # teste, aceita pendencias; grava em submissao-scholarone-RASCUNHO/
python scripts/pacote_scholarone.py              # versao de envio; recusa \todo e \refpendente
```

O pacote existe porque o conversor do ScholarOne usa TeX Live antigo, não roda `biber` e não acha arquivos em subpastas: o script junta tudo num `manuscript.tex`, apaga os comentários, escreve citações e referências em APA 7 no próprio arquivo, troca as fontes por Type 1 do TeX Live 2012, copia as figuras para a mesma pasta, compila numa pasta limpa só com `pdflatex`, compara com o `main.pdf` e recusa nomes que identifiquem os autores. As diferenças que ele lista na comparação vêm da extração de texto (índices matemáticos e números de página em outra ordem com a `mathptmx`), não do conteúdo.

Rodada de 06/11/2026, depois da rodada das skills (`--rascunho`): 27 páginas, zero erros, nenhuma fonte Type 3. A versão de envio recusa, como deve, porque há 21 referências inexistentes citadas no texto. O script agora apaga da pasta de saída as figuras de rodadas antigas.

## Enviar

Roteiro do sistema: partes B e C do `PASSO-A-PASSO-SUBMISSAO.md` do artigo B (mesmo sistema, mesmos passos). O que sobe:

| Arquivo | Designação no ScholarOne |
|---|---|
| `submissao-scholarone/manuscript.tex` | Main Document |
| oito `.jpg` de `submissao-scholarone/` | arquivo suplementar de LaTeX (ou "Image") |
| `ENVIO-SCHOLARONE/03-formularios/latex/01-Agreement-form.pdf`, assinado | Agreement form |
| `.../02-Conflict-of-Interest.pdf`, assinado | Declaration of Conflict of Interest |
| `.../03-Open-Science-Compliance-Form.pdf` | Open Science Compliance Form |
| parecer do comitê de ética (D4) | Supplemental File NOT for Review |
| texto de `ENVIO-SCHOLARONE/02-cover-letter/cover-letter.txt` | campo Cover Letter |

Dados para digitar: `ENVIO-SCHOLARONE/00-dados-para-digitar.txt`. Conferir "View PDF Proof" contra `submissao-scholarone/manuscript.pdf`. Se trocar o `manuscript.tex` depois, apagar todos os arquivos do pacote no sistema e subir de novo.

Os formulários assinados são do Heitor e do Cristiano (dois autores). Assinatura pelo gov.br (nível prata ou ouro), os dois no mesmo PDF, um depois do outro; conferir em <https://validar.iti.gov.br>.
