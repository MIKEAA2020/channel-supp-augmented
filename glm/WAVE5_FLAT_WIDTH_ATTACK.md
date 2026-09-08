# Wave 5 — The Flat-Width Attack: Conjecture `con:flat-d1` Refuted and the Refined Picture Proved

**Date:** 2026-09-08. **Author:** GLM (this assistant).
**Mandate (user, verbatim):** *"attack the flat-width conjecture (the simplex sub-case appears to be a tractable entry point)"* — under the standing policy *"for overclaims, prioritize rigorously elevating math to close gaps and meet or exceed them. do not regress or soften unless truly irrepairable/unreachable. demote to conjecture if truly plausible but proof remains out of reach. apply all corrections as new versions, commit and push."*

**Outcome in one line:** the attack **succeeds past the entry point**: the conjecture is **false as stated** (a complete, elementary proof is given below — the simplex sub-case is settled, and the refutation lifts to every output dimension `d_B`); at the same time the flatness programme is **not lost** — flatness is *proved* on the upper half of the subcritical range in the classical case and from latent dimension `n` for qubit outputs, and the refined statement survives as the new Conjecture `con:flat-refined`.

**Deliverables:** `manuscript uploads v4/instruments-paper-revised4.{txt,pdf}` and `manuscript uploads v4/main-article-revised4.{txt,pdf}` (new versions; the v2/v3 originals are untouched), produced by `scripts/edit_v4.py`.

---

## 0. Side note: the "54 edits" accounting (user's question 1)

The user asked how "applied all 54 edits" squares with "some of them were false or stale". The precise ledger (WAVE2_AUDIT_VERIFICATION_REPORT.md §0/§3–§5, WAVE3 §2):

| Disposition | Count | Applied in v3? |
|---|---|---|
| Verified genuine (CONFIRMED / VALID-MINOR) | **46** | **Yes — all 46** (as corrections, elevations, or the one demotion I2) |
| False positive (max2's `\node`→"ode" / `\nu`→"u" unescaping artifacts; `\rhodep` defined at L38) | 3 | No — nothing to fix |
| Not supported by the current text (stale quote) | 1 | No — target sentence not present |
| Rejected on the merits (I26 figure proportions) | 1 | No — criticism incorrect |
| Self-retracted by its own auditor | 1 | No |
| Conditional worry resolved as already-correct (claude's Clifford concern) | 1 | No — verified correct at L3505 |
| Suggestion-class, not a defect (I28) | 1 | No |
| **Total** | **54** | 46 applied, 8 documented |

So: **all 54 claims were evaluated; the 46 verified ones were all applied; the 8 false/stale/unconfirmed ones were explicitly not applied, each with a documented reason** (WAVE3 §2 "Explicitly not changed"). Any phrasing suggesting "all 54 edits were applied" conflated the evaluation count with the application count — the script-level counts "53 tagged edits" (instruments) and "85 tagged edits" (channel) are a third ledger: *edit operations* in `edit_instruments_v3.py`/`edit_channel_v3.py`, not claim counts. No contradiction in the underlying work; the loose phrasing is corrected here.

---

## 1. The problem

**Conjecture `con:flat-d1` (instruments paper, v3):** for `d_A = 1` and `nd_B > 2`,
`δ_{r,inst}^◇(C, B) = 1` for all `1 ≤ r ≤ nd_B² − 2`.

Under the paper's isometry, the body `Inst_n(C, B)` is the flagged state space with metric `‖τ − σ‖ = Σ_k ‖τ_k − σ_k‖₁`, and for `d_B = 1` this is the classical simplex `Σ_{n−1} ⊂ (R^n, ‖·‖₁)`. The paper knew: `δ_r ≥ 1` on the whole subcritical range (exact antipodal profile), `δ = 1` at the top subcritical index, and (for `d_B ≥ 2`) from the pinching threshold `nQ_2(d_B) − 1` upward. The bracket at `r = 1`, `d_B = 1` was `[1, 2(n−2)/(n−1)]` — open from `n ≥ 5` on.

The user's instinct that the simplex sub-case is the tractable entry point is vindicated in both directions: it is tractable enough to **refute** the full-range flatness, and simple enough to **prove** flatness on a large sub-range.

## 2. Result A — the refutation (Theorem `thm:nonflat-d1`)

**Theorem.** *Assume `d_A = 1` and `n ≥ 5`. Then `δ_{1,inst}^◇(C, B) ≥ 4/3 > 1` for every `d_B ≥ 1`.*

**Proof.** Fix a unit vector `ψ ∈ B` and let `w_j` be the instrument whose `j`-th block is `ψ` (other blocks zero). These are `n` "classical flags": `‖w_i − w_j‖ = 2`. For any decoder value `c = (c_1, …, c_n)` (an instrument: `c_k ≥ 0`, `Σ_k Tr c_k = 1`), any edge point `z = (1−λ)w_i + λw_j`:

* vertex bound: `‖w_j − c‖ ≥ 2(1 − Tr c_j)` (since `‖X‖₁ ≥ |Tr X|` and `Tr c_k ≥ 0`);
* edge bound: `‖z − c‖ ≥ 2(1 − Tr c_i − Tr c_j)`.

Let `f : Inst → R` be any continuous encoder, `g` any decoder, `τ_j = f(w_j)`. Order the `n` values; take `r = ⌈n/2⌉` (so `r ≥ 3`, `n − r ≥ 2`) and the level `t*` of the rank-`r` flag. Every point of the leaf `f⁻¹(t*)` is decoded to the single point `c = g(t*)`. Three exhaustive cases:

1. **≥ 3 flags share `t*`.** Then `Σ_{j∈G} Tr c_j ≤ 1`, so some `Tr c_j ≤ 1/3`, and that flag is at distance `≥ 2(1 − 1/3) = 4/3`.
2. **Exactly 2 flags share `t*`, with ≥ 1 flag strictly on each side** (automatic: the two occupy consecutive ranks around `r`). The leaf also contains a crossing point `z` of an edge `[w_u, w_v]` with `f(w_u) < t* < f(w_v)` (intermediate value theorem). If both flags were within `4/3`, then `Tr c_a, Tr c_b ≥ 1/3`, so `Tr c_u + Tr c_v ≤ 1/3`, so `‖z − c‖ ≥ 4/3`.
3. **Exactly 1 flag `w_m` at `t*`, with `P ≥ 2` below and `Q ≥ 2` above.** With `β = Tr c_m`: if `β ≤ 1/3` the flag itself is `≥ 4/3` away. If `β > 1/3`, the leaf meets all `PQ ≥ 4` cross edges; summing the edge bound over them gives `Σ (Tr c_u + Tr c_v) ≤ max(P, Q)(1 − β)`, so some crossing has `Tr c_u + Tr c_v ≤ (1−β)/min(P,Q) ≤ (1−β)/2 < 1/3`, i.e. distance `> 4/3`.

∎

**Remarks on the proof.**
* It is *elementary*: intermediate value theorem plus the trace-norm bounds; no algebraic topology.
* The mechanism is genuinely one-dimensional: the *order structure* of `R` forces a median level. There is no known analogue for `r ≥ 2` — this is precisely why the refutation does not propagate upward.
* The constant `4/3` is tight for the method: in case 3 the LP optimum over `c` is attained at `Tr c_m = 1/3`, the four below/above traces `1/6` each, giving distance exactly `4/3` on all five pinned points.
* The proof works verbatim for every `d_B ≥ 1` — the flags `w_j` embed a classical `(n−1)`-simplex into the quantum body — so the conjecture fails at `r = 1` for *all* output dimensions whenever `n ≥ 5`. (For `d_B ≥ 2` with `n ≤ 4` the question stays open; the counting needs five slots.)
* Scope note: the theorem is proved under `def:width`'s decoder convention (`g` instrument-valued). The affine-hull variant needs a modified counting step and is left out of the paper's statement; see §6 (open).
* Consistency checks: for `n = 4` the median rank `r = 2` has only `r − 1 = 1` below — the argument correctly does *not* fire, matching the flatness proved below; for the collapse case (`nd_B ≤ 2`) there are fewer than 5 flags.

## 3. Result B — flatness on the upper half (Theorem `thm:flat-half`)

**Theorem.** *Assume `d_A = d_B = 1`, `n ≥ 3`. Then `δ_{r,inst}^◇(C, C) = 1` for `⌈(n−2)/2⌉ ≤ r ≤ n − 2`.*

**Proof.** Lower bound: exact antipodal profile. Upper bound: the **pair-mass reduction** (`prop:mass-split`(i)): from an `(r−1)`-dimensional encoder/decoder `(φ, ψ)` of the `(n−2)`-outcome simplex with error `E`, build

`f(x) = (x₁ + x₂, m·φ(x̃))`, `g(t, w) = (t/2, t/2, m·ψ(w/m))`, `m = 1 − x₁ − x₂, x̃ = tail/m`,

with error `≤ |x₁ − t/2| + |x₂ − t/2| + m·E ≤ t + mE ≤ max{1, E}`. Iterating `(n, r) → (n−2, r−1)` preserves error `≤ 1` and lands on a base `r = 1, n ∈ {3, 4}` exactly when `n ≤ 2r + 2`. The bases are supplied by the one-dimensional encoder `f(x) = x₁ + x₂` with decoder `g(t) = (t/2, t/2, (1−t)/(n−2), …)`: for every leaf point the overlap `Σ_k min(x_k, g(t)_k) ≥ 1/2` (the pair contributes `≥ t/2`; the `n = 4` tail contributes `≥ (1−t)/2`; the `n = 3` tail is exact), hence `‖x − g(t)‖₁ ≤ 1`. ∎

The base `n = 4` (which the v3 bracket left open at `[1, 4/3]`) is new; `n = 3` recovers the top-subcritical corollary. The reduction explains *why* flatness holds only above the diagonal `n = 2r + 2`: each latent dimension buys two classical outcomes, and the leftover odd case bottoms out on the `n = 3` base.

## 4. Result C — qubit outputs (Theorem `thm:flat-qubit`)

**Theorem.** *Assume `d_A = 1`, `d_B = 2`, `n ≥ 2`. Then `δ_{r,inst}^◇(C, B) = 1` for `n ≤ r ≤ 4n − 2`.*

**Proof.** The **trace-mass reduction** (`prop:mass-split`(ii)): encode the `n − 1` outcome traces plus a compressed copy of the last block, decode block `k` as `t_k·I_B/d_B`. A block of trace `t_k` is reconstructed within `2(1 − 1/d_B)·t_k` (maximal eigenvalue of a state is `≥ 1/d_B`), so the total error is a convex combination of `2(1 − 1/d_B)` and the tail error `E`. For `d_B = 2` this is `max{1, E}`; with the base `E = δ₁(state space of the qubit) = 1` (the paper's own pinching at `n = 1`: `r_out = Q₂(2) − 1 = 1`) the error is `≤ 1` at `r = n`. ∎

This strictly improves the two-sector pinching threshold `nQ₂(2) − 1 = 2n − 1` on the whole interval `[n, 2n − 2]`. For `d_B ≥ 3` the trace-mass head cost `2(1 − 1/d_B) ≥ 4/3` blocks the argument — the classical pair-mass trick has no quantum analogue because a known-mass quantum block still carries `d_B² − 1` unknown parameters.

## 5. The refined conjecture (`con:flat-refined`)

> Assume `d_A = 1` and `nd_B > 2`. Then `δ_{r,inst}^◇(C, B) = 1` for `2 ≤ r ≤ nd_B² − 2`.

Status table for `d_A = 1` (subcritical range `1 ≤ r ≤ nd_B² − 2`):

| Case | Flat (proved) | Non-flat (proved) | Open |
|---|---|---|---|
| `d_B = 1`, `n ≤ 4` | whole range (`thm:flat-half`, `thm:collapse`) | — | — |
| `d_B = 1`, `n ≥ 5` | `r ≥ ⌈(n−2)/2⌉` (`thm:flat-half`) | `r = 1`: `δ ≥ 4/3` (`thm:nonflat-d1`) | `2 ≤ r < ⌈(n−2)/2⌉`; exact value of `δ₁ ∈ [4/3, 2(n−2)/(n−1)]` |
| `d_B = 2`, `n ≥ 2` | `r ≥ n` (`thm:flat-qubit`) and `r ≥ 2n − 1` (pinching) | `r = 1`, `n ≥ 5` (`thm:nonflat-d1`) | `2 ≤ r < n` |
| `d_B ≥ 3` | `r ≥ nQ₂(d_B) − 1` (pinching) | `r = 1`, `n ≥ 5` (`thm:nonflat-d1`) | `2 ≤ r < nQ₂(d_B) − 1` |
| channel-level `n = 1` | — | — | whole range (untouched by the counterexample, which needs 5 outcomes) |

Plausibility of the refined conjecture: the only proved obstruction lives at `r = 1` and is created by the order structure of the line (a median level is forced); latent spaces of dimension `≥ 2` have no forced median, and every proved value above the bottom index equals the floor.

## 6. What remains open (updated open-problem list)

1. `δ_r` on the classical range `2 ≤ r < ⌈(n−2)/2⌉` (`n ≥ 7`) — the residual gap of `thm:flat-half`.
2. The exact bottom width `δ₁(Δ_{n−1}) ∈ [4/3, 2(n−2)/(n−1)]` for `n ≥ 5`; the method's constant `4/3` is tight for the median-LP, the convex-projection upper end decays to `2` — where in between?
3. Quantum small-`n`: `r = 1` for `d_B ≥ 2`, `n ≤ 4` (the median argument needs five slots; intra-slot orthogonal pairs only force `≥ 1`).
4. Whether an `r ≥ 2` analogue of the median obstruction exists (e.g. via Tverberg-type partitions — though hull intersections do not control nonlinear fibres, so new ideas are needed).
5. The affine-decoder variant of `thm:nonflat-d1` (the counting step uses `Tr c_k ≥ 0`).
6. The channel-level instance (`n = 1`) — now the only place the original flat statement survives unrefuted.

## 7. How the v4 manuscripts were changed

**Instruments (`instruments-paper-revised4`):**
* Conjecture `con:flat-d1` + its evidence paragraph **removed**; replaced after the specialisation list by: Theorem `thm:nonflat-d1` (full proof), Proposition `prop:mass-split` (both reductions, full proof), Theorem `thm:flat-half` (full proof), Theorem `thm:flat-qubit` (full proof), Remark `rem:flat-status` (the table of §5 in prose), Conjecture `con:flat-refined` + status sentence.
* Pointer sentence added at the end of the input-independent specialisation item.
* Abstract: one sentence added (refutation at the bottom index; flatness upper-half/qubit).
* `rem:exact-vs-certified`: exact list extended by items (x) (classical upper half) and (xi) (qubit range).
* Table 3 ("One-sphere regime" status cell): the `d_A = 1` refinements appended.
* Conclusion: specialisation sentence and open problem (v) rewritten around the new results; open problem (v) now also asks for the exact bottom width with its bracket.

**Channel (`main-article-revised4`):** open problem 1's cross-reference updated — the flat-widths *conjecture* of the companion is now the flat-widths *problem*, with the instrument-level refutation at `n ≥ 5` noted and the channel-level case (`n = 1`, `d_B > 2`) explicitly flagged as still open. (The channel paper's own `n = 1` conjecture is unchanged — it is not refuted.)

**Verification:** both compile under Tectonic, exit 0, **zero** undefined references/citations, no duplicate labels (instruments 84 labels / 180+ refs; channel 99 labels), environments and braces balanced, `$`-parity even; overfull boxes all sub-3 pt and pre-existing (0.19 / 2.99 / 0.14 / 0.62 pt); instruments 37 pages, channel 46 pages; the new theorem titles verified present in the compiled PDF text layer. Static audit re-run clean. Edits scripted and idempotent per source (`scripts/edit_v4.py`, 8 tagged edits).

## 8. Security note

The GitHub personal access token was again shared in plaintext chat. Revoke and rotate it now that this wave is pushed.
