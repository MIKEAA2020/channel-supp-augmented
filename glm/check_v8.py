#!/usr/bin/env python3
"""v8 manuscript consistency checker — both papers.
Inherits every v7 check; the cite regex is FIXED to match the optional-argument
form \\cite[Corollary~2]{NechitaEtAl2018} (the W26 'uncited bibitem' finding
was an artifact of the old regex). Adds the v8 citation-integration checks.
"""
import re
import sys
from collections import Counter

PATHS = {
    "INST": "/home/z/my-project/channel-supp-augmented/manuscript uploads v8/instruments-paper-revised8.txt",
    "MAIN": "/home/z/my-project/channel-supp-augmented/manuscript uploads v8/main-article-revised8.txt",
}
FAIL = []

CITE_RE = re.compile(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}')


def check(name, cond, msg):
    status = "PASS" if cond else "FAIL"
    if not cond:
        FAIL.append((name, msg))
    print(f"[{status}] {name}: {msg}")


texts = {}
for name, p in PATHS.items():
    with open(p, encoding='utf-8', errors='replace') as f:
        texts[name] = f.read()

for name, text in texts.items():
    lines = text.split('\n')
    print(f"\n{'='*70}\n{name} — mechanical checks\n{'='*70}")

    # 1. label/ref matching
    labels = set(re.findall(r'\\label\{([^}]+)\}', text))
    refs = set(re.findall(r'\\(?:ref|autoref|eqref)\{([^}]+)\}', text))
    dangling = sorted(refs - labels)
    check(name, not dangling, f"dangling refs: {dangling[:8] if dangling else 'none'}")
    dups = [l for l in labels if text.count(f'\\label{{{l}}}') > 1]
    check(name, not dups, f"duplicate labels: {dups[:8] if dups else 'none'}")

    # 2. cite keys vs bibitems (FIXED regex: optional [..] argument handled)
    cite_grps = CITE_RE.findall(text)
    cited_keys = set(k.strip() for c in cite_grps for k in c.split(','))
    bibitems = set(re.findall(r'\\bibitem\{([^}]+)\}', text))
    uncited = sorted(bibitems - cited_keys)
    missbib = sorted(cited_keys - bibitems)
    check(name, not missbib, f"cite keys w/o bibitem: {missbib[:8] if missbib else 'none'}")
    print(f"      (bibitems never cited: {uncited if uncited else 'none'})")
    check(name, not uncited, f"bibitems never cited: {uncited if uncited else 'none'}")

    # 3. environment balance
    envs = re.findall(r'\\begin\{(\w+)\}', text)
    ends = re.findall(r'\\end\{(\w+)\}', text)
    be, en = Counter(envs), Counter(ends)
    diff = {k: (be.get(k, 0), en.get(k, 0)) for k in set(be) | set(en)
            if be.get(k, 0) != en.get(k, 0)}
    check(name, not diff, f"begin/end mismatches: {diff if diff else 'none'}")

    # 4. display math balance
    ndb, nde = text.count('\\['), text.count('\\]')
    check(name, ndb == nde, f"\\[ = {ndb}, \\] = {nde}")
    t2 = text.replace('\\$', '')
    nd = len(re.findall(r'(?<!\\)\$', t2))
    check(name, nd % 2 == 0, f"unescaped $ count = {nd} (even?)")

    # 5. non-ASCII
    nonascii = set(ch for ln in lines for ch in ln if ord(ch) > 127)
    check(name, not nonascii, f"non-ASCII: {sorted(nonascii)[:10] if nonascii else 'none'}")

    # 6. \left/\right balance
    nl, nr = text.count('\\left'), text.count('\\right')
    check(name, nl == nr, f"\\left = {nl}, \\right = {nr}")

print(f"\n{'='*70}\nCROSS-PAPER CLAIM-NUMBER CONSISTENCY\n{'='*70}")
I, M = texts["INST"], texts["MAIN"]

checks = [
    ("4/3 in INST (delta_2 value)", '4/3' in I or '\\tfrac43' in I or '\\frac43' in I),
    ("4/3 in MAIN sync clause", ('4/3' in M) or ('\\tfrac43' in M) or ('\\frac43' in M)),
    ("[4/3, 3/2] bracket in INST", ('3/2' in I or '\\tfrac32' in I)),
    ("H tuple Z/3 chain in INST", 'Z/3' in I or '\\mathbb Z/3' in I or '\\mathbb{Z}/3' in I),
    ("14,910 or 14910 cell count in INST",
     ('14,910' in I) or ('14910' in I) or ('14\\,910' in I)),
    ("primes <= 61 scan mentioned in INST", '61' in I),
]
for nm, cond in checks:
    check("XCHECK", cond, nm)

occ = re.findall(r'r\s*\\?ge\s*3', I)
check("XCHECK", len(occ) >= 1, f"'r>=3' occurrences in INST: {len(occ)}")
cfblock = I[I.find('label{con:coord-flat}'):I.find('label{con:coord-flat}') + 3000]
bad_r2 = re.findall(r'2r\+2', cfblock)
print(f"      (con:coord-flat block: '2r+2' count = {len(bad_r2)} — expected >=1 as the corrected upper-side)")
sd2 = I[I.find('label{thm:state-d2}'):I.find('label{thm:state-d2}') + 1200]
check("XCHECK", '4/3' in sd2 or '\\tfrac43' in sd2, "thm:state-d2 states 4/3")
check("XCHECK", '2(1-1/d_B)' in sd2 or '2\\left(1-\\frac1{d_B}' in sd2
      or '2(1-\\tfrac1{d_B})' in sd2, "thm:state-d2 upper bound 2(1-1/d_B)")
sync = 'equal-basis-plane' in M or 'machine-certified' in M or 'plane-valued' in M
check("XCHECK", sync, "MAIN has the sync clause (plane-valued / machine-certified / equal-basis-plane)")

print(f"\n{'='*70}\nV8 CITATION-INTEGRATION CHECKS\n{'='*70}")
newkeys = ["GuerraJana2025", "GuerraJanaMaiti2025", "WeberWojciechowski2017",
           "KorbasLorinc2003", "Matszangosz2021", "Singh2010", "Crabb2022"]
for k in newkeys:
    check("V8", f"\\bibitem{{{k}}}" in I, f"INST has bibitem {k}")
for k in ["GuerraJana2025", "GuerraJanaMaiti2025"]:
    check("V8", f"\\bibitem{{{k}}}" in M, f"MAIN has bibitem {k}")
check("V8", "rem:flag-literature" in I and
      I.count("rem:flag-literature") >= 3, "INST rem:flag-literature label + refs")
check("V8", "label{rem:machine-certificate}" in I, "INST rem:machine-certificate intact")
check("V8", "cite[Corollary~2]{NechitaEtAl2018}" in M, "MAIN NechitaEtAl2018 cite present (W26 artifact corrected)")
for k in newkeys:
    cited_in_I = any(k in [x.strip() for x in g.split(',')]
                     for g in CITE_RE.findall(I))
    check("V8", cited_in_I, f"INST cites {k}")
for k in ["GuerraJana2025", "GuerraJanaMaiti2025"]:
    cited_in_M = any(k in [x.strip() for x in g.split(',')]
                     for g in CITE_RE.findall(M))
    check("V8", cited_in_M, f"MAIN cites {k}")
# The W26 near-collision engagement: the differentiation axes present in the remark
flit = I[I.find('label{rem:flag-literature}'):I.find('label{rem:flag-literature}') + 3000]
for axis, pat in [("cyclic vs symmetric-group quotient", r'cyclic.{0,80}intermediate quotient|symmetric-group'),
                  ("integral vs field coefficients", r'integral.{0,60}coefficients|field.{0,20}coefficients'),
                  ("equal-value/width vs Auerbach application", r'Auerbach-basis counting')]:
    check("V8", re.search(pat, flit, re.S) is not None, f"remark differentiation: {axis}")

print(f"\n{'='*70}\nRESULT: {len(FAIL)} failures" + ("" if not FAIL else f"\n{FAIL}"))
sys.exit(1 if FAIL else 0)
