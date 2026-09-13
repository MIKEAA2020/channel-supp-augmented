# Wave 37 — The unblinded new versions (2026-09-14)

**The user directive:** "unblind both papers as new versions, with unblind
labelling in file names."

**Scope:** both papers, as new versions with unblind-labelled file names:
instruments v15 -> **v16** (`instruments-paper-unblinded16.tex/.txt/.pdf`)
and main v12 -> **v13** (`main-article-unblinded13.tex/.txt/.pdf`), both in
`manuscript uploads v16/`. No content change of any kind: prose, mathematics,
figures, captions, labels, references, and the section structure outside the
blinding sites are byte-identical to v15/v12 (the reconstruction gate below
proves this). The no-new-claims gate holds trivially.

## What "blinded" meant, and what unblinding restores

Both manuscripts have carried the double-blind review register since the
first upload, at exactly **four sites per paper** (verified by a
case-insensitive `withheld | anonymiz | blind` sweep over the full sources
— no other sites exist):

1. `\author{[Author names withheld for review]}` with the blanked `\date{}`;
2. the placeholder Acknowledgements section ("Funding and acknowledgements
   are withheld for double-blind review.");
3. the anonymized companion citations in the two bibliographies
   ("[Authors anonymized for review]").

**No author identity exists anywhere in the project** — every manuscript
version back to the first upload is blinded, the repository's git authors
are the GitHub account's noreply address and this assistant, and the
original pre-split upload (`main article before supp/`) carries an
xx-placeholder title block, which is the author's own fill-in convention:

    \author{xx xx\\
    \small xx\\
    \small ORCID: xx\\
    \small Email: \href{mailto:xx\_xx@xx.xx.xx}{xx\_xx@xx.xx.xx}}
    \date{August 28, 2026}

Unblinding therefore restores that template **verbatim** (the xx fields are
the author's fill-in points for the single-blind venues recommended by the
wave-36 venue study), restores the version date under the title (the
original carried one; the blinded versions blanked it; the new versions
carry `September 14, 2026`), removes the review-marker acknowledgements
section **outright** (the original manuscript carried no acknowledgements
section — the section was added as a double-blind marker; real
funding/acknowledgements are added by the author at submission), and
de-anonymizes the companion citations to `xx~xx` (the placeholder joined
the way the house bibliography style joins names).

## The edit (edit_v16.py: 3 anchored hunks per paper, 12 changed lines each)

| Hunk | Instruments (v15 -> v16) | Main (v12 -> v13) |
|---|---|---|
| 1 | author block + date restored (2 lines -> 6 lines) | same |
| 2 | `\section*{Acknowledgements}` + withheld sentence + blank removed (3 lines; the original carried none) | same |
| 3 | `[Authors anonymized for review], \emph{Exact diamond balls...}` -> `xx~xx, \emph{Exact diamond balls...}` | `[Authors anonymized for review],` -> `xx~xx,` (line-broken bibitem) |

The `.txt` companions are byte-identical mirrors of the `.tex` files (the
house convention since v15).

## QA (the full battery)

- **check_v16.py: 32/32 PASS, exit 0.** P-layer: the blind-marker sweep
  (source), the restored-template presences, the **reconstruction gate**
  (the new files equal the v15/v12 sources with exactly the three wave-37
  replacements applied — re-derived independently inside the checker,
  byte-verified), the `.txt == .tex` byte mirrors, and the
  no-collateral-damage ledgers: label multiset, ref/eqref/cite multiset,
  captions (brace-matched extraction, byte-identical), the section ledger
  (exactly the one `\section*{Acknowledgements}` removed per paper, all
  other section lines byte-identical), the bibitem ledger (keys unchanged;
  all bodies byte-identical except the single companion entry per paper),
  and math-delimiter parity (`$` count unchanged — no mathematics touched).
  M-layer: page counts **53/46, unchanged**; the page-1 render needles
  (the `xx xx` block, `ORCID`, `Email`, `September 14, 2026` — all
  present); the full-text blind sweep over the PDF text; and the
  de-anonymized companion-citation render needles.
- **Honest debug trail: one checker-needle bug fixed in place** — the
  main-paper companion needle `xx xx, Exact affine geometry` failed on the
  pdftotext `ﬃ` ligature ("Exact aﬃne"), the wave-36 documented quirk
  class; fixed by ffi/ff/fi/fl ligature normalization before matching
  (the same normalization the wave-32/36 QA used).
- **Tectonic: exit 0 on both**; the number-free warning **signature sets
  are IDENTICAL to the fresh v15/v12 baselines** (main 54 = 54 warning
  lines, 1:1; instruments 40 vs 26 lines — the difference is purely the
  **third TeX pass** (an `.out` rerun triggered by the removed
  Acknowledgements bookmark, then the `.aux` rerun) versus the baseline's
  two passes; per-pass warning multiset identical, every warning region
  pre-existing, with line offsets shifted exactly by the edit (+3 before
  the removed section, net 0 after: +3 author lines, -3 acknowledgements
  lines) — **zero new typesetting defects**).
- **The W31 derivation battery re-run: ALL GATES PASS** (the mathematics
  untouched).
- **VLM visual verification on both page-1 renders:** the title, the
  xx-placeholder author block, and the date present, centered, cleanly
  rendered; no overlap with each other or the abstract; no cut-off or
  misalignment. (Minor observation, matching the original template's own
  rendering: the `\small` declarations on the affiliation/ORCID/Email
  lines have no visible size effect inside `\maketitle`'s tabular — the
  original upload's template renders identically.)

## The mathematics and the verdict chain

Untouched and unchanged: x^2 != 0; the additive tuple; H^6(B;Z) = Z with
the discriminant twice a generator; delta_2(D(C^3)) = 4/3; ququart
[4/3, 3/2] OPEN; the W23 stop stands.

## For the author, at submission time

The xx fields (name, affiliation, ORCID, email) in both title blocks, and
the `xx~xx` author fields of the two companion citations
(`CompanionChannels` in the instruments paper, `CompanionInstruments` in
the main article), are the fill-in points — the wave-36 venue study
recommended single-anonymized venues (Annals of Physics, LMP, J. Phys. A
class), for which these unblinded versions are the submission forms. The
blinded v15/v12 remain available in `manuscript uploads v15/` should a
double-blind venue be chosen instead.
