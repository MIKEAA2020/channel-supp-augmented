# Audit of `main article before supp` (3,466 lines)

Scope: (1) line-level reading for mathematical flaws and internal
inconsistencies; (2) stylistic-writing and syntax scan; (3) terminology
consistency scan. All line numbers refer to the file as committed at
`f61cc46`. Every finding below was verified against the surrounding text and,
where relevant, against the paper's own lemmas. The document compiles with
`pdflatex` (two passes, 41 pages, zero errors, zero warnings); all 92 labels,
all cross-references, and all 22 bibliography entries resolve.

---

## Part 1. Flaws and internal inconsistencies (line-level findings)

### F1. MAJOR — the informationally complete POVM need not be a POVM for the stated range of $\eta$

**Site.** `prop:one-query-injective`, line 2712:

> For sufficiently small $\eta>0$, specifically
> $0<\eta<1/((D_{A,B}+1)\max_i\|H_i\|_\infty)$, the operators
> $E_i=\frac{I}{D+1}+\eta H_i$ ($1\le i\le D$), and
> $E_0=\frac{I}{D+1}-\eta\sum_{i=1}^D H_i$ are positive … They sum to the
> identity and hence form a POVM.

**Problem.** The stated condition guarantees $E_i\ge0$ for each individual
$i$, but it does **not** guarantee $E_0\ge0$. Positivity of $E_0$ requires
$\eta\|\sum_i H_i\|_\infty\le 1/(D+1)$, while the stated condition only gives
$\eta\|\sum_iH_i\|_\infty\le\eta\sum_i\|H_i\|_\infty<D/(D+1)$. For $D\ge2$
the second bound can exceed $1/(D+1)$: for example, if all $H_i$ are
multiples of one fixed traceless operator $H_1$, then $\sum_iH_i=D H_1$ and
the stated range permits $\eta$ for which $E_0$ has a negative eigenvalue.
The closing sentence, "They sum to the identity and hence form a POVM", is a
non-sequitur: summing to the identity does not imply positivity.

**Fix.** Replace the condition by
$0<\eta<1/((D_{A,B}+1)\sum_{i}\|H_i\|_\infty)$ (equivalently bound
$\|\sum_iH_i\|_\infty$ directly). This makes every $E_i$ and $E_0$ strictly
positive; the injectivity argument in the proof is unaffected.

**Propagation.** `thm:sampled-achievability` (lines 2738–2740) reuses the
same defective range: "any fixed $\eta$ with
$0<\eta<1/((D_{A,B}+1)\max\|H_i\|_\infty)$". The flaw propagates verbatim
and must be fixed in both places.

### F2. Leftover placeholder line

**Site.** Line 3345, between the Clifford proof and the Data Availability
statement:

> `xxxxxxxxxxxxxxxxxxxxxxxx`

A literal artifact; remove the line.

### F3. Stray sentence with undefined symbols inside the program-packing proof

**Site.** Appendix proof of `thm:program-packing-rate`, line 3099:

> Moreover $\|\tilde\Gamma_{j,\pi_j}-\Gamma_{\pi_U}\|_\diamond\le
> \|\tilde\Gamma_j-\Gamma\|_\diamond+\|\pi_j-\pi_U\|_1$.

**Problem.** The symbols $\tilde\Gamma$, $\Gamma$, $\pi_j$, $\pi_U$ are
defined nowhere in the paper (the only other uses of $\Gamma$ are the
variational parameter $\Gamma_{A,B}$ of Section 3 and the Clifford
generators $\Gamma_j$ of the appendix, neither of which fits this
sentence). The sentence is never used again in the proof and appears to be
leftover from an earlier draft of a different argument. It should be
deleted; the proof is complete without it (the volume argument that follows
is self-contained and correct — verified below).

### F4. Figure–theorem inconsistency, with a provable strengthening available

**Sites.** `fig:replacement-join` (lines 1105–1149) vs.
`thm:partition` + `cor:block-envelope` (lines 3165–3232).

The figure labels each block sphere by the **Jordan map**
$X\mapsto X_+/t_X$ with antipodal trace distance **2**
("$\|h_i(u)-h_i(-u)\|_1=2$"), and the join node claims "Perfect separation:
$\|h(u)-h(-u)\|_\diamond=2$, $\alpha_r=1$ for $r\le R$".

The theorems instead construct each block sphere from the **centered
trace-norm ball** (`thm:partition` proof: "use the radial map … on the
centered trace-norm ball from `lem:replacement`. It gives …
$\|h_i(u)-h_i(-u)\|_1=4/b_i$"), obtaining only
$\alpha_r(\Chan(A,B))\ge2/b_*$ for $0\le r\le R$, and
`cor:block-envelope` claims $\alpha_r\ge2/s$ for $0\le r\le R_s$.

**Analysis.** These are two different constructions with two different
values on the *same* range: for $s>2$ the theorem statements ($2/s<1$) are
strictly weaker than what the figure claims ($1$), while for $s=2$ they
coincide ($2/s=1$, and $R_2=3\lfloor d_B/2\rfloor-1$ matches the join range).
The figure's version is in fact **provable with the paper's own lemmas**:
`thm:full-state-antipodal`'s map $X\mapsto X_+/t_X$ restricted to
$\Herm_0(B_i)\subset\Herm_0(B)$ gives, for each block with $b_i\ge2$, a
continuous $h_i:S^{b_i^2-2}\to\Sstate(B_i)$ whose antipodes have orthogonal
supports, hence trace distance exactly $2$; `prop:join` then yields
$\alpha_r(\Chan(A,B))\ge1$ for $0\le r\le R_s=\sum_i(b_i^2-1)-1$ (via the
replacement isometry). Note the strengthened range never exceeds the
full-state range: for $\ell\ge2$ blocks, $\sum_i(b_i^2-1)-1\le d_B^2-3<
d_B^2-2$, and for $\ell=1$ it recovers `thm:full-state-antipodal` exactly.

**Recommended action.** Strengthen `thm:partition` to $\alpha_r\ge1$
($0\le r\le R$) using the Jordan block spheres, update
`cor:block-envelope` accordingly ($\alpha_r=1$ for $0\le r\le R_s$ for every
$s\ge2$, with the diameter bound supplying the reverse inequality), and
align the figure text with the corrected statements. Alternatively, if the
ball-based $4/b_i$ bound is deliberately retained for some reason, the
figure's labels ("$=2$", "$\alpha_r=1$") must be corrected to $4/b_i$ and
$2/b_*$ — but the strengthened version is strictly better and uses only
results already proved in the paper.

### F5. Vague justification in the memory-sharpness proof

**Site.** `prop:memory-sharpness`, line 1943: "Necessity follows from the
positive full-body lower bound below $D_{A,B}$."

The clean citation is `prop:euclidean-threshold` (its positive-relative-ball
hypothesis holds for $\Chan(A,B)$, since $\Omega_{A,B}$ is a relative
interior point), or `thm:hierarchy` together with $\beta_r>0$ for
$r<D_{A,B}$. As written, the justification does not name the statement it
uses.

### F6. Wrong theorem cited for transcript-law continuity

**Site.** `fig:comb-complete-code` minipage, line 2476: "its law is
continuous in $\Phi$ (Theorem~\ref{thm:query-independent})".

`thm:query-independent` is the bottleneck statement; it does not prove
continuity of the transcript law. The continuity (indeed the Lipschitz
estimate) is `prop:physical-continuity`, which is the theorem the sentence
should cite.

### F7. Duplicated sentence in the partition-optimization proof

**Site.** `prop:partition-optimization` proof: the sentence "A maximizing
partition leaves at most one output dimension unused: if at least two
dimensions were unused, one could add a block … strictly increasing $F$"
appears twice, at lines 3245 and 3270. Delete the second occurrence (the
proof reads correctly with either one).

### F8. Duplicated subject in the quantum-state hierarchy statement

**Site.** `thm:compression`, lines 1901–1902: "For every decoder
$\operatorname{Dec}:\Sstate(M)\to\TPHP(A,B)$ (no regularity assumed), every
map $\operatorname{Dec}$ satisfies …". The subject is stated twice; drop
"every map $\operatorname{Dec}$".

### F9. Near-duplicate empty-latent-space clauses

**Sites.** `def:width` (line 159: "Since the source $K$ is nonempty, an
empty latent space creates no additional case in the obstruction theorem
beyond the trivial infinite width") and `def:coindex` (line 330: "Since the
source $K$ is nonempty, an empty latent space admits no encoder $K\to Y$ and
creates no additional case in the obstruction theorem"). Both also refer to
"the obstruction theorem" before it is introduced. Keep one clause, placed
after the obstruction theorem (or in it), and drop the other.

### F10. Redundant shorthand declaration

`def:coindex` already states "we occasionally suppress the subscript
$\mathbb Z_2$", and `rem:convex-code-spaces` repeats "We write
$\operatorname{coind}:=\operatorname{coind}_{\mathbb Z_2}$ when the group is
clear." One of the two suffices.

### F11. Redundant parenthetical in the open-problems list

Conclusion, open problem (ii): "determine the exact perfect-separation
indices $\pi(A,B)$ and $\pi_{\mathrm U}(d)$ within the proved lower and
upper ranges (i.e., within the proved intervals, not only beyond lower
bounds)". The parenthetical restates its antecedent; delete it.

### Verified sound (spot checks performed during the line-level read)

- `thm:exact-inradius` appendix proof: spectral bound, the
  $d_A/b$-amplification identity, the $V_0,V_1$ witness with
  $\widehat J_{\mathcal E_j}=(s/d_A)P_j$, and the value $2/(d_Bs)$ — all
  correct.
- `thm:exact-chebyshev-radius` appendix proof: bipartite domination
  $\sigma_{RB}\le\min\{r,d_B\}\,\rho_R\otimes I_B$, the $K$-dominated
  trace-distance lemma $\tfrac12\|\rho-\tau\|_1\le1-1/K$, and the isometric
  extremal channel — all correct; the final step $R(\Omega)=2-\rhodep$ is
  consistent with the complementarity remark.
- `cor:id-dep`: $J=dP-I/d$, $\Tr_H|J|=2(1-1/d^2)I_H$ — recomputed and
  correct.
- `thm:depolarizing-chebyshev`: the one-sided twirl, Jensen step, and the
  two width equalities — correct.
- `lem:pinching-diamond`: $2(1-1/\ell)$ both directions — recomputed and
  correct; the $\ell=1$ edge gives $0$ consistently with the
  upper-envelope definition.
- `thm:block-pinching-upper` and `cor:balanced-pinching-upper`: affine
  dimensions $r_{\mathrm{out}}=d_A^2(\sum b_j^2-1)$ and
  $r_{\mathrm{in}}=(\sum a_i^2)(d_B^2-1)$ — recomputed and correct;
  $Q_\ell(d)$ minimality exchange argument — correct.
- `prop:convex-projection-upper`: Helly step, barycenter estimate
  $(m-1)/m\le k/(k+1)$, and the bound $2(D-r)/(D-r+1)\Delta$ — correct.
- `cor:full-width-interval` at $r=0$: $D+1\ge d_B\min\{d_A,d_B\}$ in both
  cases — correct.
- `thm:full-state-antipodal` and `prop:replacement-perfect-index` — correct.
- Clifford appendix: anticommutation of the $2q+1$ generators (verified for
  all pairs, including $\Gamma_{2q+1}$), $H_u^2=I_C$, $\sigma_u\sigma_{-u}=0$,
  unitarity of $(I+iH_u)/\sqrt2$, and the overlap
  $\tfrac1p\Tr((U_u^{(C)})^\dagger{}^2)=-\tfrac{i}{p}\Tr H_u=0$ — correct.
- `thm:program-packing-rate` appendix proof: the volume argument
  $L(\eta/2)^n\le(2+\eta/2)^n$ (states lie in the trace-norm ball of radius
  $2$ about $\rho_1$; norm balls scale as $r^n$), giving
  $\eta\le4/(L^{1/n}-1)$ and
  $e(\mathcal P)\ge\Delta/2-2/(L^{1/n}-1)$ — correct as proved.
- `cor:explicit-programming`: $d^2$ Weyl channels pairwise at distance $2$;
  the Bloch computation $\|\rho_i-\rho_j\|_1=\|r_i-r_j\|_2$,
  $\sum_{i<j}\|r_i-r_j\|_2^2\le16$, and
  $\gamma_{2,2}\ge1-\tfrac12\sqrt{8/3}$ — recomputed and correct.
- `prop:postselection`: the normalization estimate
  $\|\sigma/p-\tau/q\|_1\le2\|\sigma-\tau\|_1/p_0$ (via
  $q|1/p-1/q|=|p-q|/p$) — correct.
- `thm:sampled-transcript` and `cor:sampled-channel-transcript` — correct
  (Borsuk–Ulam on $p\circ h:S^{c-1}\to\Delta(T)\subset\mathbb R^{c-1}$).
- `thm:sampled-achievability`: $\|J_\Delta\|_1\le d_A\sqrt{d_Ad_B}\,
  \|\widehat J_\Delta\|_2$ (via $\|J\|_1\le\sqrt{d_Ad_B}\|J\|_2$ and
  $J=d_A\widehat J$), the multinomial identity, and the $O(N^{-1/2})$ bound —
  correct; only the $\eta$-range inherited from F1 is defective.
- `prop:physical-continuity`: hybrid argument with diamond-norm
  stabilization — correct.
- Coindex conventions: singleton $=-1$, discrete $\ge2$ points $=0$,
  $F_2(S^n)=n$, $\coind F_2(\Sstate(M))=m^2-2$, and the structured bounds
  for $\mathbb{CP}^{m-1}$ and rank-$k$ strata — all consistent.
- All constants in `ex:qubit` and `fig:qubit-envelope` ($D_{2,2}=12$,
  $\delta_0=3/2$, breakpoints $r=3,4,12$, convex value $1.8$ at $r=3$) —
  recomputed and correct.

---

## Part 2. Stylistic writing and syntax scan

Scripted scans (doubled words, trailing whitespace, `\epsilon`,
British/American spelling drift, `iff`, `w.r.t.`, "Sec.", contractions,
ASCII-vs-TeX quotes, dash conventions) returned no violations; American
spelling is consistent throughout (depolarizing, centered, normalized,
fiber, minimize). The remaining items are judgment calls:

1. **Date format** (line 46): `\date{friday 28 august 2026}` — lowercase
   weekday and informal casing; use a standard journal format, e.g.
   `August 28, 2026`.
2. **Author block** (lines 42–45): `\author{xx xx\\\small Email: …\\\small
   xx\\\small ORCID: xx}` — the mailto address (`xx_xx@xx.xx.xx`) and the
   displayed address (`xx\_xx@xx.xx.xx.xx`) already disagree, and "xx" lines
   without \small are typographically inconsistent. For an anonymized
   submission the whole block is fine, but unify it.
3. **Informal inline citation** (line 2504): "the diamond norm is already
   stabilized at a reference dimension $d_A$ (Watrous)" — write
   `~\cite{Watrous2018}`.
4. **Meta-commentary inside a proof** (line 2312): "(max $2$ for orthogonal
   pure states with antipodal Bloch vectors $\|r_i-r_j\|=2$, so factor $2$
   would incorrectly give $4$)" — an editorial note about an error that is
   not made in the text; delete it.
5. **Interrupting parentheticals**:
   - `thm:program-packing-rate` (line 2285): "suppose $L\ge2$ (so
     $L^{1/n}-1\neq0$) target unitary channels" — the parenthetical splits
     the object of "suppose"; rephrase, e.g. "suppose $L\ge2$ target unitary
     channels are … (for $L=1$ the bound is trivial)".
   - `prop:structured-coindex` item 2 (line 2074): "(with $n\ge1$ so that a
     small embedded $S^{n-1}$ exists)" — nested justification; fold into the
     prose.
6. **Defensive/meta statements** (inconsistent with a purely declarative
   journal style):
   - `thm:depolarizing-chebyshev` (line 1388): "No uniqueness of the optimal
     center is asserted."
   - `prop:unitary-coordinate-bound` (line 1205): "not an assertion that
     $d^2$ is sufficient."
   - `tab:channel-scales` caption (line 1797): "are not claimed to equal
     either envelope."
   - `prop:postselection` proof (line 2611): "(this Hermitian case suffices
     because the relevant states are Hermitian; no claim for arbitrary
     operators is needed)".
   - `thm:sampled-achievability` proof (line 2802): "For small $N$ or small
     $\eta$ this bound may exceed the trivial diameter $2$; it is primarily
     an existence and asymptotic statement and may be capped at $2$."
   - `rem:certified-envelope` (line 1264): "reflects the current proof
     techniques … and not necessarily the exact value" — this one is a
     legitimate statement about certified status, but the phrasing can be
     tightened to a declarative form.
7. **Awkward antecedent** (`ex:qubit`, line 1828): "This zero denotes
   existence of an exact abstract code, not a canonical physical programming
   protocol." — "This zero" refers to the width value; rephrase, e.g. "The
   vanishing of both widths at $r\ge12$ records the existence of an exact
   abstract code, not of a physical programming protocol."
8. **Layout**: two minor overfull boxes remain — 4.4pt (lines 1882–1885) and
   19.7pt (`cor:query-cq`'s inline $\mathfrak C_N^{\mathrm{cq}}(m_1,\ldots,
   m_c)$, lines 2570–2572). Both are within the 2.5cm margin; the latter can
   be fixed by allowing a break or shortening the notation.
9. **Practical note**: the preamble uses `microtype` with default Computer
   Modern fonts; pdfTeX aborts with "auto expansion is only possible with
   scalable fonts" unless scalable fonts (cm-super/lmodern) are installed.
   Consider adding `\usepackage{lmodern}` so the source compiles in any
   standard TeX distribution.

---

## Part 3. Terminology consistency scan

1. **"Compression" vs "reconstruction width".** The title ("…Compression
   Bounds…"), abstract, and keywords ("quantum channel compression") use
   "compression", but the paper's only defined object is the
   "encoder-continuous reconstruction width" (`def:width`); "compression
   width" never appears in the body. Either define compression as
   reconstruction width in the introduction, or retitle.
2. **"Pinching" vs "dephasing".** The body's canonical term is "(block)
   pinching" (31 occurrences, plus the pinching theorems and envelopes);
   the abstract says "balanced input/output dephasing" and `ex:qubit` says
   "complete output dephasing". Align the abstract and the example on
   "pinching" (dephasing is the special case of complete block pinching, and
   is a useful term only when the distinction matters).
3. **"Antipodal profile" vs "antipodal separation profile".** The definition
   is titled "Antipodal separation profile" but the body refers 4 times to
   the "antipodal profile". Pick one (preferably the definition's title, or
   introduce the abbreviation at the definition).
4. **"Flagged" is undefined terminology in this paper.** It appears at two
   sites: `fig:replacement-join` caption ("flagged version to $nd_B^2-2$
   for instruments") and the Chebyshev appendix proof ("since the flagged
   maps of channels are channels"). "Flagged" is instrument vocabulary
   (output flags), defined only in the supplement. Replace: "the dilated
   maps $(\id_R\otimes\Phi)$ are channels", and "the $n$-outcome analogue".
5. **Instrument notation leaks into the channel paper.**
   `fig:replacement-join`'s balanced note displays
   $r_{\mathrm{out}}^{(n)}=d_A^2(n\sum b_i^2-1)$ and
   $r_{\mathrm{in}}^{(n)}=(\sum a_i^2)(nd_B^2-1)$ — the outcome number $n$
   and superscript $(n)$ belong to the supplement's instrument version. The
   caption does say "(instrument analogue, cf. supplementary)", but the note
   itself does not carry that qualifier. Mark the note as the instrument
   analogue, or display the channel versions ($n=1$).
6. **Keywords list "quantum instruments"**, though instruments are deferred
   entirely to the supplement. Either drop the keyword or keep it only if
   the supplement is co-submitted.
7. **Overloaded $\Delta$.** Four different objects use $\Delta$:
   the diameter in `prop:convex-projection-upper`; the pairwise separation
   in `thm:program-packing-rate`, `prop:program-separation`, and
   `cor:explicit-programming`; the simplex $\Delta_D$ in
   `prop:one-query-injective`; and the simplex $\Delta(T)$ in
   `def:sampled-transcript`. All uses are locally clear, but renaming one of
   the two families (e.g. $\mathcal P_D$ for the simplex) would remove the
   collision.
8. **Consistent terminology confirmed.** The following are used uniformly
   and correctly: "completely depolarizing channel" / $\Omega_{A,B}$;
   "centered relative diamond in-radius" / $\rho_\diamond$; "Chebyshev
   center" / covering radius $R$; "affine dimension" $D_{A,B}$;
   "antipodal separation profile" values; the breakpoints $d_B^2-2$ and
   $d_B^2-1$; "perfect-separation index" $\pi,\pi_{\mathrm U}$; "retained
   code" / "complete retained code"; "latent space/dimension";
   $\beta_r,\ U_r,\ \rhodep,\ \delta_r^\diamond,\ \widetilde\delta_r^\diamond$;
   American spelling; and the convention $d_B>1$ after the singleton case.
9. **Theorem-environment counter**: definitions, lemmas, propositions,
   corollaries, remarks, and examples share one counter — consistent
   throughout, including the appendix (no numbering restarts).

---

## Summary of recommended actions by priority

1. Fix F1 (POVM positivity condition) in `prop:one-query-injective` and
   `thm:sampled-achievability`.
2. Remove F2 (placeholder line) and F3 (stray undefined-symbol sentence).
3. Resolve F4: strengthen `thm:partition`/`cor:block-envelope` to
   $\alpha_r\ge1$ via the Jordan block spheres (already implicit in the
   figure), or correct the figure; the strengthened version is preferred.
4. Apply the minor fixes F5–F11.
5. Apply the Part 2 style items and the Part 3 terminology items.
