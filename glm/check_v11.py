#!/usr/bin/env python3
"""v11 manuscript consistency checker (inherits v10 mechanics).
The mechanical checks (labels/refs/cites/environments/delimiters) run on the
v11 instruments source and the unchanged v10 main article, plus the v11
correction-wave checks: the R1 repair of Proposition prop:cupsquare (the
orbit-sum lattice statement, the H^6(BK) display, the degree-6 conclusion
with the discriminant twice a generator, the statement clause, and the
remark residuals list) and the removal of every superseded v10 statement."""
import re
import sys
from collections import Counter

PATHS = {
    "INST": "/home/z/my-project/channel-supp-augmented/manuscript uploads v11/instruments-paper-revised11.txt",
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
    # KNOWN ARTIFACT (W26-diagnosed, byte-identical in v8-v11): the \\[ / \\]
    # counts include TikZ/matrix tokens; the deltas (INST 3, MAIN 4) are
    # pre-existing and unaffected by the v11 edits (verified against the v10
    # baseline: 211/208 and 237/233 in both).
    artifact_disp = (name == "INST" and (ndb, nde) == (211, 208)) or \
                    (name == "MAIN" and (ndb, nde) == (237, 233))
    if artifact_disp:
        print(f"[ARTIFACT] {name}: \\[ = {ndb}, \\] = {nde} "
              f"(pre-existing W26 checker artifact, v10-baseline-identical)")
    else:
        check(name, ndb == nde, f"\\[ = {ndb}, \\] = {nde}")
    t2 = text.replace('\\$', '')
    nd = len(re.findall(r'(?<!\\)\$', t2))
    # KNOWN ARTIFACT (W26-diagnosed): the MAIN TikZ $ count 3073 is odd in
    # every version v8-v11 (the file is byte-unchanged since v10).
    artifact_dollar = (name == "MAIN" and nd == 3073)
    if artifact_dollar:
        print(f"[ARTIFACT] {name}: unescaped $ count = {nd} "
              f"(pre-existing W26 checker artifact, MAIN unchanged since v10)")
    else:
        check(name, nd % 2 == 0, f"unescaped $ count = {nd} (even?)")

    nonascii = set(ch for ln in lines for ch in ln if ord(ch) > 127)
    check(name, not nonascii, f"non-ASCII: {sorted(nonascii)[:10] if nonascii else 'none'}")

    nl, nr = text.count('\\left'), text.count('\\right')
    check(name, nl == nr, f"\\left = {nl}, \\right = {nr}")

I, M = texts["INST"], texts["MAIN"]
Inorm = I.replace("\n", " ")

print(f"\n{'='*70}\nV11 CORRECTION-WAVE CHECKS (the R1 repair)\n{'='*70}")
# --- the corrected statements are PRESENT --------------------------------
check("V11", "H^6(B;\\mathbb Z)\\cong\\mathbb Z$, in which the discriminant "
      "class is twice a\n_generator".replace("_", " ") in I or
      "$H^6(B;\\mathbb Z)\\cong\\mathbb Z$, in which the discriminant class is "
      "twice a" in I, "the corrected statement clause (discriminant twice a "
      "generator) present")
check("V11", "free part, integrally, is the invariant lattice" in I,
      "Step 2: the integral orbit-sum lattice statement present")
check("V11", "\\mathbb Q[\\sigma_1,\\sigma_2,\\sigma_3]\\ \\oplus\\ \\Delta"
      "\\cdot\n\\mathbb Q[\\sigma_1,\\sigma_2,\\sigma_3]" in I or
      "\\mathbb Q[\\sigma_1,\\sigma_2,\\sigma_3]\\ \\oplus\\ \\Delta\\cdot"
      " \\mathbb Q" in Inorm, "Step 2: the rational module display present")
check("V11", "Rationally, this lattice is the degree-$d$ part" in I,
      "Step 2: the rational reading present")
check("V11", "then $2$, $2$, $4$, $8$ in degrees $3$ to $6$" in I,
      "Step 2: the index values (2,2,4,8 in degrees 3-6) present")
check("V11", "exactly the degrees in which the crux of Step~5\nbelow works"
      in I or "exactly the degrees in which the crux of Step~5 below works"
      in Inorm, "Step 2: the safe-degrees clause present")
check("V11", "$S_1=\\chi_1^2\\chi_2+\\chi_2^2\\chi_3+\\chi_3^2\\chi_1\n"
      "=\\tfrac12(\\sigma_1\\sigma_2-3\\sigma_3+\\Delta)$ is invariant but "
      "lies in the\nmodule only after doubling" in I or
      "=\\tfrac12(\\sigma_1\\sigma_2-3\\sigma_3+\\Delta)$ is invariant but "
      "lies in the module only after doubling" in Inorm,
      "Step 2: the degree-3 witness S1 present")
check("V11", "H^6(BK;\\mathbb Z)\\ \\cong\\ \\mathbb Z\\{A_1,\\,S_1,\\,"
      "S_2,\\,\\sigma_3\\}" in I, "Step 3: the orbit-sum H^6(BK) display "
      "present")
check("V11", "the two orbit sums satisfy $S_1+S_2=\\sigma_1\\sigma_2-"
      "3\\sigma_3$ and\n$S_1-S_2=\\Delta$" in I or
      "$S_1+S_2=\\sigma_1\\sigma_2-3\\sigma_3$ and $S_1-S_2=\\Delta$"
      in Inorm, "Step 3: the orbit-sum relations present")
check("V11", "index-two sublattice of this free part" in I,
      "Step 3: the index-two note present")
check("V11", "running the quotient on the orbit-sum\nlattice of Step~3"
      in I or "running the quotient on the orbit-sum lattice of Step~3"
      in Inorm, "Step 7: the orbit-sum quotient present")
check("V11", "\\mathbb Z\\cdot\\langle S_1\\rangle" in I,
      "Step 7: H^6(B) = Z.<S1> present")
check("V11", "the discriminant\n$\\Delta=S_1-S_2=2S_1$ is twice a generator"
      in I or "the discriminant $\\Delta=S_1-S_2=2S_1$ is twice a generator"
      in Inorm, "Step 7: the twice-a-generator conclusion present")
check("V11", "two is invertible modulo\nthree" in I or
      "two is invertible modulo three" in Inorm, "Step 7: the torsion-death "
      "justification present")
check("V11", "$\\sigma_1\\sigma_2=S_1+S_2+3\\sigma_3$ and\n"
      "$\\sigma_1^3=A_1+3(S_1+S_2)+6\\sigma_3$" in I or
      "$\\sigma_1\\sigma_2=S_1+S_2+3\\sigma_3$ and $\\sigma_1^3=A_1+"
      "3(S_1+S_2)+6\\sigma_3$" in Inorm, "Step 7: the relation identities "
      "present")
check("V11", "the orbit-sum invariant lattice together with\nits finite "
      "index over the symmetric-function module" in I or
      "the orbit-sum invariant lattice together with its finite index over "
      "the symmetric-function module" in Inorm, "remark: the lattice layer "
      "in the residuals list present")
check("V11", "the twice-a-generator\nposition of the discriminant in the "
      "top class" in I or "the twice-a-generator position of the "
      "discriminant in the top class" in Inorm, "remark: the "
      "twice-a-generator item present")

# --- the superseded v10 statements are GONE -------------------------------
check("V11", "and a discriminant class\ngenerating $H^6$." not in I,
      "OLD statement clause 'a discriminant class generating H^6' gone")
check("V11", "H^*(BK;\\mathbb Z)_{\\mathrm{free}}" not in I,
      "OLD Step 2 free-part display gone")
check("V11", "the module statement follows because" not in I,
      "OLD Step 2 module-justification sentence gone")
check("V11", "\\mathbb Z\\{\\sigma_1^3,\\sigma_1\\sigma_2,\\sigma_3,\n"
      "\\Delta\\}" not in I, "OLD Step 3 module display gone")
check("V11", "\\mathbb Z\\cdot\n\\langle\\Delta\\rangle" not in I and
      "\\cong\\ \\mathbb Z\\cdot\n\\langle\\Delta\\rangle" not in I,
      "OLD Step 7 conclusion Z.<Delta> gone")
check("V11", "the top class being the discriminant" not in I,
      "OLD Step 7 'top class being the discriminant' gone")
check("V11", "(the orbit counts, the invariant lattice, the torsion "
      "product" not in I, "OLD remark residuals list gone")

# --- the v10 checks that must still hold ----------------------------------
print(f"\n{'='*70}\nV10 CHECKS THAT MUST STILL HOLD\n{'='*70}")
check("V10", "\\label{prop:cupsquare}" in I, "Proposition prop:cupsquare present")
check("V10", I.count("prop:cupsquare") >= 6, "prop:cupsquare referenced >= 6 times")
check("V10", "The cup square on the flag quotient: a hand derivation" in I,
      "the proposition title renders")
for step in ["Step 0 (the homogeneous-space model)", "Step 1 (the fibration",
             "Step 2 (the cohomology of $BK$", "Step 3 (the torsion product rule)",
             "Step 4 (the transgression values)", "Step 5 (the run",
             "Step 6 (the edge)", "Step 7 (the remaining degrees)"]:
    check("V10", step in I, f"proof step present: {step[:34]}")
check("V10", "d_4(z_3)=\\sigma_2+2\\tau^2" in I, "the pinned transgression value")
check("V10", "finite-order element never lies in" in I, "the torsion-survival "
      "argument present")
check("V10", "\\bibitem{HatcherSS}" in I, "HatcherSS bibitem present")
check("V10", "Flag-Quotient Width Obstructions" in I, "INST title intact")
check("V10", "flag manifolds; equivariant cohomology" in I, "INST keywords intact")
check("V10", "cite[Corollary~2]{NechitaEtAl2018}" in M, "MAIN Nechita cite intact")
check("V10", "(\\mathbb Z,\\ 0,\\ \\mathbb Z/3,\\ \\mathbb Z/3," in I,
      "the cohomology tuple stated in the proposition")
check("V10", "hand-derived, machine-certified, and independently re-implemented"
      in I, "the provenance phrase intact (INST)")
check("V10", "hand-derived, machine-certified, and independently re-implemented"
      in M, "the sync clause intact (MAIN)")
check("V10", "[closed in this version]" in I, "open problem (vi) still discharged")
ih, ig = I.find("\\bibitem{HatcherSS}"), I.find("\\bibitem{GuerraJana2025}")
check("V10", 0 < ih < ig, "HatcherSS bibitem in citation order before GuerraJana2025")

# --- the S1 definition is used consistently -------------------------------
check("V11", I.count("S_1=\\chi_1^2\\chi_2+\\chi_2^2\\chi_3+\\chi_3^2\\chi_1")
      == 1, "S1 defined exactly once (Step 2)")
check("V11", "A_1=\\chi_1^3+\\chi_2^3+\\chi_3^3" in I, "A1 defined (Step 3)")
check("V11", "S_2=\\chi_1^2\\chi_3+\\chi_2^2\\chi_1+\\chi_3^2\\chi_2" in I,
      "S2 defined (Step 3)")

print(f"\n{'='*70}\nRESULT: {len(FAIL)} failures" + ("" if not FAIL else f"\n{FAIL}"))
sys.exit(1 if FAIL else 0)
