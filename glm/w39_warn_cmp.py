#!/usr/bin/env python3
"""Wave 39 warning-multiset comparison (house method, from waves 37/38).

Same normalization as w37/w38_warn_cmp.py: strip the .tex basename and
all digits, then compare (a) the DISTINCT number-free signature sets
(a new-only signature would be a new typesetting defect) and (b) the
per-pass signature multiplicities (pass-ratio analysis; compile logs
repeat the warning block once per TeX pass, and the number of passes
varies with rerun triggers).

Wave 39 context: the only source change is the one-line keyword trim
per paper, at source line 53 (instruments) / 55 (main), with the line
count unchanged -- so warning line numbers must be preserved exactly,
making this comparison stricter than usual (the signature sets AND
the raw counts should coincide apart from pass multiplicity).
"""
import re
from collections import Counter

WORK = "/home/z/my-project/scripts/w39_work"
PAIRS = [
    ("instruments", f"{WORK}/w39_inst_warn.txt",
     f"{WORK}/w39_base_inst_warn.txt"),
    ("main", f"{WORK}/w39_main_warn.txt",
     f"{WORK}/w39_base_main_warn.txt"),
]

def signatures(path):
    """[signature] with basename and digits stripped."""
    sigs = []
    for l in open(path, errors="replace").read().splitlines():
        if not re.search(r"(?i)overfull|underfull", l):
            continue  # skip the summary chatter line
        l = re.sub(r"^warning:\s*", "", l)
        l = re.sub(r"^[^:]*\.tex:\d*:\s*", "", l)  # strip basename + line no.
        l = re.sub(r"\d+", "", l)                  # number-free
        l = re.sub(r"\s+", " ", l).strip()
        sigs.append(l)
    return sigs

ok = True
for name, newf, basef in PAIRS:
    a, b = signatures(newf), signatures(basef)
    set_a, set_b = set(a), set(b)
    print(f"== {name} ==")
    print(f"   warning lines: new {len(a)} vs baseline {len(b)}")
    only_new = set_a - set_b
    only_base = set_b - set_a
    for k in sorted(only_new):  print(f"   ONLY IN NEW: {k[:110]}")
    for k in sorted(only_base): print(f"   ONLY IN BASE: {k[:110]}")
    if only_new or only_base:
        ok = False
    ca, cb = Counter(a), Counter(b)
    ratios = set()
    for k in set_a | set_b:
        if ca[k] and cb[k]:
            ratios.add(round(ca[k] / cb[k], 2))
    print(f"   per-signature multiplicity ratios (new/base): "
          f"{sorted(ratios) if ratios else 'n/a'}")
    # line-number preservation check (digits NOT stripped): the raw
    # warning lines must be identical line-for-line between new and
    # baseline modulo the BASENAME (fix: strip "warning: <basename>.tex"
    # as a prefix unit; the wave-38-style ^[^:]*\.tex pattern never
    # matched because [^:] cannot cross the "warning: " colon) --
    # with the one DOCUMENTED expected delta: the instruments v17
    # keywords line was Overfull by 0.19373pt (one warning per TeX
    # pass) and the trimmed v18 line fits, so that warning is absent
    # in the new log.  Nothing else may differ.
    EXPECTED_REMOVED = {
        "instruments": ["Overfull \\hbox (0.19373pt too wide) in "
                        "paragraph at lines 53--54"],
        "main": [],
    }
    def strip_base(l):
        return re.sub(r"^warning:\s*[^:]*\.tex", "warning: X.tex", l)
    raw_a = [l for l in open(newf, errors="replace").read().splitlines()
             if re.search(r"(?i)overfull|underfull", l)]
    raw_b = [l for l in open(basef, errors="replace").read().splitlines()
             if re.search(r"(?i)overfull|underfull", l)]
    norm_a = [strip_base(l) for l in raw_a]
    norm_b = [strip_base(l) for l in raw_b]
    # remove the documented expected-delta lines from the baseline side
    for sig in EXPECTED_REMOVED[name]:
        while True:
            idx = next((i for i, l in enumerate(norm_b) if sig in l), None)
            if idx is None:
                break
            norm_b.pop(idx)
    same = norm_a == norm_b
    print(f"   raw warning lines identical modulo basename + the documented "
          f"keywords-line overfull removal: {'YES' if same else 'NO'}")
    if not same:
        ok = False
        import difflib
        for l in list(difflib.unified_diff(norm_b, norm_a, lineterm=""))[:20]:
            print("   ", l[:150])

print("\nVERDICT:", "PASS -- zero new typesetting defects; signature sets "
      "identical to the fresh v17/v14 baselines; the only raw delta is "
      "the documented removal of the v17 keywords-line 0.19pt overfull "
      "(the trimmed v18 line fits)" if ok
      else "FAIL -- inspect the deltas above")
import sys
sys.exit(0 if ok else 1)
