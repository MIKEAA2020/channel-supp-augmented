#!/usr/bin/env python3
"""Wave 38 checker: the author-identity + declarations QA battery.

P-layer (source): the blind-marker sweep, the placeholder sweep (no xx
fields remain), the identity presences (the exact filled-in author
block, the unchanged version date), the declarations presences (the
exact inserted sentences), the independent reconstruction gate (the new
files equal the v16/v13 sources with exactly the three wave-38 anchored
replacements applied), the .txt == .tex byte mirrors, and the
no-collateral-damage ledgers (labels; refs/cites -- the one expected
added \\ref{rem:machine-certificate} in the instruments declarations;
captions; the section ledger -- exactly one \\section*{Declarations}
added per paper; bibitem bodies; math delimiters).

M-layer (render): page counts (53/46 baselines, recorded honestly),
the page-1 title-block render needles (name / affiliation / ORCID /
email / date), the declarations render needles, the full-text blind and
placeholder sweeps over the PDF text, and the de-anonymized
companion-bibliography render needles.

Exit code = number of failed checks.
"""
import os, re, sys, subprocess

REPO = "/home/z/my-project/channel-supp-augmented"
SRC = {
    "INST": os.path.join(REPO, "manuscript uploads v16", "instruments-paper-unblinded16.tex"),
    "MAIN": os.path.join(REPO, "manuscript uploads v16", "main-article-unblinded13.tex"),
}
NEW = {
    "INST": os.path.join(REPO, "manuscript uploads v17", "instruments-paper-unblinded17.tex"),
    "MAIN": os.path.join(REPO, "manuscript uploads v17", "main-article-unblinded14.tex"),
}
PDF = {
    "INST": NEW["INST"].replace(".tex", ".pdf"),
    "MAIN": NEW["MAIN"].replace(".tex", ".pdf"),
}
BASE_PAGES = {"INST": 53, "MAIN": 46}

AUTHOR_BLOCK = ("\\author{Amin Abaee\\\\\n\\small Independent Researcher\\\\\n"
                "\\small ORCID: 0000-0002-0019-1842\\\\\n"
                "\\small Email: \\href{mailto:amin\\_abaee@ut.ac.ir}"
                "{amin\\_abaee@ut.ac.ir}}")

DECL_INST = ("\\section*{Declarations}\n"
             "The author declares no funding and no competing interests. "
             "The code and computation transcripts of "
             "Remark~\\ref{rem:machine-certificate} are available at "
             "the repository cited there.")
DECL_MAIN = ("\\section*{Declarations}\n"
             "The author declares no funding and no competing "
             "interests. No datasets were generated or analysed.")

# the three wave-38 replacements (re-derived here, independently of
# edit_v17.py, for the reconstruction gate)
REPLACEMENTS = {
    "INST": [
        ("\\author{xx xx\\\\\n\\small xx\\\\\n\\small ORCID: xx\\\\\n"
         "\\small Email: \\href{mailto:xx\\_xx@xx.xx.xx}{xx\\_xx@xx.xx.xx}}",
         AUTHOR_BLOCK),
        ("neither addresses the symmetric-group quotients;\n\n\\appendix",
         "neither addresses the symmetric-group quotients;\n\n"
         + DECL_INST + "\n\n\\appendix"),
        ("xx~xx, \\emph{Exact diamond balls",
         "A.~Abaee, \\emph{Exact diamond balls"),
    ],
    "MAIN": [
        ("\\author{xx xx\\\\\n\\small xx\\\\\n\\small ORCID: xx\\\\\n"
         "\\small Email: \\href{mailto:xx\\_xx@xx.xx.xx}{xx\\_xx@xx.xx.xx}}",
         AUTHOR_BLOCK),
        ("\\end{enumerate}\n\n\\appendix",
         "\\end{enumerate}\n\n" + DECL_MAIN + "\n\n\\appendix"),
        ("xx~xx,\n\\emph{Exact affine geometry",
         "A.~Abaee,\n\\emph{Exact affine geometry"),
    ],
}

results = []
def check(cid, desc, ok, note=""):
    results.append((cid, desc, bool(ok), note))

def extract_braced(text, open_idx):
    """text[open_idx] == '{'; return the full braced group."""
    depth = 0
    i = open_idx
    while i < len(text):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[open_idx:i + 1]
        i += 1
    raise ValueError("unbalanced braces")

def captions(text):
    return [extract_braced(text, m.end() - 1)
            for m in re.finditer(r"\\caption\{", text)]

def bibentries(text):
    """[(key, body), ...] for thebibliography entries."""
    out = []
    idxs = [m.start() for m in re.finditer(r"\\bibitem\{", text)]
    idxs.append(text.rfind("\\end{thebibliography}"))
    for a, b in zip(idxs, idxs[1:]):
        seg = text[a:b]
        key = re.match(r"\\bibitem\{([^}]*)\}", seg).group(1)
        out.append((key, seg))
    return out

def sections(text):
    return [l.strip() for l in text.splitlines()
            if re.match(r"\s*\\section\*?(\[|$|\{)", l)]

src = {k: open(v).read() for k, v in SRC.items()}
new = {k: open(v).read() for k, v in NEW.items()}

n = 0
for P, name in (("INST", "instruments"), ("MAIN", "main")):
    s, t = src[P], new[P]

    n += 1; check(n, f"{name}: blind-marker sweep (withheld/anonymiz/blind, ci)",
                  not re.search(r"(?i)withheld|anonymiz|blind", t))

    n += 1; check(n, f"{name}: placeholder sweep (no xx fields remain in source)",
                  not re.search(r"xx xx|xx~xx|ORCID: xx|\\small xx\\\\|xx\\_xx", t))

    n += 1; check(n, f"{name}: the filled-in author block present (byte-exact)",
                  AUTHOR_BLOCK in t)

    n += 1; check(n, f"{name}: version date unchanged under title",
                  "\\date{September 14, 2026}" in t)

    n += 1; check(n, f"{name}: declarations section present (byte-exact, brief)",
                  (DECL_INST if P == "INST" else DECL_MAIN) in t)

    # reconstruction: new == source + exactly the three replacements
    recon = s
    for old, newr in REPLACEMENTS[P]:
        assert recon.count(old) == 1, f"reconstruction anchor: {old[:60]!r}"
        recon = recon.replace(old, newr)
    n += 1; check(n, f"{name}: reconstruction gate (new == source + 3 hunks, byte-identical)",
                  recon == t)

    n += 1; check(n, f"{name}: .txt byte-mirror of .tex",
                  open(NEW[P].replace(".tex", ".txt"), "rb").read()
                  == open(NEW[P], "rb").read())

    n += 1; check(n, f"{name}: label multiset unchanged",
                  re.findall(r"\\label\{([^}]*)\}", s)
                  == re.findall(r"\\label\{([^}]*)\}", t))

    # refs/cites: instruments gains exactly one \ref{rem:machine-certificate}
    # (the declarations sentence); main gains none
    s_refs = (re.findall(r"\\(?:ref|eqref|pageref)\{([^}]*)\}", s)
              + re.findall(r"\\cite\{([^}]*)\}", s))
    t_refs = (re.findall(r"\\(?:ref|eqref|pageref)\{([^}]*)\}", t)
              + re.findall(r"\\cite\{([^}]*)\}", t))
    expected = s_refs + (["rem:machine-certificate"] if P == "INST" else [])
    n += 1; check(n, f"{name}: ref/cite multiset = source + the expected "
                  "declarations ref only",
                  sorted(t_refs) == sorted(expected),  # multiset (order-independent)
                  f"delta = {len(t_refs) - len(s_refs)} (expected "
                  f"{1 if P == 'INST' else 0})")

    n += 1; check(n, f"{name}: captions byte-identical",
                  captions(s) == captions(t))

    n += 1; check(n, f"{name}: section ledger (only Declarations added)",
                  sections(s) == [x for x in sections(t)
                                  if x != "\\section*{Declarations}"]
                  and sections(t).count("\\section*{Declarations}") == 1
                  and sections(s).count("\\section*{Declarations}") == 0)

    sb, tb = bibentries(s), bibentries(t)
    comp_key = "CompanionChannels" if P == "INST" else "CompanionInstruments"
    n += 1; check(n, f"{name}: bibitem keys unchanged",
                  [k for k, _ in sb] == [k for k, _ in tb])
    n += 1; check(n, f"{name}: bib bodies identical except the companion entry",
                  all(a == b for (ka, a), (kb, b) in zip(sb, tb) if ka != comp_key)
                  and sum(1 for (ka, a), (kb, b) in zip(sb, tb)
                          if ka == comp_key and a != b) == 1)
    n += 1; check(n, f"{name}: companion entry de-anonymized to A.~Abaee",
                  f"A.~Abaee," in dict(tb)[comp_key]
                  and "xx~xx" not in dict(tb)[comp_key])

    n += 1; check(n, f"{name}: math-delimiter parity ($ count unchanged, no math touched)",
                  s.count("$") == t.count("$"))

# ---------------------------------------------------------------- M-layer
# pdftotext ligature normalization (the wave-36/37 documented quirk class:
# lmodern runs yield ffi/ff ligatures, e.g. "aﬃne" for "affine")
LIG = {"\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl",
       "\ufb03": "ffi", "\ufb04": "ffl", "\u2019": "'", "\u2018": "'"}

def normalize(s):
    for k, v in LIG.items():
        s = s.replace(k, v)
    return re.sub(r"\s+", " ", s)

def pdftotext(path, first=None, last=None):
    cmd = ["pdftotext"]
    if first: cmd += ["-f", str(first)]
    if last:  cmd += ["-l", str(last)]
    cmd += [path, "-"]
    return subprocess.run(cmd, capture_output=True, text=True).stdout

def npages(path):
    out = subprocess.run(["pdfinfo", path], capture_output=True, text=True).stdout
    m = re.search(r"Pages:\s+(\d+)", out)
    return int(m.group(1)) if m else -1

for P, name in (("INST", "instruments"), ("MAIN", "main")):
    n += 1
    pc = npages(PDF[P]) if os.path.exists(PDF[P]) else -1
    base = BASE_PAGES[P]
    ok = abs(pc - base) <= 2 if pc > 0 else False
    note = (f"{base} -> {pc} pages "
            + ("(unchanged)" if pc == base
               else "(declarations insertion, explained)" if pc == base + 1
               else "(unexpected reflow -- inspect)"))
    check(n, f"{name}: page count within tolerance of the {base}-page baseline",
          ok, note)

    n += 1
    p1 = pdftotext(PDF[P], 1, 1) if os.path.exists(PDF[P]) else ""
    p1n = normalize(p1)
    needles = ["Amin Abaee", "Independent Researcher",
               "ORCID: 0000-0002-0019-1842", "amin_abaee@ut.ac.ir",
               "September 14, 2026"]
    missing = [x for x in needles if x not in p1n]
    check(n, f"{name}: page-1 title-block render needles (name/affiliation/ORCID/email/date)",
          not missing, f"missing: {missing}" if missing else "all present")

    n += 1
    full = pdftotext(PDF[P]) if os.path.exists(PDF[P]) else ""
    norm = normalize(full)
    check(n, f"{name}: full-text blind sweep (PDF text)",
          not re.search(r"(?i)withheld|anonymiz|double-blind", norm))

    n += 1
    ph_missing = [x for x in ["xx xx", "ORCID: xx", "xx_xx@xx"]
                  if x in norm]
    check(n, f"{name}: full-text placeholder sweep (PDF text, no xx fields)",
          not ph_missing, f"found: {ph_missing}" if ph_missing else "none")

    n += 1
    decl_needles = (["Declarations",
                     "The author declares no funding and no competing interests",
                     "available at the repository cited there"] if P == "INST"
                    else ["Declarations",
                          "The author declares no funding and no competing interests",
                          "No datasets were generated or analysed"])
    missing = [x for x in decl_needles if x not in norm]
    check(n, f"{name}: declarations render needles", not missing,
          f"missing: {missing}" if missing else "all present")

    n += 1
    comp_needle = ("A. Abaee, Exact diamond balls" if P == "INST"
                   else "A. Abaee, Exact affine geometry")
    check(n, f"{name}: de-anonymized companion citation renders",
          comp_needle in norm)

# ---------------------------------------------------------------- report
fails = 0
print(f"=== Wave 38 checker: {len(results)} checks ===")
for cid, desc, ok, note in results:
    tag = "PASS" if ok else "FAIL"
    if not ok: fails += 1
    line = f"[{tag}] {cid:2d}. {desc}"
    if note and not ok: line += f"  -- {note}"
    elif note: line += f"  ({note})"
    print(line)
print(f"\n{len(results) - fails}/{len(results)} PASS, {fails} FAILURES")
sys.exit(fails)
