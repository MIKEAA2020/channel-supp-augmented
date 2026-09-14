#!/usr/bin/env python3
"""Wave 40 checker: QIP cover letters for both papers.

Checks (both letters):
 1. PDF exists, exactly 1 page, A4.
 2. PDF metadata: Title, Author == "Amin Abaee", Subject present.
 3. Rendered-text needles (ligature-normalized): identity block, date,
    recipient, Re: line, salutation/closing, per-letter research needles,
    companion cross-reference, declarations phrases.
 4. Blind/placeholder/boilerplate sweeps: no 'xx', no 'anonymized', no
    'DRAFT', no stray LaTeX tokens in the rendered text, no unresolved
    refs ('??').
 5. .txt mirror: exists, non-empty, same needle set present.
 6. Source sanity: '\\end{document}' present, brace balance, no
    placeholder markers.
 7. Companion cross-consistency: each letter cites the other paper's
    exact title; both disclose separate submission.
Exit 0 iff all checks pass.
"""

import re
import subprocess
import sys

BASE = "/home/z/my-project/channel-supp-augmented/cover letters"

LETTERS = {
    "main": {
        "tex": "qip-cover-letter-main.tex",
        "pdf": "qip-cover-letter-main.pdf",
        "txt": "qip-cover-letter-main.txt",
        "title": "Exact Diamond Balls, Antipodal Widths, and Query-Uniform Compression Bounds for Quantum Channels",
        "companion_title": "Exact Affine Geometry, Optimal Centres, Certified Compression Bounds, and Flag-Quotient Width Obstructions for Finite-Outcome Quantum Instruments",
        "needles": [
            "Amin Abaee", "Independent Researcher", "amin_abaee@ut.ac.ir",
            "ORCID: 0000-0002-0019-1842", "September 14, 2026",
            "The Editors", "Quantum Information Processing", "Springer Nature",
            "Re: Submission of the research article",
            "Dear Editors", "Yours sincerely",
            "46-page", "Borsuk", "Ulam", "deleted-product coindex",
            "depolarizing channel", "diamond-norm", "O(N",
            "programmable processors", "tomography",
            "flag-quotient flatness dichotomy",
            "submitted separately to the journal",
            "not under consideration elsewhere",
            "no funding and no competing interests",
            "purely theoretical",
        ],
    },
    "instruments": {
        "tex": "qip-cover-letter-instruments.tex",
        "pdf": "qip-cover-letter-instruments.pdf",
        "txt": "qip-cover-letter-instruments.txt",
        "title": "Exact Affine Geometry, Optimal Centres, Certified Compression Bounds, and Flag-Quotient Width Obstructions for Finite-Outcome Quantum Instruments",
        "companion_title": "Exact Diamond Balls, Antipodal Widths, and Query-Uniform Compression Bounds for Quantum Channels",
        "needles": [
            "Amin Abaee", "Independent Researcher", "amin_abaee@ut.ac.ir",
            "ORCID: 0000-0002-0019-1842", "September 14, 2026",
            "The Editors", "Quantum Information Processing", "Springer Nature",
            "Re: Submission of the research article",
            "Dear Editors", "Yours sincerely",
            "53-page", "Borsuk", "Ulam", "flag quotient",
            "uniform depolarising instrument", "diamond-norm", "flat-width",
            "4/3", "affine dimension", "complementarity identity",
            "machine computation",
            "submitted separately to the journal",
            "not under consideration elsewhere",
            "no funding and no competing interests",
            "public repository",
        ],
    },
}

FORBIDDEN_RENDER = [
    "xx", "anonymized", "Anonymized", "DRAFT", "TODO", "PLACEHOLDER",
    "\\emph", "\\begin", "\\textbf", "\\href", "\\noindent",
    "??", "undefined", "blind",
]

LIG = {
    "\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl", "\ufb03": "ffi",
    "\ufb04": "ffl",
}


def norm(s: str) -> str:
    for k, v in LIG.items():
        s = s.replace(k, v)
    s = s.replace("\u2014", "-").replace("\u2013", "-")
    s = re.sub(r"-\s*\n\s*", "", s)  # rejoin hyphenated line breaks
    s = re.sub(r"\s+", " ", s)
    return s


def loose(haystack: str, needle: str) -> bool:
    """Hyphen/whitespace-insensitive containment (robust to line breaks
    at real hyphens, e.g. Flag-Quotient split across lines)."""
    sq = re.sub(r"[\s-]+", "", haystack)
    nq = re.sub(r"[\s-]+", "", needle)
    return nq in sq


def pdftext(path: str) -> str:
    out = subprocess.run(["pdftotext", path, "-"], capture_output=True, text=True, check=True)
    return out.stdout


def pdfinfo(path: str) -> dict:
    out = subprocess.run(["pdfinfo", path], capture_output=True, text=True, check=True)
    info = {}
    for line in out.stdout.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            info[k.strip()] = v.strip()
    return info


def main() -> int:
    failures = []
    passes = 0

    def check(cond: bool, msg: str):
        nonlocal passes
        if cond:
            passes += 1
        else:
            failures.append(msg)

    for key, spec in LETTERS.items():
        tex_p = f"{BASE}/{spec['tex']}"
        pdf_p = f"{BASE}/{spec['pdf']}"
        txt_p = f"{BASE}/{spec['txt']}"

        # 1. pages + size
        info = pdfinfo(pdf_p)
        check(info.get("Pages") == "1", f"{key}: page count == 1 (got {info.get('Pages')})")
        check("595" in info.get("Page size", "") and "841" in info.get("Page size", ""),
              f"{key}: A4 page size (got {info.get('Page size')})")

        # 2. metadata
        check(spec["title"].split(",")[0] in info.get("Title", ""), f"{key}: PDF Title metadata")
        check(info.get("Author") == "Amin Abaee", f"{key}: PDF Author == Amin Abaee (got {info.get('Author')})")
        check("Quantum Information Processing" in info.get("Subject", ""), f"{key}: PDF Subject metadata")

        # 3. rendered needles
        rt = norm(pdftext(pdf_p))
        for n in spec["needles"] + [spec["title"], spec["companion_title"]]:
            check(loose(rt, n), f"{key}: rendered needle missing: {n!r}")

        # 4. forbidden sweeps (word-boundary for short tokens)
        for f in FORBIDDEN_RENDER:
            if len(f) <= 3:
                hit = re.search(rf"\b{re.escape(f)}\b", rt) is not None
            else:
                hit = f in rt
            check(not hit, f"{key}: forbidden token in render: {f!r}")

        # 5. txt mirror
        try:
            txt = norm(open(txt_p, encoding="utf-8").read())
            for n in spec["needles"] + [spec["title"], spec["companion_title"]]:
                check(loose(txt, n), f"{key}: txt-mirror needle missing: {n!r}")
        except FileNotFoundError:
            check(False, f"{key}: txt mirror missing")

        # 6. source sanity
        src = open(tex_p, encoding="utf-8").read()
        check("\\end{document}" in src, f"{key}: \\end{{document}} present")
        check(src.count("{") == src.count("}"), f"{key}: brace balance")
        check("XX" not in src and "TODO" not in src and "DRAFT" not in src,
              f"{key}: no source placeholders")

        # 7. word count report
        words = len(re.findall(r"[A-Za-z][A-Za-z'-]*", rt))
        print(f"[{key}] rendered word count: {words}")

    print(f"\nRESULT: {passes} PASS, {len(failures)} FAIL")
    for f in failures:
        print(f"  FAIL: {f}")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
