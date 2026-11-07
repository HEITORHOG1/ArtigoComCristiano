# -*- coding: utf-8 -*-
"""
pacote_scholarone.py
Gera o pacote LaTeX de submissao da Production no ScholarOne a partir do main.tex desta pasta.
Copiado do artigo B (Production-ABEPRO-secao-tematica-2027) e adaptado em 06/11/2026 ao artigo
Kirkpatrick: oito figuras, refs.bib unico, sem a chave versaocega (nao ha dissertacao a
anonimizar), sem xurl (nao existe no TeX Live 2012), pasta temporaria dentro do projeto (o
%TEMP% do Windows vem com caminho curto e o pdflatex nao grava nele) e modo --rascunho.
Decisao do autor (25/10/2026): submeter sempre em LaTeX. O guia oficial do ScholarOne para LaTeX
(Clarivate, "Author LaTeX File Upload Guide", 2017) diz que o conversor usa pdfTeX 1.40.13 do
TeX Live 2012, pede todos os arquivos numa pasta so, sem subpastas, e manda colar a bibliografia
no .tex quando o .bib falha. Por isso o pacote:
  1. junta main.tex, secoes/ e dados/tabelas/ num arquivo so (manuscript.tex);
  2. apaga todos os comentarios, que citam a UCP, a dissertacao e o autor (versao cega);
  3. troca biblatex-apa + biber por texto fixo: o pandoc (citeproc + scripts/csl/apa.csl, APA 7)
     formata cada citacao e a lista de referencias, que entram escritas no proprio .tex;
  4. troca newtxtext/newtxmath por mathptmx e helvet (Times e Helvetica Type 1 de qualquer
     TeX Live) e poe os URLs na fonte do texto, sem fonte bitmap (Type 3);
  5. converte os caracteres nao ASCII em comandos LaTeX (por exemplo, c cedilha vira \\c{c});
  6. copia as figuras JPEG para a mesma pasta, sem caminho;
  7. compila o pacote numa pasta limpa so com pdflatex e compara o texto com o main.pdf.
Nao recalcula nada: texto e numeros sao os do main.tex.
Uso: python scripts/pacote_scholarone.py   (antes, compilar o main.tex para a comparacao)
     python scripts/pacote_scholarone.py --rascunho
        aceita os marcadores de pendencia (todo, refpendente) e grava em
        submissao-scholarone-RASCUNHO/; serve so para testar o conversor, NUNCA para enviar.
"""
from __future__ import annotations

import difflib
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
SAIDA = RAIZ / "submissao-scholarone"
CSL = AQUI / "csl" / "apa.csl"
NOME = "manuscript"
FIGURAS = ["fig1-conceptual-model.jpg", "fig2-as9100.jpg", "fig3-regulation.jpg",
           "fig4-process-original.jpg", "fig5-process-redesigned.jpg", "fig6-reaction-scores.jpg",
           "fig7-final-grades.jpg", "fig8-customer-satisfaction.jpg"]
BIBS_CEGA = ["refs.bib"]
RASCUNHO = "--rascunho" in sys.argv
if RASCUNHO:
    SAIDA = RAIZ / "submissao-scholarone-RASCUNHO"

# Lista de referencias com recuo pendente de 0,5 polegada (APA 7).
LISTA_INICIO = ("\\section*{References}\n"
                "\\begin{list}{}{\\setlength{\\leftmargin}{0.5in}\\setlength{\\itemindent}{-0.5in}"
                "\\setlength{\\itemsep}{0pt}\\setlength{\\parsep}{0pt}}\n")
LISTA_FIM = "\\end{list}\n"

ACENTOS = {
    "á": "\\'a", "à": "\\`a", "â": "\\^a", "ã": "\\~a", "ä": '\\"a',
    "é": "\\'e", "è": "\\`e", "ê": "\\^e", "ë": '\\"e',
    "í": "\\'{\\i}", "î": "\\^{\\i}", "ï": '\\"{\\i}',
    "ó": "\\'o", "ò": "\\`o", "ô": "\\^o", "õ": "\\~o", "ö": '\\"o',
    "ú": "\\'u", "ù": "\\`u", "û": "\\^u", "ü": '\\"u',
    "ç": "\\c{c}", "ñ": "\\~n", "ý": "\\'y",
    "Á": "\\'A", "À": "\\`A", "Â": "\\^A", "Ã": "\\~A", "É": "\\'E", "Ê": "\\^E",
    "Í": "\\'I", "Ó": "\\'O", "Ô": "\\^O", "Õ": "\\~O", "Ú": "\\'U", "Ü": '\\"U',
    "Ç": "\\c{C}", "Ñ": "\\~N",
    "ą": "\\k{a}", "ę": "\\k{e}", "ł": "{\\l}", "Ł": "{\\L}", "ś": "\\'s", "Ś": "\\'S",
    "ź": "\\'z", "ż": "\\.z", "Ż": "\\.Z", "ń": "\\'n", "ć": "\\'c", "ő": "\\H{o}", "ű": "\\H{u}",
    "ğ": "\\u{g}", "Ğ": "\\u{G}", "ı": "{\\i}", "İ": "\\.I", "ş": "\\c{s}", "Ş": "\\c{S}",
    "–": "--", "—": "---", "’": "'", "‘": "`", "“": "``", "”": "''", "\u00a0": "~", "…": "\\ldots{}",
}

# Nomes que nao podem aparecer no manuscrito cego fora da lista de referencias. "Pereira" saiu da
# lista em 06/11/2026: a autocitacao em terceira pessoa "(Pereira et al., 2017)" e permitida no
# duplo-cego; o nome completo ("Cristiano") continua proibido.
IDENTIFICADORES = ["UCP", "Petr", "Heitor", "Cristiano", "Gon\\c", "GE Aviation",
                   "General Electric", "Celma", "Cat\\'olica", "Catolica", "Claude"]
if not RASCUNHO:
    IDENTIFICADORES += ["TODO"]


def chaves_nao_localizadas() -> set[str]:
    """Chaves do refs.bib com keywords = {naolocalizada}: referencias do artigo original que nao
    foram achadas no Crossref nem no OpenAlex (06/11/2026). A versao de envio recusa todas; o
    rascunho as imprime em vermelho."""
    texto = (RAIZ / "refs.bib").read_text(encoding="utf-8")
    nl = set()
    for bloco in re.split(r"(?m)^(?=@)", texto):
        m = re.match(r"@\w+\{([^,]+),", bloco)
        if m and re.search(r"(?m)^\s*keywords\s*=\s*\{[^}]*naolocalizada", bloco):
            nl.add(m.group(1).strip())
    return nl


NAOLOC = chaves_nao_localizadas()


def primeiro_pct(linha: str) -> int | None:
    """Posicao do primeiro % que abre comentario (ignora \\% e outros escapes)."""
    i = 0
    while i < len(linha):
        if linha[i] == "\\":
            i += 2
            continue
        if linha[i] == "%":
            return i
        i += 1
    return None


def sem_comentarios(texto: str) -> str:
    """Apaga comentarios sem mudar o que o TeX compoe: linha so de comentario sai inteira;
    comentario no fim de linha vira um % sozinho, que continua engolindo a quebra de linha."""
    saida = []
    for linha in texto.split("\n"):
        pos = primeiro_pct(linha)
        if pos is None:
            saida.append(linha)
        elif linha[:pos].strip():
            saida.append(linha[:pos] + "%")
    return "\n".join(saida)


def achatar(texto: str) -> str:
    """Troca cada \\input{arquivo} pelo conteudo, sem comentarios (caminhos relativos a RAIZ)."""
    def troca(m):
        nome = m.group(1).strip()
        arq = RAIZ / (nome if nome.endswith(".tex") else nome + ".tex")
        return achatar(sem_comentarios(arq.read_text(encoding="utf-8"))).rstrip("\n")
    return re.sub(r"\\input\{([^}]*)\}", troca, texto)


def itens_citados(texto: str) -> list[tuple[str, tuple[str, ...]]]:
    itens = []
    for m in re.finditer(r"\\(parencite|textcite|cite)\{([^}]*)\}", texto):
        item = (m.group(1), tuple(k.strip() for k in m.group(2).split(",")))
        if item not in itens:
            itens.append(item)
    return itens


def limpar_bib(texto: str) -> str:
    """Copia do .bib para o pandoc. O citeproc junta organization e publisher na editora e
    imprimia "NIST; NIST." e "ISO/IEC; ISO."; o biblatex-apa omite a organizacao (que repete o
    autor) e a editora igual ao autor. Aqui se faz o mesmo antes de chamar o pandoc.
    (A troca "Ji-guang" -> "Ji-Guang", feita aqui ate 26/10/2026, passou para o .bib de origem
    em 29/10/2026: as duas saidas imprimem J.-G.)"""
    blocos = []
    for bloco in re.split(r"(?m)^(?=@)", texto):
        bloco = re.sub(r"(?m)^\s*(organization|org-short)\s*=.*\n", "", bloco)
        autor = re.search(r"(?m)^\s*author\s*=\s*\{\{?([^{}]*)\}?\}", bloco)
        editora = re.search(r"(?m)^\s*publisher\s*=\s*\{([^{}]*)\}", bloco)
        if autor and editora and autor.group(1).strip() == editora.group(1).strip():
            bloco = re.sub(r"(?m)^\s*publisher\s*=.*\n", "", bloco)
        blocos.append(bloco)
    return "".join(blocos)


def formatar_com_pandoc(itens, bibs, tmp: Path):
    """Formata cada citacao e a lista de referencias em APA 7 (pandoc citeproc + apa.csl)."""
    md = ["---", "link-citations: false", "lang: en-US", "---", ""]
    for i, (cmd, chaves) in enumerate(itens):
        if cmd == "textcite":
            if len(chaves) != 1:
                sys.exit(f"\\textcite com mais de uma chave nao previsto: {chaves}")
            md += [f"CITA{i:03d}: @{chaves[0]}", ""]
        else:
            md += [f"CITA{i:03d}: [" + "; ".join("@" + k for k in chaves) + "]", ""]
    md += ["::: {#refs}", ":::", ""]
    entrada = tmp / "citacoes.md"
    entrada.write_text("\n".join(md), encoding="utf-8")
    cmd = ["pandoc", str(entrada), "-f", "markdown", "-t", "latex", "--wrap=none",
           "--citeproc", "--csl", str(CSL)]
    for b in bibs:
        copia = tmp / b
        copia.write_text(limpar_bib((RAIZ / b).read_text(encoding="utf-8")), encoding="utf-8")
        cmd += ["--bibliography", str(copia)]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0 or "not found" in r.stderr:
        sys.exit("pandoc falhou: " + r.stderr)
    saida = r.stdout
    # sem link-citations nao deveria haver \citeproc{}{}, mas se houver fica so o texto
    saida = re.sub(r"\\citeproc\{[^}]*\}\{([^}]*)\}", r"\1", saida)
    textos = {}
    for i, (cmd_cit, chaves) in enumerate(itens):
        m = re.search(rf"^CITA{i:03d}: (.*)$", saida, re.M)
        if not m:
            sys.exit(f"citacao {i} nao encontrada na saida do pandoc")
        t = m.group(1).strip()
        if cmd_cit == "textcite":
            t = t.replace(" \\& ", " and ")  # APA 7: "and" na citacao narrativa, "&" entre parenteses
        elif cmd_cit == "cite":
            assert t.startswith("(") and t.endswith(")"), t
            t = t[1:-1]  # \cite do biblatex-apa: autor e ano, sem parenteses
        if RASCUNHO and any(k in NAOLOC for k in chaves):
            t = "\\textcolor{red}{" + t + "}"  # como no main.pdf: referencia nao localizada em vermelho
        textos[(cmd_cit, chaves)] = t
    bloco = re.search(r"\\begin\{CSLReferences\}\{[^}]*\}\{[^}]*\}(.*?)\\end\{CSLReferences\}", saida, re.S)
    if not bloco:
        sys.exit("lista de referencias nao encontrada na saida do pandoc")
    pares = re.findall(r"\\bibitem\[\\citeproctext\]\{ref-([^}]*)\}(.*?)(?=\\bibitem\[\\citeproctext\]|\Z)",
                       bloco.group(1), re.S)
    if not pares:
        sys.exit("entradas da lista de referencias nao encontradas na saida do pandoc")
    entradas = []
    for chave, e in pares:
        e = e.strip()
        if chave in NAOLOC:  # so acontece no rascunho; a versao de envio recusa antes
            e = "\\textcolor{red}{" + e + " [NOT FOUND in Crossref, OpenAlex or a web search on 6 Nov 2026]}"
        entradas.append(e)
    # iniciais presas umas as outras (espaco inseparavel, que para_ascii() troca por ~): o pandoc
    # deixava "Li, G." numa linha e "P." na seguinte; o biblatex-apa ja faz isso no main.pdf
    entradas = [re.sub(r"\b([A-Z]\.) (?=[A-Z]\.)", "\\1\u00a0", e) for e in entradas]
    return textos, entradas


def ajustar_preambulo(t: str) -> str:
    # mathptmx + helvet: Times e Helvetica Type 1 de qualquer TeX Live (newtx pode nao existir no
    # TeX Live 2012); URL na fonte do texto, como no biblatex-apa (a fonte de maquina de escrever
    # do TeX Live sem cm-super sai em bitmap, Type 3); emergencystretch absorve a pequena diferenca
    # de metrica entre as duas Times, que estourava duas linhas.
    for velho, novo in [("\\usepackage{newtxtext,newtxmath}",
                         "\\usepackage{mathptmx}\n\\usepackage[scaled=0.92]{helvet}"),
                        ("\\usepackage[hidelinks]{hyperref}",
                         "\\PassOptionsToPackage{hyphens}{url}\n\\usepackage[hidelinks]{hyperref}\n"
                         "\\urlstyle{same}\n\\setlength{\\emergencystretch}{1.5em}"),
                        ("\\usepackage{csquotes}\n", ""),
                        ("\\graphicspath{{figuras/}}\n", ""),
                        ("\\usepackage{xurl} %\n", "")] + (
                       [] if RASCUNHO else [("\\newcommand{\\todo}[1]{\\textcolor{red}{[TODO: #1]}}\n", "")]):
        if velho not in t:
            sys.exit(f"trecho esperado do preambulo nao encontrado: {velho!r}")
        t = t.replace(velho, novo)
    t = re.sub(r"\\usepackage\[[^\]]*\]\{biblatex\}\n?", "", t)
    t = re.sub(r"\\DeclareLanguageMapping\{[^}]*\}\{[^}]*\}\n?", "", t)
    t = re.sub(r"\\ifdefined\\versaocega\s*\\addbibresource\{[^}]*\}\s*\\else\s*\\addbibresource\{[^}]*\}\s*\\fi\n?", "", t)
    t = re.sub(r"\\addbibresource\{[^}]*\}\n?", "", t)
    # ganchos de cor do biblatex (referencias nao localizadas em vermelho) e ajuste do xurl: nao
    # existem sem biblatex e xurl no TeX Live 2012 do ScholarOne
    t = re.sub(r"(?m)^\\(AtEveryCitekey|AtEveryBibitem)\{.*\}\s*%?\n", "", t)
    t = re.sub(r"(?m)^\\Urlmuskip=.*\n", "", t)
    t = t.replace("\\notafonte", "\\sourcenote")  # nome neutro no fonte que vai para os revisores
    return t


def para_ascii(t: str) -> str:
    t = t.replace("ı́", "í")  # o pandoc le {\'\i} do .bib como i sem pingo + acento combinante
    t = unicodedata.normalize("NFC", t)
    t = "".join(ACENTOS.get(c, c) for c in t)
    resto = sorted({c for c in t if ord(c) > 127})
    if resto:
        sys.exit(f"caracteres sem conversao para LaTeX: {resto}")
    return t


def compilar(pasta: Path) -> dict:
    for _ in range(2):  # duas passadas: referencias cruzadas das equacoes, tabelas e figuras
        subprocess.run(["pdflatex", "-interaction=nonstopmode", f"{NOME}.tex"], cwd=str(pasta),
                       capture_output=True, text=True)
    log = (pasta / f"{NOME}.log").read_text(encoding="utf-8", errors="replace")
    pdf = pasta / f"{NOME}.pdf"
    info = {"erros": [l for l in log.splitlines() if l.startswith("!")],
            "undefined": len(re.findall(r"undefined", log, re.I)),
            "overfull": len(re.findall(r"Overfull", log)),
            "paginas": None, "type3": None}
    if pdf.exists():
        p = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
        info["paginas"] = int(re.search(r"Pages:\s+(\d+)", p).group(1))
        f = subprocess.run(["pdffonts", str(pdf)], capture_output=True, text=True).stdout
        info["type3"] = sum(1 for l in f.splitlines() if "Type 3" in l)
    return info


def palavras_do_pdf(pdf: Path) -> list[str]:
    t = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, text=True,
                       encoding="utf-8", errors="replace").stdout
    t = re.sub(r"-\n(?=[a-z])", "", t)  # junta palavras hifenizadas no fim da linha
    return t.split()


def main():
    principal = sem_comentarios((RAIZ / "main.tex").read_text(encoding="utf-8"))
    if "\\author" in principal or "\\maketitle" in principal:
        sys.exit("main.tex com bloco de autores: o pacote de submissao tem de ser a versao cega")
    t = achatar(principal)
    itens = itens_citados(t)
    citadas_nl = sorted({k for _, chaves in itens for k in chaves if k in NAOLOC})
    if citadas_nl:
        print(f"referencias nao localizadas ainda citadas ({len(citadas_nl)}): {', '.join(citadas_nl)}")
        if not RASCUNHO:
            sys.exit("a versao de envio nao pode citar referencia nao localizada (refs.bib, keywords = naolocalizada)")
    with tempfile.TemporaryDirectory(dir=RAIZ, prefix=".tmp-") as tmp:
        textos, entradas = formatar_com_pandoc(itens, BIBS_CEGA, Path(tmp))
    t = re.sub(r"\\(parencite|textcite|cite)\{([^}]*)\}",
               lambda m: textos[(m.group(1), tuple(k.strip() for k in m.group(2).split(",")))], t)
    t = ajustar_preambulo(t)
    lista = LISTA_INICIO + "\n".join("\\item " + e for e in entradas) + "\n" + LISTA_FIM
    t, n = re.subn(r"\\printbibliography(\[[^\]]*\])?\n?", lambda m: lista, t)
    if n != 1:
        sys.exit("\\printbibliography nao encontrado")
    t = re.sub(r"\n{3,}", "\n\n", t)
    t = para_ascii(t)
    proibidos = ["\\parencite", "\\textcite", "\\cite{", "biblatex", "figuras/"]
    if not RASCUNHO:
        proibidos += ["\\todo{", "\\citepend{"]
    for proibido in proibidos:
        if proibido in t:
            sys.exit(f"sobrou {proibido!r} no manuscrito")
    corpo = t.split("\\section*{References}")[0]
    achados = [(p, corpo[max(0, m.start() - 50):m.end() + 50].replace("\n", " "))
               for p in IDENTIFICADORES for m in re.finditer(re.escape(p), corpo)]
    if achados:
        for p, ctx in achados:
            print(f"ATENCAO, possivel identificacao ({p}): ...{ctx}...")
        sys.exit("o manuscrito cego tem nomes que identificam os autores")

    SAIDA.mkdir(exist_ok=True)
    for velho in SAIDA.glob("*.jpg"):  # figuras de rodadas antigas (nomes que mudaram) nao vao para o pacote
        if velho.name not in FIGURAS:
            velho.unlink()
    (SAIDA / f"{NOME}.tex").write_text(t, encoding="ascii", newline="\n")
    for fig in FIGURAS:
        shutil.copy2(RAIZ / "figuras" / fig, SAIDA / fig)
    print(f"pacote: {SAIDA.name}/{NOME}.tex + {', '.join(FIGURAS)}")
    print(f"citacoes formatadas: {len(itens)} | referencias: {len(entradas)}")

    with tempfile.TemporaryDirectory(dir=RAIZ, prefix=".tmp-") as tmp:
        limpa = Path(tmp)
        for arq in [f"{NOME}.tex"] + FIGURAS:
            shutil.copy2(SAIDA / arq, limpa / arq)
        info = compilar(limpa)
        if (limpa / f"{NOME}.pdf").exists():
            shutil.copy2(limpa / f"{NOME}.pdf", SAIDA / f"{NOME}.pdf")
    print(f"compilacao limpa (so pdflatex): erros {len(info['erros'])} | undefined {info['undefined']} | "
          f"overfull {info['overfull']} | paginas {info['paginas']} | Type 3 {info['type3']}")
    for e in info["erros"][:5]:
        print("  ", e)
    if info["erros"] or info["paginas"] is None:
        sys.exit("o pacote nao compilou")

    original = RAIZ / "main.pdf"
    if original.exists():
        a, b = palavras_do_pdf(original), palavras_do_pdf(SAIDA / f"{NOME}.pdf")
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        difs = [op for op in sm.get_opcodes() if op[0] != "equal"]
        print(f"comparacao com main.pdf: {len(a)} x {len(b)} palavras | trechos diferentes: {len(difs)}")
        for tag, i1, i2, j1, j2 in difs[:30]:
            print(f"   main.pdf: {' '.join(a[i1:i2])[:90]!r}  |  pacote: {' '.join(b[j1:j2])[:90]!r}")
    print("pronto")


if __name__ == "__main__":
    main()
