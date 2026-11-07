# -*- coding: utf-8 -*-
"""
gerar_figuras.py
Gera as oito figuras do manuscrito em JPEG em figuras/ (regra da revista Production: figuras em JPEG,
300 dpi ou mais).

1. Figuras 1 a 5 (modelo conceitual e diagramas): TikZ de figs-tikz/, compiladas isoladas (classe
   standalone, Times via newtx) e rasterizadas a 400 dpi com pdftoppm. Os diagramas 2 a 5 redesenham
   fielmente as Figuras 4 a 7 do artigo original (conferido em 06/11/2026).
2. Figuras 6 a 8 (dados): as IMAGENS ORIGINAIS do artigo (Paper Training - 15 Nov 2025.pdf, Figs. 8 a
   10), extraidas com pdfimages para figuras-originais/ e so convertidas para JPEG, sem mexer nos dados.
   Resolucao nativa: 115, 137 e 164 dpi, abaixo dos 300 exigidos. PENDENTE: pedir ao Cristiano a
   planilha ou o grafico de origem para exportar a 300 dpi ou mais.
   Os graficos que a versao JATM "reconstruiu" ficam em figs-tikz/_reconstrucoes-jatm-NAO-USAR/
   (os valores nao batem com os originais).

Numeracao: ordem da primeira citacao no texto (estrutura do original restaurada em 06/11/2026:
AS9100 em 3.1, regulacao em 3.2).
Uso: python scripts/gerar_figuras.py
Adaptado da etapa 3 do preparar_production.py do artigo B (pasta Production-ABEPRO-secao-tematica-2027).
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RAIZ = Path(__file__).resolve().parent.parent
FONTE = RAIZ / "figs-tikz"
ORIGINAIS_DIR = RAIZ / "figuras-originais"
SAIDA = RAIZ / "figuras"

# 400 dpi nas TikZ: acima dos 300 exigidos e com as figuras abaixo do limite de 3 MB do arquivo.
TIKZ = {
    "fig1-conceptual-model": "fig0-conceptual-model.tex",
    "fig2-as9100": "fig4-as9100.tex",
    "fig3-regulation": "fig5-regulation.tex",
    "fig4-process-original": "fig6-training-process-original.tex",
    "fig5-process-redesigned": "fig7-training-process-changed.tex",
}
ORIGINAIS = {
    "fig6-reaction-scores": "original-fig8-reacao.png",
    "fig7-final-grades": "original-fig9-notas.png",
    "fig8-customer-satisfaction": "original-fig10-clientes.png",
}

PREAMBULO = r"""\documentclass[border=6pt]{standalone}
\usepackage[T1]{fontenc}
\usepackage{amsmath}
\usepackage{newtxtext,newtxmath}
\usepackage{xcolor}
\usepackage{tikz}
\usetikzlibrary{positioning,arrows.meta,shapes.geometric,shapes.misc,calc,fit,backgrounds,patterns}
\definecolor{kpBlue}{HTML}{2171B5}
\definecolor{kpBlueL}{HTML}{C6DBEF}
\definecolor{kpGreen}{HTML}{2C9F2C}
\definecolor{kpGreenL}{HTML}{CDEFCD}
\definecolor{kpOrange}{HTML}{E69138}
\definecolor{kpOrangeL}{HTML}{FCE5CD}
\definecolor{kpRed}{HTML}{CC0000}
\definecolor{kpRedL}{HTML}{F4CCCC}
\begin{document}
"""


def main():
    SAIDA.mkdir(parents=True, exist_ok=True)
    # Pasta temporaria dentro do projeto: no %TEMP% o Windows devolve o caminho curto (HEITOR~1)
    # e o pdflatex do MiKTeX nao grava nele.
    with tempfile.TemporaryDirectory(dir=RAIZ, prefix=".tmpfig-") as tmpd:
        tmp = Path(tmpd)
        for nome, arq in TIKZ.items():
            src = tmp / f"{nome}.tex"
            src.write_text(PREAMBULO + (FONTE / arq).read_text(encoding="utf-8") + "\n\\end{document}\n",
                           encoding="utf-8")
            r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-output-directory", str(tmp), str(src)],
                               capture_output=True, text=True, cwd=str(tmp))
            pdf = tmp / f"{nome}.pdf"
            if r.returncode != 0 or not pdf.exists():
                log = (tmp / f"{nome}.log").read_text(encoding="utf-8", errors="replace")
                sys.exit(f"falha ao compilar {arq}: {[l for l in log.splitlines() if l.startswith('!')][:3]}")
            subprocess.run(["pdftoppm", "-jpeg", "-r", "400", "-jpegopt", "quality=92", "-singlefile",
                            str(pdf), str(SAIDA / nome)], check=True)
            print(f"{nome}.jpg  ({(SAIDA / f'{nome}.jpg').stat().st_size // 1024} KB, 400 dpi)  <- {arq}")
    for nome, arq in ORIGINAIS.items():
        im = Image.open(ORIGINAIS_DIR / arq).convert("RGB")
        im.save(SAIDA / f"{nome}.jpg", "JPEG", quality=95)
        print(f"{nome}.jpg  ({im.size[0]}x{im.size[1]} px, imagem ORIGINAL, resolucao nativa)  <- {arq}")
    print("pronto")


if __name__ == "__main__":
    main()
