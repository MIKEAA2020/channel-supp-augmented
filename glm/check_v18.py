#!/usr/bin/env python3
"""Wave 39 checker: the six-top-keywords QA battery.

P-layer (source): the blind-marker and placeholder sweeps (the wave-38
identity/declarations properties persist), the identity author block
and the declarations presences byte-exact, the NEW keyword line
byte-exact with exactly six entries, the dropped entries absent from
the keyword line (they may legitimately occur in the body prose),
the independent reconstruction gate (the new files equal the v17/v14
sources with exactly the one wave-39 anchored keyword replacement
applied), the .txt == .tex byte mirrors, and the no-collateral-damage
ledgers (labels; refs/cites -- NO deltas this wave; captions; the
section ledger -- unchanged; bibitem keys AND bodies; math
delimiters; line counts).

M-layer (render): page counts (53/46 baselines), the page-1 title
block render needles, the page-1 KEYWORDS line render gate (the six
kept entries present in the rendered Keywords line, the dropped
entries absent from that line), the declarations render needles, and
the de-anonymized companion-bibliography render needle.

Exit code = number of failed checks.
"""
import os, re, sys, subprocess

REPO = "/home/z/my-project/channel-supp-augmented"
SRC = {
    "INST": os.path.join(REPO, "manuscript uploads v17", "instruments-paper-unblinded17.tex"),
    "MAIN": os.path.join(REPO, "manuscript uploads v17", "main-article-unblinded14.tex"),
}
NEW = {
    "INST": os.path.join(REPO, "manuscript uploads v18", "instruments-paper-unblinded18.tex"),
    "MAIN": os.path.join(REPO, "manuscript uploads v18", "main-article-unblinded15.tex"),
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

# the one wave-39 replacement per paper (re-derived here, independently
# of edit_v18.py, for the reconstruction gate)
KW_INST = ("\\noindent\\textbf{Keywords:} quantum instruments; diamond norm; "
           "compression width; Chebyshev radius; equivariant cohomology; "
           "Borsuk--Ulam theorem.")
KW_MAIN = ("\\noindent\\textbf{Keywords:} quantum channel compression; "
           "diamond norm; antipodal width; exact in-radius; nonlinear "
           "approximation; Borsuk--Ulam theorem.")
REPLACEMENTS = {
    "INST": KW_INST,
    "MAIN": KW_MAIN,
}

KEPT = {
    "INST": ["quantum instruments", "diamond norm", "compression width",
             "Chebyshev radius", "equivariant cohomology",
             "Borsuk--Ulam theorem"],
    "MAIN": ["quantum channel compression", "diamond norm",
             "antipodal width", "exact in-radius",
             "nonlinear approximation", "Borsuk--Ulam theorem"],
}
DROPPED = {
    "INST": ["antipodal profile", "quantum measurements",
             "flag manifolds", "no-programming theorem"],
    "MAIN": ["quantum combs", "flat-width dichotomy",
             "flag-quotient cohomology"],
}

results = []
def check(cid, desc, ok, note=""):
    results.append((cid, desc, bool(ok), note))

def extract_braced(text, open_idx):
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

    n += 1; check(n, f"{name}: the wave-38 identity author block retained (byte-exact)",
                  AUTHOR_BLOCK in t)

    n += 1; check(n, f"{name}: version date unchanged under title",
                  "\\date{September 14, 2026}" in t)

    n += 1; check(n, f"{name}: declarations section retained (byte-exact, brief)",
                  (DECL_INST if P == "INST" else DECL_MAIN) in t)

    n += 1; check(n, f"{name}: the new six-keyword line present (byte-exact)",
                  REPLACEMENTS[P] in t)

    # exactly six entries, and only the six kept ones, on the keyword line
    m = re.search(r"\\noindent\\textbf\{Keywords:\}(.+?)\.\s*\n", t)
    kw_body = m.group(1) if m else ""
    entries = [e.strip() for e in kw_body.split(";")]
    n += 1; check(n, f"{name}: keyword line carries exactly 6 entries",
                  len(entries) == 6, f"found {len(entries)}: {entries}")
    n += 1; check(n, f"{name}: keyword entries = the six kept ones (order kept)",
                  entries == [k.replace("--", "-") for k in KEPT[P]]
                  or entries == KEPT[P],
                  f"got {entries}")
    kw_line = kw_body
    n += 1; check(n, f"{name}: dropped entries absent from the keyword line",
                  not any(d in kw_line for d in DROPPED[P]),
                  f"present: {[d for d in DROPPED[P] if d in kw_line]}")

    # reconstruction: new == source + the one keyword replacement
    old_kw = None
    if P == "INST":
        old_kw = ("\\noindent\\textbf{Keywords:} quantum instruments; diamond "
                  "norm; compression width; antipodal profile; Chebyshev "
                  "radius; quantum measurements; flag manifolds; equivariant "
                  "cohomology; Borsuk--Ulam theorem; no-programming theorem.")
    else:
        old_kw = ("\\noindent\\textbf{Keywords:} quantum channel compression; "
                  "diamond norm; antipodal width; exact in-radius; "
                  "Borsuk--Ulam theorem; quantum combs; nonlinear "
                  "approximation; flat-width dichotomy; flag-quotient "
                  "cohomology.")
    assert s.count(old_kw) == 1, "reconstruction anchor"
    recon = s.replace(old_kw, REPLACEMENTS[P])
    n += 1; check(n, f"{name}: reconstruction gate (new == source + 1 hunk, byte-identical)",
                  recon == t)

    n += 1; check(n, f"{name}: .txt byte-mirror of .tex",
                  open(NEW[P].replace(".tex", ".txt"), "rb").read()
                  == open(NEW[P], "rb").read())

    n += 1; check(n, f"{name}: label multiset unchanged",
                  re.findall(r"\\label\{([^}]*)\}", s)
                  == re.findall(r"\\label\{([^}]*)\}", t))

    s_refs = (re.findall(r"\\(?:ref|eqref|pageref)\{([^}]*)\}", s)
              + re.findall(r"\\cite\{([^}]*)\}", s))
    t_refs = (re.findall(r"\\(?:ref|eqref|pageref)\{([^}]*)\}", t)
              + re.findall(r"\\cite\{([^}]*)\}", s))  # cite from SOURCE (see below)
    t_refs = (re.findall(r"\\(?:ref|eqref|pageref)\{([^}]*)\}", t)
              + re.findall(r"\\cite\{([^}]*)\}", t))
    n += 1; check(n, f"{name}: ref/cite multiset unchanged (no deltas this wave)",
                  sorted(t_refs) == sorted(s_refs),
                  f"delta = {len(t_refs) - len(s_refs)} (expected 0)")

    n += 1; check(n, f"{name}: captions byte-identical",
                  captions(s) == captions(t))

    n += 1; check(n, f"{name}: section ledger unchanged",
                  sections(s) == sections(t))

    sb, tb = bibentries(s), bibentries(t)
    n += 1; check(n, f"{name}: bibitem keys unchanged",
                  [k for k, _ in sb] == [k for k, _ in tb])
    n += 1; check(n, f"{name}: bibitem bodies all identical",
                  all(a == b for (_, a), (_, b) in zip(sb, tb)))

    n += 1; check(n, f"{name}: math-delimiter parity ($ count unchanged, no math touched)",
                  s.count("$") == t.count("$"))

    n += 1; check(n, f"{name}: source line count unchanged (warning line numbers preserved)",
                  len(s.splitlines()) == len(t.splitlines()))

# ---------------------------------------------------------------- M-layer
# pdftotext ligature normalization (the wave-36/37/38 documented quirk
# class: lmodern runs yield ff/fi/fl/ffi/ffl ligatures)
LIG = {"\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl",
       "\ufb03": "ffi", "\ufb04": "ffl", "\u2019": "'", "\u2018": "'",
       "\u2013": "-"}

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
    ok = pc == base
    note = (f"{base} -> {pc} pages "
            + ("(unchanged)" if pc == base else "(UNEXPECTED reflow -- inspect)"))
    check(n, f"{name}: page count = the {base}-page baseline", ok, note)

    n += 1
    p1 = pdftotext(PDF[P], 1, 1) if os.path.exists(PDF[P]) else ""
    p1n = normalize(p1)
    needles = ["Amin Abaee", "Independent Researcher",
               "ORCID: 0000-0002-0019-1842", "amin_abaee@ut.ac.ir",
               "September 14, 2026"]
    missing = [x for x in needles if x not in p1n]
    check(n, f"{name}: page-1 title-block render needles (name/affiliation/ORCID/email/date)",
          not missing, f"missing: {missing}" if missing else "all present")

    # the rendered Keywords line (page 1, after the abstract): the six
    # kept entries present, the dropped ones absent FROM THAT LINE
    n += 1
    m = re.search(r"Keywords:\s*(.{0,300}?)(?:\.|$)", p1n)
    seg = m.group(1) if m else ""
    kept_miss = [k.replace("--", "-") for k in KEPT[P]
                 if k.replace("--", "-") not in seg]
    drop_hit = [d for d in DROPPED[P] if d in seg]
    check(n, f"{name}: page-1 rendered Keywords line: 6 kept entries present",
          m is not None and not kept_miss,
          f"missing: {kept_miss}" if kept_miss else "all present")

    n += 1
    check(n, f"{name}: page-1 rendered Keywords line: dropped entries absent",
          not drop_hit, f"found: {drop_hit}" if drop_hit else "none")

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
print(f"=== Wave 39 checker: {len(results)} checks ===")
for cid, desc, ok, note in results:
    tag = "PASS" if ok else "FAIL"
    if not ok: fails += 1
    line = f"[{tag}] {cid:2d}. {desc}"
    if note and not ok: line += f"  -- {note}"
    elif note: line += f"  ({note})"
    print(line)
print(f"\n{len(results) - fails}/{len(results)} PASS, {fails} FAILURES")
sys.exit(fails)
