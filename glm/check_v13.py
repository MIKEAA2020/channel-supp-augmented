#!/usr/bin/env python3
"""Wave 34 checker: verify the v13 (instruments) + v11 (main) hygiene edits.

P-layer (textual): every anchored edit applied exactly once; every superseded
diary phrase gone; the mathematical core of prop:cupsquare / lem:flag-cohomology
/ thm:state-d2 untouched (must-hold anchors); F1/F2 folded; .txt == .tex;
broad informal sweep; main-article sync intact with no proof internals.

M-layer (exact integer, sympy): the Step-7 degree-6 quotient re-computed by
Smith normal form (free rank 1, no torsion, [S1] generating, [S2] = -[S1],
[A1] = 0); THE F2 GATE (the new lift-independence clause): [Delta + c tau^3]
= 2[S1] for c = 0,1,2,5 and [S1 + a tau^3] = [S1] for a = 0,1,2; the Step-2
lattice-index table [orbit-sum lattice : symmetric module] = 1,1,1,2,2,4,8 in
degrees 0..6 with the degree-3 witness (S1 not in the module, 2*S1 in it).
"""
import os, re, sys, math
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form

REPO = "/home/z/my-project/channel-supp-augmented"
INST = os.path.join(REPO, "manuscript uploads v13", "instruments-paper-revised13")
MAIN = os.path.join(REPO, "manuscript uploads v13", "main-article-revised11")

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
    print(("PASS " if cond else "FAIL ") + name + (("  -- " + detail) if detail and not cond else ""))

inst_tex = open(INST + ".tex").read()
inst_txt = open(INST + ".txt").read()
main_tex = open(MAIN + ".tex").read()
main_txt = open(MAIN + ".txt").read()

# ---------------------------------------------------------------- P layer
NEW_PHRASES = [
 ("F1 killed+marker", "there are killed before the $E_8$-page (the classes $\\sigma_1$, $\\sigma_2$,\n$\\tau$ and the transgression values invoked here are established in\nSteps~2--4 below)"),
 ("F2 lift-independence clause", "taking with it the $\\tau^3$-tail ambiguity of the orbit-sum\nlifts (Step~3), so that the quotient and the discriminant's position in it\nare lift-independent"),
 ("C1 abstract", "the qutrit exactly $4/3$ at both, the second-index result resting on the integral cohomology of the cyclic flag quotient."),
 ("C2 intro", "through a Chern-transgression derivation of the integral cohomology of the cyclic flag quotient, cross-checked by an independent exact-integer machine computation"),
 ("C3 median bound", "(an elementary median\nmatching bound at $r=1$ on the coordinate flags $(j,k)$, with the constant $2(q-1)/q$)"),
 ("C4 ebp", "(Theorem~\\ref{thm:equal-basis-plane}, proved through the cohomology of the flag quotient; Lemma~\\ref{lem:flag-cohomology} and Proposition~\\ref{prop:cupsquare})"),
 ("C5 expected complete", "the expected complete statement being Conjecture~\\ref{con:coord-flat}."),
 ("C6 comment", "% ---- Equal-value orthonormal bases and the state-space bottom widths ----"),
 ("C7 title", "\\begin{proposition}[The cup square on the flag quotient]"),
 ("C8 worlds", "The decision between the two worlds is\nsupplied by Proposition~\\ref{prop:cupsquare}, which proves $x^2\\ne0$ by an\nintegral transgression computation independent of the present Cartan--Leray\npage; and"),
 ("C9 proof-end", "The independent machine computation recorded in\nRemark~\\ref{rem:machine-certificate} confirms the same conclusion"),
 ("C10 remark title", "\\begin{remark}[The computational verification of Lemma~\\ref{lem:flag-cohomology}]"),
 ("C10 analytic", "The proof of Lemma~\\ref{lem:flag-cohomology} is analytic:"),
 ("C10 certification consists", "The certification consists of\nexact integer arithmetic on that complex:"),
 ("C10 model cases", "was\nchecked against two externally known model cases"),
 ("C10 three qualifications", "Three qualifications remain. First, the arithmetic of"),
 ("C10 twice independently", "the cellulation was implemented twice\nindependently, the second implementation following the design specification"),
 ("C10 three routes", "carried by three mutually\nindependent routes --- the analytic derivation, the cellulation, and its\nindependent re-implementation"),
 ("C10 repo", "The code and\nthe full transcripts of both computations are available in the public\nrepository."),
 ("C11 derivation", "The derivation of Proposition~\\ref{prop:cupsquare} is the"),
 ("C12 computational verification", "The computational verification of\nRemark~\\ref{rem:machine-certificate} remains complementary"),
 ("C13 pinching only", "two-sector pinching threshold $nQ_2(2)-1=2n-1$);"),
 ("C14 non-flat state spaces", "; the one-outcome\nstate spaces are non-flat, the qutrit having"),
 ("C15 fails", "and at $r=2$ this requirement fails for every"),
 ("C16 plain conjecture", "Conjecture~\\ref{con:coord-flat} states the expected complete"),
 ("C17 therefore", "). The content of the conjecture is therefore"),
 ("C18 conclusion", "(Theorem~\\ref{thm:state-d2}, proved through the cohomology of the flag quotient; Lemma~\\ref{lem:flag-cohomology} and Proposition~\\ref{prop:cupsquare})"),
 ("C19 coordinate conj", "--- and the coordinate Conjecture~\\ref{con:coord-flat} covering"),
 ("C20v", "(v) settle the coordinate flat-widths Conjecture~\\ref{con:coord-flat}"),
 ("C20v-now", "of which the smallest, $\\delta_2$ of the qutrit, is exactly $4/3$"),
 ("C21 open (vi)", "(vi) determine the unstable integral cohomology of the symmetric-group quotients themselves"),
]
for name, s in NEW_PHRASES:
    check("P: " + name, inst_tex.count(s) == 1, f"count={inst_tex.count(s)}")

MAIN_NEW = [
 ("M1 abstract", "through a flag-quotient cohomology computation."),
 ("M2 extension bounds", "plane-valued extension of the equal-value-basis theorem likewise bounds"),
 ("M2 that extension", "the cyclic flag quotient underlying that extension sits between"),
]
for name, s in MAIN_NEW:
    check("P-main: " + name, main_tex.count(s) == 1, f"count={main_tex.count(s)}")

MUSTHOLD = [
 ("prop statement tuple", "H^k(B;\\mathbb Z)\\ =\\ \\bigl(\\mathbb Z,\\ 0,\\ \\mathbb Z/3,\\ \\mathbb Z/3,\\\n\\mathbb Z/3,\\ \\mathbb Z/3,\\ \\mathbb Z\\bigr)"),
 ("prop statement H6", "in which the discriminant class is twice a\ngenerator."),
 ("Step1 display", "d_2(z_1)=\\iota^*c_1,\\qquad d_4(z_3)=\\iota^*c_2,\\qquad d_6(z_5)=\\iota^*c_3,"),
 ("Step2 index sentence", "one in degrees $d\\le2$, exactly the degrees in which the crux of Step~5\nbelow works, then $2$, $2$, $4$, $8$ in degrees $3$ to $6$"),
 ("Step2 witness", "S_1=\\chi_1^2\\chi_2+\\chi_2^2\\chi_3+\\chi_3^2\\chi_1\n=\\tfrac12(\\sigma_1\\sigma_2-3\\sigma_3+\\Delta)"),
 ("Step3 display", "H^6(BK;\\mathbb Z)\\ \\cong\\ \\mathbb Z\\{A_1,\\,S_1,\\,S_2,\\,\\sigma_3\\}\\oplus\n\\mathbb Z/3\\cdot\\tau^3"),
 ("Step3 relations", "$S_1+S_2=\\sigma_1\\sigma_2-3\\sigma_3$ and\n$S_1-S_2=\\Delta$"),
 ("Step4 pins display", "d_2(z_1)=\\sigma_1,\\qquad d_4(z_3)=\\sigma_2+2\\tau^2,\\qquad\nd_6(z_5)=\\sigma_3 ."),
 ("Step4 b-pin", "Hence $0=s^*(\\iota^*c_1)=s^*(\\sigma_1+b\\,\\tau)=bu$"),
 ("Step5 crux", "E_\\infty^{4,0}\\ =\\ \\bigl(\\mathbb Z\\sigma_2\\oplus\\mathbb Z/3\\cdot\\tau^2\\bigr)\n\\big/\\langle\\sigma_2+2\\tau^2\\rangle\\ \\cong\\ \\mathbb Z/3"),
 ("Step6 edge", "x^2\\ =\\ \\gamma^*(\\tau^2)\\ =\\ \\bigl[\\tau^2\\bigr]\\ \\ne\\ 0"),
 ("Step7 quotient display", "H^6(B;\\mathbb Z)\\ \\cong\\ \\bigl(\\mathbb Z\\{A_1,S_1,S_2,\\sigma_3\\}\\oplus\n\\mathbb Z/3\\cdot\\tau^3\\bigr)\\big/\\langle\\sigma_1^3,\\ \\sigma_1\\sigma_2,\\\n2\\tau^3,\\ \\sigma_3\\rangle\\ \\cong\\ \\mathbb Z\\cdot\\langle S_1\\rangle"),
 ("Step7 identities", "using $\\sigma_1\\sigma_2=S_1+S_2+3\\sigma_3$ and\n$\\sigma_1^3=A_1+3(S_1+S_2)+6\\sigma_3$"),
 ("Step7 Delta", "$\\Delta=S_1-S_2=2S_1$ is twice a generator"),
 ("lem statement", "and $x^2=\\kappa^*(u^2)$ generates $H^4(B;\\mathbb Z)$; in particular $x^2\\ne0$."),
 ("thm state d2", "\\delta_{2,\\mathrm{inst}}^{\\diamond}(\\mathbb C,B)\\ \\ge\\ \\frac43"),
 ("R7 marking intact", "is lift-dependent: the class of $\\Delta$ in\n$H^6(BK;\\mathbb Z)$ is fixed only up to a $\\tau^3$-tail"),
 ("proof framing", "It is self-contained apart from three classical inputs,"),
 ("Step0 title", "\\emph{Step 0 (the homogeneous-space model).}"),
]
for name, s in MUSTHOLD:
    check("P-hold: " + name, inst_tex.count(s) == 1, f"count={inst_tex.count(s)}")

FORBIDDEN = [
 "hand-derived, machine-certified", "equivariant battery", "the earlier audit",
 "now doubly implemented", "has since been", "previous version", "earlier version",
 "corrected twice", "[closed in this version]", "in its corrected form",
 "the corrected statement", "the corrected coordinate", "stress-tested",
 "Residuals, stated plainly", "a hand derivation", "Wave 7", "wave 3",
 "trace-mass threshold", "five-outcome counterexample", "the machine certificate",
 "supplied by hand", "certification battery", "machine-certified",
 "referee", "strawman", "TODO", "FIXME", "XXX",
 "upgraded from the earlier", "left bracketed in the previous",
 "derived by hand", "the hand derivation", "reader can check line by line",
]
for phrase in FORBIDDEN:
    check("P-absent(inst): " + phrase, inst_tex.count(phrase) == 0, f"count={inst_tex.count(phrase)}")
    check("P-absent(main): " + phrase, main_tex.count(phrase) == 0, f"count={main_tex.count(phrase)}")

check("P: .txt == .tex (instruments)", inst_txt == inst_tex)
check("P: .txt == .tex (main)", main_txt == main_tex)

check("P-main: flag-quotient sync present", "flag-quotient" in main_tex)
check("P-main: companion sync present", main_tex.count("companion") >= 1)
for internal in ["orbit-sum", "lattice-index", "$S_1$", "$\\tau^3$", "prop:cupsquare",
                 "rem:machine-certificate", "lem:flag-cohomology", "sigma_1", "b\\,\\tau"]:
    check("P-main: no proof internal <%s>" % internal, internal not in main_tex)

def strip_comments(t):
    return "\n".join(ln.split("%", 1)[0] if not ln.lstrip().startswith("%") else "" for ln in t.split("\n"))
SWEEP = [r"\bstress[- ]tested\b", r"\bbattery\b", r"\bdebug\b", r"\bhands? on\b",
         r"\bwe confess\b", r"\bhonestly\b", r"\bhunch\b", r"\bgut feeling\b"]
for label, t in [("inst", strip_comments(inst_tex)), ("main", strip_comments(main_tex))]:
    hits = [p for p in SWEEP for _ in re.finditer(p, t, re.I)]
    check("P: informal sweep (%s)" % label, not hits, str(hits))

# ---------------------------------------------------------------- M layer
# ---- M1: the Step-7 degree-6 quotient, with tau^3-tail lifts -------------
# basis (A1, S1, S2, sigma3, t), t = tau^3 lift; relations:
#   sigma1^3 = (1,3,3,6,0);  sigma1 sigma2 = (0,1,1,3,0);  sigma3 = (0,0,0,1,0)
#   2t = (0,0,0,0,2);  3t = (0,0,0,0,3)  (tau^3 of order 3 in H^6(BK))
REL = Matrix([[1,3,3,6,0],
              [0,1,1,3,0],
              [0,0,0,1,0],
              [0,0,0,0,2],
              [0,0,0,0,3]])
S = smith_normal_form(REL * 1)  # 5x5, rank 4
diag = [abs(S[i, i]) for i in range(min(S.rows, S.cols)) if S[i, i] != 0]
check("M: quotient SNF diag = (1,1,1,1) -> Z, no torsion", diag == [1, 1, 1, 1], f"got {diag}")

# lattice = rowspan(REL); membership via HNF of the transpose (columns)
H = hermite_normal_form(REL.T)  # 5x4, columns generate the same lattice
def in_lattice(v):
    b = Matrix([list(v)]).T  # 5x1
    if H.rank() != Matrix.hstack(H, b).rank():
        return False  # not even in the rational span
    sol = H.solve_least_squares(b) if False else None
    # exact solve: H is 5x4 full column rank -> unique rational solution
    try:
        sol = H.solve(b)
    except Exception:
        # try least squares / consistency via sympy linsolve
        from sympy import linsolve, symbols
        ys = symbols("y0:%d" % H.cols)
        solset = linsolve((H, b))
        if not solset:
            return False
        sol = next(iter(solset))
    vec = list(sol) if not isinstance(sol, Matrix) else list(sol)
    return all(x.q == 1 for x in [Matrix([vec]).T[i, 0] if isinstance(vec, list) else x for x in (vec if not isinstance(vec, Matrix) else vec)])
# (simpler robust wrapper)
def member(v):
    b = Matrix([list(v)]).T
    aug = Matrix.hstack(H, b)
    if H.rank() != aug.rank():
        return False
    from sympy import linsolve
    s = linsolve((H, b))
    if not s:
        return False
    tup = next(iter(s))
    return all(x.q == 1 for x in tup)

check("M: sigma1^3 in lattice (relation)", member([1,3,3,6,0]))
check("M: t = tau^3 in lattice (2 inv mod 3: 3t-2t=t)", member([0,0,0,0,1]))
check("M: [A1] = 0", member([1,0,0,0,0]))
check("M: [S2] = -[S1]", member([0,1,1,0,0]))
check("M: [sigma3] = 0", member([0,0,0,1,0]))
check("M: [sigma1 sigma2] = 0", member([0,1,1,3,0]))
# THE F2 GATES
# Delta = (0,1,-1,0,0); Delta + c tau^3 - 2 S1 = (0,-1,-1,0,c)
for c in (0, 1, 2, 5):
    check(f"M: F2 [Delta + {c}*tau^3] = 2[S1]", member([0, -1, -1, 0, c]))
for a in (1, 2):
    check(f"M: F2 [S1 + {a}*tau^3] = [S1]", member([0, 0, 0, 0, a]))
check("M: 2[S1] != 0 in the free quotient (2S1 not a relation)", not member([0, 2, 0, 0, 0]))
check("M: [S1] != 0 (S1 not a relation)", not member([0, 1, 0, 0, 0]))
check("M: [Delta] != 0", not member([0, 1, -1, 0, 0]))

# ---- M2: Step-2 lattice-index table [orbit-sum lattice : sym module] ----
def monomials(deg):
    # exponent triples (a,b,c) with a+b+c == deg exactly
    return [(a, b, deg - a - b) for a in range(deg + 1) for b in range(deg + 1 - a)]

def orbit_sum_basis(deg):
    mons = monomials(deg)
    idx = {m: i for i, m in enumerate(mons)}
    basis, used = [], set()
    for m in mons:
        if m in used:
            continue
        orb = {m, (m[2], m[0], m[1]), (m[1], m[2], m[0])}
        used |= orb
        v = [0] * len(mons)
        for x in orb:
            v[idx[x]] = 1
        basis.append(v)
    return mons, basis

def mul(p1, p2):
    out = {}
    for m1, c1 in p1.items():
        for m2, c2 in p2.items():
            m = (m1[0]+m2[0], m1[1]+m2[1], m1[2]+m2[2])
            out[m] = out.get(m, 0) + c1 * c2
    return {k: v for k, v in out.items() if v != 0}

SIG1 = {(1,0,0): 1, (0,1,0): 1, (0,0,1): 1}
SIG2 = {(1,1,0): 1, (1,0,1): 1, (0,1,1): 1}
SIG3 = {(1,1,1): 1}
DELTA = mul(mul({(1,0,0): 1, (0,1,0): -1}, {(1,0,0): 1, (0,0,1): -1}), {(0,1,0): 1, (0,0,1): -1})

def sigma_prod(a, b, c):
    p = {(): 1} if False else {(0,0,0): 1}
    for _ in range(a):
        p = mul(p, SIG1)
    for _ in range(b):
        p = mul(p, SIG2)
    for _ in range(c):
        p = mul(p, SIG3)
    return p

def sym_module_gens(deg):
    gens = []
    for a in range(deg + 1):
        for b in range(deg // 2 + 1):
            for c in range(deg // 3 + 1):
                if a + 2 * b + 3 * c == deg:
                    gens.append(sigma_prod(a, b, c))
    if deg >= 3:
        for a in range(deg - 2):
            for b in range((deg - 3) // 2 + 1):
                for c in range((deg - 3) // 3 + 1):
                    if a + 2 * b + 3 * c == deg - 3:
                        gens.append(mul(DELTA, sigma_prod(a, b, c)))
    return [g for g in gens if g]

def to_vec(poly, mons):
    idx = {m: i for i, m in enumerate(mons)}
    v = [0] * len(mons)
    for m, co in poly.items():
        v[idx[m]] += co
    return v

def lattice_index(deg):
    mons, Lb = orbit_sum_basis(deg)
    L = Matrix(Lb)  # rows: orbit sums, disjoint supports -> independent basis
    Mg = sym_module_gens(deg)
    M = Matrix([to_vec(g, mons) for g in Mg])
    rL, rM = L.rank(), M.rank()
    if rL != rM:
        return ("rank mismatch", rL, rM)
    if rL == 0:
        return 1
    # coordinates of each M-generator as an integer row combination of L:
    # solve L^T y = m^T  (unique since the orbit sums are a basis)
    coords = []
    for row in M.tolist():
        sol = L.T.solve(Matrix([row]).T)
        if any(x.q != 1 for x in sol):
            return ("non-integral",)
        coords.append([int(x) for x in sol])
    C = Matrix(coords)  # rM x rL, integral, rank rL
    d = smith_normal_form(C)
    dd = [abs(d[i, i]) for i in range(min(d.rows, d.cols)) if d[i, i] != 0]
    if len(dd) != rL or Matrix(C).rank() != rL:
        return ("bad rank", dd)
    return math.prod(dd)

table = [lattice_index(deg) for deg in range(0, 7)]
check("M: Step-2 index table [L:M] = 1,1,1,2,2,4,8", table == [1, 1, 1, 2, 2, 4, 8], f"got {table}")

# degree-3 witness: S1 = chi1^2 chi2 + chi2^2 chi3 + chi3^2 chi1 (orbit sum),
# not in the symmetric module; 2 S1 = sigma1 sigma2 - 3 sigma3 + Delta in it.
mons3, Lb3 = orbit_sum_basis(3)
Mg3 = sym_module_gens(3)
M3 = Matrix([to_vec(g, mons3) for g in Mg3])  # rows: module generators
S1_poly = {(2,1,0): 1, (0,2,1): 1, (1,0,2): 1}
def in_module(vpoly):
    v = to_vec(vpoly, mons3)
    aug = Matrix(M3.tolist() + [v])  # row-style rank test: v in rowspan(M3)?
    if M3.rank() != aug.rank():
        return False
    from sympy import linsolve
    s = linsolve((M3.T, Matrix([v]).T))  # M3.T y = v^T
    if not s:
        return False
    tup = next(iter(s))
    return all(x.q == 1 for x in tup)
check("M: witness S1 NOT in the symmetric module", not in_module(S1_poly))
check("M: witness 2*S1 IS in the module", in_module(mul(S1_poly, {(0,0,0): 2})))
# polynomial identity: 2 S1 - sigma1 sigma2 + 3 sigma3 - Delta = 0
comp = {}
for poly, sign in [(mul(S1_poly, {(0,0,0): 2}), 1), (sigma_prod(1,1,0), -1),
                    (sigma_prod(0,0,1), 3), (DELTA, -1)]:
    for m, co in poly.items():
        comp[m] = comp.get(m, 0) + sign * co
check("M: identity 2 S1 = sigma1 sigma2 - 3 sigma3 + Delta", all(v == 0 for v in comp.values()))
# and the coordinate identities of Step 7 on (A1,S1,S2,sigma3):
#   sigma1 sigma2 = (0,1,1,3), sigma1^3 = (1,3,3,6), Delta = (0,1,-1,0)
mons_full, Lb_full = orbit_sum_basis(3)
idx_full = {m: i for i, m in enumerate(mons_full)}
def row_for(m):
    for r in Lb_full:
        if r[idx_full[m]] == 1:
            return r
# the paper's basis order (A1, S1, S2, chi1chi2chi3):
Lb_paper = [row_for((3, 0, 0)), row_for((2, 1, 0)), row_for((2, 0, 1)), row_for((1, 1, 1))]
Lf = Matrix(Lb_paper)
def coords_in_L(poly):
    sol = Lf.T.solve(Matrix([to_vec(poly, mons_full)]).T)
    return [int(x) for x in sol]
check("M: sigma1 sigma2 = 0*A1+1*S1+1*S2+3*chi1chi2chi3", coords_in_L(sigma_prod(1,1,0))[0:4] == [0,1,1,3])
check("M: sigma1^3 = 1*A1+3*S1+3*S2+6*chi1chi2chi3", coords_in_L(sigma_prod(3,0,0))[0:4] == [1,3,3,6])
check("M: Delta = S1 - S2 (coords (0,1,-1,0))", coords_in_L(DELTA)[0:4] == [0,1,-1,0])

# ---------------------------------------------------------------- tally
fails = [r for r in results if not r[1]]
print()
print("=" * 60)
print(f"TOTAL: {len(results)} checks, {len(results) - len(fails)} PASS, {len(fails)} FAIL")
if fails:
    for n, _, det in fails:
        print("  FAIL:", n, det)
    sys.exit(1)
print("ALL PASS")
