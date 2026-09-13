#!/usr/bin/env python3
"""v10 manuscript consistency checker (inherits v9 mechanics) — both papers.
All v9 mechanical checks (labels/refs/cites/environments/delimiters) run on
the v10 sources, plus the v10 integration checks for the machine-free
derivation (Proposition prop:cupsquare and its provenance updates)."""
import re
import sys
from collections import Counter

PATHS = {
    "INST": "/home/z/my-project/channel-supp-augmented/manuscript uploads v10/instruments-paper-revised10.txt",
    "MAIN": "/home/z/my-project/channel-supp-augmented/manuscript uploads v10/main-article-revised10.txt",
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

    labels = set(re.findall(r'\\label\{([^}]+)\}', text))
    refs = set(re.findall(r'\\(?:ref|autoref|eqref)\{([^}]+)\}', text))
    dangling = sorted(refs - labels)
    check(name, not dangling, f"dangling refs: {dangling[:8] if dangling else 'none'}")
    dups = [l for l in labels if text.count(f'\\label{{{l}}}') > 1]
    check(name, not dups, f"duplicate labels: {dups[:8] if dups else 'none'}")

    cite_grps = CITE_RE.findall(text)
    cited_keys = set(k.strip() for c in cite_grps for k in c.split(','))
    bibitems = set(re.findall(r'\\bibitem\{([^}]+)\}', text))
    uncited = sorted(bibitems - cited_keys)
    missbib = sorted(cited_keys - bibitems)
    check(name, not missbib, f"cite keys w/o bibitem: {missbib[:8] if missbib else 'none'}")
    print(f"      (bibitems never cited: {uncited if uncited else 'none'})")
    check(name, not uncited, f"bibitems never cited: {uncited if uncited else 'none'}")

    envs = re.findall(r'\\begin\{(\w+)\}', text)
    ends = re.findall(r'\\end\{(\w+)\}', text)
    be, en = Counter(envs), Counter(ends)
    diff = {k: (be.get(k, 0), en.get(k, 0)) for k in set(be) | set(en)
            if be.get(k, 0) != en.get(k, 0)}
    check(name, not diff, f"begin/end mismatches: {diff if diff else 'none'}")

    ndb, nde = text.count('\\['), text.count('\\]')
    check(name, ndb == nde, f"\\[ = {ndb}, \\] = {nde}")
    t2 = text.replace('\\$', '')
    nd = len(re.findall(r'(?<!\\)\$', t2))
    check(name, nd % 2 == 0, f"unescaped $ count = {nd} (even?)")

    nonascii = set(ch for ln in lines for ch in ln if ord(ch) > 127)
    check(name, not nonascii, f"non-ASCII: {sorted(nonascii)[:10] if nonascii else 'none'}")

    nl, nr = text.count('\\left'), text.count('\\right')
    check(name, nl == nr, f"\\left = {nl}, \\right = {nr}")

I, M = texts["INST"], texts["MAIN"]

print(f"\n{'='*70}\nV10 INTEGRATION CHECKS (the machine-free derivation)\n{'='*70}")
# the new proposition
check("V10", "\\label{prop:cupsquare}" in I, "Proposition prop:cupsquare present")
check("V10", I.count("prop:cupsquare") >= 6, "prop:cupsquare referenced >= 6 times "
      "(lemma proof, remark, lit-remark, open problems, intro, conclusion)")
check("V10", "The cup square on the flag quotient: a hand derivation" in I,
      "the proposition title renders")
for step in ["Step 0 (the homogeneous-space model)", "Step 1 (the fibration",
             "Step 2 (the cohomology of $BK$", "Step 3 (the torsion product rule)",
             "Step 4 (the transgression values)", "Step 5 (the run",
             "Step 6 (the edge)", "Step 7 (the remaining degrees)"]:
    check("V10", step in I, f"proof step present: {step[:34]}")
check("V10", "d_4(z_3)=\\sigma_2+2\\tau^2" in I, "the pinned transgression value "
      "d_4(z_3) = sigma_2 + 2 tau^2")
check("V10", "finite-order element never lies in" in I, "the torsion-survival "
      "argument present")
check("V10", "regular representation\n$1\\oplus\\omega\\oplus\\omega^2$" in I
      or "regular representation $1\\oplus\\omega\\oplus\\omega^2$" in I,
      "the regular-representation Chern computation present")
check("V10", "H^*(BK;\\mathbb Z)_{\\mathrm{free}}" in I, "the free-part "
      "identification of H^*(BK) present")
check("V10", "bidegree $(2k,6a)$" in I, "the torsion-slot description present")
Inorm = I.replace("\n", " ")
check("V10", "the $q>0$ slots map to zero" in Inorm, "the splitting-section "
      "vanishing argument present")
# the HatcherSS citation
check("V10", "\\bibitem{HatcherSS}" in I, "HatcherSS bibitem present")
cited_h = any("HatcherSS" in [x.strip() for x in g.split(',')]
              for g in CITE_RE.findall(I))
check("V10", cited_h, "HatcherSS is cited")
# the lemma's new decision text
check("V10", "The decision between the two worlds is now\nsupplied by hand" in I
      or "The decision between the two worlds is now supplied by hand" in I
      or "supplied by hand" in I, "the hand-decision sentence present")
check("V10", "The decision between the two worlds is supplied\nby the machine "
      "computation" not in I and "worlds is supplied by the machine computation"
      not in I, "the OLD machine-decision sentence is gone")
check("V10", "independently certifies the same\nconclusion" in I
      or "independently certifies the same conclusion" in I.replace("\n", " "),
      "the machine cross-check sentence present in the lemma proof")
# rem:machine-certificate rewrite
mc = I[I.find('label{rem:machine-certificate}'):I.find('label{rem:machine-certificate}') + 7000]
check("V10", "is derived by hand" in mc, "rem:machine-certificate opens with "
      "the hand-derivation provenance")
check("V10", "three mutually\nindependent routes" in mc
      or "three mutually independent routes" in mc.replace("\n", " "),
      "the three-routes closing present")
check("V10", "$D^2=0$ coherence check" in mc, "the script-verification "
      "mention present")
check("V10", "SU(2)/C_3" in mc, "the lens model case validation present")
# rem:flag-literature update
fl = I[I.find('label{rem:flag-literature}'):I.find('label{rem:flag-literature}') + 3300]
check("V10", "integral lift of the transgression route" in fl.replace("\n", " "),
      "rem:flag-literature names the integral lift")
# open problem (vi) discharged
check("V10", "[closed in this version]" in I, "open problem (vi) discharged")
check("V10", "the premise now rests on two independent implementations" not in I,
      "the stale (vi) phrasing gone")
# phrase updates
check("V10", "hand-derived, machine-certified, and independently re-implemented"
      in I, "INST updated provenance phrase (intro/conclusion)")
check("V10", "hand derivation of the integral cohomology of the cyclic flag "
      "quotient" in I.replace("\n", " ").replace("\n", " "),
      "INST abstract phrase updated")
check("V10", "hand-derived, machine-certified, and independently re-"
      "implemented" in M.replace("\n", " "),
      "MAIN sync clauses updated")
check("V10", "machine-certified and independently re-implemented" not in M
      .replace("\n", " ").replace("hand-derived, ", ""),
      "MAIN has no stale un-updated sync clause")
# v9 checks that must still hold
check("V10", "Flag-Quotient Width Obstructions" in I, "INST title intact")
check("V10", "flag manifolds; equivariant cohomology" in I, "INST keywords intact")
check("V10", "cite[Corollary~2]{NechitaEtAl2018}" in M, "MAIN Nechita cite intact")
# the tuple statement in the proposition
check("V10", "\\bigl(\\mathbb Z,\\ 0,\\ \\mathbb Z/3,\\ \\mathbb Z/3,\\\n"
      " \\ \\mathbb Z/3,\\ \\mathbb Z/3,\\ \\mathbb Z\\bigr)" in I
      or "(\\mathbb Z,\\ 0,\\ \\mathbb Z/3,\\ \\mathbb Z/3," in I,
      "the cohomology tuple stated in the proposition")
# the bibliography ordering: HatcherSS before GuerraJana2025 (citation order)
ih, ig = I.find("\\bibitem{HatcherSS}"), I.find("\\bibitem{GuerraJana2025}")
check("V10", 0 < ih < ig, "HatcherSS bibitem in citation order before GuerraJana2025")

print(f"\n{'='*70}\nRESULT: {len(FAIL)} failures" + ("" if not FAIL else f"\n{FAIL}"))
sys.exit(1 if FAIL else 0)
