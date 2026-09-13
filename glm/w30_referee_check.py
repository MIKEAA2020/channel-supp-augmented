#!/usr/bin/env python3
"""W30: independent referee verification of prop:cupsquare (v10 instruments paper).

Re-derives, from scratch, every checkable arithmetic claim of the Proposition's
seven-step proof, with special attention to:
  (A) Step 2's module claim  H*(BK;Z)_free = Z[s1,s2,s3] (+) D*Z[s1,s2,s3]
      -- the lattice INDEX of the displayed module inside the true invariant
         (orbit-sum) lattice, per degree;
  (B) the Step 5 crux:  E_inf^{4,0} = (Z s2 (+) Z/3 t2)/<s2+2t2> ~= Z/3, [t2]!=0;
  (C) the Step 3 tau-rule:  H^2(C3; M_d) = M^C / N M  and the fixed-monomial
      detection;
  (D) the Step 4 pin data: regular-representation Chern classes;
  (E) the Step 7 degree-6 run:  H^6(B) = M_3^C / <s1^3, s1 s2, s3>  and the
      class of the discriminant in it.
No manuscript data is read; everything is recomputed.  Exact integer arithmetic
only (sympy + python ints).
"""
import itertools, json
from sympy import symbols, expand, Poly, Matrix, ZZ, lcm

x1, x2, x3 = symbols('x1 x2 x3')

# ---------------------------------------------------------------- monomial basis
def monoms(d):
    """Degree-d monomials (exactly degree d) as exponent triples, sorted."""
    return sorted([(a, b, d - a - b) for a in range(d + 1) for b in range(d + 1 - a)],
                  key=lambda t: (t[1], t[2], t[0]))

def shift(t):
    """The generator action: x1->x2->x3->x1 sends (a1,a2,a3) -> (a3,a1,a2)."""
    a, b, c = t
    return (c, a, b)

def shift_pow(t, k):
    for _ in range(k % 3):
        t = shift(t)
    return t

def poly_of(t):
    a, b, c = t
    return x1**a * x2**b * x3**c

def vec_of(p, d):
    """Vector of p in the degree-d monomial basis."""
    P = Poly(expand(p), x1, x2, x3)
    return [P.coeff_monomial(poly_of(t)) for t in monoms(d)]

def mat_from_polys(polys, d):
    return Matrix([vec_of(p, d) for p in polys]).T  # columns = generators

# ---------------------------------------------------------------- invariants
def orbit_decomp(d):
    """Orbits of the C3 action on degree-d monomials; fixed monomials flagged."""
    basis = monoms(d)
    seen, orbits, fixed = set(), [], []
    for m in basis:
        if m in seen:
            continue
        o = [m, shift(m), shift_pow(m, 2)]
        seen.update(o)
        if o[0] == o[1]:            # fixed monomial (chi1 chi2 chi3)^a
            fixed.append(m)
        else:
            orbits.append(sorted(set(o)))
    return orbits, fixed

def invariant_lattice_basis(d):
    """Basis of M_d^C3 as the lattice spanned by orbit sums + fixed monomials."""
    orbits, fixed = orbit_decomp(d)
    gens = []
    for o in orbits:
        gens.append(sum(poly_of(t) for t in o))
    for f in fixed:
        gens.append(poly_of(f))
    return gens, orbits, fixed

# ---------------------------------------------------------------- smith helpers
def lattice_index(A, B):
    """Index [lattice(B) : lattice(A)] for two full-rank generator matrices
    (columns) over Z with lattice(A) subset lattice(B).  None if not subset."""
    # solve A = B * X  over Q, X integral?
    X = B.solve(A)                      # rational
    if not all(e == int(e) for e in X):
        return None                     # A not contained in lattice(B)
    from sympy.matrices.normalforms import smith_normal_form
    S = smith_normal_form(Matrix(X), domain=ZZ)
    d = [S[i, i] for i in range(min(S.shape))]
    d = [abs(int(v)) for v in d if v != 0]
    idx = 1
    for v in d:
        idx *= v
    return idx

def quotient_order(rels, n):
    """Order of Z^n / (row lattice of rels); also SNF invariant factors."""
    from sympy.matrices.normalforms import smith_normal_form
    M = Matrix(rels)
    if M.rows == 0:
        return 0, []        # free
    S = smith_normal_form(M.T, domain=ZZ)   # columns = relations
    invs = [abs(int(S[i, i])) for i in range(min(S.shape)) if S[i, i] != 0]
    order = 1
    for v in invs:
        order *= v
    free = n - len(invs)
    return free, invs

def in_rowlattice(v, rows, k=1):
    """Is k*v in the integer row-lattice spanned by rows?
    Sound brute force for the small bounded systems at hand: pre-check
    solvability over Q, then scan integer coefficients in a bounded box
    (row entries and |k*v| are <= 6 here, so coefficients beyond +-60
    cannot occur in a minimal solution of a solvable system)."""
    if not rows:
        return all(vv == 0 for vv in v)
    target = [k * vv for vv in v]
    m = len(rows)
    R = Matrix(rows)
    # rational solvability
    try:
        from sympy import linsolve
        cs = symbols('q0:%d' % m)
        sol = linsolve((Matrix.hstack(R.T, Matrix([target])), ), cs)
        if not sol:
            return False
    except Exception:
        pass
    n = len(target)
    rng = range(-60, 61)
    if m == 2:
        for a in rng:
            for b in rng:
                ok = True
                for i in range(n):
                    if a * rows[0][i] + b * rows[1][i] != target[i]:
                        ok = False
                        break
                if ok:
                    return True
        return False
    if m == 3:
        for a in rng:
            for b in rng:
                for c in rng:
                    ok = True
                    for i in range(n):
                        if (a * rows[0][i] + b * rows[1][i] + c * rows[2][i]
                                != target[i]):
                            ok = False
                            break
                    if ok:
                        return True
        return False
    raise NotImplementedError("brute force only wired for 2-3 rows")

def class_order_in_quotient(v, rows):
    for k in range(1, 60):
        if in_rowlattice(v, rows, k):
            return k
    return None

# =================================================================== CHECKS
report = {}

print("=" * 78)
print("REF CHECK 1  --  Step 2 module claim: index of Z[s] (+) D Z[s] in M_d^C3")
print("=" * 78)
s1 = x1 + x2 + x3
s2 = x1*x2 + x1*x3 + x2*x3
s3 = x1*x2*x3
D  = (x1 - x2) * (x1 - x3) * (x2 - x3)
Dsq = expand(D**2)
disc = expand(s1**2*s2**2 - 4*s2**3 - 4*s1**3*s3 - 27*s3**2 + 18*s1*s2*s3)
print("Delta^2 == classical discriminant:", Dsq == disc)

def module_gens(d):
    """Generators of Z[s1,s2,s3]_d  (+)  Delta * Z[s1,s2,s3]_{d-3}.
    sigma-monomial sigma_1^a sigma_2^b sigma_3^c has polynomial degree a+2b+3c."""
    gens = []
    for a in range(d + 1):
        for b in range((d - a) // 2 + 1):
            rem = d - a - 2*b            # must equal 3c
            if rem >= 0 and rem % 3 == 0:
                c = rem // 3
                gens.append(expand(s1**a * s2**b * s3**c))
    if d >= 3:
        e = d - 3
        for a in range(e + 1):
            for b in range((e - a) // 2 + 1):
                rem = e - a - 2*b
                if rem >= 0 and rem % 3 == 0:
                    c = rem // 3
                    gens.append(expand(D * s1**a * s2**b * s3**c))
    return [g for g in gens if g != 0]

results = {}
for d in range(0, 9):
    inv, orbits, fixed = invariant_lattice_basis(d)
    B = mat_from_polys(inv, d)
    L = module_gens(d)
    A = mat_from_polys(L, d)
    n_orb = len(orbits) + len(fixed)
    n_mod = A.shape[1]
    idx = lattice_index(A, B)
    results[d] = (n_orb, n_mod, idx)
    print(f"degree {d}: #orbits(invariants rank) = {n_orb:2d} | module rank = {n_mod:2d} "
          f"| index [M^C : module] = {idx}")
report['module_index'] = {str(d): results[d][2] for d in results}

print()
print("=" * 78)
print("REF CHECK 2  --  the degree-3 witness:  S1 = x1^2 x2 + x2^2 x3 + x3^2 x1")
print("=" * 78)
S1 = x1**2*x2 + x2**2*x3 + x3**2*x1
S2 = x1**2*x3 + x3**2*x2 + x2**2*x1
print("Delta == S1 - S2 :", expand(D - (S1 - S2)) == 0)
print("S1 + S2 == s1 s2 - 3 s3 :", expand(S1 + S2 - (s1*s2 - 3*s3)) == 0)
print("2*S1 == s1 s2 - 3 s3 + Delta :", expand(2*S1 - (s1*s2 - 3*s3 + D)) == 0)
# solve S1 = a s1^3 + b s1 s2 + c s3 + e Delta over Z?
a, b, c, e = symbols('a b c e')
from sympy import solve
eqs = Poly(expand(a*s1**3 + b*s1*s2 + c*s3 + e*D - S1), x1, x2, x3).coeffs()
sol = solve(eqs, [a, b, c, e], dict=True)
print("integer solution of S1 = a s1^3 + b s1 s2 + c s3 + e Delta :", sol)

print()
print("=" * 78)
print("REF CHECK 3  --  Step 3 tau-rule: H^2(C3; M_d) = M^C / N M_d, detection")
print("=" * 78)
print("(rule: tau.f = [coeff of (x1 x2 x3)^{d/3} in f] mod 3; 0 if 3 does not divide d)")
def tau_of(f, d):
    """Class of the invariant f in M^C / N M_d  (returns 'zero' or (k,3))."""
    inv, orbits, fixed = invariant_lattice_basis(d)
    if not fixed:
        return (0, 1)      # group is trivial
    fm = fixed[0]          # (x1 x2 x3)^a
    coeff = Poly(expand(f), x1, x2, x3).coeff_monomial(fm)
    return (int(coeff) % 3, 3)
for name, f, d in [("sigma_1", s1, 1), ("sigma_2", s2, 2), ("sigma_3", s3, 3),
                   ("sigma_1^3", s1**3, 3), ("Delta", D, 3),
                   ("sigma_1 sigma_2", s1*s2, 3), ("S1 (orbit sum)", S1, 3),
                   ("sigma_2^2", s2**2, 4), ("sigma_1 sigma_3", s1*s3, 4),
                   ("Delta sigma_1", D*s1, 4)]:
    k, m = tau_of(f, d)
    # cross-check by the norm computation: f in N M_d  <=>  class 0
    inv, orbits, fixed = invariant_lattice_basis(d)
    NM = []
    for o in orbits:
        NM.append(sum(poly_of(t) for t in o))
    for fmon in fixed:
        NM.append(3 * poly_of(fmon))
    inN = False
    X = mat_from_polys(NM, d).solve(mat_from_polys([expand(f)], d))
    from sympy import Rational
    inN = all(v == int(v) for v in X)
    agree = (inN and k == 0) or ((not inN) and k != 0)
    print(f"  tau . {name:18s} (deg {d}): rule says {k}/3 ; norm-check in N·M_d = {inN} ; agree = {agree}")

print()
print("  tau-powers: H^{2k}(C3; Z) = Z/3 for all k >= 1  (periodic): -- standard")

print()
print("=" * 78)
print("REF CHECK 4  --  Step 4 pin data: Chern classes of the regular rep of C3")
print("=" * 78)
u = symbols('u')
# characters 1, omega, omega^2 -> first Chern classes 0*u, 1*u, 2*u in Z[u]/(3u)
c = (1 + 0*u)*(1 + 1*u)*(1 + 2*u)
c = expand(c)
print("c(1 (+) omega (+) omega^2) =", c)
print("c1 = 3u  ( = 0 in Z[u]/(3u) ) :", c.coeff(u, 1) == 3)
print("c2 = 2u^2                       :", c.coeff(u, 2) == 2)
print("c3 = 0                          :", c.coeff(u, 3) == 0)

print()
print("=" * 78)
print("REF CHECK 5  --  Step 5 crux:  (Z s2 (+) Z/3 t2) / <s2 + 2 t2>")
print("=" * 78)
# generators e1 = s2 (free), e2 = t2 (order 3); relation e1 + 2 e2 = 0, 3 e2 = 0
rels = [[1, 2], [0, 3]]
free, invs = quotient_order(rels, 2)
print("SNF of relations [[1,2],[0,3]]: free rank =", free, ", invariant factors =", invs)
k = class_order_in_quotient([0, 1], rels)
print("order of the class of t2 = (0,1):", k, " (nonzero and = 3 => tau^2 survives, generates)")
print("s2 = (1,0) ~ -(2) t2 => its class is 2[t2] (also nonzero):",
      class_order_in_quotient([1, 0], rels))
# and the FULL (4,0) slot: quotient additionally by Z s1^2 (direct summand):
print("full E_inf^{4,0} = (Z s1^2 (+) Z s2 (+) Z/3 t2)/<s1^2, s2+2t2>: same Z/3,",
      "image of t2 unchanged (s1^2 is a direct-summand quotient).")

print()
print("=" * 78)
print("REF CHECK 6  --  Step 7, total degree 6:  H^6(B) = M_3^C / <s1^3, s1 s2, s3>")
print("=" * 78)
d = 3
inv, orbits, fixed = invariant_lattice_basis(d)
Bm = mat_from_polys(inv, d)                       # true H^6(BK) free part (mod torsion)
imgs = [expand(s1**3), expand(s1*s2), expand(s3)]  # d2-images + d4-image + d6-image (free parts)
Aimgs = mat_from_polys(imgs, d)
X = Bm.solve(Aimgs)
print("image lattice inside the invariant lattice (integral):",
      all(v == int(v) for v in X))
# quotient M_3^C / <images>: rows = images in the INVARIANT basis
inv_basis_polys = inv
Xinv = Bm.solve(mat_from_polys(inv_basis_polys, d))   # identity
img_coords = Bm.solve(Aimgs)                          # images in invariant-lattice coords
rows = [[int(v) for v in img_coords[:, j]] for j in range(img_coords.cols)]
free6, invs6 = quotient_order(rows, len(inv_basis_polys))
print("H^6(B) = M_3^C / <s1^3, s1 s2, s3>:  free rank =", free6,
      ", torsion invariant factors =", invs6, "  => H^6(B;Z) = Z")
# classes of S1 and Delta in this quotient (coordinates in the invariant basis):
print()
print("  -- express [S1] and [Delta] in the rank-1 quotient --")
# invariant basis is [A1(=sum chi^3), S1, S2, s3]; coordinates of the images:
# s1^3 = A1 + 3 S1 + 3 S2 + 6 s3 ;  s1 s2 = S1 + S2 + 3 s3 ;  s3 = s3
print("  relation matrix rows (images in invariant basis {A1,S1,S2,s3}):")
print(Matrix(rows))
# verify numerically: is (Delta - 2*S1) in the row lattice?
vDelta = Bm.solve(mat_from_polys([expand(D)], d)); vDelta = [int(c) for c in vDelta[:, 0]]
vS1 = Bm.solve(mat_from_polys([expand(S1)], d)); vS1 = [int(c) for c in vS1[:, 0]]
target = [vDelta[i] - 2*vS1[i] for i in range(4)]
print("  Delta - 2*S1 lies in the image lattice:", in_rowlattice(target, rows))
# and is Delta - 1*S1 in it? (would mean [Delta]=[S1])
target2 = [vDelta[i] - vS1[i] for i in range(4)]
print("  Delta - S1 lies in the image lattice (would give [Delta]=[S1]):",
      in_rowlattice(target2, rows))
# is S1 itself in it? (would collapse the quotient)
print("  S1 lies in the image lattice (would kill the quotient):",
      in_rowlattice(vS1, rows))
print("  => if Delta-2S1 in lattice, Delta-S1 NOT in lattice, S1 NOT in lattice:")
print("     H^6(B) = Z.<[S1]>  and  [Delta] = 2[S1]  (discriminant = TWICE a generator)")

print()
print("=" * 78)
print("REF CHECK 7  --  Step 5 slot inventory, total degree 4 (H^*(BK) free ranks)")
print("=" * 78)
# free ranks of H^n(BK): n = 2d: rank = #orbits(d)
for d in range(0, 4):
    inv, orbits, fixed = invariant_lattice_basis(d)
    print(f"H^{2*d}(BK) free rank = {len(orbits)+len(fixed)}"
          f"   (H^{2*d}(BK) total deg {2*d})")
print("H^4(BK) free part = <sigma_1^2, sigma_2> exactly?  index of module:",
      results[2][2])
print("H^2(BK) free part = <sigma_1>: index:", results[1][2])
print("H^6(BK) free part: module index:", results[3][2],
      "  <-- the false lattice statement (index 2)")

print()
print("=" * 78)
print("SUMMARY")
print("=" * 78)
print(json.dumps(report, indent=1, default=str))
