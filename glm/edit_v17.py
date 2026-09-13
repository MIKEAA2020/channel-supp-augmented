#!/usr/bin/env python3
"""Wave 38 edit script: the author identity filled in + brief declarations.

The user directive (2026-09-14), continuing Wave 37's unblinded versions:
the author identity is supplied (Amin Abaee, Independent Researcher,
ORCID 0000-0002-0019-1842, amin_abaee@ut.ac.ir) and "for declarations,
keep it brief."

Wave 37 restored the author's own xx-placeholder template as the fill-in
convention.  This wave fills those fields with the real identity and adds
the standard brief declarations section at the exact site where the
double-blind manuscripts carried their withheld-marker acknowledgements
section (between the conclusion and the appendix -- the canonical journal
position), plus the companion-citation author fields.

Three anchored hunks per paper; nothing else changes: no prose, no
mathematics, no figures, no captions, no labels, no existing references
-> the no-new-claims gate holds trivially (pure authorial front matter:
identity, declarations, and the companion-citation author).  The one
added \ref{rem:machine-certificate} in the instruments declarations points
at the remark that already carries the repository footnote (no new
factual content; the sentence restates the existing footnote).

Inputs (current state, wave 37 output):
  manuscript uploads v16/instruments-paper-unblinded16.tex   (instruments v16)
  manuscript uploads v16/main-article-unblinded13.tex       (main v13)

Outputs (new state, unblind-labelled file names continued):
  manuscript uploads v17/instruments-paper-unblinded17.tex + .txt  (v17)
  manuscript uploads v17/main-article-unblinded14.tex + .txt       (v14)

Every replacement is anchored and asserted to match exactly once.
"""
import os

REPO = "/home/z/my-project/channel-supp-augmented"
SRC_INST = os.path.join(REPO, "manuscript uploads v16", "instruments-paper-unblinded16.tex")
SRC_MAIN = os.path.join(REPO, "manuscript uploads v16", "main-article-unblinded13.tex")
OUT_DIR = os.path.join(REPO, "manuscript uploads v17")

def apply(text, old, new, label):
    n = text.count(old)
    assert n == 1, f"[{label}] anchor count = {n} (expected 1)\nANCHOR: {old[:120]!r}"
    return text.replace(old, new)

# =====================================================================
# Hunk 1 (both papers): the author block -- the xx template filled in
# with the supplied identity (same 4-line structure, same \small
# convention, same \href{mailto:...}{...} email form).
# =====================================================================
OLD_AUTHOR = ("\\author{xx xx\\\\\n"
              "\\small xx\\\\\n"
              "\\small ORCID: xx\\\\\n"
              "\\small Email: \\href{mailto:xx\\_xx@xx.xx.xx}{xx\\_xx@xx.xx.xx}}")
NEW_AUTHOR = ("\\author{Amin Abaee\\\\\n"
              "\\small Independent Researcher\\\\\n"
              "\\small ORCID: 0000-0002-0019-1842\\\\\n"
              "\\small Email: \\href{mailto:amin\\_abaee@ut.ac.ir}{amin\\_abaee@ut.ac.ir}}")

# =====================================================================
# Hunk 2 (both papers): the brief declarations section, inserted at the
# exact site of the former double-blind withheld-marker section
# (conclusion -> appendix).  Brief per the directive: funding none,
# competing interests none, data availability in one sentence.
#   instruments: points at the remark that already carries the public
#   repository footnote (rem:machine-certificate);
#   main: purely theoretical, no datasets.
# =====================================================================
OLD_DECL_INST = "neither addresses the symmetric-group quotients;\n\n\\appendix"
NEW_DECL_INST = ("neither addresses the symmetric-group quotients;\n"
                 "\n"
                 "\\section*{Declarations}\n"
                 "The author declares no funding and no competing "
                 "interests. The code and computation transcripts of "
                 "Remark~\\ref{rem:machine-certificate} are available at "
                 "the repository cited there.\n"
                 "\n"
                 "\\appendix")

OLD_DECL_MAIN = "\\end{enumerate}\n\n\\appendix"
NEW_DECL_MAIN = ("\\end{enumerate}\n"
                 "\n"
                 "\\section*{Declarations}\n"
                 "The author declares no funding and no competing "
                 "interests. No datasets were generated or analysed.\n"
                 "\n"
                 "\\appendix")

# =====================================================================
# Hunk 3: the companion-citation author fields, house bib style
# (initial + tilde + surname, as in J.~Matousek / A.~Barvinok).
#   instruments cites the main article;  main cites the instruments paper.
# =====================================================================
OLD_COMP_INST = "xx~xx, \\emph{Exact diamond balls"
NEW_COMP_INST = "A.~Abaee, \\emph{Exact diamond balls"

OLD_COMP_MAIN = "xx~xx,\n\\emph{Exact affine geometry"
NEW_COMP_MAIN = "A.~Abaee,\n\\emph{Exact affine geometry"

# =====================================================================
# Apply
# =====================================================================
inst = open(SRC_INST).read()
inst = apply(inst, OLD_AUTHOR,    NEW_AUTHOR,    "I1 author block filled in")
inst = apply(inst, OLD_DECL_INST, NEW_DECL_INST, "I2 declarations inserted")
inst = apply(inst, OLD_COMP_INST, NEW_COMP_INST, "I3 companion citation author")

main = open(SRC_MAIN).read()
main = apply(main, OLD_AUTHOR,    NEW_AUTHOR,    "M1 author block filled in")
main = apply(main, OLD_DECL_MAIN, NEW_DECL_MAIN, "M2 declarations inserted")
main = apply(main, OLD_COMP_MAIN, NEW_COMP_MAIN, "M3 companion citation author")

# =====================================================================
# Write the new wave folder (unblind-labelled file names continued;
# byte-identical .txt mirrors, the house convention since v15).
# =====================================================================
os.makedirs(OUT_DIR, exist_ok=True)
inst_out = os.path.join(OUT_DIR, "instruments-paper-unblinded17.tex")
main_out = os.path.join(OUT_DIR, "main-article-unblinded14.tex")
open(inst_out, "w").write(inst)
open(inst_out.replace(".tex", ".txt"), "w").write(inst)  # byte-identical mirror
open(main_out, "w").write(main)
open(main_out.replace(".tex", ".txt"), "w").write(main)  # byte-identical mirror

# diff audit: every line-level difference must be one of the three hunks
def difflines(a_path, b_text, name):
    a = open(a_path).read().splitlines()
    b = b_text.splitlines()
    import difflib
    d = [l for l in difflib.unified_diff(a, b, lineterm="", n=0)
         if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))]
    print(f"{name}: {len(d)} changed diff lines")
    for l in d:
        print("   ", l[:150])

print("=== diff audit ===")
difflines(SRC_INST, inst, "instruments v16 -> v17 (identity + declarations)")
difflines(SRC_MAIN, main, "main v13 -> v14 (identity + declarations)")
print("\nWrote:", inst_out)
print("Wrote:", main_out)
