#!/usr/bin/env python3
"""Wave 35 edit script: add the two merited figures and the two merited text
additions to the instruments paper (the flat-width phase diagram with its
operational reading; the fibration diagram with the proof guide).

Every addition is gated by the no-new-claims discipline: each figure element
and each sentence restates or instantiates a statement already present in the
paper (see WAVE35_FIGURES_AND_READINGS.md for the trace table).

Inputs (current state):
  manuscript uploads v13/instruments-paper-revised13.tex   (instruments v13)
  manuscript uploads v13/main-article-revised11.tex        (main v11, UNCHANGED)

Outputs (new state):
  manuscript uploads v14/instruments-paper-revised14.tex + .txt  (instruments v14)

Every replacement is anchored and asserted to match exactly once.
"""
import os, sys

REPO = "/home/z/my-project/channel-supp-augmented"
SRC_INST = os.path.join(REPO, "manuscript uploads v13", "instruments-paper-revised13.tex")
OUT_DIR = os.path.join(REPO, "manuscript uploads v14")
FIG_FIBRATION = "/home/z/my-project/scripts/w35_fibration_fig.tex"
FIG_PHASES = "/home/z/my-project/scripts/w35_phases_fig.tex"

def apply(text, old, new, label):
    n = text.count(old)
    assert n == 1, f"[{label}] anchor count = {n} (expected 1)\nANCHOR: {old[:120]!r}"
    return text.replace(old, new)

inst = open(SRC_INST).read()
orig_len = len(inst)

fig_fib = open(FIG_FIBRATION).read().rstrip("\n")
fig_pha = open(FIG_PHASES).read().rstrip("\n")

# =====================================================================
# Hunk 1: the fibration diagram (Figure fig:flag-fibration), placed in the
# running text immediately before Proposition prop:cupsquare.
# =====================================================================
inst = apply(inst,
"% ---- Second-index widths: the certified qutrit core ----\n\n"
"\\begin{proposition}[The cup square on the flag quotient]",
"% ---- Second-index widths: the certified qutrit core ----\n\n"
+ fig_fib + "\n\n"
"\\begin{proposition}[The cup square on the flag quotient]",
"H1 fibration figure")

# =====================================================================
# Hunk 2: the proof guide (text addition 2), inserted between the proof's
# opening paragraph and Step 0.
# =====================================================================
GUIDE = (
"The computation is organised in seven steps, and Figure~\\ref{fig:flag-fibration} "
"records the spaces and the maps used throughout. Step~0 trades the quotient "
"description $B=\\mathrm{Fl}/\\langle c\\rangle$ for the homogeneous-space model "
"$B=U(3)/K$. Step~1 replaces the cover by the Borel fibration with fibre $U(3)$ "
"and reduces the differentials of its Serre spectral sequence to the Chern "
"classes of the inclusion $\\iota\\colon K\\hookrightarrow U(3)$, extended by the "
"Leibniz rule. Steps~2--4 prepare the $E_2$-page: the integral cohomology of "
"$BK$ in Step~2, the product rule for the torsion class $\\tau$ in Step~3, and "
"the pinning of the three transgression constants through the splitting "
"section in Step~4. The crux is Step~5, in total degree four: the incoming "
"images kill the free summands and the fibre class $z_1z_3$, but the torsion "
"class $\\tau^2$ survives, and this survival, transferred by the edge "
"homomorphism in Step~6, is the assertion $x^2\\ne0$. Step~7 completes the "
"remaining degrees and exhibits the discriminant as twice a generator of the "
"top class.")

inst = apply(inst,
"the cohomology of the flag manifold and of\n"
"$BU(3)$, Borel's transgression computation, and the cyclic cohomology of\n"
"finite modules.\n\n"
"\\emph{Step 0 (the homogeneous-space model).}",
"the cohomology of the flag manifold and of\n"
"$BU(3)$, Borel's transgression computation, and the cyclic cohomology of\n"
"finite modules.\n\n"
+ GUIDE + "\n\n"
"\\emph{Step 0 (the homogeneous-space model).}",
"H2 proof guide")

# =====================================================================
# Hunk 3: the operational reading (text addition 1) + Hunk 4: the phase
# diagram (Figure fig:flat-regimes), placed after the conjecture discussion
# and before the worked example ex:222.
# =====================================================================
READING = (
"Figure~\\ref{fig:flat-regimes} displays the resulting regimes. The "
"classification admits a direct operational reading. The value $1$ is the "
"antipodal floor: the exact antipodal profile of the input-independent case "
"forces error at least $1$ throughout the subcritical range, so a flat width "
"means that the topological lower bound is attained --- the latent dimension "
"is as economical as the obstruction permits. The bound $\\delta_r\\ge4/3$ is a "
"fixed surcharge of one third above the floor, and its mechanism is visible "
"in the proofs of Theorems~\\ref{thm:state-nonflat} and~\\ref{thm:state-d2}: "
"every continuous real function, and at the second index every continuous "
"plane-valued map, takes a common value on some orthonormal basis "
"(Theorems~\\ref{thm:equal-basis} and~\\ref{thm:equal-basis-plane}), and the "
"decoder attached to that value under-weights one of the basis states by mass "
"at least $2/3$, the trace norm charging twice the missing mass. At the "
"qutrit the surcharge is exact at each of the first two latent dimensions, "
"and it is operationally detectable: by the discrimination formula of "
"Remark~\\ref{rem:operational}, an error of $4/3$ corresponds to a single-use "
"discrimination success probability of $5/6$, so every one- or "
"two-dimensional code of the qutrit state space leaves some state whose "
"coded reconstruction is distinguishable from it with probability at least "
"$5/6$.")

inst = apply(inst,
"there $\\delta_{n-1}=2(1-1/d_B)>1$.\n\n"
"\\begin{example}[$d_A=d_B=2$, $n=2$]",
"there $\\delta_{n-1}=2(1-1/d_B)>1$.\n\n"
+ READING + "\n\n"
+ fig_pha + "\n\n"
"\\begin{example}[$d_A=d_B=2$, $n=2$]",
"H3+H4 reading and phase figure")

# =====================================================================
# Write outputs (.tex and identical .txt twin)
# =====================================================================
os.makedirs(OUT_DIR, exist_ok=True)
out_inst = os.path.join(OUT_DIR, "instruments-paper-revised14.tex")
open(out_inst, "w").write(inst)
open(out_inst.replace(".tex", ".txt"), "w").write(inst)

delta_i = len(inst) - orig_len
print()
print("instruments v14 written: %d chars (delta %+d)" % (len(inst), delta_i))

# quick global sanity: no informal/diary phrases added; labels unique
forbidden = [
    "we believe", "we think", "in this version", "earlier version", "previous version",
    "hand-derived, machine-certified", "the earlier audit", "as noted above",
    "it is worth noting", "roughly speaking", "intuitively", "of course",
]
for phrase in forbidden:
    n = inst.count(phrase)
    assert n == 0, f"forbidden phrase present: {phrase!r} (count={n})"
for lab in ["fig:flag-fibration", "fig:flat-regimes"]:
    n_def = inst.count("\\label{" + lab + "}")
    n_ref = inst.count("Figure~\\ref{" + lab + "}")
    assert n_def == 1, f"label {lab}: {n_def} definitions"
    assert n_ref >= 1, f"label {lab}: {n_ref} references"
# every \ref target used in the new blocks exists
import re
labels = set(re.findall(r"\\label\{([^}]+)\}", inst))
for ref in re.findall(r"\\ref\{([^}]+)\}", inst):
    assert ref in labels, f"dangling \\ref{{{ref}}}"
print("forbidden-phrase scan + label sanity: CLEAN")
print("OK")
