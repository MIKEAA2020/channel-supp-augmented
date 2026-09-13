#!/usr/bin/env python3
"""Wave 36 checker: the two figure-positioning repairs (pure positioning).

Layers:
  P  (textual): the three hunks present exactly once; the pure-positioning
      gate (the ONLY line-level differences vs v14/v11 are the three
      hunks - nothing else may differ); .txt == .tex; both figure
      captions byte-identical; labels unique; refs resolve; no informal
      register; page counts unchanged.
  R  (render): pdftotext needles for both figures in the compiled PDFs;
      the compile logs' number-free warning multisets identical to the
      v14/v11 baselines (parsed from the saved logs).
  V  (visual): VLM verification of both rendered pages (recorded in
      WAVE36_FIGURE_POSITIONING.md; not re-run here).
  M  (mathematical): no mathematics touched (the diff gate implies it);
      the Wave-31 derivation battery re-run separately (12 gates).
"""
import os, re, sys, subprocess
from collections import Counter

REPO = "/home/z/my-project/channel-supp-augmented"
V15 = os.path.join(REPO, "manuscript uploads v15", "instruments-paper-revised15")
V14 = os.path.join(REPO, "manuscript uploads v14", "instruments-paper-revised14")
M12 = os.path.join(REPO, "manuscript uploads v15", "main-article-revised12")
M11 = os.path.join(REPO, "manuscript uploads v13", "main-article-revised11")

results, fails = [], 0
def check(name, cond, detail=""):
    global fails
    results.append((name, bool(cond)))
    if not cond:
        fails += 1
        print("FAIL " + name + (("  -- " + str(detail)) if detail else ""))
    else:
        print("PASS " + name)

inst = open(V15 + ".tex").read()
main = open(M12 + ".tex").read()

# ---------------------------------------------------------------- P layer
check("P: new gamma-annotation line present",
      inst.count("at (5.0,-0.42) {classifies $U(3)\\to U(3)/K$}") == 1)
check("P: old gamma-annotation line gone",
      inst.count("at (4.1,-1.42)") == 0)
check("P: new FB placement present",
      main.count("(FB) at (0,-53.8mm)") == 1)
check("P: old FB placement gone",
      main.count("below=5mm of B] (FB) at (0,-36mm)") == 0)
check("P: new orthogonal-join route present",
      main.count("(B.east) -- ++(12mm,0) |- (J.north) node[pos=0.86, above") == 1)
check("P: old orthogonal-join route gone",
      main.count("(B.east) -- ++(5mm,0) |- (J.north) node[pos=0.25, below, xshift=1mm") == 0)

# pure-positioning gate: only the intended diff lines
import difflib
def changed_lines(a_path, b_text):
    a = open(a_path).read().splitlines()
    b = b_text.splitlines()
    return [l for l in difflib.unified_diff(a, b, lineterm="", n=0)
            if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))]
di = changed_lines(V14 + ".tex", inst)
dm = changed_lines(M11 + ".tex", main)
check("P: instruments diff = exactly 2 lines (1 removed, 1 added)", len(di) == 2, di)
check("P: main diff = exactly 8 lines (4 removed, 4 added)", len(dm) == 8, dm)
check("P: no prose changed in instruments hunk",
      "classifies $U(3)\\to U(3)/K$" in di[1] and "classifies $U(3)\\to U(3)/K$" in di[0])
check("P: no prose changed in main hunks",
      all(("Herm(B_i)" in l or "orthogonal join" in l or l[1:].lstrip().startswith("%"))
          for l in dm))

check("P: .txt == .tex (instruments v15)",
      open(V15 + ".txt").read() == inst)
check("P: .txt == .tex (main v12)",
      open(M12 + ".txt").read() == main)

# captions byte-identical (no caption/text change anywhere)
cap_fib = "caption{The spaces and maps of the proof of Proposition"
cap_rep = "caption{Replacement-family geometry and orthogonal-block join."
inst14 = open(V14 + ".tex").read()
main11 = open(M11 + ".tex").read()
check("P: fibration caption byte-identical",
      inst[inst.index(cap_fib):inst.index(cap_fib) + 3000] ==
      inst14[inst14.index(cap_fib):inst14.index(cap_fib) + 3000])
check("P: replacement-join caption byte-identical",
      main[main.index(cap_rep):main.index(cap_rep) + 1500] ==
      main11[main11.index(cap_rep):main11.index(cap_rep) + 1500])

# labels unique; refs resolve
labels = re.findall(r"\\label\{([^}]+)\}", inst)
check("P: instruments labels unique", len(labels) == len(set(labels)))
labels_m = re.findall(r"\\label\{([^}]+)\}", main)
check("P: main labels unique", len(labels_m) == len(set(labels_m)))
inst_log = open("/tmp/inst_v15.log", errors="replace").read()
main_log = open("/tmp/main_v12.log", errors="replace").read()
check("P: no undefined references (instruments)", "undefined" not in inst_log.lower())
check("P: no undefined references (main)", "undefined" not in main_log.lower())

# informal-register sweep: precise W34-style forbidden phrases over both
# full sources (the diff gate above already confines all changes to three
# coordinate lines); plus a check that the only new text (two source
# comments) is technical
INFORMAL = ["the previous version", "earlier versions", "in its corrected form",
            "the corrected statement", "the corrected coordinate", "change-log",
            "we fixed", "this version closes", "wave 3", "wave3", "the wave",
            "the audit", "our audit", "TODO", "FIXME"]
for src, nm in [(inst, "instruments v15"), (main, "main v12")]:
    hits = [p for p in INFORMAL if p.lower() in src.lower()]
    check(f"P: informal-register sweep clean ({nm})", not hits, hits)
new_comments = [l for l in dm if l.startswith("+") and l[1:].lstrip().startswith("%")]
check("P: new source comments technical only",
      all(re.fullmatch(r"[% a-z0-9.,+()\-']*", l.lower().replace("flagged space", "").replace("orthogonal join arrow", "").replace("moved", "").replace("down and to a deterministic centre placement", "").replace("clears the", "").replace("turns right of the box's east edge; label above the horizontal run", "")) for l in new_comments) and len(new_comments) == 2)

# page counts
def pages(pdf):
    out = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    return int(re.search(r"Pages:\s+(\d+)", out).group(1))
check("P: instruments v15 page count = 53", pages(V15 + ".pdf") == 53)
check("P: main v12 page count = 46", pages(M12 + ".pdf") == 46)

# ---------------------------------------------------------------- R layer
def render(pdf):
    return subprocess.run(["pdftotext", "-layout", pdf, "-"],
                          capture_output=True, text=True).stdout
r15 = render(V15 + ".pdf")
r12 = render(M12 + ".pdf")
pages15 = r15.split("\f")
pages12 = r12.split("\f")
check("R: gamma annotation renders (instruments p.36, pdftotext spacing)",
      any("classifies U (3)" in p for p in pages15[35:37]))
check("R: fibration caption renders",
      any("The spaces and maps of the proof" in p for p in pages15[35:37]))
check("R: orthogonal join label renders (main p.15)",
      any("orthogonal join" in p for p in pages12[14:16]))
check("R: replacement-join caption renders",
      any("Replacement-family geometry and orthogonal-block join" in p for p in pages12[14:16]))
check("R: balanced-partitions note still renders (moved with the box)",
      any("Balanced partitions" in p for p in pages12[14:17]))

# warning multisets identical to baselines (number-free)
def multiset(logpath):
    txt = open(logpath, errors="replace").read()
    pats = [f"{m.group(1)} {m.group(2)}"
            for m in re.finditer(r"(Overfull|Underfull) \\[hv]box \(([^)]+)\)", txt)]
    return Counter(re.sub(r"\d+(\.\d+)?", "N", p) for p in pats)
check("R: instruments warning multiset identical to v14 baseline",
      multiset("/tmp/inst_v15.log") == multiset("/home/z/my-project/compile-test/w36base/inst_v14.log"))
check("R: main warning multiset identical to v11 baseline",
      multiset("/tmp/main_v12.log") == multiset("/home/z/my-project/compile-test/w36base/main_v11.log"))

# ---------------------------------------------------------------- summary
print(f"\n{len(results) - fails}/{len(results)} PASS, {fails} FAIL")
sys.exit(1 if fails else 0)
