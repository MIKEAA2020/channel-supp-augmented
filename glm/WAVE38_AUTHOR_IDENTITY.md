# Wave 38 — The author identity filled in + brief declarations (2026-09-14)

**The user directive:** the author identity supplied — Amin Abaee,
Independent Researcher, ORCID 0000-0002-0019-1842,
amin_abaee@ut.ac.ir — and "for declarations, keep it brief."

**Scope:** both papers, as the continuation of the unblind-labelled
line: instruments v16 -> **v17**
(`instruments-paper-unblinded17.tex/.txt/.pdf`) and main v13 ->
**v14** (`main-article-unblinded14.tex/.txt/.pdf`), both in
`manuscript uploads v17/`. No content change of any kind: prose,
mathematics, figures, captions, labels, and the section structure
outside the three authorial sites are byte-identical to v16/v13 (the
reconstruction gate below proves this). The no-new-claims gate holds
trivially — the additions are authorial front matter only (identity,
declarations, companion-citation authors); the single added
`\ref{rem:machine-certificate}` points at the remark that already
carries the public-repository footnote, restating it without new
factual content.

## What wave 37 left open, and what this wave fills

Wave 37 restored the author's own xx-placeholder template as the
fill-in convention: the xx fields (title block + companion citations)
were the author's fill-in points for the single-blind venues
recommended by the wave-36 venue study. This wave fills them with the
supplied identity and adds the standard declarations section at the
exact site where the double-blind manuscripts carried their
withheld-marker acknowledgements section (between the conclusion and
the appendix — the canonical journal position), per the directive's
brevity instruction.

## The edit (edit_v17.py: 3 anchored hunks per paper, 13 changed diff lines each)

| Hunk | Instruments (v16 -> v17) | Main (v13 -> v14) |
|---|---|---|
| 1 | the author block filled in: `Amin Abaee` / `Independent Researcher` / `ORCID: 0000-0002-0019-1842` / `Email: amin_abaee@ut.ac.ir` (same 4-line structure, same `\small` convention, same `\href{mailto:...}{...}` form; the `\date{September 14, 2026}` untouched) | same |
| 2 | `\section*{Declarations}` inserted between the conclusion and the appendix: "The author declares no funding and no competing interests. The code and computation transcripts of Remark~\ref{rem:machine-certificate} are available at the repository cited there." | `\section*{Declarations}` after the open-problems list, before the appendix: "The author declares no funding and no competing interests. No datasets were generated or analysed." |
| 3 | companion citation `xx~xx` -> `A.~Abaee` (`CompanionChannels`, the house bib style: initial + tilde + surname, as in J.~Matou\v{s}ek / A.~Barvinok) | companion citation `xx~xx` -> `A.~Abaee` (`CompanionInstruments`, line-broken bibitem) |

**Declarations wording, kept brief per the directive:** two sentences
per paper — funding none, competing interests none, and one data
availability sentence. The instruments sentence points at
`rem:machine-certificate`, whose footnote already gives the public
repository URL (`https://github.com/MIKEAA2020/channel-supp-augmented`)
— a restatement, not a new claim. The main article is purely
theoretical and carries no data statement beyond the standard "no
datasets" sentence. No acknowledgements section is added (the original
manuscript carried none; wave 37 removed the review-marker section
outright).

The `.txt` companions are byte-identical mirrors of the `.tex` files
(the house convention since v15).

## QA (the full battery)

- **check_v17.py: 42/42 PASS, exit 0.** P-layer: the blind-marker
  sweep (source), the placeholder sweep (no `xx` fields remain —
  `xx xx` / `xx~xx` / `ORCID: xx` / `\small xx` / `xx_xx` all absent),
  the identity presences (the exact filled-in author block,
  byte-exact; the unchanged version date), the declarations
  presences (the exact inserted sentences, byte-exact), the
  **reconstruction gate** (the new files equal the v16/v13 sources
  with exactly the three wave-38 replacements applied — re-derived
  independently inside the checker, byte-verified), the `.txt ==
  .tex` byte mirrors, and the no-collateral-damage ledgers: label
  multiset; ref/cite multiset (instruments gains exactly the one
  expected `\ref{rem:machine-certificate}`, main unchanged);
  captions (brace-matched extraction, byte-identical); the section
  ledger (exactly the one `\section*{Declarations}` added per paper,
  all other section lines byte-identical); the bibitem ledger (keys
  unchanged; all bodies byte-identical except the single companion
  entry per paper, de-anonymized to `A.~Abaee`); math-delimiter
  parity (`$` count unchanged — no mathematics touched).
- **Honest debug trail: three checker-needle bugs fixed in place** —
  the ref/cite and section-ledger checks compared ordered lists where
  the design calls for multisets/order-insensitive comparison (the
  added ref and section sit in their document positions, not at the
  list ends); fixed by multiset comparison and by comparing the
  section list with the Declarations entry filtered out. (The
  reconstruction gate had already proven the bytes correct; these
  were checker-expression bugs, the documented wave-36/37 quirk
  class.)
- **Tectonic: exit 0 on both; page counts 53/46, unchanged** (the
  declarations sections fit without page growth).
- **The number-free warning signature sets are IDENTICAL to the fresh
  v16/v13 baselines** (w38_warn_cmp.py, the wave-37 method): main 54
  vs 54 warning lines 1:1; instruments 26 vs 40 lines — the
  difference is purely the TeX pass count (the fresh baseline
  compile's extra `.aux` rerun passes: 2 passes new vs 3 baseline),
  per-pass multiset consistent (ratios 0.64–0.67 ≈ 2/3), every
  warning region pre-existing — **zero new typesetting defects**.
- **The W31 derivation battery re-run: ALL GATES PASS** (the
  mathematics untouched).
- **VLM visual verification, four pages:** both page-1 title blocks
  (the name, affiliation, ORCID, email, and date present, centered,
  cleanly rendered; no overlap with each other or the abstract; no
  cut-off or misalignment) and both declarations pages (instruments
  p. 47, main p. 39 — heading and paragraph rendered cleanly and
  fully; no disruption of the surrounding layout, no orphaned
  headings).

## The mathematics and the verdict chain

Untouched and unchanged: x^2 != 0; the additive tuple; H^6(B;Z) = Z
with the discriminant twice a generator; delta_2(D(C^3)) = 4/3;
ququart [4/3, 3/2] OPEN; the W23 stop stands.

## For the author, at submission time

The v17/v14 unblinded versions are the submission-ready forms for the
single-anonymized venues recommended by the wave-36 venue study
(Annals of Physics, LMP, J. Phys. A class): identity filled in,
brief declarations in place, companion citations attributed. If a
venue's declaration form differs (e.g. a separate conflict-of-interest
form or a data-availability field in the submission system), the two
sentences here transfer directly. The blinded v15/v12 and the
placeholder unblinded v16/v13 remain in their folders for the audit
trail. Standing recommendations unchanged: the author-side MathSciNet
pass at submission time; PAT rotation after the session.
