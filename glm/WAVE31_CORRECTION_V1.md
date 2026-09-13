# WAVE 31 — THE V11 CORRECTION WAVE (the R1 repair + the strengthened lattice-index gate)

**Date:** 2026-09-13
**Charge:** "a correction wave (v11) applying the ~six-line R1 repair and the
strengthened lattice-index gate" — i.e., Wave 30's Finding R1 (the one
mandatory correction of the referee read of Proposition 6.16 /
`prop:cupsquare`), repaired in the manuscript as v11, with the verifier's
gate-design gap closed by a new lattice-index gate, exactly as the referee
recommended. R2–R7 (the six one-line repairs) were **not** in the charge and
are **not** applied; they remain on the record as recommendations.

**Deliverable:** `manuscript uploads v11/instruments-paper-revised11.tex/.txt/.pdf`
(the main article needs no change — the referee's integration assessment,
confirmed here: its sync clauses reference the flag-quotient computation, not
the top-class generator; grep for "discriminant" in the main article returns
nothing).

---

## 1. The six-part R1 repair, as applied

All edits by `edit_v11.py` (five anchored replacements, each asserted to
match exactly once in the v10 source; the v10→v11 diff is confined to
exactly those five regions — statement 1872–1873, Step 2 1945–1955, Step 3
1985–1988, Step 7 2072–2081, remark 2213–2217):

1. **The Proposition statement (R1 part 4).** "…and a discriminant class
   generating `H⁶`" → "…and `H⁶(B;Z) ≅ Z`, in which the discriminant class
   is twice a generator."
2. **Step 2 (R1 part 1).** The integral module equality
   `Z[σ₁,σ₂,σ₃] ⊕ Δ·Z[σ₁,σ₂,σ₃]` is replaced by the two-level statement:
   the **integral** free part is the **orbit-sum invariant lattice** (spanned
   by the `C₃`-orbit sums of the degree-`d` monomials, fixed monomials
   included — the whole invariant lattice, because an invariant polynomial's
   monomials occur with equal coefficients on each orbit), which
   **rationally** is the degree-`d` part of
   `Q[σ₁,σ₂,σ₃] ⊕ Δ·Q[σ₁,σ₂,σ₃]` (orbit counts = module monomial counts),
   and **integrally** the module is only a finite-index sublattice — index
   one in degrees `d ≤ 2` (exactly the crux's degrees), then `2, 2, 4, 8` in
   degrees 3–6 — with the degree-3 witness stated in the text:
   `S₁ = χ₁²χ₂+χ₂²χ₃+χ₃²χ₁ = ½(σ₁σ₂−3σ₃+Δ)` is invariant but lies in the
   module only after doubling.
3. **Step 3 (R1 part 2).** The `H⁶(BK)` display now reads
   `Z{A₁, S₁, S₂, σ₃} ⊕ Z/3·τ³` (the orbit-sum basis; `A₁ = χ₁³+χ₂³+χ₃³`,
   `S₂ = χ₁²χ₃+χ₂²χ₁+χ₃²χ₂`), with the relations
   `S₁+S₂ = σ₁σ₂−3σ₃`, `S₁−S₂ = Δ` stated, and the index-two note ("the
   symmetric-function module of Step 2 spans an index-two sublattice of this
   free part, the four orbit sums generating it exactly"). The `H⁴(BK)`
   display is untouched — it was already correct as a lattice (the referee's
   "safe degrees").
4. **Step 7 (R1 part 3).** The degree-6 run now quotes the quotient on the
   orbit-sum lattice:
   `H⁶(B;Z) = (Z{A₁,S₁,S₂,σ₃} ⊕ Z/3·τ³)/⟨σ₁³, σ₁σ₂, 2τ³, σ₃⟩ ≅ Z·⟨S₁⟩`,
   with the substituting chain spelled out (`σ₁σ₂ = S₁+S₂+3σ₃`,
   `σ₁³ = A₁+3(S₁+S₂)+6σ₃`; the relations kill `σ₃`, then `S₁+S₂`, then
   `A₁`; `2τ³=0` forces `τ³=0` since two is invertible modulo three), and
   the conclusion: the top class is the orbit sum `S₁`, in which the
   discriminant `Δ = S₁−S₂ = 2S₁` is **twice a generator** — consistent with
   the rational cohomology `Q ⊕ Q·Δ̄`, where two is invertible and the
   discriminant does generate.
5. **`rem:machine-certificate` (the R1 knock-on the referee flagged in §5).**
   The residuals list now names the lattice layer the strengthened gate
   certifies: "the orbit counts, the orbit-sum invariant lattice together
   with its finite index over the symmetric-function module, the
   twice-a-generator position of the discriminant in the top class, the
   torsion product rule, …". (The "self-contained invariant-theory step"
   phrase stands: the step is self-contained and, after the repair, correct.)
6. **The supersession note (R1 part 6).** This section: the wave-29 record
   "H⁶ = Z·Δ" (in `WAVE29_MACHINE_FREE_DERIVATION.md` and its commit
   message) is **superseded** by `H⁶(B;Z) ≅ Z·⟨S₁⟩` with `[Δ] = 2[S₁]`. The
   wave-29 note is left as the historical record (project practice: the
   waves' notes are immutable; corrections are recorded in the correcting
   wave — cf. wave 27's two W26 corrections). The additive tuple
   `(Z, 0, Z/3, Z/3, Z/3, Z/3, Z)` — the object the three independent routes
   agree on — is unaffected, since it records the group `Z`, not the
   generator.

**Nothing else moved.** The crux (Step 5), the transgression pins (Step 4),
Lemma 6.17, `thm:equal-basis`, `thm:equal-basis-plane`, `thm:state-d2`, and
`δ₂(D(C³)) = 4/3` are untouched — the referee's scoping (R1 is confined to
the decorative layer: the module presentation and the top-degree generator)
was verified line by line before editing: `thm:equal-basis`'s proof uses only
`H²(B) = Z/3`; the abstract/intro/conclusion provenance phrases assert the
additive cohomology and the cup-square decision, not the generator.

---

## 2. The strengthened lattice-index gate (R1 part 5)

The gate-design gap: Wave 29's G3 compared **ranks** only
(`#orbits` vs `nmons(d)+nmons(d−3)`) — an index-2 sublattice is invisible to
a rank check. The strengthened verifier
`w31_derivation_check.py` (= the wave-29 verifier + the new gate **G3L**,
inserted immediately after G3; the wave-29 script and transcript are
preserved unchanged as the historical artifacts) re-runs the **full battery**
with the lattice fine structure now certified:

* **(a) The index table.** For each degree `d = 0..8`: the orbit-sum
  invariant lattice `M_d`, the module lattice
  `L_d = Z[σ]_d + Δ·Z[σ]_{d−3}`, the containment `L_d ⊆ M_d` (rational solve
  + integrality), and the index `[M_d : L_d]` by Smith normal form of the
  change-of-basis matrix: **1, 1, 1, 2, 2, 4, 8, 16, 32** — exactly the
  referee's table. The log states the consequence: index one in degrees
  0–2, the degrees of the Step-5 crux, so the `H²/H⁴(BK)` displays
  `Zσ₁` and `Zσ₁² ⊕ Zσ₂` are exact lattice statements.
* **(b) The orbit-sum identities** the repaired text uses:
  `S₁+S₂+3σ₃ = σ₁σ₂`, `S₁−S₂ = Δ`, `2S₁ = σ₁σ₂−3σ₃+Δ`,
  `σ₁³ = A₁+3(S₁+S₂)+6σ₃` — all verified as polynomial identities.
* **(c) The degree-3 witness.** The named system
  `S₁ = a·σ₁³ + b·σ₁σ₂ + c·σ₃ + e·Δ` has the unique rational solution
  `(a,b,c,e) = (0, ½, −3/2, ½)` — **not integral**, so `S₁ ∉ L₃`; and
  `2S₁ ∈ L₃`. (Development note: this gate's first run caught a label-order
  bug in my own witness printout — the solved values were the referee's but
  printed against the wrong column names, and the `σ₁³` identity had its
  operands transposed; both fixed, gate re-run. The mathematics never
  changed.)
* **(d) The top-class quotient.** The relation rows of
  `⟨σ₁³, σ₁σ₂, σ₃⟩` in the invariant basis `{A₁,S₁,S₂,σ₃}` are
  `[[1,3,3,6],[0,1,1,3],[0,0,0,1]]`; SNF gives invariant factors
  `(1,1,1)` → `M₃/⟨σ₁³,σ₁σ₂,σ₃⟩ ≅ Z`, free rank 1, no torsion; the
  membership triple: `Δ−2S₁` **in** the relation lattice, `Δ−S₁` and `S₁`
  **not** — so `H⁶(B) = Z·⟨[S₁]⟩` and `[Δ] = 2[S₁]`; and `gcd(2,3)=1`
  records the torsion death. This certifies the repaired Step-7 conclusion
  verbatim.

**Result: all 12 gates PASS** (G1–G10, G8a, and the new G3L), exit 0
(transcript `w31_derivation_check_output.txt`, JSON summary
`w31_derivation_check.json`). The machine tuple is still read only as
corroboration (G10). During development the strengthened run also
overwrote the wave-29 transcript once (the output paths were still
w29-named); the historical `w29_derivation_check_output.txt` was restored
byte-identical from the committed repo mirror, and the w31 outputs were
repointed to `w31_*` before the final run recorded here.

---

## 3. Build QA

* **tectonic** on `instruments-paper-revised11.tex`: exit 0, **no errors, no
  undefined references**, **51 pages** (v10 was 51; the +25 source lines
  flow within the existing pagination). Every box warning maps to a
  pre-existing v10 region: the full warning list was compared against a
  fresh v10 compile — including the two-pass pair
  (3.34pt pass-1 / 11.59pt pass-2) on the untouched flag-literature
  paragraph (v10 lines 2249–2282 = v11 lines 2275–2308), which is
  byte-identical in both versions.
* **check_v11.py** (the v10 checker + 30 v11-specific checks): **0
  failures**. The only 3 raw flags are now explicitly annotated in-checker
  as the W26-diagnosed pre-existing artifacts (`\[`=211/`\]`=208 INST,
  237/233 MAIN, the MAIN TikZ $ count 3073 — all byte-identical to the v10
  baseline; the v11 `$`-count delta +52 = exactly the 26 new math pairs,
  parity even). The v11 checks verify: all corrected statements present
  (the statement clause, the orbit-sum lattice, the rational module, the
  index values, the witness, the safe-degrees clause, the `H⁶(BK)` display,
  the orbit-sum relations, the index-two note, the Step-7 quotient,
  `Z·⟨S₁⟩`, the twice-a-generator conclusion, the torsion-death
  justification, the relation identities, both remark phrases), all
  superseded v10 statements **gone** (the old statement clause, the
  `H^*(BK)_{free}` display, the module-justification sentence, the old
  Step-3 and Step-7 displays, "the top class being the discriminant", the
  old residuals list), and every v10 integration check that must still hold
  (the proposition, its steps, the pinned transgression, the
  torsion-survival argument, the tuple, HatcherSS, the title/keywords, the
  provenance phrases, the discharged open problem (vi), the bibitem order,
  and `S₁` defined exactly once with `A₁`/`S₂` defined at first use).
* **PDF render verification** (pdftotext + whitespace-normalized matching):
  every new element renders — the corrected statement clause, the
  integral-lattice sentence, the rational module, the index values, the
  witness `S₁`, the `H⁶(BK) ≅ Z{A₁,S₁,S₂,σ₃} ⊕ Z/3·τ³` display, the
  relations, the Step-7 quotient `…/⟨σ₁³,σ₁σ₂,2τ³,σ₃⟩ ≅ Z·⟨S₁⟩`,
  `σ₁σ₂ = S₁+S₂+3σ₃` and `σ₁³ = A₁+3(S₁+S₂)+6σ₃`, `Δ = S₁−S₂ = 2S₁` twice
  a generator, "two is invertible modulo three", and both remark phrases;
  the old statements are absent from the rendered PDF.
* **Diff scope:** the v10→v11 diff touches exactly the five intended
  regions; net +25 lines.

---

## 4. Epistemic status after the wave

* The referee's verdict "accept with minor revision" is now, on the R1
  axis, **fully implemented**: the one mandatory correction is in the
  manuscript, and the gate-design gap that let it through is closed by a
  gate that would fail on any future re-introduction of the false module
  statement (it tests containment, index, witness, and generator — not
  ranks).
* `x² ≠ 0`; the tuple `(Z, 0, Z/3, Z/3, Z/3, Z/3, Z)`; `x` generating
  `H²`, `x²` generating `H⁴`; `H⁶(B;Z) ≅ Z` with `[Δ] = 2[S₁]` — all
  hand-derived (Wave 29), machine-certified (13C), independently
  re-implemented (Wave 28), referee-verified (Wave 30), and now
  lattice-fine-structure-gated (this wave). `thm:state-d2` and
  `δ₂(D(C³)) = 4/3` stand untouched.
* The rational framing `H^*(B;Q) = Q ⊕ Q·Δ̄` — the referee's "the right
  framing for the discriminant" — is retained verbatim in Step 7.
* **Open items on the R1 axis: none.** On the R2–R7 axis: the six one-line
  repairs remain recommended-but-not-applied (not in this wave's charge);
  the W23 stop, the ququart bracket `[4/3, 3/2]`, and the remaining merited
  queue (the author-side MathSciNet pass at submission time) are unchanged.

---

## 5. Artifacts of this wave

* `manuscript uploads v11/` — `instruments-paper-revised11.tex/.txt/.pdf`
  (the corrected paper; the main article is unchanged at v10).
* `scripts/w31_derivation_check.py` — the strengthened verifier (the
  wave-29 battery + G3L); `scripts/w31_derivation_check_output.txt` /
  `.json` — the transcript (12/12 gates PASS) and the machine-readable
  summary.
* `scripts/edit_v11.py` — the anchored v11 build (5 hunks, each asserted to
  match exactly once).
* `scripts/check_v11.py` — the v11 consistency checker (0 failures; the 3
  pre-existing artifacts annotated).
* This note, `glm/WAVE31_CORRECTION_V1.md`; `glm/README.md` updated (waves
  1–31, the current-manuscripts pointer: instruments v11 + main v10).
* All scripts/transcripts mirrored into `glm/`; the v11 PDF and this note
  copied to the session download folder. Committed and pushed with the
  session PAT (transient `GIT_ASKPASS` helper, trailing period stripped,
  never echoed, never committed; the helper deleted after use).
