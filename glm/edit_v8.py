#!/usr/bin/env python3
"""Wave 27 -- the v8 citation-integration pass (v7 -> v8), per the W26 verdict:

"1. The v8 citation/positioning pass -- REQUIRED before any submission, and now
the only blocking item: add the Guerra-Jana pair (both papers), Weber/Korbas
(Auerbach-via-flag-cup-length school) and the Z_p-BU background to the
instruments paper's related work; one positioning paragraph each (...); the
same anchors where the main article touches the flag story; drop or cite
NechitaEtAl2018."

Honest corrections to the W26 record established before this edit ran:
  * NechitaEtAl2018 IS cited in v7 (line 725: \\cite[Corollary~2]{...}) -- the
    W26 "uncited bibitem" finding was a CHECKER ARTIFACT: check_v7.py's cite
    regex \\cite\\{...\\} does not match the optional-argument form
    \\cite[...]{...}. No manuscript change is made for it; check_v8.py fixes
    the regex and this is recorded in the wave note.
  * The Korbas 2003 cup-length paper has TWO authors (Korbas and Lorinc,
    Fundam. Math. 178, 2003) -- verified live via Crossref + zbMATH Open.

All bibliographic data below was live-verified on 2026-09-13 from Crossref,
zbMATH Open (API), arXiv abs pages, and the Springer/AMS DOI landings; the
evidence logs are scripts/novelty_pass/v8_citation_data.json,
v8_probe_results.json, abs_v8_*.html, cr_*.json, zbm_v8_*.json.

Instruments paper (v8): intro positioning sentence; the new Remark
rem:flag-literature (the positioning paragraph) between rem:machine-certificate
and thm:equal-basis-plane; the open-problem (vi) candidate-route clause; seven
new bibitems.
Main article (v8): the sync-clause differentiation + the two bibitems.

Every replacement is anchored on exact word sequences (whitespace-flexible)
and asserted to match exactly once, per the edit_v7.py convention.
"""
import os
import re
import sys

V7 = "/home/z/my-project/channel-supp-augmented/manuscript uploads v7"
V8 = "/home/z/my-project/channel-supp-augmented/manuscript uploads v8"
INST7 = f"{V7}/instruments-paper-revised7.txt"
MAIN7 = f"{V7}/main-article-revised7.txt"
INST8 = f"{V8}/instruments-paper-revised8.txt"
MAIN8 = f"{V8}/main-article-revised8.txt"


def flex(text: str) -> str:
    """Whitespace-flexible regex matching the exact word sequence of `text`."""
    return r"\s+".join(re.escape(w) for w in text.split())


def sub1(text: str, old: str, new: str, name: str) -> str:
    pat = flex(old)
    n = len(re.findall(pat, text, flags=re.S))
    assert n == 1, f"[{name}] expected exactly 1 match, found {n}"
    out, k = re.subn(pat, new.replace("\\", "\\\\"), text, count=1, flags=re.S)
    assert k == 1, f"[{name}] replacement failed"
    print(f"  OK  {name}")
    return out


# ----------------------------------------------------------------------------
# The new remark (instruments paper, between rem:machine-certificate and
# thm:equal-basis-plane).
# ----------------------------------------------------------------------------
REMARK = r"""\begin{remark}[The neighbouring flag-quotient literature]
\label{rem:flag-literature}
The quotient $B=\mathrm{Fl}/\langle c\rangle$ of Lemma~\ref{lem:flag-cohomology}
sits next to an active line on the cohomology of quotients of flag manifolds
and their applications. Guerra and Jana~\cite{GuerraJana2025} determine the
cohomology of the complete unordered flag manifolds
$\mathrm{Fl}_n(\mathbb C)/\Sigma_n$ and $\mathrm{Fl}_n(\mathbb R)/\Sigma_n$
--- homological stability, closed forms for the stable rings, and an
algorithmic procedure for the unstable additive cohomology --- and, with
Maiti~\cite{GuerraJanaMaiti2025}, compute the mod-$2$ cohomology of the
low-dimensional real unordered flag manifolds, improving the known estimates
of the number of Auerbach bases of small-dimensional normed spaces; this is
the line opened by Weber and Wojciechowski's Lusternik--Schnirelmann-category
estimate via real flag varieties~\cite{WeberWojciechowski2017}, together with
the cup-length computations of Korba{\v s} and L\"orinc~\cite{KorbasLorinc2003}
and Matszangosz's algorithm for the integer cohomology of real partial flag
manifolds~\cite{Matszangosz2021}. The classical backdrop of the antipodal
arguments specialised here to $\mathbb Z/3$ is the cyclic-group
Borsuk--Ulam literature, from the simple proof for
$\mathbb Z_p$-actions~\cite{Singh2010} to the connective $K$-theory version
for cyclic $p$-groups~\cite{Crabb2022}. The differentiation is precise. That
programme treats the \emph{symmetric-group} quotients, with \emph{field}
coefficients, in the service of Auerbach-basis counting; the present premise
concerns the \emph{cyclic} intermediate quotient
$\mathrm{Fl}/\langle c\rangle$, with \emph{integral} coefficients and the
$3$-torsion exponents pinned, in the service of the equal-value-basis and
compression-width chain. The algorithmic procedure of
Ref.~\cite{GuerraJana2025} is accordingly a natural candidate route for the
hand derivation posed as open problem (vi) below; and the machine certificate
of Remark~\ref{rem:machine-certificate} is complementary to, not subsumed by,
that programme --- the integral $3$-torsion of the cyclic quotient, with the
exponents fixed, is precisely the layer not addressed by field-coefficient
algorithms.
\end{remark}"""


BIBS_INST = r"""\bibitem{GuerraJana2025}
L. Guerra and S. Jana, \emph{Cohomology of complete unordered flag manifolds},
Trans. Amer. Math. Soc. \textbf{378}, 3507--3550 (2025).

\bibitem{GuerraJanaMaiti2025}
L. Guerra, S. Jana, and A. Maiti, \emph{The mod-2 cohomology groups of
low-dimensional unordered flag manifolds and Auerbach bases},
Topology Appl. \textbf{365}, 109279 (2025).

\bibitem{WeberWojciechowski2017}
A. Weber and M. Wojciechowski, \emph{On the Pe\l{}czy\'nski conjecture on
Auerbach bases}, Commun. Contemp. Math. \textbf{19}, 1750016 (2017).

\bibitem{KorbasLorinc2003}
J. Korba{\v s} and J. L\"orinc, \emph{The $\mathbb Z_2$-cohomology cup-length
of real flag manifolds}, Fund. Math. \textbf{178}, 143--158 (2003).

\bibitem{Matszangosz2021}
\'A.~K. Matszangosz, \emph{On the cohomology rings of real flag manifolds:
Schubert cycles}, Math. Ann. \textbf{381}, 1537--1588 (2021).

\bibitem{Singh2010}
M. Singh, \emph{A simple proof of the Borsuk--Ulam theorem for
$\mathbb Z_p$-actions}, Topology Proc. \textbf{36}, 249--253 (2010).

\bibitem{Crabb2022}
M.~C. Crabb, \emph{A Borsuk--Ulam theorem for cyclic $p$-groups},
arXiv:2211.08087 (2022).

\end{thebibliography}"""


BIBS_MAIN = r"""\bibitem{GuerraJana2025}
L. Guerra and S. Jana, \emph{Cohomology of complete unordered flag manifolds},
Trans. Amer. Math. Soc. \textbf{378}, 3507--3550 (2025).

\bibitem{GuerraJanaMaiti2025}
L. Guerra, S. Jana, and A. Maiti, \emph{The mod-2 cohomology groups of
low-dimensional unordered flag manifolds and Auerbach bases},
Topology Appl. \textbf{365}, 109279 (2025).

\end{thebibliography}"""


# ----------------------------------------------------------------------------
# Instruments paper edit.
# ----------------------------------------------------------------------------
def edit_inst(txt: str) -> str:
    print("instruments-paper-revised8.txt:")
    # I1: intro positioning sentence (end of the contributions paragraph).
    txt = sub1(
        txt,
        "\\ref{thm:state-nonflat}, \\ref{thm:state-d2}; "
        "Corollaries~\\ref{cor:exact-d1} and~\\ref{cor:bottom-dichotomy}).",
        "\\ref{thm:state-nonflat}, \\ref{thm:state-d2}; "
        "Corollaries~\\ref{cor:exact-d1} and~\\ref{cor:bottom-dichotomy}). "
        "The cohomological premise entering through "
        "Lemma~\\ref{lem:flag-cohomology} sits next to an active literature on "
        "the cohomology of unordered flag quotients, Auerbach bases, and "
        "cyclic-group Borsuk--Ulam theorems; Remark~\\ref{rem:flag-literature} "
        "records the precise differentiation.",
        "I1 intro positioning sentence",
    )

    # I2: the positioning remark between rem:machine-certificate and
    # thm:equal-basis-plane.
    txt = sub1(
        txt,
        "\\end{remark} \\begin{theorem}[Equal-value bases for plane-valued maps]",
        "\\end{remark}\n\n" + REMARK + "\n\n\\begin{theorem}[Equal-value bases for plane-valued maps]",
        "I2 rem:flag-literature insertion",
    )

    # I3: open problem (vi) candidate-route clause.
    txt = sub1(
        txt,
        "(Lemma~\\ref{lem:flag-cohomology}), or an independent re-implementation "
        "of the certified computation;",
        "(Lemma~\\ref{lem:flag-cohomology}), or an independent re-implementation "
        "of the certified computation --- for the former, the algorithmic "
        "procedure of Ref.~\\cite{GuerraJana2025} for the unstable additive "
        "cohomology of the unordered quotients is a natural candidate route "
        "(Remark~\\ref{rem:flag-literature});",
        "I3 open problem (vi) route clause",
    )

    # I4: bibliography.
    txt = sub1(
        txt,
        "\\end{thebibliography}",
        BIBS_INST,
        "I4 bibliography insertion (7 items)",
    )
    return txt


# ----------------------------------------------------------------------------
# Main article edit.
# ----------------------------------------------------------------------------
def edit_main(txt: str) -> str:
    print("main-article-revised8.txt:")
    # M1: sync-clause differentiation.
    txt = sub1(
        txt,
        "likewise bounds $\\delta_2^\\diamond\\ge4/3$ for every $d_B\\ge3$, "
        "the qutrit again exactly at $4/3$);",
        "likewise bounds $\\delta_2^\\diamond\\ge4/3$ for every $d_B\\ge3$, "
        "the qutrit again exactly at $4/3$ --- the cyclic flag quotient "
        "underlying that premise sits between the complete flag manifold and "
        "the symmetric-group unordered quotients whose cohomology is computed "
        "in Refs.~\\cite{GuerraJana2025,GuerraJanaMaiti2025});",
        "M1 sync-clause differentiation",
    )

    # M2: bibliography.
    txt = sub1(
        txt,
        "\\end{thebibliography}",
        BIBS_MAIN,
        "M2 bibliography insertion (2 items)",
    )
    return txt


def main() -> None:
    os.makedirs(V8, exist_ok=True)
    with open(INST7, encoding="utf-8") as f:
        inst = f.read()
    with open(MAIN7, encoding="utf-8") as f:
        main_txt = f.read()

    inst8 = edit_inst(inst)
    main8 = edit_main(main_txt)

    with open(INST8, "w", encoding="utf-8") as f:
        f.write(inst8)
    with open(MAIN8, "w", encoding="utf-8") as f:
        f.write(main8)

    # Post-write verification (handles combined \cite{a,b} key lists).
    newkeys = ["GuerraJana2025", "GuerraJanaMaiti2025", "WeberWojciechowski2017",
               "KorbasLorinc2003", "Matszangosz2021", "Singh2010", "Crabb2022"]

    def cite_groups(text: str):
        return [grp for grp in re.findall(r"\\cite\{([^}]+)\}", text)]

    print("\npost-write verification:")
    for k in newkeys:
        n_b = inst8.count(f"\\bibitem{{{k}}}")
        n_c = sum(1 for grp in cite_groups(inst8) if k in [x.strip() for x in grp.split(",")])
        ok = n_b == 1 and n_c >= 1
        print(f"  INST {k}: bibitems={n_b} cites={n_c}  {'OK' if ok else 'FAIL'}")
        assert ok, k
    for k in ["GuerraJana2025", "GuerraJanaMaiti2025"]:
        n_b = main8.count(f"\\bibitem{{{k}}}")
        n_c = sum(1 for grp in cite_groups(main8) if k in [x.strip() for x in grp.split(",")])
        ok = n_b == 1 and n_c >= 1
        print(f"  MAIN {k}: bibitems={n_b} cites={n_c}  {'OK' if ok else 'FAIL'}")
        assert ok, k
    # Also verify with the fixed optional-argument cite regex (the W26 lesson).
    n_opt = len(re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]+)\}", main8))
    print(f"  MAIN total \\cite occurrences (incl. \\cite[...]): {n_opt}")
    assert "rem:flag-literature" in inst8 and inst8.count("rem:flag-literature") >= 2
    assert "NechitaEtAl2018" in main8 and "cite[Corollary~2]{NechitaEtAl2018}" in main8
    print("  rem:flag-literature label + >=1 ref: OK")
    print("  NechitaEtAl2018 cite[Corollary~2] present (W26 artifact corrected): OK")
    print("\nv8 sources written:")
    print(f"  {INST8}  ({len(inst8.splitlines())} lines)")
    print(f"  {MAIN8}  ({len(main8.splitlines())} lines)")


if __name__ == "__main__":
    main()
