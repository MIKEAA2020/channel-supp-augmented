#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WAVE 28 - PART 2: THE v9 MANUSCRIPT-ALIGNMENT EDIT.

Per the user directive: "update all manuscript sections, including title,
abstract, keywords and other sections to align with all surviving findings
and waves".  The surviving-findings delta since v8:
  * the WAVE 28 independent re-implementation (this wave): the machine
    premise of thm:state-d2 now rests on TWO implementations; the
    "not independently re-implemented" residual is stale; open problem
    (vi)'s re-implementation clause is discharged; the prime scan is now
    p <= 31 across the two implementations; the convention data is
    falsification-certified.
Title, abstract, keywords, the intro contributions, the specialisations
note, the lemma proof pointer, the machine-certificate remark, the
flag-literature remark, the conclusion, and the open problems are updated
in the instruments paper; the sync clause, keywords, and the abstract in
the main article.  The main title is already fully aligned with its own
surviving claims (all its theorems stand; the flag-quotient content is
companion-reported and lives in the open problems) -- recorded here, not
silently skipped.

Method: anchored replacements, each asserted to match the expected number
of times; v8 sources in "manuscript uploads v8", v9 written to
"manuscript uploads v9".
"""
import os
import shutil
import sys

SRC = "/home/z/my-project/channel-supp-augmented/manuscript uploads v8"
DST = "/home/z/my-project/channel-supp-augmented/manuscript uploads v9"
INST = "instruments-paper-revised8.txt"
MAIN = "main-article-revised8.txt"


def apply(text, edits):
    for (old, new, expect) in edits:
        n = text.count(old)
        assert n == expect, "anchor x%d (want %d): %r..." % (n, expect, old[:90])
        text = text.replace(old, new)
    return text


INST_EDITS = [
    # 1. TITLE: add the flag-quotiet width-obstruction family (the W25/W28
    #    surviving headline results) to the paper's own branding.
    ("\\title{\\bf Exact Affine Geometry, Optimal Centres, and Certified Compression Bounds for Finite-Outcome Quantum Instruments}",
     "\\title{\\bf Exact Affine Geometry, Optimal Centres, Certified Compression Bounds, and Flag-Quotient Width Obstructions for Finite-Outcome Quantum Instruments}",
     1),
    # 2. ABSTRACT: the flat-width classification + the machine premise's
    #    status are INSERTED (the v8 abstract predates the W25 block).
    ("the zero-error threshold equals the affine dimension. The single-outcome case recovers quantum channels,",
     "the zero-error threshold equals the affine dimension. For the input-independent case the flat-width classification is complete: the flat value one holds exactly on the classical $n\\le4$ and qubit $n\\le2$ bodies and fails at least $4/3$ on every other, including every state space of dimension $\\ge3$ at the bottom and second latent dimensions alike, the qutrit exactly $4/3$ at both --- the second-index results through the integral cohomology of the cyclic flag quotient, computed by an exact-integer equivariant battery and reproduced by an independent re-implementation. The single-outcome case recovers quantum channels,",
     1),
    # 4. INTRO (x1): the machine premise's status.
    ("the latter through a machine-certified computation of the cohomology of the flag quotient (Theorems~",
     "the latter through a machine computation of the integral cohomology of the cyclic flag quotient, certified by an exact-integer equivariant battery and reproduced by an independent re-implementation (Theorems~",
     1),
    # 3. KEYWORDS: add the surviving cohomological vocabulary.
    ("\\noindent\\textbf{Keywords:} quantum instruments; diamond norm; compression width; antipodal profile; Chebyshev radius; quantum measurements; no-programming theorem.",
     "\\noindent\\textbf{Keywords:} quantum instruments; diamond norm; compression width; antipodal profile; Chebyshev radius; quantum measurements; flag manifolds; equivariant cohomology; Borsuk--Ulam theorem; no-programming theorem.",
     1),
    # 5. SPECIALISATIONS note (sec 7): the equal-basis-plane provenance.
    ("(Theorem~\\ref{thm:equal-basis-plane}, proved through the machine-certified cohomology of the flag quotient, Lemma~\\ref{lem:flag-cohomology})",
     "(Theorem~\\ref{thm:equal-basis-plane}, proved through the cohomology of the flag quotient, machine-certified and independently re-implemented, Lemma~\\ref{lem:flag-cohomology})",
     1),
    # 6. LEMMA proof pointer (the two-worlds decision).
    ("by the machine-certified computation recorded in\nRemark~\\ref{rem:machine-certificate}: the integral homology of $B$ is",
     "by the machine computation recorded in\nRemark~\\ref{rem:machine-certificate}, certified by its battery and reproduced\nby an independent re-implementation: the integral homology of $B$ is",
     1),
    # 7. rem:machine-certificate: the residuals are updated (the honest
    #    statement of the W28 result).
    ("Residuals, stated plainly: the cellulation is one\nimplementation (re-run and reproduced across independent sessions, but not\nindependently re-implemented); its geometric identification with the flag\nquotient is warranted by the construction lineage and the battery, not by an\nexplicit diffeomorphism; and the prime scan is finite.",
     "Residuals, stated plainly: the cellulation began as one\nimplementation and has since been independently re-implemented from the\ndesign specification with fresh algorithms at every layer (phase measurement\nby column ratios rather than a joint gauge solve, Newton inversions, sign\nderivation by constraint propagation from $\\partial T=T\\partial$, direct\n$\\mathbb Z/12$ elimination rather than the Chinese-remainder route, and an\nincremental subgroup-order computation of the $\\mathbb Z/9$ ladder); the two\nimplementations agree on every input datum, on the full battery, and on the\nhomology tuple, and the convention data of the construction is forced by the\nbattery (each falsified variant breaks either the equivariance certificate\nor the orbit homology); the geometric identification with the flag quotient\nremains warranted by the construction lineage and the battery, not by an\nexplicit diffeomorphism; and the prime scan is finite, covering $p\\le 31$\nacross the two implementations.",
     1),
    # 8. OPEN PROBLEM (vi): the re-implementation clause is discharged.
    ("(vi) close the last computational premise of Theorem~\\ref{thm:state-d2}: give a hand derivation of the degree-three and degree-four cohomology of the flag quotient $B$ (Lemma~\\ref{lem:flag-cohomology}), or an independent re-implementation of the certified computation --- for the former, the algorithmic procedure of Ref.~\\cite{GuerraJana2025} for the unstable additive cohomology of the unordered quotients is a natural candidate route (Remark~\\ref{rem:flag-literature});",
     "(vi) close the last computational premise of Theorem~\\ref{thm:state-d2}: give a hand derivation of the degree-three and degree-four cohomology of the flag quotient $B$ (Lemma~\\ref{lem:flag-cohomology}) --- the premise now rests on two independent implementations (Remark~\\ref{rem:machine-certificate}), so the hand derivation is the remaining route, and the algorithmic procedure of Ref.~\\cite{GuerraJana2025} for the unstable additive cohomology of the unordered quotients is a natural candidate (Remark~\\ref{rem:flag-literature});",
     1),
    # 9. CONCLUSION: the state-d2 provenance.
    ("(Theorem~\\ref{thm:state-d2}, proved through the machine-certified cohomology of the flag quotient, Lemma~\\ref{lem:flag-cohomology})",
     "(Theorem~\\ref{thm:state-d2}, proved through the cohomology of the flag quotient, machine-certified and independently re-implemented, Lemma~\\ref{lem:flag-cohomology})",
     1),
    # 10. rem:flag-literature closing note.
    ("and the machine certificate\nof Remark~\\ref{rem:machine-certificate} is complementary to, not subsumed by,\nthat programme",
     "and the machine certificate\nof Remark~\\ref{rem:machine-certificate}, now doubly implemented, is complementary\nto, not subsumed by, that programme",
     1),
]

MAIN_EDITS = [
    # 1. ABSTRACT: append the input-independent flat-width clause (the
    #    surviving companion-reported dichotomy).
    ("a one-query informationally complete measurement achieves the injective threshold, and repetition gives an $O(N^{-1/2})$ expected-error bound.\n\\end{abstract}",
     "a one-query informationally complete measurement achieves the injective threshold, and repetition gives an $O(N^{-1/2})$ expected-error bound. In the input-independent case the widths are governed by the companion's flatness dichotomy: the flat value one fails for every output dimension at least three at the bottom two latent dimensions, the qutrit sitting exactly at $4/3$ there, through a flag-quotient computation that is machine-certified and independently re-implemented.\n\\end{abstract}",
     1),
    # 2. KEYWORDS.
    ("\\noindent\\textbf{Keywords:} quantum channel compression; diamond norm; antipodal width; exact in-radius; Borsuk--Ulam theorem; quantum combs; nonlinear approximation.",
     "\\noindent\\textbf{Keywords:} quantum channel compression; diamond norm; antipodal width; exact in-radius; Borsuk--Ulam theorem; quantum combs; nonlinear approximation; flat-width dichotomy; flag-quotient cohomology.",
     1),
    # 3. SYNC CLAUSE (open problem 1): the premise status.
    ("the companion's plane-valued extension of the equal-value-basis theorem, whose homological premise is machine-certified, likewise bounds",
     "the companion's plane-valued extension of the equal-value-basis theorem, whose homological premise is machine-certified and independently re-implemented, likewise bounds",
     1),
]


def main():
    os.makedirs(DST, exist_ok=True)
    with open(os.path.join(SRC, INST), encoding="utf-8") as f:
        inst = f.read()
    inst9 = apply(inst, INST_EDITS)
    with open(os.path.join(DST, "instruments-paper-revised9.txt"), "w", encoding="utf-8") as f:
        f.write(inst9)
    print("instruments: %d anchored edits applied (11 hunks)" % len(INST_EDITS))

    with open(os.path.join(SRC, MAIN), encoding="utf-8") as f:
        maina = f.read()
    main9 = apply(maina, MAIN_EDITS)
    with open(os.path.join(DST, "main-article-revised9.txt"), "w", encoding="utf-8") as f:
        f.write(main9)
    print("main article: %d anchored edits applied" % len(MAIN_EDITS))
    print("v9 sources written to %s" % DST)


if __name__ == "__main__":
    main()
