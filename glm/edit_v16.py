#!/usr/bin/env python3
"""Wave 37 edit script: the unblinded new versions.

The user directive (2026-09-14): "unblind both papers as new versions,
with unblind labelling in file names."

Both manuscripts have carried the double-blind review register since the
first upload, at exactly four sites each: (1) the author block
\\author{[Author names withheld for review]} with the blanked \\date{},
(2) the placeholder Acknowledgements section added for review ("Funding
and acknowledgements are withheld for double-blind review." -- the
author's original pre-split manuscript carried NO acknowledgements
section), and (3) the anonymized companion citations in the two
bibliographies ("[Authors anonymized for review]").  No author identity
exists anywhere in the project: the original upload's title block was
itself an xx-placeholder template, which is the author's own fill-in
convention.  Unblinding therefore RESTORES that template verbatim (the
xx fields are the author's fill-in points for the single-blind venues
recommended by the wave-36 venue study), restores the version date
under the title (the original carried one; the blinded versions
blanked it), removes the review-marker acknowledgements section
outright (matching the original's structure), and de-anonymizes the
companion citations to "xx~xx" (the placeholder joined the way the
house bib style joins names).

    \\author{xx xx\\\\
    \\small xx\\\\
    \\small ORCID: xx\\\\
    \\small Email: \\href{mailto:xx\\_xx@xx.xx.xx}{xx\\_xx@xx.xx.xx}}
    \\date{September 14, 2026}

Three anchored hunks per paper; nothing else changes: no prose, no
math, no figures, no captions, no labels, no references -> the
no-new-claims gate holds trivially (pure de-anonymization of the review
register).

Inputs (current state, wave 36 output):
  manuscript uploads v15/instruments-paper-revised15.tex   (instruments v15)
  manuscript uploads v15/main-article-revised12.tex        (main v12)

Outputs (new state, unblind-labelled file names):
  manuscript uploads v16/instruments-paper-unblinded16.tex + .txt  (v16)
  manuscript uploads v16/main-article-unblinded13.tex + .txt       (v13)

Every replacement is anchored and asserted to match exactly once.
"""
import os

REPO = "/home/z/my-project/channel-supp-augmented"
SRC_INST = os.path.join(REPO, "manuscript uploads v15", "instruments-paper-revised15.tex")
SRC_MAIN = os.path.join(REPO, "manuscript uploads v15", "main-article-revised12.tex")
OUT_DIR = os.path.join(REPO, "manuscript uploads v16")

def apply(text, old, new, label):
    n = text.count(old)
    assert n == 1, f"[{label}] anchor count = {n} (expected 1)\nANCHOR: {old[:120]!r}"
    return text.replace(old, new)

# =====================================================================
# Hunk 1 (both papers): the author block -- restore the author's own
# template from the original pre-split upload, and restore the version
# date under the title.
# =====================================================================
OLD_AUTHOR = "\\author{[Author names withheld for review]}\n\\date{}"
NEW_AUTHOR = ("\\author{xx xx\\\\\n"
              "\\small xx\\\\\n"
              "\\small ORCID: xx\\\\\n"
              "\\small Email: \\href{mailto:xx\\_xx@xx.xx.xx}{xx\\_xx@xx.xx.xx}}\n"
              "\\date{September 14, 2026}")

# =====================================================================
# Hunk 2 (both papers): remove the double-blind acknowledgements
# marker (the original manuscript carried no acknowledgements section;
# the author adds real funding/acknowledgements at submission).
# =====================================================================
OLD_ACKS = ("\\section*{Acknowledgements}\n"
            "Funding and acknowledgements are withheld for double-blind review.\n"
            "\n\\appendix")
NEW_ACKS = "\\appendix"

# =====================================================================
# Hunk 3: de-anonymize the companion citations.
#   instruments cites the main article;  main cites the instruments paper.
# =====================================================================
OLD_COMP_INST = "[Authors anonymized for review], \\emph{Exact diamond balls"
NEW_COMP_INST = "xx~xx, \\emph{Exact diamond balls"

OLD_COMP_MAIN = "[Authors anonymized for review],\n\\emph{Exact affine geometry"
NEW_COMP_MAIN = "xx~xx,\n\\emph{Exact affine geometry"

# =====================================================================
# Apply
# =====================================================================
inst = open(SRC_INST).read()
inst = apply(inst, OLD_AUTHOR, NEW_AUTHOR, "I1 author block unblinded")
inst = apply(inst, OLD_ACKS,  NEW_ACKS,  "I2 acknowledgements marker removed")
inst = apply(inst, OLD_COMP_INST, NEW_COMP_INST, "I3 companion citation de-anonymized")

main = open(SRC_MAIN).read()
main = apply(main, OLD_AUTHOR, NEW_AUTHOR, "M1 author block unblinded")
main = apply(main, OLD_ACKS,  NEW_ACKS,  "M2 acknowledgements marker removed")
main = apply(main, OLD_COMP_MAIN, NEW_COMP_MAIN, "M3 companion citation de-anonymized")

# =====================================================================
# Write the new wave folder (unblind-labelled file names; byte-identical
# .txt mirrors, the house convention since v15).
# =====================================================================
os.makedirs(OUT_DIR, exist_ok=True)
inst_out = os.path.join(OUT_DIR, "instruments-paper-unblinded16.tex")
main_out = os.path.join(OUT_DIR, "main-article-unblinded13.tex")
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
difflines(SRC_INST, inst, "instruments v15 -> v16 (unblinded)")
difflines(SRC_MAIN, main, "main v12 -> v13 (unblinded)")
print("\nWrote:", inst_out)
print("Wrote:", main_out)
