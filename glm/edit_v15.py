#!/usr/bin/env python3
"""Wave 36 edit script: the two figure-positioning repairs.

(1) INSTRUMENTS paper, Figure fig:flag-fibration: the annotation
    'classifies U(3)->U(3)/K' superimposed on the shaft of the curved
    gamma arrow (measured: the curve crosses the label band diagonally
    through 439 label-bbox pixels).  A one-line 34.4mm x 5.8mm label has
    NO collision-free slot below the gamma belly (the corridor between
    the belly, the pi curve, the BC_3 node, and the kappa curve is
    7.7-9.0mm tall versus the 7.5mm needed incl. margins - rasterised
    free-placement search: 0 candidates below, 391 above).  Fix: move
    the label into the whitespace ABOVE the gamma curve, centred
    (5.0,-0.42), directly above the gamma symbol - adjacent to the
    arrow it describes, in clear whitespace.

(2) MAIN article, Figure fig:replacement-join: the lowest box (the
    block-diagonal flagged-space box) crossed the orthogonal-join arrow
    to its right.  Root cause (measured): the box grew to 73.1mm wide
    (text-driven, past its 56mm design minimum), so its east edge
    (+36.6mm) passed the arrow's turning abscissa (+33.2mm), while the
    turning height (J.north) sits 1.5mm BELOW the box's top edge because
    J is positioned on the box's centreline - both arrow segments cut
    the box's top-right region.  The crossing is translation-invariant
    (moving the box drags J and hence the turning height with it), so
    the repair is twofold: the box moves DOWN 3.5mm (as directed), and
    the arrow turns at +12mm from B.east (3.6mm clear of the box's east
    edge) so that its shaft and horizontal run stay above and outside
    the box; the 'orthogonal join' label moves with the horizontal run.

No text content changes: two node coordinates and one arrow route.
Same labels, same captions, same claims -> the no-new-claims gate holds
trivially (pure positioning).

Inputs (current state):
  manuscript uploads v14/instruments-paper-revised14.tex   (instruments v14)
  manuscript uploads v13/main-article-revised11.tex        (main v11)

Outputs (new state):
  manuscript uploads v15/instruments-paper-revised15.tex + .txt  (instruments v15)
  manuscript uploads v15/main-article-revised12.tex + .txt       (main v12)

Every replacement is anchored and asserted to match exactly once.
"""
import os, shutil

REPO = "/home/z/my-project/channel-supp-augmented"
SRC_INST = os.path.join(REPO, "manuscript uploads v14", "instruments-paper-revised14.tex")
SRC_MAIN = os.path.join(REPO, "manuscript uploads v13", "main-article-revised11.tex")
OUT_DIR = os.path.join(REPO, "manuscript uploads v15")

def apply(text, old, new, label):
    n = text.count(old)
    assert n == 1, f"[{label}] anchor count = {n} (expected 1)\nANCHOR: {old[:120]!r}"
    return text.replace(old, new)

# =====================================================================
# Instruments paper: move the gamma-annotation into the whitespace
# above the gamma curve (validated band for a one-line label: centres
# (5.0,-0.37)..(5.0,-0.47); -0.42 maximises the minimum clearance to
# the gamma symbol below and the B-iota arrow above).
# =====================================================================
inst = open(SRC_INST).read()

inst = apply(inst,
    "  \\node[font=\\scriptsize, text=gray!60!black] at (4.1,-1.42) {classifies $U(3)\\to U(3)/K$};",
    "  \\node[font=\\scriptsize, text=gray!60!black] at (5.0,-0.42) {classifies $U(3)\\to U(3)/K$};",
    "I1 gamma-annotation reposition")

# =====================================================================
# Main article, hunk 1: the flagged-space box moves down 3.5mm, to a
# deterministic centre placement (0,-53.8mm) - the box, the two flanking
# spheres, and the balanced-partitions note move together (all are
# positioned relative to the box).
# =====================================================================
main = open(SRC_MAIN).read()

main = apply(main,
    "% Flagged space - below B with more gap\n"
    "\\node[block, minimum width=56mm, minimum height=18mm, below=5mm of B] (FB) at (0,-36mm) "
    "{$\\bigoplus_i\\Herm(B_i)$: block-diagonal, $\\sum_i b_i^2$ real dim};",
    "% Flagged space - moved 3.5mm down and to a deterministic centre placement "
    "(clears the orthogonal-join arrow)\n"
    "\\node[block, minimum width=56mm, minimum height=18mm] (FB) at (0,-53.8mm) "
    "{$\\bigoplus_i\\Herm(B_i)$: block-diagonal, $\\sum_i b_i^2$ real dim};",
    "M1 flagged-space box lowered")

# =====================================================================
# Main article, hunk 2: the orthogonal-join arrow turns 12mm right of
# B.east (3.6mm clear of the box's 73.1mm-wide east edge) instead of
# 5mm (inside the box); its label rides above the horizontal run.
# =====================================================================
main = apply(main,
    "% Orthogonal join arrow - label clear of Rep box\n"
    "\\draw[->] (B.east) -- ++(5mm,0) |- (J.north) node[pos=0.25, below, xshift=1mm, font=\\scriptsize] {orthogonal join};",
    "% Orthogonal join arrow - turns right of the box's east edge; label above the horizontal run\n"
    "\\draw[->] (B.east) -- ++(12mm,0) |- (J.north) node[pos=0.86, above, font=\\scriptsize] {orthogonal join};",
    "M2 orthogonal-join arrow rerouted")

# =====================================================================
# Write the new wave folder
# =====================================================================
os.makedirs(OUT_DIR, exist_ok=True)
inst_out = os.path.join(OUT_DIR, "instruments-paper-revised15.tex")
main_out = os.path.join(OUT_DIR, "main-article-revised12.tex")
open(inst_out, "w").write(inst)
open(inst_out.replace(".tex", ".txt"), "w").write(inst)  # byte-identical mirror
open(main_out, "w").write(main)
open(main_out.replace(".tex", ".txt"), "w").write(main)  # byte-identical mirror

# pure-positioning gate: the only line-level differences are the three
# hunks; every other line byte-identical
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
difflines(SRC_INST, inst, "instruments v14 -> v15")
difflines(SRC_MAIN, main, "main v11 -> v12")
print("\nWrote:", inst_out)
print("Wrote:", main_out)
