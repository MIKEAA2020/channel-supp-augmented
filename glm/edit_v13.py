#!/usr/bin/env python3
"""Wave 34 edit script: fold W33 findings F1/F2 into the instruments paper and
strip the change-log / diary / meta-commentary language from BOTH manuscripts.

Inputs (current state):
  manuscript uploads v12/instruments-paper-revised12.tex   (instruments v12)
  manuscript uploads v10/main-article-revised10.tex        (main v10)

Outputs (new state, one wave folder):
  manuscript uploads v13/instruments-paper-revised13.tex + .txt  (instruments v13)
  manuscript uploads v13/main-article-revised11.tex      + .txt  (main v11)

Every replacement is anchored and asserted to match exactly once.
"""
import os, sys, shutil

REPO = "/home/z/my-project/channel-supp-augmented"
SRC_INST = os.path.join(REPO, "manuscript uploads v12", "instruments-paper-revised12.tex")
SRC_MAIN = os.path.join(REPO, "manuscript uploads v10", "main-article-revised10.tex")
OUT_DIR = os.path.join(REPO, "manuscript uploads v13")

def apply(text, old, new, label):
    n = text.count(old)
    assert n == 1, f"[{label}] anchor count = {n} (expected 1)\nANCHOR: {old[:120]!r}"
    return text.replace(old, new)

# =====================================================================
# INSTRUMENTS PAPER: v12 -> v13
# =====================================================================
inst = open(SRC_INST).read()
orig_len = len(inst)

# ---- A. F1 (Wave 33, Step 1 of prop:cupsquare): ---------------------
# (i) lead-in word: "boundaries" conflates boundaries with non-cycles
#     (the degree-9 free classes and the residual degree-8 classes die as
#     non-cycles, not boundaries) -> "killed";
# (ii) forward-dependency marker for sigma/tau and the transgression values
#      used 38 lines before their definitions.
inst = apply(inst,
"there are boundaries before the $E_8$-page. In fibre degree nine,",
"there are killed before the $E_8$-page (the classes $\\sigma_1$, $\\sigma_2$,\n"
"$\\tau$ and the transgression values invoked here are established in\n"
"Steps~2--4 below). In fibre degree nine,",
"F1 Step-1")

# ---- B. F2 (Wave 33, Step 7 of prop:cupsquare): ---------------------
# lift-independence half-clause: the tau^3-tail ambiguity of the orbit-sum
# lifts dies with the torsion in the quotient (2 tau^3 = 0), so the quotient
# and the discriminant's position in it are lift-independent.
inst = apply(inst,
"$\\tau^3$ dies because $2\\tau^3=0$ forces it (two is invertible modulo\n"
"three), and the top class is the orbit sum $S_1$, in which the discriminant",
"$\\tau^3$ dies because $2\\tau^3=0$ forces it (two is invertible modulo\n"
"three) --- taking with it the $\\tau^3$-tail ambiguity of the orbit-sum\n"
"lifts (Step~3), so that the quotient and the discriminant's position in it\n"
"are lift-independent --- and the top class is the orbit sum $S_1$, in which\n"
"the discriminant",
"F2 Step-7")

# ---- C. Remnant strips (change-log / diary / meta-commentary): ------

# C1. Abstract: implementation-summary clause -> factual statement.
inst = apply(inst,
"the qutrit exactly $4/3$ at both --- the second-index results through the integral cohomology of the cyclic flag quotient, computed by an exact-integer equivariant battery and reproduced by an independent re-implementation.",
"the qutrit exactly $4/3$ at both, the second-index result resting on the integral cohomology of the cyclic flag quotient.",
"C1 abstract")

# C2. Introduction: same family, formalised.
inst = apply(inst,
"the latter through a hand derivation of the integral cohomology of the cyclic flag quotient by a Chern-transgression computation, cross-checked by an exact-integer equivariant battery and an independent re-implementation (Theorems~",
"the latter through a Chern-transgression derivation of the integral cohomology of the cyclic flag quotient, cross-checked by an independent exact-integer machine computation (Theorems~",
"C2 intro")

# C3. Phantom reference: "earlier five-outcome counterexample" (superseded
#     earlier-version content) dropped.
inst = apply(inst,
"(an elementary median\nmatching bound at $r=1$, upgraded from the earlier five-outcome counterexample to the\ncoordinate flags $(j,k)$ and the constant $2(q-1)/q$)",
"(an elementary median\nmatching bound at $r=1$ on the coordinate flags $(j,k)$, with the constant $2(q-1)/q$)",
"C3 five-outcome")

# C4. Section-5 survey: triple verification-qualification dropped.
inst = apply(inst,
"(Theorem~\\ref{thm:equal-basis-plane}, proved through the cohomology of the flag quotient --- hand-derived, machine-certified, and independently re-implemented; Lemma~\\ref{lem:flag-cohomology} and Proposition~\\ref{prop:cupsquare})",
"(Theorem~\\ref{thm:equal-basis-plane}, proved through the cohomology of the flag quotient; Lemma~\\ref{lem:flag-cohomology} and Proposition~\\ref{prop:cupsquare})",
"C4 equal-basis-plane")

# C5. cor:flat-fails: "the corrected statement" (version history) dropped.
inst = apply(inst,
"is refuted at every output dimension, and the corrected statement is Conjecture~\\ref{con:coord-flat}.",
"is refuted at every output dimension, the expected complete statement being Conjecture~\\ref{con:coord-flat}.",
"C5 corrected-statement")

# C6. Internal wave comment in the source.
inst = apply(inst,
"% ---- Wave 7 block: equal-value orthonormal bases and the state-space bottom widths ----",
"% ---- Equal-value orthonormal bases and the state-space bottom widths ----",
"C6 wave7 comment")

# C7. Proposition title: self-referential "a hand derivation" subtitle dropped.
inst = apply(inst,
"\\begin{proposition}[The cup square on the flag quotient: a hand derivation]",
"\\begin{proposition}[The cup square on the flag quotient]",
"C7 prop title")

# C8. lem:flag-cohomology proof: "now supplied by hand" + "in front of us".
inst = apply(inst,
"The decision between the two worlds is now\nsupplied by hand. Proposition~\\ref{prop:cupsquare} proves $x^2\\ne0$ by an\nintegral transgression computation, independent of the Cartan--Leray page in\nfront of us; and",
"The decision between the two worlds is\nsupplied by Proposition~\\ref{prop:cupsquare}, which proves $x^2\\ne0$ by an\nintegral transgression computation independent of the present Cartan--Leray\npage; and",
"C8 two-worlds")

# C9. End of the same proof: machine cross-reference, formalised.
inst = apply(inst,
"The machine computation recorded in\nRemark~\\ref{rem:machine-certificate} independently certifies the same\nconclusion and agrees with the full cohomology tuple of\nProposition~\\ref{prop:cupsquare}.",
"The independent machine computation recorded in\nRemark~\\ref{rem:machine-certificate} confirms the same conclusion and agrees\nwith the full cohomology tuple of Proposition~\\ref{prop:cupsquare}.",
"C9 proof-end cross-ref")

# C10. The remark rem:machine-certificate itself: full formal rewrite
#      (title, "derived by hand", "battery", "stress-tested",
#      "Residuals, stated plainly", "the earlier audit", "began as one
#      implementation and has since been", "now doubly implemented",
#      "one a reader can check line by line", "the code, the battery").
START = "\\begin{remark}[The machine certificate behind Lemma~\\ref{lem:flag-cohomology}]"
END = "\\end{remark}"
i0 = inst.find(START)
i1 = inst.find(END, i0)
assert i0 != -1 and i1 != -1 and inst.count(START) == 1, "C10 remark block not located"
old_block = inst[i0:i1 + len(END)]
new_block = """\\begin{remark}[The computational verification of Lemma~\\ref{lem:flag-cohomology}]
\\label{rem:machine-certificate}
The proof of Lemma~\\ref{lem:flag-cohomology} is analytic: its decision input
$x^2\\ne0$ is Proposition~\\ref{prop:cupsquare}, whose transgression
computation uses only cited classical results (the cohomology of
$U(3)$ and $BU(3)$, Borel's transgression, and the cyclic cohomology of finite
modules \\cite{MilnorStasheff1974,HatcherSS,Brown1982}) plus a self-contained
invariant-theory step. An independent machine computation, described in this
remark, cross-checks the conclusion: it determines the integral homology of
$B$ directly and agrees with the full cohomology tuple of
Proposition~\\ref{prop:cupsquare}.

The homology of $B$ was computed from a free
$\\mathbb Z/3$-equivariant finite cellulation of $\\mathrm{Fl}$ with
$14\\,910$ cells, constructed on the boundary stratification of the
unistochastic region of the three-dimensional unitary group (a two-sheet book
over the stratified base, seam-subdivided). The certification consists of
exact integer arithmetic on that complex: cell counts and Euler
characteristic $\\chi(\\mathrm{Fl})=6=3\\,\\chi(B)$; $\\partial^2=0$ on every
cell; the induced action $T$ satisfies $T^3=\\mathrm{id}$ and
$\\partial T=T\\partial$; the action is free; the cover homology is the
classical one, $H_*(\\mathrm{Fl})=(\\mathbb Z,0,\\mathbb Z^2,0,\\mathbb Z^2,0,
\\mathbb Z)$, with vanishing torsion at the primes $2,3,5,7$; and the orbit
complex of $B$ satisfies $\\bar\\partial^2=0$, from which the Smith normal
forms of the orbit boundary matrices pin every slot,
$H_*(B)=(\\mathbb Z,\\mathbb Z/3,\\mathbb Z/3,\\mathbb Z/3,\\mathbb Z/3,0,\\mathbb
Z)$, with the torsion exponents fixed ($H_2=H_3=H_4=\\mathbb Z/3$, no
$\\mathbb Z/9$ summands) and no further torsion at any prime $p\\le61$. The
computation is anchored externally at four independent points: the
Poincar\\'e polynomial of $\\mathrm{Fl}=U(3)/U(1)^3$; $H_1(B)=\\mathbb Z/3$,
which Cartan--Leray forces for any free $\\mathbb Z/3$-quotient of the simply
connected $\\mathrm{Fl}$; $\\chi(\\mathrm{Fl})=3\\chi(B)$; and the palindromic
universal-coefficient ladder of $H_*(B)$. The decision logic of the lemma
--- the reading of $d_3^{1,2}$ off the certified cohomology, and the
Euler-class arithmetic of Theorem~\\ref{thm:equal-basis-plane} below --- was
checked against two externally known model cases: the lens space
$L(3;1,1,1)$, where $x^2\\ne0$ and $d_3^{1,2}=0$, and
$\\mathbb{RP}^2\\times S^2$, where $x^2=0$ and $d_3^{1,2}$ is an isomorphism;
in both, the direct homology, the spectral-sequence page, and the cup-square
computation agree.

Three qualifications remain. First, the arithmetic of
Proposition~\\ref{prop:cupsquare} rests on three cited classical inputs ---
Borel's transgression computation for the universal bundle, the Chern-root
restriction, and the cyclic cohomology of finite modules --- and its
internal bookkeeping (the orbit counts, the orbit-sum invariant lattice
together with its finite index over the symmetric-function module, the
twice-a-generator position of the discriminant in the top class, the torsion
product rule, the Chern classes of the regular representation, and the
Leibniz-signed page bookkeeping, including the $D^2=0$ coherence check) is
verified by an exact-integer computation; the transgression mechanism itself
reproduces the classical cohomology on the model fibration
$SU(2)\\to SU(2)/C_3\\to BC_3$, where the same differential structure
($d_4(z_3)=2u^2$, the second Chern class of the regular representation)
yields $H^*(L(3;1);\\mathbb Z)=
(\\mathbb Z,0,\\mathbb Z/3,\\mathbb Z)$ with the transfer edge
$\\pi^*[L]^*=3[S^3]^*$. Second, the cellulation was implemented twice
independently, the second implementation following the design specification
with different algorithms at every layer (phase measurement by column ratios
rather than a joint gauge solve, Newton inversions, sign derivation by
constraint propagation from $\\partial T=T\\partial$, direct $\\mathbb Z/12$
elimination rather than the Chinese-remainder route, and an incremental
subgroup-order computation of the $\\mathbb Z/9$ ladder); the two
implementations agree on every input datum and on the homology tuple, and
the convention data of the construction is forced by the certification (each
falsified variant breaks either the equivariance certificate or the orbit
homology). Third, the geometric identification with the flag quotient is
warranted by the construction lineage and the certification, not by an
explicit diffeomorphism, and the prime scan is finite, covering $p\\le 31$
across the two implementations. The premise of
Lemma~\\ref{lem:flag-cohomology} is thus carried by three mutually
independent routes --- the analytic derivation, the cellulation, and its
independent re-implementation --- which agree on the tuple. The code and
the full transcripts of both computations are available in the public
repository.\\footnote{\\url{https://github.com/MIKEAA2020/channel-supp-augmented}}
\\end{remark}"""
inst = inst[:i0] + new_block + inst[i1 + len(END):]
print("C10 remark rewrite: -%d / +%d chars" % (len(old_block), len(new_block)))

# C11. rem:flag-literature: "hand derivation" -> "derivation".
inst = apply(inst,
"The hand derivation of Proposition~\\ref{prop:cupsquare} is the",
"The derivation of Proposition~\\ref{prop:cupsquare} is the",
"C11 flag-lit hand")

# C12. rem:flag-literature closing: "now doubly implemented" dropped.
inst = apply(inst,
"The machine certificate of\nRemark~\\ref{rem:machine-certificate}, now doubly implemented, remains\ncomplementary to, not subsumed by, that programme.",
"The computational verification of\nRemark~\\ref{rem:machine-certificate} remains complementary to, not subsumed\nby, that programme.",
"C12 doubly")

# C13. Phantom "earlier trace-mass threshold" (not stated anywhere in the
#      paper) dropped; the internal pinching-threshold comparison stays.
inst = apply(inst,
"improving the\ntwo-sector pinching threshold $nQ_2(2)-1=2n-1$ and the earlier trace-mass threshold\n$r=n$);",
"improving the\ntwo-sector pinching threshold $nQ_2(2)-1=2n-1$);",
"C13 trace-mass")

# C14. Version reference in rem:flat-status.
inst = apply(inst,
"; the two\none-outcome cases left bracketed in the previous version are closed in the negative\ndirection --- the qutrit state space has",
"; the one-outcome\nstate spaces are non-flat, the qutrit having",
"C14 previous version")

# C15. Change-log "now".
inst = apply(inst,
"and at $r=2$ this requirement now fails certifiably for every",
"and at $r=2$ this requirement fails for every",
"C15 now fails")

# C16. "in its corrected form" (version history) dropped.
inst = apply(inst,
"Conjecture~\\ref{con:coord-flat}, in its corrected form, states the expected complete",
"Conjecture~\\ref{con:coord-flat} states the expected complete",
"C16 corrected form")

# C17. The conjecture-history diary passage (two superseded earlier forms of
#      the conjecture narrated) removed; the surviving mathematical facts
#      (flat direction proved for d_B in {1,2}; fails at r in {1,2} for
#      d_B >= 3) are already stated in the retained sentence.
inst = apply(inst,
"): the conjecture has been corrected twice, each time by a state-space result. The first form, without the clause $r\\ge2$, predicted $\\delta_1=1$ on the one-outcome bodies with $nd_B\\le4$, i.e. exactly the two residual state-space cases, and is refuted --- the qutrit has $\\delta_1=4/3$ exactly and the ququart at least $4/3$. The second form, with the clause $r\\ge2$, predicted $\\delta_2=1$ on the one-outcome qutrit ($nd_B=3\\le2\\cdot2+2$), and is refuted by Theorem~\\ref{thm:state-d2} --- the qutrit has $\\delta_2=4/3$ exactly --- which is why the clause now reads $r\\ge3$. The content of the conjecture is therefore",
"). The content of the conjecture is therefore",
"C17 conjecture diary")

# C18. Conclusion survey: triple qualification dropped (same family as C4).
inst = apply(inst,
"(Theorem~\\ref{thm:state-d2}, proved through the cohomology of the flag quotient --- hand-derived, machine-certified, and independently re-implemented; Lemma~\\ref{lem:flag-cohomology} and Proposition~\\ref{prop:cupsquare})",
"(Theorem~\\ref{thm:state-d2}, proved through the cohomology of the flag quotient; Lemma~\\ref{lem:flag-cohomology} and Proposition~\\ref{prop:cupsquare})",
"C18 conclusion triple")

# C19. Conclusion: "the corrected coordinate Conjecture" -> "the coordinate
#      Conjecture" (version history dropped).
inst = apply(inst,
"--- and the corrected coordinate Conjecture~\\ref{con:coord-flat} covering",
"--- and the coordinate Conjecture~\\ref{con:coord-flat} covering",
"C19 corrected conj")

# C20. Open problems: (v) "corrected" dropped; "now" dropped.
inst = apply(inst,
"(v) settle the corrected coordinate flat-widths Conjecture~\\ref{con:coord-flat}",
"(v) settle the coordinate flat-widths Conjecture~\\ref{con:coord-flat}",
"C20(v) corrected")
inst = apply(inst,
"of which the smallest, $\\delta_2$ of the qutrit, is now exactly $4/3$",
"of which the smallest, $\\delta_2$ of the qutrit, is exactly $4/3$",
"C20(v) now")

# C21. Open problems: item (vi) is a change-log entry ("[closed in this
#      version] ... posed as an open problem in earlier versions ...") --
#      replaced by the genuinely open research direction, stated formally.
inst = apply(inst,
"(vi) [closed in this version] the hand derivation of the cohomology of the flag quotient $B$ posed as an open problem in earlier versions is supplied by Proposition~\\ref{prop:cupsquare}, whose transgression computation removes the last computational premise of Theorem~\\ref{thm:state-d2}; the machine certificate (Remark~\\ref{rem:machine-certificate}) is retained as an independent cross-check, and the remaining research direction in its neighbourhood is the unstable integral cohomology of the symmetric-group quotients themselves, where the field-coefficient algorithms of Ref.~\\cite{GuerraJana2025} leave the torsion layers open;",
"(vi) determine the unstable integral cohomology of the symmetric-group quotients themselves, where the field-coefficient algorithms of Ref.~\\cite{GuerraJana2025} leave the torsion layers open --- the transgression computation of Proposition~\\ref{prop:cupsquare} settles the integral cohomology of the cyclic intermediate quotient $B$, with the computational verification of Remark~\\ref{rem:machine-certificate} as an independent cross-check, but neither addresses the symmetric-group quotients;",
"C21 open (vi)")

# =====================================================================
# MAIN ARTICLE: v10 -> v11
# =====================================================================
main = open(SRC_MAIN).read()

# M1. Abstract: verification-workflow clause dropped.
main = apply(main,
"the qutrit sitting exactly at $4/3$ there, through a flag-quotient computation that is hand-derived, machine-certified, and independently re-implemented.",
"the qutrit sitting exactly at $4/3$ there, through a flag-quotient cohomology computation.",
"M1 abstract")

# M2. Open problems: the companion's plane-valued extension described without
#     the verification triple; "that premise" (whose antecedent was removed)
#     -> "that extension".
main = apply(main,
", whose homological premise is hand-derived, machine-certified, and independently re-implemented, likewise bounds",
" likewise bounds",
"M2a triple")
main = apply(main,
"the cyclic flag quotient underlying that premise sits between",
"the cyclic flag quotient underlying that extension sits between",
"M2b premise")

# =====================================================================
# Write outputs (.tex and identical .txt twins)
# =====================================================================
os.makedirs(OUT_DIR, exist_ok=True)
out_inst = os.path.join(OUT_DIR, "instruments-paper-revised13.tex")
out_main = os.path.join(OUT_DIR, "main-article-revised11.tex")
open(out_inst, "w").write(inst)
open(out_inst.replace(".tex", ".txt"), "w").write(inst)
open(out_main, "w").write(main)
open(out_main.replace(".tex", ".txt"), "w").write(main)

delta_i = len(inst) - orig_len
print()
print("instruments v13 written: %d chars (delta %+d)" % (len(inst), delta_i))
print("main v11 written:        %d chars" % len(main))

# quick global sanity: no diary phrases remain
forbidden = [
    "hand-derived, machine-certified", "equivariant battery", "the earlier audit",
    "now doubly implemented", "has since been", "previous version", "earlier versions",
    "corrected twice", "[closed in this version]", "in its corrected form",
    "the corrected statement", "the corrected coordinate", "stress-tested",
    "Residuals, stated plainly", "a hand derivation", "Wave 7 block",
    "trace-mass threshold", "five-outcome counterexample", "the machine certificate",
    "supplied by hand", "certification battery",
]
for phrase in forbidden:
    ci, cm = inst.count(phrase), main.count(phrase)
    assert ci == 0 and cm == 0, f"forbidden phrase still present: {phrase!r} (inst={ci}, main={cm})"
print("forbidden-phrase scan: CLEAN (both papers, %d phrases)" % len(forbidden))
print("OK")
