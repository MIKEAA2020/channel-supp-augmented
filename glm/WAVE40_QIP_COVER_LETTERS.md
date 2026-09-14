# Wave 40 — The QIP cover letters, one per article

**User directive (2026-09-14, English only):** "Provide a cover letter for
qip, one for each article, outlining the research. The cover letter should
briefly discuss the context and importance of the submitted work and why it
is appropriate for the journal."

## Scope

Two new artefacts, one per paper, for the journal line of the wave-36 study
(Quantum Information Processing, Springer Nature). Both letters accompany
the submission-ready unblinded forms of wave 39:

| Letter | For | Manuscript form |
|---|---|---|
| `../cover letters/qip-cover-letter-main.tex/.txt/.pdf` | main article | `main-article-unblinded15` (46 pp.) |
| `../cover letters/qip-cover-letter-instruments.tex/.txt/.pdf` | instruments paper | `instruments-paper-unblinded18` (53 pp.) |

The manuscripts themselves are untouched (byte-verified by the commit diff:
the wave adds files only, the no-new-claims gate holds trivially).

## Letter structure (identical skeleton, mirrored content)

- Sender block top-left: Amin Abaee / Independent Researcher /
  amin_abaee@ut.ac.ir / ORCID 0000-0002-0019-1842; date top-right,
  September 14, 2026 (the manuscripts' own version date).
- Recipient block: The Editors / *Quantum Information Processing* /
  Springer Nature (no editor named by guess; the generic address is the
  correct form for a portal-submitted letter).
- `Re:` line carrying the full manuscript title, verbatim.
- Six body paragraphs:
  1. **Submission statement** — article type and length (46/53 pp.,
     single-author).
  2. **Research outline** — grounded strictly in the paper's own abstract:
     the main letter covers the channel-compression question (continuous
     latent parameters, diamond-norm accuracy, continuous encoder /
     unrestricted decoder), the nonlinear-width positioning against
     tomography and programmable processors, the fibre-radius
     characterisation, the Borsuk–Ulam / deleted-product coindex lower
     bounds, the exact largest diamond ball at the completely depolarizing
     channel (optimal centre and optimal constant decoder, exact covering
     radius, the two envelopes meeting at zero latent dimension), the
     convex-projection / balanced-pinching upper bounds with the collapse
     and affine-dimension thresholds, and the query-uniformity theorem with
     the one-query injective threshold and the O(N^{-1/2}) repetition rate;
     the instruments letter covers the exact affine geometry (dimension
     d_A^2(n d_B^2 - 1), in-radius 2/(n d_B min{d_A,d_B}) at the uniform
     depolarising instrument, complementarity identity), the
     single-shot operational meaning via discrimination error, the
     antipodal lower envelope against the constant-code / projection /
     pinching upper bounds, the zero-error threshold, the complete
     flat-width classification (classical n <= 4 and qubit n <= 2 flat,
     >= 4/3 otherwise, the qutrit exactly 4/3), the cyclic flag-quotient
     cohomology with its machine cross-check, and the channel/measurement
     specialisations.
  3. **Context and importance** — the resource-theoretic framing (memory
     cost of representing channels/instruments with guaranteed worst-case
     accuracy), the exact-vs-asymptotic differentiation, the
     architecture-agnostic scope of the bounds, and, for the instruments
     letter, the exact-vs-certified bookkeeping and the role of the
     cohomological obstructions (with the literature relation deferred to
     the manuscript's own remark, no novelty claims coined).
  4. **Companion disclosure** — each letter names the other paper's exact
     title and states that it is being submitted separately to the same
     journal, that the two papers are self-contained, cross-cite each
     other, and can be reviewed independently. This is the standard
     editorial-transparency requirement for concurrent companion
     submissions; the wording matches the manuscripts' own companion
     bibitems ("submitted concurrently with the present work").
  5. **Fit for the journal** — grounded in QIP's published scope
     ("experimental and theoretical research across the entire spectrum of
     quantum information science", per the wave-36 journal-fit lookups),
     the standard formalism of the field, and the readership areas (channel
     and instrument simulation, quantum communication, resource-efficient
     processing); no page-limit claims beyond "full-length research
     article" (the length policy evidence lives in the wave-36 study, not
     the letters).
  6. **Brief declarations** — original, unpublished, not under
     consideration elsewhere, sole author, no funding, no competing
     interests; data availability mirrors each paper's own declarations
     section (main: purely theoretical, no datasets; instruments: the code
     and computation transcripts at the public repository cited in the
     manuscript).
- Closing: thanks, "Yours sincerely," signature block with name /
  affiliation / email (the ORCID stays in the letterhead; both letters are
  single-page A4 at 10pt with the manuscripts' own font stack — lmodern,
  T1, microtype, hidelinks hyperref).

## Content discipline

Every technical sentence in the letters traces to the corresponding
paper's abstract or introduction (the one deliberate framing sentence —
the diamond norm as the standard single-shot distinguishability distance —
is textbook-level common ground, not a new claim). No novelty adjectives,
no invented scope, no editorial-committee claims, no names guessed. The
letters are deliberately signed/unblinded artefacts: they accompany the
unblinded forms on the single-blind venue line.

## QA

- **Tectonic:** exit 0 on both; exactly ONE page each; zero warnings
  (no overfull/underfull). First compile was two pages (the signature
  block spilled); reclaimed by margin 2.3 -> 2.15 cm, parskip
  0.45 -> 0.35 em, tightened header/closing spacing, signature block
  trimmed to three lines (ORCID already in the letterhead), and two
  prose micro-trims (the "as an original research article" duplication —
  the Re: line already carries the type; the datasets sentence merged
  into the declarations sentence).
- **check_w40.py (154/154 PASS, exit 0):** per letter — page count == 1,
  A4 size, PDF metadata (Title / Author == "Amin Abaee" / Subject), the
  rendered-text needle set (identity block, date, recipient, Re: title,
  salutation and closing, the per-letter research needles, the companion
  title, the declarations phrases), the blind/placeholder/boilerplate
  sweeps (no "xx", no "anonymized", no stray LaTeX tokens, no unresolved
  refs), the .txt mirrors (same needle set), and source sanity (brace
  balance, `\end{document}`, no placeholders). Honest debug trail: two
  checker bugs fixed in place — (i) the hyphen-rejoin regex destroyed
  real hyphens at line breaks ("Flag-Quotient" split across lines),
  fixed by hyphen/whitespace-insensitive needle matching; the first run
  also caught a genuine needle failure thereby (the companion title in
  the main letter), which the fix resolved as a checker artifact, not a
  letter defect.
- **pdf-skill validators:** `poster_validate.py check-tex` — no errors,
  one benign advisory per letter (tabularx not loaded; the signature
  block is a fixed single-column `tabular`, no width risk).
  `pdf_qa.py` — PASS 10/10 on both (metadata, embedded fonts, no
  overflow, no blank pages, symmetric margins, single-page fill check
  skipped by design).
- **VLM verification (glm-5v-turbo):** both page renders — letterhead
  complete and cleanly laid out, all text within margins, no truncation,
  overlap, or artifacts, professional single-page appearance; verdicts
  recorded in `w40_vlm_main.json` / `w40_vlm_inst.json`. One low-dpi OCR
  artifact ("Amin Abaee" misread at 110 dpi) settled by a 300-dpi header
  crop re-check (`w40_vlm_inst_hdr.json`): the name reads exactly
  "Amin Abaee".
- **No-new-claims gate:** the manuscripts are untouched; the commit
  contains new files only (the letters, this note, the checker, the QA
  transcripts, the README pointer update).

## Deliverables

- `cover letters/qip-cover-letter-main.tex` / `.pdf` / `.txt`
  (`.txt` = the rendered letter as plain text, for pasting into
  submission-portal text fields).
- `cover letters/qip-cover-letter-instruments.tex` / `.pdf` / `.txt`.
- Session download folder copies of all six files.
- `glm/README.md` updated to waves 1-40 with the cover-letters pointer.

The verdict chain is untouched by construction (no manuscript content
changed): x^2 != 0; the tuple; H^6 = Z with the discriminant twice a
generator; delta_2 = 4/3; ququart [4/3, 3/2] OPEN; the W23 stop stands.
