#!/usr/bin/env python3
"""v7 manuscript consistency checker — both papers.
Mechanical checks: labels/refs, cites/bibitems, environment balance,
math delimiters, non-ASCII; plus claim-number cross-checks between papers.
"""
import re, sys

PATHS = {
    "INST": "/home/z/my-project/channel-supp-augmented/manuscript uploads v7/instruments-paper-revised7.txt",
    "MAIN": "/home/z/my-project/channel-supp-augmented/manuscript uploads v7/main-article-revised7.txt",
}
FAIL = []

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

    # 2. cite keys vs bibitems
    cites = set(re.findall(r'\\cite\{([^}]+)\}', text))
    cited_keys = set(k.strip() for c in cites for k in c.split(','))
    bibitems = set(re.findall(r'\\bibitem\{([^}]+)\}', text))
    uncited = sorted(bibitems - cited_keys)
    missbib = sorted(cited_keys - bibitems)
    check(name, not missbib, f"cite keys w/o bibitem: {missbib[:8] if missbib else 'none'}")
    print(f"      (bibitems never cited: {uncited if uncited else 'none'})")

    # 3. environment balance
    envs = re.findall(r'\\begin\{(\w+)\}', text)
    ends = re.findall(r'\\end\{(\w+)\}', text)
    from collections import Counter
    be, en = Counter(envs), Counter(ends)
    diff = {k: (be.get(k,0), en.get(k,0)) for k in set(be)|set(en) if be.get(k,0)!=en.get(k,0)}
    check(name, not diff, f"begin/end mismatches: {diff if diff else 'none'}")

    # 4. display math balance
    ndb = text.count('\\[')
    nde = text.count('\\]')
    check(name, ndb == nde, f"\\[ = {ndb}, \\] = {nde}")
    # single-$ count should be even (rough)
    # strip escaped \$ and \\$ first
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

# Key numbers and their expected presence
checks = [
    ("4/3 in INST (delta_2 value)", r'4/3' in I or r'\\tfrac43' in I or '\\frac43' in I),
    ("4/3 in MAIN sync clause", ('4/3' in M) or ('\\tfrac43' in M) or ('\\frac43' in M)),
    ("[4/3, 3/2] bracket in INST", ('3/2' in I or '\\tfrac32' in I)),
    ("H tuple Z/3 chain in INST", 'Z/3' in I or '\\mathbb Z/3' in I or '\\mathbb{Z}/3' in I),
    ("14,910 or 14910 cell count in INST", ('14,910' in I) or ('14910' in I) or ('14\\,910' in I)),
    ("primes <= 61 scan mentioned in INST", '61' in I),
]
for nm, cond in checks:
    check("XCHECK", cond, nm)

# The con:coord-flat corrected clause: r >= 3 consistency in INST
occ = re.findall(r'r\s*\\?ge\s*3', I)
check("XCHECK", len(occ) >= 1, f"'r>=3' occurrences in INST: {len(occ)}")
# no lingering 'r >= 2' coord-flat form near 'con:coord-flat'
cfblock = I[I.find('label{con:coord-flat}'):I.find('label{con:coord-flat}')+3000]
bad_r2 = re.findall(r'2r\+2', cfblock)
print(f"      (con:coord-flat block: '2r+2' count = {len(bad_r2)} — expected >=1 as the corrected upper-side)")
# check the instruments 'thm:state-d2' block numbers
sd2 = I[I.find('label{thm:state-d2}'):I.find('label{thm:state-d2}')+1200]
check("XCHECK", '4/3' in sd2 or '\\tfrac43' in sd2, "thm:state-d2 states 4/3")
check("XCHECK", '2(1-1/d_B)' in sd2 or '2\\left(1-\\frac1{d_B}' in sd2 or '2(1-\\tfrac1{d_B})' in sd2, "thm:state-d2 upper bound 2(1-1/d_B)")

# MAIN sync clause references the companion's plane theorem
sync = 'equal-basis-plane' in M or 'machine-certified' in M or 'plane-valued' in M
check("XCHECK", sync, "MAIN has the sync clause (plane-valued / machine-certified / equal-basis-plane)")

print(f"\n{'='*70}\nRESULT: {len(FAIL)} failures" + ("" if not FAIL else f"\n{FAIL}"))
sys.exit(1 if FAIL else 0)
