#!/usr/bin/env python3
"""Wave 39 edit script: the keyword lines set to the six top keywords
per paper (user directive 2026-09-14: "for both papers, select 6 top
keywords"), continuing the unblind-labelled version line.

Both papers carry longer keyword lines (instruments: 10 entries; main:
9).  This wave trims each line to the six most representative entries,
SELECTED FROM THE EXISTING LISTS ONLY (no new keyword text coined):

  instruments v17 -> v18, keep (6 of 10):
      quantum instruments        -- the paper's object (title)
      diamond norm               -- the metric throughout
      compression width          -- the central quantity (title: Certified
                                    Compression Bounds)
      Chebyshev radius           -- the exact affine geometry / optimal
                                    centres (title: Optimal Centres)
      equivariant cohomology     -- the flag-quotient obstruction
                                    machinery (title: Flag-Quotient Width
                                    Obstructions)
      Borsuk--Ulam theorem       -- the antipodal obstruction engine
  dropped: antipodal profile; quantum measurements; flag manifolds;
      no-programming theorem (appendix-only material)

  main v14 -> v15, keep (6 of 9):
      quantum channel compression -- the problem statement (title level)
      diamond norm                 -- the metric (title: Exact Diamond
                                      Balls)
      antipodal width              -- the central obstruction concept
                                      (title: Antipodal Widths)
      exact in-radius              -- the exact-geometry headline
      nonlinear approximation      -- the mathematical lineage
                                      (DeVore--Howard--Micchelli/Pinkus,
                                      the abstract's framing sentence)
      Borsuk--Ulam theorem         -- the topological engine
  dropped: quantum combs (the cited adaptive-network framework; the
      query-uniform results are already indexed by "quantum channel
      compression"); flat-width dichotomy; flag-quotient cohomology
      (the companion's contributions, appearing here only as the
      input-independent specialisation summary)

ONE changed line per paper (a metadata trim of the keyword line only):
no prose, no mathematics, no figures, no captions, no labels, no refs
-> the no-new-claims gate holds trivially (front-matter metadata).
The line count of both files is unchanged, so compile-warning line
numbers are preserved for the wave-39 baseline comparison.

Inputs (current state, wave 38 output):
  manuscript uploads v17/instruments-paper-unblinded17.tex   (v17)
  manuscript uploads v17/main-article-unblinded14.tex       (v14)

Outputs (unblind-labelled file names continued):
  manuscript uploads v18/instruments-paper-unblinded18.tex + .txt  (v18)
  manuscript uploads v18/main-article-unblinded15.tex + .txt       (v15)

Every replacement is anchored and asserted to match exactly once.
"""
import os

REPO = "/home/z/my-project/channel-supp-augmented"
SRC_INST = os.path.join(REPO, "manuscript uploads v17", "instruments-paper-unblinded17.tex")
SRC_MAIN = os.path.join(REPO, "manuscript uploads v17", "main-article-unblinded14.tex")
OUT_DIR = os.path.join(REPO, "manuscript uploads v18")

def apply(text, old, new, label):
    n = text.count(old)
    assert n == 1, f"[{label}] anchor count = {n} (expected 1)\nANCHOR: {old[:120]!r}"
    return text.replace(old, new)

# =====================================================================
# Hunk 1 (each paper): the keyword line trimmed to the six top
# keywords -- a subset of the existing entries, order preserved.
# =====================================================================
OLD_KW_INST = ("\\noindent\\textbf{Keywords:} quantum instruments; diamond "
               "norm; compression width; antipodal profile; Chebyshev "
               "radius; quantum measurements; flag manifolds; equivariant "
               "cohomology; Borsuk--Ulam theorem; no-programming theorem.")
NEW_KW_INST = ("\\noindent\\textbf{Keywords:} quantum instruments; diamond "
               "norm; compression width; Chebyshev radius; equivariant "
               "cohomology; Borsuk--Ulam theorem.")

OLD_KW_MAIN = ("\\noindent\\textbf{Keywords:} quantum channel compression; "
               "diamond norm; antipodal width; exact in-radius; "
               "Borsuk--Ulam theorem; quantum combs; nonlinear "
               "approximation; flat-width dichotomy; flag-quotient "
               "cohomology.")
NEW_KW_MAIN = ("\\noindent\\textbf{Keywords:} quantum channel compression; "
               "diamond norm; antipodal width; exact in-radius; nonlinear "
               "approximation; Borsuk--Ulam theorem.")

# =====================================================================
# Apply
# =====================================================================
inst = open(SRC_INST).read()
inst = apply(inst, OLD_KW_INST, NEW_KW_INST, "I1 keyword line trimmed to six")

main = open(SRC_MAIN).read()
main = apply(main, OLD_KW_MAIN, NEW_KW_MAIN, "M1 keyword line trimmed to six")

# =====================================================================
# Write the new wave folder (unblind-labelled file names continued;
# byte-identical .txt mirrors, the house convention since v15).
# =====================================================================
os.makedirs(OUT_DIR, exist_ok=True)
inst_out = os.path.join(OUT_DIR, "instruments-paper-unblinded18.tex")
main_out = os.path.join(OUT_DIR, "main-article-unblinded15.tex")
open(inst_out, "w").write(inst)
open(inst_out.replace(".tex", ".txt"), "w").write(inst)  # byte-identical mirror
open(main_out, "w").write(main)
open(main_out.replace(".tex", ".txt"), "w").write(main)  # byte-identical mirror

# diff audit: every line-level difference must be the one keyword hunk
def difflines(a_path, b_text, name):
    a = open(a_path).read().splitlines()
    b = b_text.splitlines()
    import difflib
    d = [l for l in difflib.unified_diff(a, b, lineterm="", n=0)
         if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))]
    print(f"{name}: {len(d)} changed diff lines")
    for l in d:
        print("   ", l[:150])

print("=== diff audit ===")
difflines(SRC_INST, inst, "instruments v17 -> v18 (keyword line to six)")
difflines(SRC_MAIN, main, "main v14 -> v15 (keyword line to six)")
print("\nWrote:", inst_out)
print("Wrote:", main_out)
