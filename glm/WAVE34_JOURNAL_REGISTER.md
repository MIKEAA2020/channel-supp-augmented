# WAVE 34 — THE JOURNAL-REGISTER PASS: F1/F2 folded, the change-log and diary language stripped from both manuscripts

**Date:** 2026-09-13
**Charge (user directive, four parts):** (1) fold the two W33 polish
findings F1/F2 into the instruments paper; (2) scan BOTH manuscripts for
remnants and redundancy; (3) make both read as journal articles — no
change-log, no diary, no version references, no editorial or self-praise
statements, no informal chat terms, no phantom or strawman points; claims,
methods, evidence, proofs, insights and implications only; (4) proofs
presented in full, not condensed, with the literature-repetition exception
handled by citation.

**Deliverables.** `manuscript uploads v13/` containing
`instruments-paper-revised13.tex/.txt/.pdf` (v12 → v13) and
`main-article-revised11.tex/.txt/.pdf` (v10 → v11): one wave folder, both
current manuscripts. The previous versions remain in their folders
(`v12/`, `v11/`, `v10/`, ...).

---

## 1. Part 1 — F1 and F2 folded (the two W33 optional polish items)

* **F1 (Step 1 of prop:cupsquare, the even-r clause).** The lead-in "the
  fibre classes there are *boundaries* before the $E_8$-page" conflated two
  death modes (the $\sigma_1$-multiple degree-8 classes are $d_2$-boundaries,
  but the degree-9 free classes and the residual degree-8 classes die as
  non-cycles); it now reads "**killed** before the $E_8$-page" — the
  elaborating sentences were already precise, so only the lead-in word was
  loose. The forward dependency is now marked exactly as W33 proposed: the
  clause carries the parenthetical "(the classes $\sigma_1$, $\sigma_2$,
  $\tau$ and the transgression values invoked here are established in
  Steps 2–4 below)" — matching the odd-r clause's existing "by Step 3
  below" marker. ($\sigma_i$ is introduced in Step 2, $\tau$ at Step 2's
  end, and the transgression values are pinned in Step 4: the range 2–4 is
  the accurate one.)
* **F2 (Step 7).** The half-clause is in: after "the torsion class
  $\tau^3$ dies because $2\tau^3=0$ forces it (two is invertible modulo
  three)" the text now reads "--- taking with it the $\tau^3$-tail
  ambiguity of the orbit-sum lifts (Step 3), so that the quotient and the
  discriminant's position in it are lift-independent ---". This states
  exactly what W33 verified as gate M4 and identifies as the well-definedness
  of the statement's "discriminant class" clause; the claim is now gated
  directly (below, M-layer).

Both folds are one-clause insertions on untouched mathematics; the
proposition's statement, all seven steps' formulas, displays and
computations are byte-identical to v12 except at the two insertion points
(verified by 19 must-hold anchors).

## 2. Part 2 — the remnant and redundancy scan (both manuscripts, full text)

Method: full reads of both sources (instruments 2,915 lines, main 3,758)
plus systematic pattern sweeps (version references, wave/change-log
markers, referee/audit vocabulary, model names, informal and editorial
registers, chat-history terms, phantom-source references, duplicate
sentences, repeated word-runs).

**Remnants found and removed (instruments, 21 sites):**

1. Abstract: "computed by an exact-integer equivariant battery and
   reproduced by an independent re-implementation" → "resting on the
   integral cohomology of the cyclic flag quotient" (implementation
   workflow out of the abstract).
2. Introduction: "through a hand derivation ... cross-checked by an
   exact-integer equivariant battery and an independent re-implementation"
   → "through a Chern-transgression derivation ... cross-checked by an
   independent exact-integer machine computation".
3. §5 survey: "(an elementary median matching bound at $r=1$, **upgraded
   from the earlier five-outcome counterexample** to the coordinate flags"
   — a phantom reference to superseded-version content; the five-outcome
   counterexample appears nowhere in the paper. Now: "on the coordinate
   flags $(j,k)$, with the constant $2(q-1)/q$".
4. Same paragraph: "proved through the cohomology of the flag quotient ---
   **hand-derived, machine-certified, and independently re-implemented**;
   Lemma ... Proposition" → the triple qualification deleted (the citation
   chain already says everything a reader needs).
5. cor:flat-fails: "and **the corrected statement** is
   Conjecture~\ref{con:coord-flat}" → "the expected complete statement
   being Conjecture ..." (version history out; the mathematical fact —
   blanket flatness refuted at every output dimension — stays).
6. Source comment "% ---- Wave 7 block: ..." → "% ---- Equal-value
   orthonormal bases ..." (internal wave label out of the source).
7. Proposition 6.16's title: "[The cup square on the flag quotient: **a
   hand derivation**]" → "[The cup square on the flag quotient]" (the mode
   of derivation is self-description, not content; the proof is a full
   proof and needs no subtitle).
8. Lemma 6.17's proof: "The decision between the two worlds is **now
   supplied by hand**. Proposition ... independent of the Cartan–Leray page
   **in front of us**" → "is supplied by Proposition 6.16, which proves
   $x^2\ne0$ by an integral transgression computation independent of the
   present Cartan–Leray page".
9. Lemma 6.17's proof end: "The machine computation ... independently
   **certifies**" → "The independent machine computation ... confirms".
10. **Remark 6.18 (rem:machine-certificate) — the epicentre — rewritten in
    full, formal register.** Title: "The machine certificate behind
    Lemma 6.17" → "The computational verification of Lemma 6.17".
    "is derived by hand" → "The proof ... is analytic". "The certification
    battery" → "The certification consists of exact integer arithmetic".
    "was re-derived independently and stress-tested" → "was checked
    against two externally known model cases". "**Residuals, stated
    plainly. On the hand side ... On the machine side, the cellulation
    began as one implementation and has since been independently
    re-implemented from the design specification with fresh algorithms at
    every layer (...)**" → "Three qualifications remain. First ... Second,
    the cellulation was implemented twice independently, the second
    implementation following the design specification with different
    algorithms at every layer (...) ... Third ...". "**the earlier
    audit**" (phantom: the internal audits are unpublished) → the passage
    now cites the two model cases once, in the validation paragraph (the
    double listing was also a redundancy). "The code, the battery, and the
    full machine transcripts ... in the public companion repository" →
    "The code and the full transcripts of both computations are available
    in the public repository" (footnote URL unchanged; the repository is
    public and legitimately citable). The closing summary "the hand
    derivation is the one **a reader can check line by line**" dropped.
    **Nothing mathematical was removed**: the cellulation (14,910 cells),
    every certification check, the four external anchors, both model
    cases, the double implementation with its algorithm list, the
    convention-forcing, the lineage-vs-diffeomorphism caveat, the
    $p\le31$ prime-scan caveat, and the code-availability footnote all
    remain.
11. Remark 6.19 (flag-literature): "The **hand derivation** of Proposition
    6.16 is the integral lift ..." → "The derivation ...". Literature
    contrast (Guerra–Jana, Weber–Wojciechowski, Korbaš–Lőrinc,
    Matszangosz, Singh, Crabb) untouched — published-literature
    positioning is exactly what a journal article should do.
12. Same remark: "The machine certificate of Remark ..., **now doubly
    implemented**, remains complementary" → "The computational
    verification of Remark ... remains complementary".
13. rem:flat-status: "improving the two-sector pinching threshold
    $nQ_2(2)-1=2n-1$ **and the earlier trace-mass threshold $r=n$**" — a
    phantom (trace-mass appears nowhere else in either paper); dropped.
14. Same remark: "the two one-outcome cases **left bracketed in the
    previous version are closed in the negative direction**" → "the
    one-outcome state spaces are non-flat, the qutrit having $\delta_1=4/3$
    exactly and the ququart in $[4/3, 3/2]$" (same facts, zero version
    reference).
15. "at $r=2$ this requirement **now fails certifiably**" → "fails".
16. "Conjecture 6.26, **in its corrected form**, states ..." →
    "Conjecture 6.26 states ...".
17. **The conjecture-history diary passage removed**: "the conjecture has
    been corrected twice, each time by a state-space result. The first
    form, without the clause $r\ge2$, predicted ... The second form, with
    the clause $r\ge2$, predicted ... **which is why the clause now reads
    $r\ge3$**." — a narrative of two superseded earlier forms of the
    paper's own conjecture (unpublished-version references, precisely the
    forbidden species). The surviving mathematical content was already
    stated in the retained sentence ("fails at $r\in\{1,2\}$ for every
    $d_B\ge3$"), so the paragraph now runs "... together with
    Theorem 6.15). The content of the conjecture is therefore the flat
    direction at $d_B\ge3$ with $r\ge3$: that ...".
18. Conclusion survey: the same triple qualification as (4) deleted.
19. "the **corrected** coordinate Conjecture" → "the coordinate
    Conjecture" (conclusion, two sites: survey + open problem (v)).
20. Open problems: "of which the smallest, $\delta_2$ of the qutrit, is
    **now** exactly $4/3$" → "is exactly $4/3$".
21. **Open problem (vi) — a pure change-log entry — replaced**: "(vi)
    **[closed in this version]** the hand derivation of the cohomology of
    the flag quotient $B$ **posed as an open problem in earlier versions
    is supplied by** Proposition 6.16, whose transgression computation
    **removes the last computational premise** of Theorem 6.15; the
    machine certificate ... is **retained** as an independent
    cross-check, and the remaining research direction ..." → "(vi)
    determine the unstable integral cohomology of the symmetric-group
    quotients themselves, where the field-coefficient algorithms of
    Ref. [Guerra–Jana] leave the torsion layers open — the transgression
    computation of Proposition 6.16 settles the integral cohomology of
    the cyclic intermediate quotient $B$, with the computational
    verification of Remark 6.18 as an independent cross-check, but
    neither addresses the symmetric-group quotients". A solved problem is
    presented as a contribution, not narrated as a closed diary entry;
    the genuinely open direction remains on the list.

**Remnants found and removed (main, 2 sites):**

1. Abstract: "... the qutrit sitting exactly at $4/3$ there, through a
   flag-quotient computation **that is hand-derived, machine-certified,
   and independently re-implemented**" → "... through a flag-quotient
   cohomology computation."
2. Open problem 1: "the companion's plane-valued extension of the
   equal-value-basis theorem, **whose homological premise is hand-derived,
   machine-certified, and independently re-implemented**, likewise
   bounds ..." → the qualification deleted ("... extension ... likewise
   bounds ..."); the follow-on "the cyclic flag quotient underlying
   **that premise**" re-anchored to "that extension" (its antecedent was
   the deleted clause).

**Redundancy findings.** The duplicate-sentence and repeated-word-run
scans: the main article is clean (no duplicated sentences ≥ 80 chars, no
repeated 8-word runs ≥ 4×). The instruments paper's only duplicated
sentence pair is the parallel statement clauses of
thm:equal-basis / thm:equal-basis-plane (two different theorems with
intentionally parallel statements — correct as is). The one genuine
redundancy was inside the old Remark 6.18: the model cases
$L(3;1,1,1)$ and $\mathbb{RP}^2\times S^2$ were listed twice (validation
paragraph + "earlier audit" passage); the rewrite keeps them once.

**Phantom/strawman audit.** No strawman debunking survives: the refuted
positions in the text are either published literature (Guerra–Jana field-
coefficient algorithms do leave the torsion layers open) or the naive
blanket-flatness reading of the paper's own proved dichotomies, which is
the mathematically necessary context for the conjecture's $r\ge3$ clause.
All references to unpublished prior versions, internal audits, and
superseded conjecture forms are gone (verified by 34 absence patterns on
both papers + 21 forbidden phrases + 23 PDF-render absences).

## 3. Part 4 — the proof-presentation audit

All 124 proof environments across the two papers (56 instruments, 68
main) were audited for length and completeness. **No proof is condensed.
No proof is omitted.** The short proofs (≤ 8 lines) are immediate
reductions to results proved earlier in the same paper ("Combine
Theorem X with Corollary Y") — complete proofs of corollary-type
statements. The two "included/reproduced here for completeness" proofs
(the convex-projection estimate, the pinching-norm lemma) are given in
full, adapted to the present setting, with the companion-paper source
cited — the citation-plus-full-adapted-proof pattern, which satisfies the
literature-repetition exception in both directions. The seven-step proof
of prop:cupsquare, the Cartan–Leray proof of Lemma 6.17, the two
equal-value-basis proofs, and the state-space width proofs are all
presented in full (unchanged by this wave apart from the two F1/F2
clauses).

## 4. Verification (three independent layers)

* **`check_v13.py` (written for this wave): 157 checks, all PASS, exit 0.**
  P-layer: 32 new-phrase presences (each edit applied exactly once), 2
  main-article presences, 19 must-hold anchors (the statements and every
  load-bearing display of prop:cupsquare / lem:flag-cohomology /
  thm:state-d2 byte-identical to v12), 68 absence checks (34 phrases ×
  both papers), `.txt == .tex` for both manuscripts, the main-article
  sync clauses present with no proof internals leaked, informal-register
  sweep clean. M-layer (sympy, exact): the Step-7 quotient re-computed by
  Smith normal form (diagonal $(1,1,1,1)$ → $\mathbb Z$, no torsion;
  $[A_1]=0$, $[S_2]=-[S_1]$, $[\sigma_1^3]=[\sigma_1\sigma_2]=[\sigma_3]=
  0$); **the F2 gate — the new clause's claim verified directly:**
  $[\Delta+c\,\tau^3]=2[S_1]$ for $c=0,1,2,5$ and $[S_1+a\,\tau^3]=[S_1]$
  for $a=1,2$ (the $\tau^3$-tail dies in the quotient, $2$ invertible mod
  $3$), with $2[S_1]\ne0$ and $[\Delta]\ne0$; the Step-2 lattice-index
  table $[L:M]=1,1,1,2,2,4,8$ re-computed for degrees $0$–$6$; the
  degree-3 witness ($S_1$ not in the symmetric module, $2S_1$ in it) and
  the identity $2S_1=\sigma_1\sigma_2-3\sigma_3+\Delta$; the Step-7
  coordinate identities $(0,1,1,3)$, $(1,3,3,6)$, $(0,1,-1,0)$ in the
  paper's basis order.
  *Honest debug trail (my own checker, fixed before any conclusion):* a
  sign error in the F2 membership vector (the $\Delta+c\tau^3-2S_1$
  coordinate was $(0,-1,-1,0,c)$, not $(0,-1,1,0,c)$); a monomial
  generator that did not enforce $a+b+c=d$ (poisoning the index table
  with lower-degree monomials); a row/column orientation mix-up in the
  module-membership solve; an R7 anchor with the wrong line break; and
  the orbit-basis enumeration order ($S_2$ enumerated before $S_1$) —
  each fixed in place, battery re-run to all-PASS.
* **Tectonic: both papers compile with exit 0.** Instruments v13: 51
  pages (v12: 51). Main v11: 46 pages (v10: 46). The number-free warning
  multisets are **byte-identical to the baselines** for both papers (all
  pre-existing regions: the flag-literature overfull pair, the
  bibliography underfulls) — no new typesetting defects from 21+2 edits
  and the remark rewrite.
* **PDF render QA (pdftotext with ligature/whitespace/dash
  normalisation):** 23 new-phrase render presences + 21 superseded-phrase
  render absences on the instruments PDF; 3 presences + 4 absences on the
  main PDF. All pass. (En-route artifacts, all diagnosed as pdftotext
  extraction quirks rather than manuscript defects: the $\ne$ glyph
  extracting as `6=`, an en-dash vs hyphen encoding difference, and a
  line-break hyphenation.)
* **The Wave-31 derivation battery re-run: ALL 12 GATES PASS, exit 0** —
  the mathematics layer is untouched by the register pass (as it must
  be: the wave edits only language, plus two one-clause markings whose
  mathematical content W33 had already verified).

## 5. What deliberately did NOT change

* The mathematics: every theorem, lemma, proposition, corollary,
  conjecture statement, proof, display, and constant in both papers is
  unchanged (19 must-hold anchors + the W31 battery + the check_v13
  M-layer). The verdict chain — $x^2\ne0$; the tuple $(\mathbb Z,0,
  \mathbb Z/3,\mathbb Z/3,\mathbb Z/3,\mathbb Z/3,\mathbb Z)$; $H^6(B;
  \mathbb Z)\cong\mathbb Z$ with the discriminant twice a generator;
  $\delta_2(\mathcal D(\mathbb C^3))=4/3$; the ququart bracket
  $[4/3,3/2]$ open; the W23 stop — is untouched.
* The literature positioning (Remark 6.19 and the main article's
  flag-quotient passages): contrasting published work is legitimate
  journal content; only the verification-workflow vocabulary around it
  was formalised.
* The code-availability footnote (the repository is public).
* Double-blind conventions, keywords, section structure, labels (all
  internal labels — `prop:cupsquare`, `rem:machine-certificate`, ...
  — unchanged, so all cross-references resolve).

## 6. Artifacts

* `manuscript uploads v13/` — `instruments-paper-revised13.tex/.txt/.pdf`
  and `main-article-revised11.tex/.txt/.pdf`.
* `glm/edit_v13.py` — the anchored edit script (23 replacements + the
  remark block rewrite, each asserted to match exactly once; the
  forbidden-phrase scan built in).
* `glm/check_v13.py` + `glm/check_v13_output.txt` — the wave checker and
  its transcript (157/157 PASS).
* This note; the compiled PDFs also copied to the session download
  folder.
* Committed and pushed with the session PAT (the token handled via a
  transient `GIT_ASKPASS` helper, never echoed, never committed, the
  helper deleted after use).
