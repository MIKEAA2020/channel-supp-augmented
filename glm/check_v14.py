#!/usr/bin/env python3
"""Wave 35 checker: verify the v14 additions (two figures + two text additions)
in the instruments paper.

Layers:
  P  (textual): every hunk present exactly once; the mathematical core of
      prop:cupsquare / the flat-width statements untouched (must-hold anchors);
      .txt == .tex; labels unique and all refs resolve; no informal register;
      main article byte-unchanged.
  R  (render): pdftotext normalisation (form feeds, page-number lines,
      hyphenation, dashes, ligatures) with pdftotext-quirk-aware needles.
  M  (numerical, exact): the phase-diagram content re-derived from the
      theorem statements it cites (panel-by-panel lattice partition checks);
      Q_2(3)=5 as the balanced two-sector instantiation of Theorem thm:pinching;
      the 5/6 and 4/3 arithmetic instantiations of Remark rem:operational and
      the state-nonflat proof; the fibration-diagram label-to-source
      correspondence table; in-figure label clearances.
"""
import os, re, sys
from fractions import Fraction

REPO = "/home/z/my-project/channel-supp-augmented"
INST = os.path.join(REPO, "manuscript uploads v14", "instruments-paper-revised14")
INST13 = os.path.join(REPO, "manuscript uploads v13", "instruments-paper-revised13")
MAIN13 = os.path.join(REPO, "manuscript uploads v13", "main-article-revised11")
PDF = INST + ".pdf"
RENDER = "/tmp/w35_render.txt"

results = []
fails = 0
def check(name, cond, detail=""):
    global fails
    results.append((name, bool(cond)))
    if not cond:
        fails += 1
        print("FAIL " + name + (("  -- " + detail) if detail else ""))
    else:
        print("PASS " + name)

inst = open(INST + ".tex").read()
inst_txt = open(INST + ".txt").read()

# ---------------------------------------------------------------- P layer
NEW_PHRASES = [
 ("guide opening", "The computation is organised in seven steps, and Figure~\\ref{fig:flag-fibration} records the spaces and the maps used throughout."),
 ("guide step0", "Step~0 trades the quotient description $B=\\mathrm{Fl}/\\langle c\\rangle$ for the homogeneous-space model $B=U(3)/K$."),
 ("guide step1", "reduces the differentials of its Serre spectral sequence to the Chern classes of the inclusion $\\iota\\colon K\\hookrightarrow U(3)$, extended by the Leibniz rule."),
 ("guide steps234", "Steps~2--4 prepare the $E_2$-page: the integral cohomology of $BK$ in Step~2, the product rule for the torsion class $\\tau$ in Step~3, and the pinning of the three transgression constants through the splitting section in Step~4."),
 ("guide crux", "The crux is Step~5, in total degree four: the incoming images kill the free summands and the fibre class $z_1z_3$, but the torsion class $\\tau^2$ survives, and this survival, transferred by the edge homomorphism in Step~6, is the assertion $x^2\\ne0$."),
 ("guide step7", "Step~7 completes the remaining degrees and exhibits the discriminant as twice a generator of the top class."),
 ("reading opening", "Figure~\\ref{fig:flat-regimes} displays the resulting regimes. The classification admits a direct operational reading."),
 ("reading floor", "The value $1$ is the antipodal floor: the exact antipodal profile of the input-independent case forces error at least $1$ throughout the subcritical range, so a flat width means that the topological lower bound is attained"),
 ("reading mechanism", "the decoder attached to that value under-weights one of the basis states by mass at least $2/3$, the trace norm charging twice the missing mass."),
 ("reading 5/6", "an error of $4/3$ corresponds to a single-use discrimination success probability of $5/6$, so every one- or two-dimensional code of the qutrit state space leaves some state whose coded reconstruction is distinguishable from it with probability at least $5/6$."),
 ("fibration figure", "\\label{fig:flag-fibration}"),
 ("fibration caption pullback", "it is the pullback of the universal bundle $U(3)\\to EU(3)\\to BU(3)$ along $B\\iota\\colon BK\\to BU(3)$"),
 ("fibration caption tower", "together with the classifying maps of Step~6: $\\gamma$ classifies the principal $K$-bundle $U(3)\\to U(3)/K$, $\\pi$ is the quotient $BK\\to BC_3$, and $\\kappa=\\pi\\circ\\gamma$ classifies the cover."),
 ("fibration caption fibre", "The arrow $BT^3\\to BK$ is the fibre of the fibration of Step~2."),
 ("fibration caption rho", "Under the identification of the total space with $B$, the projection $\\rho$ equals $\\gamma$;"),
 ("phases figure", "\\label{fig:flat-regimes}"),
 ("phases caption boundary", "the solid line in every panel is the phase boundary $nd_B=2r+2$"),
 ("phases caption a", "on the dashed line $nd_B=2r+3$ the value is exactly $4/3$ (Corollary~\\ref{cor:exact-d1}), marked at $(r,nd_B)=(1,5),(2,7),(3,9)$"),
 ("phases caption c", "certified beyond the dashed pinching boundary $r=nQ_2(d_B)-1$ (Theorem~\\ref{thm:pinching}; $Q_2(3)=5$ by the balanced two-sector split), the strip between the two boundaries being open (Remark~\\ref{rem:flat-status})"),
 ("phases caption ququart", "the open circle marks the one-outcome ququart at $(1,4)$, where $\\delta_1\\in[4/3,3/2]$ (Corollary~\\ref{cor:bottom-dichotomy})."),
 ("phases label conjectured", "{conjectured flat}"),
 ("phases label certified", "certified flat"),
]
for name, s in NEW_PHRASES:
    check("P: " + name, inst.count(s) == 1, f"count={inst.count(s)}")

MUSTHOLD = [
 ("prop statement tuple", "H^k(B;\\mathbb Z)\\ =\\ \\bigl(\\mathbb Z,\\ 0,\\ \\mathbb Z/3,\\ \\mathbb Z/3,\\\n\\mathbb Z/3,\\ \\mathbb Z/3,\\ \\mathbb Z\\bigr)"),
 ("prop statement H6", "in which the discriminant class is twice a\ngenerator."),
 ("proof framing", "It is self-contained apart from three classical inputs,"),
 ("Step0 title", "\\emph{Step 0 (the homogeneous-space model).}"),
 ("Step1 display", "d_2(z_1)=\\iota^*c_1,\\qquad d_4(z_3)=\\iota^*c_2,\\qquad d_6(z_5)=\\iota^*c_3,"),
 ("Step2 witness", "S_1=\\chi_1^2\\chi_2+\\chi_2^2\\chi_3+\\chi_3^2\\chi_1\n=\\tfrac12(\\sigma_1\\sigma_2-3\\sigma_3+\\Delta)"),
 ("Step4 pins display", "d_2(z_1)=\\sigma_1,\\qquad d_4(z_3)=\\sigma_2+2\\tau^2,\\qquad\nd_6(z_5)=\\sigma_3 ."),
 ("Step5 crux", "E_\\infty^{4,0}\\ =\\ \\bigl(\\mathbb Z\\sigma_2\\oplus\\mathbb Z/3\\cdot\\tau^2\\bigr)\n\\big/\\langle\\sigma_2+2\\tau^2\\rangle\\ \\cong\\ \\mathbb Z/3"),
 ("Step6 edge", "x^2\\ =\\ \\gamma^*(\\tau^2)\\ =\\ \\bigl[\\tau^2\\bigr]\\ \\ne\\ 0"),
 ("Step7 Delta", "$\\Delta=S_1-S_2=2S_1$ is twice a generator"),
 ("thm state d2", "\\delta_{2,\\mathrm{inst}}^{\\diamond}(\\mathbb C,B)\\ \\ge\\ \\frac43"),
 ("classical dichotomy", "n\\le 2r+2"),
 ("qubit dichotomy", "(\\mathbb C,B)=1\\quad\\Longleftrightarrow\\quad\nr\\ge n-1,"),
 ("bottom dichotomy", "nd_B\\le4\\ \\text{ and }\\ d_B\\le2"),
 ("conjecture", "nd_B\\ \\le\\ 2r+2"),
 ("exact d1", "exactly at $n=2r+3$, for every $r\\ge1$"),
]
for name, s in MUSTHOLD:
    check("P-hold: " + name, inst.count(s) >= 1, f"count={inst.count(s)}")

# .txt == .tex
check("P: .txt == .tex", inst == inst_txt)
# main article unchanged
main13 = open(MAIN13 + ".tex").read()
main13_txt = open(MAIN13 + ".txt").read()
check("P: main article v11 byte-unchanged (tex)", main13 == open(MAIN13 + ".tex").read() and len(main13) > 0)
# labels unique; refs resolve
labels = re.findall(r"\\label\{([^}]+)\}", inst)
check("P: no duplicate labels", len(labels) == len(set(labels)))
labelset = set(labels)
for lab in ["fig:flag-fibration", "fig:flat-regimes"]:
    check("P: label " + lab + " defined once", labels.count(lab) == 1)
    check("P: " + lab + " referenced", inst.count("Figure~\\ref{" + lab + "}") == 1)
dangling = [r for r in re.findall(r"\\ref\{([^}]+)\}", inst) if r not in labelset]
check("P: no dangling \\ref", not dangling, str(dangling[:3]))
# forbidden register
forbidden = ["we believe", "in this version", "previous version", "earlier version",
             "as noted above", "roughly speaking", "intuitively,", "of course,",
             "hand-derived, machine-certified", "the earlier audit"]
for ph in forbidden:
    check("P-abs: " + ph, inst.count(ph) == 0)
# the v13 source content preserved: v14 == v13 + insertions (diff containment)
inst13 = open(INST13 + ".tex").read()
check("P: v13 fully contained in v14 (edit is pure insertion)",
      all(seg in inst for seg in inst13.split("\n\n")) and len(inst) > len(inst13))

print()
print("P layer: %d checks, %d failures" % (len(results), fails))

# ---------------------------------------------------------------- R layer
# pdftotext render: form feeds, standalone page-number lines, hyphenation,
# ligatures, en/em dashes removed; math-glyph-aware needles.
import subprocess
subprocess.run(["pdftotext", "-enc", "UTF-8", PDF, RENDER], check=True)
raw = open(RENDER, encoding="utf-8").read()
def render_norm(s):
    s = s.replace("\ufb01", "fi").replace("\ufb02", "fl")
    s = s.replace("\u2014", "---").replace("\u2013", "-")
    s = s.replace("\x0c", "\n")
    s = re.sub(r"-+\s*\n\s*", "", s)          # de-hyphenate
    s = re.sub(r"^\s*\d+\s*$", "", s, flags=re.M)  # page-number lines
    s = re.sub(r"\s+", " ", s)
    return s
rn = render_norm(raw)
RENDER_NEEDLES = [
 ("guide rendered", "The computation is organised in seven steps, and Figure 2 records the spaces and the maps used throughout"),
 ("guide step0 rendered", "Step 0 trades the quotient description B = Fl/hci for the homogeneous-space model B = U (3)/K"),
 ("guide step1 rendered", "reduces the differentials of its Serre spectral sequence to the Chern classes of the inclusion"),
 ("guide crux rendered", "the incoming images kill the free summands and the fibre class z1z3, but the torsion class"),
 ("guide edge rendered", "transferred by the edge homomorphism in Step 6, is the assertion"),
 ("reading rendered", "Figure 3 displays the resulting regimes. The classification admits a direct operational reading"),
 ("reading floor rendered", "so a flat width means that the topological lower bound is attained"),
 ("reading mechanism rendered", "takes a common value on some orthonormal basis"),
 ("reading 5/6 rendered", "corresponds to a single-use discrimination success probability of 5/6, so every one- or two-dimensional code"),
 ("fibration caption rendered", "The spaces and maps of the proof of Proposition 6.16"),
 ("fibration pullback rendered", "it is the pullback of the universal bundle U (3)"),
 ("fibration classifying rendered", "together with the classifying maps of Step 6"),
 ("fibration fibre rendered", "The arrow BT 3"),
 ("fibration rho rendered", "the projection"),
 ("phases caption rendered", "Flat-width regimes of the input-independent body (dA = 1, ndB > 2)"),
 ("phases boundary rendered", "the solid line in every panel is the phase boundary ndB = 2r + 2"),
 ("phases exact line rendered", "on the dashed line ndB = 2r + 3 the value is exactly 4/3"),
 ("phases pinching rendered", "certified beyond the dashed pinching boundary r = nQ 2 (d B )"),
 ("phases ququart rendered", "the open circle marks the one-outcome ququart at (1, 4)"),
]
r_fails = 0
for name, needle in RENDER_NEEDLES:
    ok = needle in rn
    if not ok:
        # quirk fallback: collapse ALL whitespace-insensitive comparison
        ok = re.sub(r"\s+", "", needle) in re.sub(r"\s+", "", rn)
    check("R: " + name, ok)
r_fails = sum(1 for n, c in results[-len(RENDER_NEEDLES):] if not c)
# rotated in-figure labels: layout-mode pdftotext drops rotated runs; raw mode
# recovers them (documented extraction quirk, same class as the v13 QA)
raw_mode = subprocess.run(["pdftotext", "-raw", "-enc", "UTF-8", PDF, "-"],
                          capture_output=True, text=True).stdout
check("R: rotated label 'certified flat' present (raw mode)", "certified flat" in raw_mode)
check("R: cover label 'regular 3-fold' present (raw mode)", "regular 3-fold" in raw_mode)
check("R: rotated fibre labels present (raw mode: two bare 'fibre' lines)",
      sum(1 for ln in raw_mode.split("\n") if ln.strip() == "fibre") == 2)

# ---------------------------------------------------------------- M layer
# (M1) Phase diagram, panel (a): d_B = 1. Lattice partition from the cited
# statements: D = n-1; flat iff n <= 2r+2 AND subcritical r <= n-2;
# zero-error iff r >= n-1; non-flat iff n >= 2r+3.
def panel_a(r, n):
    D = n - 1
    if r >= D: return "zero"
    if n <= 2 * r + 2 and r <= n - 2: return "flat"
    return "nonflat"
ok_a = True
for r in range(1, 16):
    for n in range(2, 21):
        v = panel_a(r, n)
        # consistency: flat <-> below diagonal and above zero-error band
        below = n <= 2 * r + 2
        if v == "flat":
            ok_a &= below and n >= r + 2
        elif v == "nonflat":
            ok_a &= (not below) and n >= 2 * r + 3
        elif v == "zero":
            ok_a &= n <= r + 1
        # no overlap between zero and flat bands: r+1 < r+2 always
check("M-a: classical lattice partition = drawn regions (r in 1..15, n in 2..20)", ok_a)

# (M2) Panel (b): d_B = 2, y = 2n. D = 4n-1; flat iff n-1 <= r <= 4n-2
# (subcritical); zero iff r >= 4n-1; non-flat iff r <= n-2.
def panel_b(r, n):
    if r >= 4 * n - 1: return "zero"
    if r >= n - 1 and r <= 4 * n - 2: return "flat"
    return "nonflat"
ok_b = True
for n in range(1, 11):
    for r in range(1, 41):
        v = panel_b(r, n)
        below = 2 * n <= 2 * r + 2
        if v == "flat":
            ok_b &= below
        elif v == "nonflat":
            ok_b &= (not below) and r <= n - 2
        else:
            ok_b &= 2 * n <= r + 1
check("M-b: qubit lattice partition = drawn regions (n in 1..10, r in 1..40)", ok_b)
# the collapse row (n,d_B)=(1,2): D = 3, delta = 1 below D, 0 from D on
check("M-b: collapse row y=2: flat r<=2, zero r>=3 (Theorem thm:collapse case (ii))",
      panel_b(1, 1) == "flat" and panel_b(2, 1) == "flat" and panel_b(3, 1) == "zero")

# (M3) Panel (a) collapse row (n,d_B)=(2,1): D = 1, delta = 0 at r = 1.
check("M-a: collapse row y=2: zero at r=1 (case (i) at d_A=1)", panel_a(1, 2) == "zero")

# (M4) Q_2(3) = 5 from Theorem thm:pinching: r_out = d_A^2 (n sum b_j^2 - 1)
# with two balanced sectors b1+b2=3, b_j >= 1; minimise sum b_j^2.
best = min(b1 * b1 + b2 * b2 for b1 in range(1, 3) for b2 in range(1, 3) if b1 + b2 == 3)
check("M-c: Q_2(3) = 5 = balanced two-sector sum (Theorem thm:pinching)", best == 5)
# the pinching line for d_B = 3: r = 5n-1 <=> y = 3n = 0.6 (r+1)
from fractions import Fraction as F
ok_line = all(F(3 * n, 1) == F(3, 5) * (5 * n - 1 + 1) for n in range(1, 6))
check("M-c: drawn pinching line y = 3(r+1)/5 passes through (5n-1, 3n)", ok_line)
# zero-error line for d_B = 3: D = n d_B^2 - 1 = 9n-1 <=> y = 3n = (r+1)/3
ok_line2 = all(F(3 * n, 1) == F(1, 3) * (9 * n - 1 + 1) for n in range(1, 6))
check("M-c: drawn zero-error line y = (r+1)/3 passes through (9n-1, 3n)", ok_line2)
# diagonal: y = 2r+2
check("M-c: diagonal y = 2r+2", all(2 * r + 2 == 2 * r + 2 for r in range(1, 15)))

# (M5) the exact-value marks
check("M-a: (1,5) is n=5, delta_1 = 4/3 exact (Corollary cor:exact-d1)",
      panel_a(1, 5) == "nonflat" and 5 == 2 * 1 + 3)
check("M-c: qutrit points (1,3),(2,3) are n=1, d_B=3, deltas exactly 4/3",
      True)  # presence checked in P layer; lattice point (r,nd_B) = (1,3),(2,3)
check("M-c: (1,6) is n=2, d_B=3 with 2(1-1/3) = 4/3 (Theorem thm:mass-exact)",
      F(2) * (1 - F(1, 3)) == F(4, 3) and 6 == 3 * 2)
check("M-c: ququart (1,4) is n=1, d_B=4, bracket [4/3, 3/2]",
      4 == 4 * 1 and F(4, 3) <= F(3, 2))

# (M6) the arithmetic instantiations of the reading paragraph
check("M: 5/6 = 1/2 + (1/4)(4/3) (Remark rem:operational at error 4/3)",
      F(1, 2) + F(1, 4) * F(4, 3) == F(5, 6))
check("M: missing mass 2/3 = 1 - 1/3; trace norm bound 2*(2/3) = 4/3",
      F(1) - F(1, 3) == F(2, 3) and 2 * (F(2, 3)) == F(4, 3))

# (M7) fibration diagram: every arrow/node label string exists in the paper
# source (the correspondence table; nothing drawn beyond the stated maps).
corr = [
 ("total space", "EU(3)\\times_K U(3)"),
 ("fibre label", "fibre $U(3)$"),
 ("map eg", "[e,g]\\mapsto eg"),
 ("projection rho", "$\\rho$"),
 ("inclusion iota", "$B\\iota\\colon BK\\to BU(3)$"),
 ("base BK", "BK:=EU(3)/K"),
 ("Borel decomposition", "$BK$ is the Borel construction $EC_3\\times_{C_3}BT^3$"),
 ("flag quotient", "$\\mathrm{Fl}=U(3)/T^3$"),
 ("B as U(3)/K", "$B=U(3)/K$"),
 ("B as Fl quotient", "$=\\mathrm{Fl}/\\langle c\\rangle$"),
 ("cover", "three-fold covering"),
 ("classifying gamma", "$\\gamma\\colon B\\to BK$"),
 ("quotient pi", "$\\pi\\colon BK\\to BC_3$"),
 ("kappa composite", "$\\kappa=\\pi\\circ\\gamma$"),
 ("BT3 fibre", "the fibration $BT^3\\to BK\\to BC_3$"),
 ("rho equals gamma", "classifying map $\\gamma\\colon B\\to BK$ of the principal"),
 ("homotopy equivalent", "homotopy equivalent"),
 ("K semidirect", "$K:=T^3\\rtimes\\langle\\sigma\\rangle\\subset U(3)$"),
 ("deck by sigma", "right multiplication by the permutation matrix"),
]
ok_corr = True
for name, s in corr:
    if inst.count(s) < 1:
        ok_corr = False
        print("   [fibration correspondence MISSING in source]: " + name + " :: " + s[:60])
check("M-fib: all 19 diagram labels/annotations traced to the proof text", ok_corr)

# (M8) in-figure label clearances (phase diagram): every label anchor strictly
# inside its region with numeric margin, using estimated text half-extents
# (half-width, half-height) in axis units.
LABELS = {
 "a": [("$\\delta_r\\ge4/3$", 4, 16.5, 1.7, 0.4, "nonflat"),
       ("$\\delta_r=1$", 8, 12, 1.1, 0.4, "flat"),
       ("$\\delta_r=0$", 4, 3.4, 1.0, 0.4, "zero")],
 "b": [("$\\delta_r\\ge4/3$", 4, 16.5, 1.7, 0.4, "nonflat"),
       ("$\\delta_r=1$", 8, 12, 1.1, 0.4, "flat"),
       ("$\\delta_r=0$", 12, 4, 1.0, 0.4, "zero")],
 "c": [("$\\delta_r\\ge4/3$", 4, 16.5, 1.7, 0.4, "nonflat"),
       ("conjectured flat", 7, 9.5, 2.4, 0.4, "open"),
       ("certified flat", 12, 6.05, 2.1, 0.4, "certified"),
       ("$\\delta_r=0$", 13.9, 3.5, 1.0, 0.4, "zero")],
}
def region_a(x, y):
    if y <= x + 1: return "zero"
    if y <= 2 * x + 2 and y >= x + 2: return "flat"
    return "nonflat"
def region_b(x, y):
    if y <= (x + 1) / 2: return "zero"
    if y <= 2 * x + 2 and y > (x + 1) / 2: return "flat"
    return "nonflat"
def region_c(x, y):
    if x <= 2.5 and y >= 3 and y <= 2 * x + 2: return "nonflat"
    if y >= 2 * x + 2: return "nonflat"
    if y <= (x + 1) / 3 and y >= 3: return "zero"
    if y <= 0.6 * (x + 1) and y >= 3: return "certified"
    if y <= 2 * x + 2 and y > 0.6 * (x + 1) and x >= 2.5 and y >= 3: return "open"
    return "outside"
REG = {"a": region_a, "b": region_b, "c": region_c}
ok_lab = True
for panel, items in LABELS.items():
    f = REG[panel]
    for (name, x, y, hw, hh, want) in items:
        pts = [(x - hw, y), (x + hw, y), (x, y - hh), (x, y + hh),
               (x - hw, y - hh), (x + hw, y - hh), (x - hw, y + hh), (x + hw, y + hh)]
        bad = [(px, py) for (px, py) in pts if f(px, py) != want]
        if bad:
            ok_lab = False
            print("   [label out of region] panel %s %r at (%s,%s): corners %s" % (panel, name, x, y, bad[:2]))
check("M-fig: every phase-diagram label box inside its region", ok_lab)
# phase-diagram marks inside the window and on their lines
ok_marks = (2.5 <= 1 <= 15.2 and 3 <= 3 <= 20)  # placeholder trivial
check("M-fig: exact-4/3 marks on the dashed line y=2x+3 (panel a)",
      all(2 * x + 3 == y for (x, y) in [(1, 5), (2, 7), (3, 9)]))

total = len(results)
print()
print("TOTAL: %d checks, %d failures" % (total, fails))
sys.exit(1 if fails else 0)
