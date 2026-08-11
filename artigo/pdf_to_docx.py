"""
Convert a LaTeX manuscript or PDF to DOCX.

Priority:
  1. If a .tex file is found alongside the PDF, use pandoc (LaTeX -> DOCX).
     Pandoc preserves text flow, citations, and equations far better than
     any PDF parser can.
  2. If pandoc is not on PATH and no .tex file exists, fall back to pdf2docx
     (PDF -> DOCX). Quality is lower for two-column / math-heavy documents.

Usage:
    python pdf_to_docx.py [input.pdf | input.tex] [output.docx]

Defaults to converting main.pdf (or main.tex if present) -> main.docx.

Requirements:
    pip install pdf2docx          # fallback
    winget install JohnMacFarlane.Pandoc  # preferred
"""

import shutil
import subprocess
import sys
from pathlib import Path


PANDOC = shutil.which("pandoc") or (
    # winget installs pandoc here and does not update the current session PATH
    Path.home()
    / "AppData/Local/Microsoft/WinGet/Packages"
    / "JohnMacFarlane.Pandoc_Microsoft.Winget.Source_8wekyb3d8bbwe"
    / "pandoc-3.9.0.2/pandoc.exe"
)


def _pandoc_available() -> bool:
    p = Path(PANDOC) if not isinstance(PANDOC, str) else Path(PANDOC)
    return p.exists() or shutil.which("pandoc") is not None


def _convert_via_pandoc(tex_path: Path, docx_path: Path) -> None:
    bib = tex_path.parent / "references.bib"
    cmd = [
        str(PANDOC),
        str(tex_path),
        "--from=latex",
        "--to=docx",
        f"--output={docx_path}",
        f"--resource-path={tex_path.parent}",
        "--wrap=none",
    ]
    if bib.exists():
        cmd += [f"--bibliography={bib}", "--citeproc"]

    result = subprocess.run(cmd, capture_output=True, text=True)
    # Surface only non-WARNING lines so the caller sees real errors
    errors = [l for l in result.stderr.splitlines() if "WARNING" not in l]
    if errors:
        print("\n".join(errors))
    if result.returncode != 0:
        raise RuntimeError(f"pandoc failed (exit {result.returncode})")


def _convert_via_pdf2docx(pdf_path: Path, docx_path: Path) -> None:
    try:
        from pdf2docx import Converter
    except ImportError:
        raise ImportError("pdf2docx not installed. Run: pip install pdf2docx")

    cv = Converter(str(pdf_path))
    cv.convert(str(docx_path))
    cv.close()


def convert(source: str | Path, output: str | Path | None = None) -> Path:
    """Convert a .tex or .pdf manuscript to .docx.

    Args:
        source:  Path to a .tex or .pdf file.
        output:  Destination .docx path. Defaults to <source>.docx.

    Returns:
        Path to the generated .docx file.
    """
    source = Path(source).resolve()
    if not source.exists():
        raise FileNotFoundError(f"Source not found: {source}")

    docx_path = Path(output).resolve() if output else source.with_suffix(".docx")

    # Prefer .tex source if caller passed a PDF but a sibling .tex exists
    tex_candidate = source.with_suffix(".tex")
    if source.suffix.lower() == ".pdf" and tex_candidate.exists() and _pandoc_available():
        print(f"LaTeX source found. Using pandoc: {tex_candidate.name} -> {docx_path.name}")
        _convert_via_pandoc(tex_candidate, docx_path)
    elif source.suffix.lower() == ".tex" and _pandoc_available():
        print(f"Using pandoc: {source.name} -> {docx_path.name}")
        _convert_via_pandoc(source, docx_path)
    else:
        pdf_path = source if source.suffix.lower() == ".pdf" else source.with_suffix(".pdf")
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF not found: {pdf_path}")
        print(f"Using pdf2docx (pandoc not available): {pdf_path.name} -> {docx_path.name}")
        _convert_via_pdf2docx(pdf_path, docx_path)

    print(f"Done: {docx_path}")
    return docx_path


if __name__ == "__main__":
    args = sys.argv[1:]
    script_dir = Path(__file__).parent

    # Default: main.tex (preferred) or main.pdf
    default = script_dir / "main.tex" if (script_dir / "main.tex").exists() else script_dir / "main.pdf"
    source = Path(args[0]) if args else default
    output = Path(args[1]) if len(args) > 1 else None

    convert(source, output)
