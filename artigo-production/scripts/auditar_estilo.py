"""Diagnostico de estilo do manuscrito (passo 1 da skill anti-vicios-ia).

Conta, por arquivo e no total: travessoes, transicoes genericas, vocabulario-marcador,
listas de exatamente tres itens (aproximado), comprimento de frase, sequencias de frases
de tamanho parecido, paragrafos seguidos com a mesma primeira palavra e voz passiva
(aproximada). So le os arquivos; nao altera nada.

Uso (da pasta artigo-production):
    python scripts/auditar_estilo.py            # resumo por arquivo e total
    python scripts/auditar_estilo.py --detalhe  # lista cada ocorrencia com arquivo:linha
"""
import re
import statistics
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ARQUIVOS = sorted((RAIZ / "secoes").glob("*.tex")) + sorted((RAIZ / "tabelas").glob("*.tex"))

TRANSICOES = ["Furthermore", "Moreover", "Additionally", "In addition", "In conclusion",
              "To conclude", "In essence", "In summary", "Overall", "Ultimately", "Notably",
              "Importantly", "Crucially", "Indeed", "Thus", "Hence", "Consequently",
              "Therefore", "However", "Nevertheless", "In this context", "In this sense",
              "In this regard"]
MARCADORES = ["delve", "tapestry", "navigat", "realm", "landscape", "intricate", "nuanced",
              "robust", "leverag", "facilitat", "underscor", "showcas", "embark", "shed light",
              "testament", "pivotal", "crucial", "important to note", "worth noting",
              "worth mentioning", "holistic", "seamless", "foster", "bolster", "comprehensive",
              "multifaceted", "paradigm", "synerg", "not only", "serves as", "transformative",
              "cutting-edge", "unlock", "empower", "streamlin", "harness", "elevat", "vital",
              "critical", "significant", "essential", "key role", "crucial role", "ensur",
              "enhanc", "optimi", "valuable insights", "plays a", "in today", "ever-",
              "a wide range", "various", "numerous", "dynamic", "innovative", "novel"]
MACROS = {"AS": "AS9100", "ICAO": "ICAO", "FAA": "FAA", "EASA": "EASA", "ANAC": "ANAC",
          "SMS": "SMS", "MRO": "MRO", "ERP": "ERP", "LMS": "LMS", "CAA": "CAA", "ROI": "ROI",
          "ESG": "ESG", "CoQ": "CoQ"}
ABREV = ["e.g.", "i.e.", "et al.", "Fig.", "Figs.", "Eq.", "Eqs.", "No.", "vs.", "approx.",
         "U.S.", "Rev.", "Sect.", "cf.", "p.", "pp."]


def sem_comentarios(linha):
    return re.sub(r"(?<!\\)%.*", "", linha)


def tirar_comando_com_chaves(texto, nome, troca=""):
    """Remove \\nome{...} com chaves aninhadas (para \\todo e \\citepend)."""
    saida, i, alvo = [], 0, "\\" + nome + "{"
    while True:
        j = texto.find(alvo, i)
        if j < 0:
            saida.append(texto[i:])
            return "".join(saida)
        saida.append(texto[i:j])
        k, nivel = j + len(alvo), 1
        while k < len(texto) and nivel:
            nivel += {"{": 1, "}": -1}.get(texto[k], 0)
            k += 1
        saida.append(troca)
        i = k


def para_texto(fonte):
    t = "\n".join(sem_comentarios(l) for l in fonte.splitlines())
    t = re.sub(r"\\begin\{(tabular\*?|tabularx|tikzpicture|equation\*?|align\*?)\}.*?\\end\{\1\}",
               "\n\n", t, flags=re.S)
    t = tirar_comando_com_chaves(t, "todo")
    t = tirar_comando_com_chaves(t, "citepend", "(Cite)")
    t = re.sub(r"\\(?:text|paren|auto)?cites?\*?(?:\[[^\]]*\])*\{[^}]*\}", "(Cite)", t)
    t = re.sub(r"\\(?:ref|eqref|autoref|cref|Cref)\{[^}]*\}", "1", t)
    t = re.sub(r"\\(?:label|includegraphics|input|notafonte)(?:\[[^\]]*\])?\{[^}]*\}", "", t)
    t = re.sub(r"\\(?:sub)*section\*?\{[^}]*\}", "\n\n", t)
    t = re.sub(r"\\(?:begin|end)\{[^}]*\}(?:\[[^\]]*\])?", "\n\n", t)
    t = re.sub(r"\\item\b(?:\[[^\]]*\])?", "\n\n", t)
    for m, v in MACROS.items():
        t = re.sub(r"\\" + m + r"(?![A-Za-z])(?:\{\})?", v, t)
    t = re.sub(r"\$[^$]*\$", "X", t)
    t = t.replace("---", "\u2014").replace("--", "\u2013").replace("~", " ")
    t = t.replace("\\%", "%").replace("\\&", "&").replace("\\,", " ").replace("\\ ", " ")
    t = re.sub(r"\\[A-Za-z]+\*?(?:\[[^\]]*\])?", "", t)
    t = t.replace("{", "").replace("}", "")
    return t


def frases_de(paragrafo):
    p = " ".join(paragrafo.split())
    for a in ABREV:  # so abreviatura isolada: o "p." de "scrap." nao conta
        p = re.sub(r"(?<![A-Za-z])" + re.escape(a), a.replace(".", "\u00b7"), p)
    partes = re.split(r"(?<=[.!?])\s+(?=[A-Z(\"\u201c])", p)
    return [x.replace("\u00b7", ".") for x in partes if len(x.split()) >= 3]


def tricolons(frase):
    n = 0
    for oracao in re.split(r"[;:]", frase):
        m = re.search(r"(^|[^,]*?)([^,]+), ([^,]+),? (and|or) ([^,]+)$", oracao.strip().rstrip("."))
        if m and oracao.count(",") in (1, 2):
            n += 1
    return n


PASSIVA = re.compile(r"\b(is|are|was|were|be|been|being)\s+(?:\w+ly\s+)?\w+(?:ed|en|wn|lt|ught|ade|id)\b",
                     re.I)


def analisar(caminho, detalhe):
    bruto = caminho.read_text(encoding="utf-8")
    linhas = [sem_comentarios(l) for l in bruto.splitlines()]
    r = {"arquivo": caminho.relative_to(RAIZ).as_posix()}
    ocorr = []

    def contar(padrao, rotulo, flags=0):
        total = 0
        for n, l in enumerate(linhas, 1):
            achados = re.findall(padrao, l, flags)
            if achados:
                total += len(achados)
                ocorr.append(f"  {r['arquivo']}:{n}  [{rotulo}]  {l.strip()[:110]}")
        return total

    r["travessoes"] = contar(r"---|\u2014", "travessao") + contar(r"\s--\s", "travessao (--)")
    r["transicoes"] = sum(contar(r"(?:^|[.!?]\s+|\n)" + re.escape(t) + r"\b,?", "transicao: " + t)
                          for t in TRANSICOES)
    r["marcadores"] = sum(contar(r"\b" + re.escape(m), "marcador: " + m, re.I) for m in MARCADORES)

    texto = para_texto(bruto)
    paragrafos = [p for p in re.split(r"\n\s*\n", texto) if len(p.split()) >= 12]
    frases = [f for p in paragrafos for f in frases_de(p)]
    tam = [len(f.split()) for f in frases]
    r["frases"] = len(frases)
    r["media"] = round(statistics.mean(tam), 1) if tam else 0
    r["dp"] = round(statistics.pstdev(tam), 1) if len(tam) > 1 else 0
    r["acima35"] = sum(1 for x in tam if x > 35)
    r["abaixo8"] = sum(1 for x in tam if x < 8)
    seq, maior = 1, 1
    for a, b in zip(tam, tam[1:]):
        seq = seq + 1 if abs(a - b) <= 3 else 1
        maior = max(maior, seq)
    r["seq_parecidas"] = maior
    r["tricolons"] = sum(tricolons(f) for f in frases)
    r["passiva_pct"] = round(100 * sum(1 for f in frases if PASSIVA.search(f)) / len(frases)) if frases else 0
    inicios = [p.split()[0].strip("(\u201c\"") for p in paragrafos]
    seq_ini, maior_ini = 1, 1
    for a, b in zip(inicios, inicios[1:]):
        seq_ini = seq_ini + 1 if a == b else 1
        maior_ini = max(maior_ini, seq_ini)
    r["paragrafos_mesmo_inicio"] = maior_ini
    r["palavras"] = sum(len(p.split()) for p in paragrafos)
    if detalhe:
        r["ocorrencias"] = ocorr
        r["longas"] = [f"  {r['arquivo']}  ({len(f.split())} palavras)  {f[:120]}..."
                       for f in frases if len(f.split()) > 35]
    return r


def main():
    detalhe = "--detalhe" in sys.argv
    res = [analisar(a, detalhe) for a in ARQUIVOS]
    cab = ["arquivo", "palavras", "travessoes", "transicoes", "marcadores", "tricolons", "frases",
           "media", "dp", "acima35", "abaixo8", "seq_parecidas", "paragrafos_mesmo_inicio", "passiva_pct"]
    print(" | ".join(cab))
    for r in res:
        print(" | ".join(str(r[c]) for c in cab))
    tot = {c: sum(r[c] for r in res) for c in cab[1:7] + ["acima35", "abaixo8"]}
    todas = []
    for a in ARQUIVOS:
        texto = para_texto(a.read_text(encoding="utf-8"))
        paragrafos = [p for p in re.split(r"\n\s*\n", texto) if len(p.split()) >= 12]
        todas += [len(f.split()) for p in paragrafos for f in frases_de(p)]
    print(f"TOTAL | {tot['palavras']} | {tot['travessoes']} | {tot['transicoes']} | {tot['marcadores']} | "
          f"{tot['tricolons']} | {tot['frases']} | {round(statistics.mean(todas), 1)} | "
          f"{round(statistics.pstdev(todas), 1)} | {tot['acima35']} | {tot['abaixo8']} | - | - | -")
    if detalhe:
        print("\nOCORRENCIAS")
        for r in res:
            for o in r["ocorrencias"]:
                print(o)
        print("\nFRASES COM MAIS DE 35 PALAVRAS")
        for r in res:
            for o in r["longas"]:
                print(o)


if __name__ == "__main__":
    main()
