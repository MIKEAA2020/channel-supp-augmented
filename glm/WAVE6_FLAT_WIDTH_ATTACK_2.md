# Wave 6 — The Flat-Width Attack, Part 2: the Coordinate Dichotomy

**Date:** 2026-09-08. **Author:** GLM (this assistant).
**Mandate (user, verbatim):** *"**Suggested next attacks:** (a) close the exact value `δ₁(Δ₄) ∈ [4/3, 3/2]`; (b) the classical range `2 ≤ r < ⌈(n−2)/2⌉` (does an `r ≥ 2` median-type obstruction exist?); (c) the quantum small-`n` cases at `r = 1`."* — under the standing policy of elevating mathematics rather than softening claims, applying all corrections as new versions, and committing and pushing.

**Outcome in one line:** all three attacks land, and they unify: replacing the v4 slot-counting by **coordinate counting** (`nd_B` flags indexed by (slot, ONB vector)) turns the scattered v4 picture into a single **coordinate dichotomy** — `δ_r = 1` above the diagonal `nd_B ≤ 2r+2`, `δ_r ≥ 4/3` below it — which is now a **theorem for `d_B ∈ {1, 2}`** (complete classical and qubit dichotomies), refutes the v4 refined conjecture at `r ≥ 2`, closes `δ₁(Δ₄) = 4/3` exactly, settles nearly all quantum small-`n` cases including the channel-level `n = 1` instance, and survives as the new Conjecture `con:coord-flat` only in its `d_B ≥ 3` flat direction.

**Deliverables:** `manuscript uploads v5/instruments-paper-revised5.{txt,pdf}` and `manuscript uploads v5/main-article-revised5.{txt,pdf}` (new versions; v2/v3/v4 originals untouched), produced by `scripts/edit_v5.py` (9 tagged edits) with the replacement block at `scripts/wave6_block.tex`.

---

## 1. The key move: coordinate flags

The v4 obstruction (Theorem `thm:nonflat-d1`) counted **slots**: `n` flags `w_j` (slot `j`), so the median argument needed `n ≥ 5`. The upgrade counts **coordinates**: fix an ONB `(ψ_k)` of `B` and let `w_{(j,k)}` be the instrument whose `j`-th block is `ψ_kψ_k*`. There are `N = nd_B` such **coordinate flags**, pairwise at distance `2`, and the linear-programming bounds transfer verbatim with the coordinate weights `c_{(j,k)} = ⟨ψ_k|c_j|ψ_k⟩ ≥ 0`, `Σ c_{(j,k)} = 1`:

* vertex bound `‖w_{(j,k)} − c‖ ≥ 2(1 − c_{(j,k)})` (positive-part argument: `‖X‖₁ = 2Tr X₊ ≥ 2⟨ψ_k|X|ψ_k⟩`);
* edge bound `‖z − c‖ ≥ 2(1 − c_u − c_v)` for `z ∈ [w_u, w_v]` (trace-norm duality with sign-aligned diagonal test operators);
* general support bound: any `x` supported on a coordinate set `V` has `‖x − c‖ ≥ 2(1 − Σ_{u∈V} c_u)`.

**Disjoint-support pigeonhole:** if one fibre contains `q` points on pairwise disjoint coordinate sets, every decoder value errs by `≥ 2(q−1)/q` (numerically verified, V3).

Two mechanisms then produce the `q` disjointly-supported fibre points:

1. **Median + bipartite matching (r = 1, elementary, all q).** Take `t*` = the `q`-th smallest flag value. With `G` = flags at `t*`, `P` below, `Q` above: `P ≤ q−1`, `P + |G| ≥ q`, and `Q ≥ nd_B − P − |G| ≥ q − |G|`; a matching of size `min(P, Q) ≥ q − |G|` between below- and above-flags supplies IVT crossing points on the segments `[w_b, w_a]`. Total disjoint supports: `|G| + min(P,Q) ≥ q`. (Verified against 18 000 tie-heavy random instances, V2.)
2. **Topological Tverberg (r ≥ 2, q a prime power).** The coordinate embedding `Φ: Δ_{nd_B−1} → Inst_n`, `x ↦ Σ x_u w_u` is affine and injective; Özaydin's prime-power topological Tverberg theorem applied to `f ∘ Φ` on a `(q−1)(r+1)`-face gives `q` vertex-disjoint faces with a common image point. (For `q = 2` this is exactly the paper's Borsuk–Ulam antipodal profile — the two frameworks dovetail.)

## 2. Attack (a) — closed: `δ₁(Δ₄) = 4/3` exactly

* **Lower bound:** median matching with `q = 3` needs `2·3 − 1 = 5 ≤ nd_B`; at `n = 5`, `d_B = 1` this is the v4 bound `4/3`.
* **Upper bound (new, Proposition `prop:pair-d1`):** the v4 pair-mass *base* encoder `f(x) = x₁ + x₂`, `g(t) = (t/2, t/2, (1−t)/(n−2), …)` run at **general `n`** gives `δ₁ ≤ max{1, 2(n−3)/(n−2)}` (worst case at `t = 0`, tail concentrated: verified, V1). At `n = 5` this is `4/3`.

**`δ₁` of the four-dimensional simplex is `4/3`.** More generally `δ_r = 4/3` exactly at `n = 2r+3` for every `r ≥ 1` (Corollary `cor:exact-d1`: matching/Tverberg below, pair-mass recursion to the `(5,1)` base above). The general classical `r = 1` bracket improves from the v4 `[4/3, 2(n−2)/(n−1)]` (convex projection) to `[2(q−1)/q, 2(n−3)/(n−2)]` with `q = ⌊(n+1)/2⌋` — both ends → 2 as `n → ∞` with gap `O(1/n)` (e.g. `n = 7`: `[3/2, 8/5]`).

## 3. Attack (b) — yes: the `r ≥ 2` median-type obstruction exists, and it is Tverberg

**Theorem `thm:tverberg`:** `δ_r ≥ 2(q−1)/q` whenever `q` is a prime power with `(q−1)(r+1) ≤ nd_B − 1`. With `q = 3` (prime):

> **Corollary `cor:flat-fails`:** `δ_r ≥ 4/3 > 1` whenever `nd_B ≥ 2r + 3` — every `d_B ≥ 1`, every `r ≥ 1`.

Consequences:

* **The v4 refined conjecture `con:flat-refined` (flat throughout `2 ≤ r ≤ nd_B²−2`) is refuted** — e.g. at `(n, d_B, r) = (7, 1, 2)` and `(2, 4, 2)` (both inside the conjectured range). The v4 narrative ("the median argument is specific to one-dimensional latent spaces; no analogue for `r ≥ 2` is known") is corrected: the order structure of the line is *not* the mechanism — Tverberg's forced `q`-fold fibre intersection is, and it fires at every `r`.
* **Classical dichotomy (Corollary `cor:classical-dichotomy`), complete:** `d_A = d_B = 1`: `δ_r = 1 ⟺ n ≤ 2r+2` on the whole subcritical range; `δ_r ≥ 4/3` for `n ≥ 2r+3`. The v4 open range `2 ≤ r < ⌈(n−2)/2⌉` is entirely absorbed: flatness fails there for every `n ≥ 2r+3`. The classical flat-width problem is **solved** (exact flat values by `thm:flat-half`, exact boundary value `4/3`, two-sided brackets elsewhere).
* **Qubit dichotomy (Corollary `cor:qubit-dichotomy`), complete:** `d_B = 2`: `δ_r = 1 ⟺ r ≥ n−1` on the whole subcritical range. The flat threshold improves twice over v4: `n` → `n−1` (new direct **mass-split encoder**, Proposition `prop:mass-split`(ii): encode `n−1` traces, decode block `k` as `t_k I/d_B` — replaces the v4 trace-mass recursion with base `(1,1)`), and the obstruction covers `r ≤ n−2` (since `2n ≥ 2r+3 ⟺ r ≤ n−2`).
* **Exact interior value (Theorem `thm:mass-exact`):** for `d_B` a prime power, `δ_{n−1} = 2(1 − 1/d_B)` **exactly** — Tverberg with `q = d_B` (hypothesis `(d_B − 1)n ≤ nd_B − 1` always holds) meets the mass-split encoder. So `δ₁(2,3) = 4/3`, `δ₁(2,4) = 3/2`, `δ₁(2,5) = 8/5`, …, and for `d_B = 2` it reproduces the flat value `1`.

## 4. Attack (c) — the quantum small-`n` cases at `r = 1`: nearly closed

The coordinate counting dissolves the v4 belief that "`n ≤ 4` with `d_B ≥ 2` stays open (the counting needs five slots)". Five **coordinates** suffice, and one slot with `d_B ≥ 5` already carries them:

| case | verdict |
|---|---|
| `(n, d_B)` with `nd_B ≤ 4`, `d_B ≥ 2`: `(1,2)`, `(2,2)` | **flat** (`δ₁ = 1`): `(1,2)` is the collapse; `(2,2)` by the mass-split encoder — *new* (the smallest non-collapse quantum case, closed) |
| `n ≤ 4`, `d_B = 1` | flat (v4 `thm:flat-half` bases) |
| `nd_B ≥ 5` (e.g. `(3,2)`, `(4,2)`, `(2,3)`, `(2,4)`, `(1,5)`, …) | **non-flat**: `δ₁ ≥ 4/3` (`q = 3` matching); at `(2, d_B)` with prime-power `d_B ≥ 3`: exactly `2(1 − 1/d_B)` |
| `(1,3)`, `(1,4)` — qutrit/ququart **state spaces** | **the only open `r = 1` cases**: `δ₁ ∈ [1, 4/3]` and `[1, 3/2]` (constant decoder) |

**Correction of a v4 claim (recorded here):** the v4 instruments remark and the v4 channel open problem 1 stated that the *channel-level* `n = 1` instance "remains open / is not refuted". That assessment came from slot-counting; with coordinate flags the channel-level flat claim (`d_A = 1`, `δ_r^◇ = 1` on `1 ≤ r ≤ d_B²−2`, `d_B > 2`) **fails at `r = 1` for every `d_B ≥ 5`** and at every `r ≤ (d_B−3)/2` (Tverberg). The transfer is clean because at `d_A = 1` the diamond norm on channel differences is the trace norm on output states, so the channel widths coincide with the one-outcome instrument widths. The channel paper's open problem 1 now records this resolution; the flat value survives there only for `d_B ∈ {3,4}`.

## 5. The corrected conjecture (`con:coord-flat`, replacing `con:flat-refined`)

> Assume `d_A = 1` and `nd_B > 2`. Then `δ_{r,inst}^◇(C, B) = 1` **iff** `nd_B ≤ 2r + 2` (`1 ≤ r ≤ nd_B² − 2`).

Status: the obstruction direction is **proved for every `d_B`** (`cor:flat-fails`, sharpened to `2(q−1)/q`); the flat direction is **proved for `d_B ∈ {1,2}`**; the content is the `d_B ≥ 3` flat direction (one latent dimension per two flag coordinates — far beyond the pinching rate `Q₂(d_B)` per slot), consistent with `thm:mass-exact` (for `d_B ≥ 3`, `r = n−1` lies below the conjectured flat range and indeed `δ_{n−1} = 2(1−1/d_B) > 1`).

## 6. How the v5 manuscripts were changed

**Instruments (`instruments-paper-revised5`, 40 pages, +3 over v4):**
* `thm:nonflat-d1` **upgraded in place**: statement now `δ₁ ≥ 2(q−1)/q` for every `q` with `2q−1 ≤ nd_B` (all `d_B`, all `n ≥ 1`, including the state space); proof rewritten as the coordinate-flag + level-group + bipartite-matching argument (the v4 three-case analysis is its `q = 3` instance).
* **New** `thm:tverberg` (topological Tverberg bound, every `r`), `rem:prime-powers` (scope note), `cor:flat-fails` (the `4/3` corollary + refutation note).
* `prop:mass-split`(ii) **rewritten** as the direct mass-split encoder (`r = n−1`, error `≤ 2(1−1/d_B)`, decoder affine on the latent simplex — subsumes the v4 trace-mass reduction).
* **New** `prop:pair-d1` (pair-mass at `r = 1`, general `n`), `cor:exact-d1` (`δ₁ = 4/3` at `n = 5`; `δ_r = 4/3` at `n = 2r+3`), `cor:classical-dichotomy`, `cor:qubit-dichotomy`, `thm:mass-exact`.
* `thm:flat-qubit` **upgraded** to `n−1 ≤ r ≤ 4n−2` with the new proof.
* `rem:flat-status` **rewritten** (full coordinate picture, the two residual state-space cases, the `2 − 1/k` sub-boundary qubit bracket); `con:flat-refined` **replaced** by `con:coord-flat` + status paragraph.
* Abstract, `rem:exact-vs-certified` (items (x)/(xi) upgraded, new (xii), (a) scoped), Table 3 one-sphere row, conclusion specialisation, open problem (v) all updated; bibliography += Özaydin 1987, Tverberg 1966.

**Channel (`main-article-revised5`, 46 pages, unchanged length):** open problem 1's `d_A = 1` parenthetical rewritten: the channel-level instance is settled in the negative direction (`d_B ≥ 5` at `r = 1`, `r ≤ (d_B−3)/2` in general), with the diamond-vs-trace identification spelled out and the residual `d_B ∈ {3,4}` bracket noted.

**Verification:** numerical pre-flight `scripts/verify_wave6.py` — 25/25 checks pass (pair-mass worst cases incl. `4/3` at `n = 5`; 18 000 tie-heavy matching trials; disjoint-support LP; `(2,2)` flatness sampling; tail-`k` bounds; one-slot lemma; state-space radii; recursion boundary values). Both papers compile under Tectonic, exit 0, **zero** undefined references/citations, no duplicate labels (instruments 92 labels / 252 refs, channel 99 / 176; the channel's odd naive `$`-count is a pre-v5 counter artifact from multi-line inline math, byte-identical in v4); overfull boxes all sub-3 pt and pre-existing (0.19 / 2.99 / 0.14 pt); instruments 40 pages, channel 46; all 12 new theorem titles, the exact-value statements, the Özaydin/Tverberg entries, and the channel cross-reference verified in the compiled PDF text layers. Edits scripted and idempotent per source (`scripts/edit_v5.py`, 9 tagged edits).

## 7. What remains open (updated)

1. `con:coord-flat`, flat direction, `d_B ≥ 3`: does `r ≥ ⌈(nd_B−2)/2⌉` suffice for error one? (Pinching certifies only from `nQ₂(d_B) − 1`; the open window is `(nd_B−3)/2 < r < nQ₂(d_B)−1`.)
2. Exact sub-diagonal widths: classical `[2(q−1)/q, 2(n−2r−1)/(n−2r+2)]`; qubit `[4/3, 2 − 1/k]` at `r = n−k`.
3. The two residual state-space cases at `r = 1`: `d_B ∈ {3,4}` (brackets `[1, 4/3]`, `[1, 3/2]`).
4. Non-prime-power refinements of `thm:tverberg` (the r = 1 matching already avoids the restriction).
5. The affine-decoder variant of the median/Tverberg bounds (the LP uses `c_u ≥ 0`, which holds for instrument-valued decoders).

## 8. Security note

The GitHub personal access token was again shared in plaintext chat. Revoke and rotate it now that this wave is pushed.
