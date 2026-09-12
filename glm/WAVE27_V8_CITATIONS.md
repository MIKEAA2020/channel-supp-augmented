# WAVE 27 — THE v8 CITATION-INTEGRATION PASS
### Executed per the user directive of 2026-09-13: "1- v8 citation-integration
### edit 2- independent re-implementation and machine-free derivation of
### H^{3,4}(B) only if genuinely merited and useful to science 3- which
### MathSciNet articles can't u access? give dois"
### This is merited-queue item 1 of the W26 verdict (the only blocking item
### for submission), plus the two adjudications the user asked for.

**Artifacts:** `../manuscript uploads v8/` (both papers, .txt sources +
tectonic-compiled PDFs, 48 and 46 pages, no errors); the generation script
`scripts/edit_v8.py` (6 anchored replacements, each asserted to match exactly
once); the fixed checker `scripts/check_v8.py`; the citation-evidence logs
`glm/novelty_pass/v8_*` (Crossref + zbMATH Open + arXiv + DOI-resolution
probes, all live on 2026-09-13); this note.

**Bottom line.** The W26 near-collision line is now cited and differentiated
in both papers (v8): the instruments paper gains the positioning remark
`rem:flag-literature` (Guerra–Jana, Guerra–Jana–Maiti, Weber–Wojciechowski,
Korbaš–Lörinc, Matszangosz, and the Z_p-BU pair Singh/Crabb), an intro
cross-reference, the open-problem (vi) candidate-route clause, and seven new
bibitems; the main article gains the sync-clause differentiation and the two
Guerra–Jana bibitems. Every new bibliographic field was live-verified from
Crossref/zbMATH/arXiv before insertion — nothing cited from memory. **One
W26 finding is retracted as a checker artifact** (the "uncited
NechitaEtAl2018": the citation exists, in the optional-argument form
`\cite[Corollary~2]{...}` that the v7 checker's regex could not match; the
regex is fixed in `check_v8.py` and no manuscript change was needed). **One
W26 attribution is corrected**: the cup-length paper has two authors (Korbaš
and Lörinc). The submission-blocking citation gap is closed.

---

## 1. The edits (six anchored hunks, v7 → v8)

| paper | hunk | content |
|---|---|---|
| instruments | intro (¶ after the contributions paragraph) | one sentence: the flag-quotient premise sits next to the unordered-flag/Auerbach/Z_p-BU literature, `Remark~\ref{rem:flag-literature}` records the differentiation |
| instruments | between `rem:machine-certificate` and `thm:equal-basis-plane` | **`rem:flag-literature`** (the positioning paragraph): the Guerra–Jana TAMS result (Σ_n quotients of Fl_n(C), Fl_n(R); homological stability; stable rings in closed form; an algorithmic procedure for the unstable additive cohomology); Guerra–Jana–Maiti (mod-2 cohomology of the low-dimensional real unordered flag manifolds; improved Auerbach-basis counts); the school (Weber–Wojciechowski's LS-category estimate, Korbaš–Lörinc's cup-length, Matszangosz's integer-cohomology algorithm); the Z_p-BU backdrop (Singh's simple proof, Crabb's connective-K-theory version); **the differentiation**: symmetric-group vs cyclic intermediate quotient, field vs integral coefficients with the 3-torsion exponents pinned, Auerbach counting vs the equal-value/width chain; and the two closing notes (their algorithmic procedure is a candidate route for open problem (vi); the machine certificate is complementary — the integral 3-torsion layer is precisely what field-coefficient algorithms do not touch) |
| instruments | open problem (vi) | the candidate-route clause (cite Guerra–Jana, cross-ref the remark) |
| instruments | bibliography | 7 new bibitems |
| main | open problem (1) sync clause | the differentiation clause: the cyclic flag quotient sits between the complete flag manifold and the symmetric-group unordered quotients of `Refs.~\cite{GuerraJana2025,GuerraJanaMaiti2025}` |
| main | bibliography | the 2 Guerra–Jana bibitems |

**Build QA.** `tectonic` on both v8 sources: **no errors** (48 pages
instruments / 46 main); all over/underfull box warnings map to pre-existing
v7 regions (line-shifted; none inside any inserted hunk). `check_v8.py`:
labels/refs/cites/environments/delimiters all PASS, all 24 v8
citation-integration checks PASS; the only three raw flags are the
W26-diagnosed checker artifacts (the `\\[4pt]` line-skip tokens 200/197 and
237/233, the TikZ `\$`-node count 3071 — same counts as v7, i.e. nothing
new). PDF text verified: the remark heading, every new bibitem, the
sync-clause differentiation, and the intact `\cite[Corollary~2]` Nechita
citation all render (the one extraction false alarm was the PDF "fl"
ligature). The v7→v8 diff is exactly the six hunks above.

## 2. Two honest corrections to the W26 record

1. **The NechitaEtAl2018 finding is RETRACTED.** v7 line 725 reads
   `~\cite[Corollary~2]{NechitaEtAl2018}` — the citation exists; the v7
   checker's regex `\\cite\{...\}` cannot match the optional-argument form
   `\cite[...]{...}`, so "bibitem never cited" was a checker artifact, not a
   manuscript flaw. Correction applied to the tool, not the paper:
   `check_v8.py` uses `\\cite(?:\[[^\]]*\])?\{...\}` and now reports zero
   uncited bibitems in either paper. (The W26 verdict's other option — "drop
   or cite" — is moot: the entry was cited all along.)
2. **The Korbaš attribution is corrected.** The 2003 cup-length paper is by
   **Korbaš and Lörinc** (Fundam. Math. 178, 143–158; Crossref
   `10.4064/fm178-2-4` and zbMATH agree). W26's prose said "Korbaš 2003"; the
   v8 bibitem carries both authors.

Nothing else in the W26 record changed: the null-collision verdicts, the
near-collision identification, and the flaw-audit PASSes all stand.

## 3. The citation data (every field live-verified 2026-09-13)

| key | reference | verified via |
|---|---|---|
| `GuerraJana2025` | L. Guerra, S. Jana, *Cohomology of complete unordered flag manifolds*, Trans. Amer. Math. Soc. **378** (2025), 3507–3550. DOI 10.1090/tran/9358 | Crossref + zbMATH (`zbm_v8_guerra_tams2.json`) + DOI resolves to the AMS article page |
| `GuerraJanaMaiti2025` | L. Guerra, S. Jana, A. Maiti, *The mod-2 cohomology groups of low-dimensional unordered flag manifolds and Auerbach bases*, Topology Appl. **365** (2025), 109279. DOI 10.1016/j.topol.2025.109279 | zbMATH (W26 record `zbm_unflag.json`) + Crossref + arXiv abs page (3 authors: Guerra, Jana, **Maiti**) |
| `WeberWojciechowski2017` | A. Weber, M. Wojciechowski, *On the Pełczyński conjecture on Auerbach bases*, Commun. Contemp. Math. **19** (2017), 1750016. DOI 10.1142/s021919971750016x | Crossref + the zbMATH review of `GuerraJanaMaiti2025` (which cites it verbatim) |
| `KorbasLorinc2003` | J. Korbaš, J. Lörinc, *The Z₂-cohomology cup-length of real flag manifolds*, Fundam. Math. **178** (2003), 143–158. DOI 10.4064/fm178-2-4 | Crossref + zbMATH |
| `Matszangosz2021` | Á. K. Matszangosz, *On the cohomology rings of real flag manifolds: Schubert cycles*, Math. Ann. **381** (2021), 1537–1588. DOI 10.1007/s00208-021-02237-z | Crossref + zbMATH + arXiv + Springer landing title (the registered title ends at "Schubert cycles" in all four sources) |
| `Singh2010` | M. Singh, *A simple proof of the Borsuk–Ulam theorem for Z_p-actions*, Topology Proc. **36** (2010), 249–253 | arXiv abs page (journal_ref deposited) |
| `Crabb2022` | M. C. Crabb, *A Borsuk–Ulam theorem for cyclic p-groups*, arXiv:2211.08087 (2022) | arXiv abs page; no published version in Crossref |

The arXiv export API was again rate-limited (429, as in W26 — recorded in
`v8_probe_results.json`); the website abs pages (a different endpoint)
supplied the records. All claims inside `rem:flag-literature` (homological
stability, the algorithmic procedure, the Auerbach application, the
LS-category estimate, the cup-length and integer-cohomology algorithms, the
connective-K-theory version) are drawn from the saved W26 search evidence
and the abstract pages — none from memory.

## 4. Task 2 — the merit verdict on the re-implementation / machine-free derivation

**Merited: yes — with a precise ranking and an honest scope.**

* **The machine-free derivation is the high-merit item in principle.** It
  would remove the last machine premise of `thm:state-d2`, converting the
  flagship theorem into a fully hand-checkable one — exactly the
  "theorem vs homology computation" distinction the bridge audit was built
  to police. It is the paper's own open problem (vi), now with the
  candidate route named in the paper itself. By the project's P5 pattern
  (W24: d₃ = 0 ⟺ x² ≠ 0, machine-anchored on the lens and ℝP²×S² model
  cases), the derivation reduces to a hand proof that the cup square x²
  survives on the cyclic quotient — and that integral 3-torsion layer is
  precisely what the Guerra–Jana field-coefficient programme does not
  cover. This is new research-grade work with a real risk of not
  converging: it is an integral lift of an unstable additive algorithm to a
  quotient that line does not treat, not a routine adaptation.
* **The independent re-implementation is the merited, bounded item.** A
  second implementation of the 13C-7 chain from
  `WAVE13_CELLULATION_DESIGN_SPEC.md` (fresh code, same spec, full battery +
  tuple comparison) closes honest residual (i) of the bridge audit ("one
  implementation, not independently re-implemented"). It catches
  implementation bugs; it does not catch spec bugs and does not change the
  premise's epistemic class (two agreeing implementations are stronger
  evidence, not a hand proof).
* **Not merited:** Lean-level formalisation of the premise (disproportionate:
  the premise already carries four independent classical anchors), and —
  per the W23 stop certificate, unchanged — any new wave campaign on the
  n=4 complex or δ₂(ququart)/δ₃(qutrit) attacks.

**Execution this session: none, deliberately.** The v8 pass was the only
*blocking* item and took the session. A re-implementation rushed into the
session tail would share time-pressure failure modes with the original — the
opposite of independence — and the no-fabrication gate forbids presenting a
partial one as a certificate. The recommended next dedicated session: (1)
re-implement the cellulation + boundary + orbit-SNF chain from the spec,
(2) compare the full battery and the tuple (Z, Z/3, Z/3, Z/3, Z/3, 0, Z),
(3) then, if budget remains, the bounded Guerra–Jana-route derivation
attempt. The v8 remark now points the paper's readers at exactly this route.

## 5. Task 3 — the MathSciNet access report (live-probed 2026-09-13)

**MathSciNet is account-gated, not article-gated: without institutional
credentials, every review page is equally unreachable — so "which articles
can't you access" = all of them, and it is not about the articles.** Live
probes (logs in `v8_probe_results.json`):

* `mathscinet.ams.org/mathscinet/search/publications.html?...` → HTTP 302 →
  **`connect.liblynx.com/wayf/...` "Where Are You From"** — the LibLynx
  institutional-login gateway (page markers: log in / login / credentials /
  institutional access). No search results are served without an
  institution.
* `mathscinet.ams.org/mrlookup` → loads (the free MR Lookup bibliographic
  tool) — the free lookup shell is open; the review database is not.
* MR reviews carry MR numbers, not DOIs, so there is no "MathSciNet DOI
  list" to hand over in the first place; DOIs belong to the underlying
  publisher versions.
* The **open substitutes worked for everything this project needed**:
  zbMATH Open API (fully open — all queries 200; only its *web UI*
  Cloudflare-blocks this client, a bot filter, not a paywall), Crossref
  (fully open), arXiv (fully open).
* The near-collision line's underlying papers, with DOIs and the open route
  for each (this is the genuine answer to "give dois"):

| DOI | article | open route |
|---|---|---|
| 10.1090/tran/9358 | Guerra–Jana, Trans. AMS 378 (2025) 3507–3550 | arXiv:2309.00429 (AMS landing page loads; full text publisher-side) |
| 10.1016/j.topol.2025.109279 | Guerra–Jana–Maiti, Topology Appl. 365 (2025) 109279 | arXiv:2304.12990 (zbMATH marks "has open version") |
| 10.1142/s021919971750016x | Weber–Wojciechowski, Commun. Contemp. Math. 19 (2017) 1750016 | author preprint (duch.mimuw.edu.pl, found in W26) |
| 10.4064/fm178-2-4 | Korbaš–Lörinc, Fundam. Math. 178 (2003) 143–158 | EUDML (open; found in W26) |
| 10.1007/s00208-021-02237-z | Matszangosz, Math. Ann. 381 (2021) 1537–1588 | arXiv:1910.11149 |
| — | Singh, Topology Proc. 36 (2010) 249–253 | Topology Proceedings reprint PDF (open) |
| — | Crabb, arXiv:2211.08087 | arXiv (open) |

**Net: nothing in the v8-relevant literature is actually inaccessible from
this environment.** The only unreachable layer is MathSciNet's own review
text, which duplicates zbMATH Open's coverage; the author-side institutional
pass (W26 item 3, ~1 hour) remains the final check before submission.

## 6. The scoreboard

* **The submission-blocking item is closed**: both v8 papers now cite and
  differentiate the Guerra–Jana line and the surrounding school; the
  merited queue is empty except the optional premise-hardening of §4.
* Qutrit verdict unchanged and now fully positioned for submission: H₂(B₃) =
  ℤ/3, δ₂(D(ℂ³)) = 4/3; δ₁(ququart) OPEN, bracket [4/3, 3/2] intact.
* The W26 record is corrected in two places (one finding retracted as a
  checker artifact, one attribution fixed) — both corrections evidence-led,
  nothing fabricated in either direction.
* Commit: this round is committed in the nested repo; the push awaits a
  live PAT (not re-supplied this turn; the Task-23/26/30 precedent — commit
  local, ready to push).
