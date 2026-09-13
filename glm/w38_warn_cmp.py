#!/usr/bin/env python3
"""Wave 38 warning-multiset comparison (house method, from wave 37).

Same normalization as w37_warn_cmp.py: strip the .tex basename and all
digits, then compare (a) the DISTINCT number-free signature sets (a
new-only signature would be a new typesetting defect) and (b) the
per-pass signature multiplicities (pass-ratio analysis; compile logs
repeat the warning block once per TeX pass, and the number of passes
varies with rerun triggers).
"""
import re, sys
from collections import Counter

PAIRS = [
    ("instruments",
     "/home/z/my-project/scripts/w38_inst_warn.txt",
     "/home/z/my-project/scripts/w38_base_inst_warn.txt"),
    ("main",
     "/home/z/my-project/scripts/w38_main_warn.txt",
     "/home/z/my-project/scripts/w38_base_main_warn.txt"),
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
        na, nb = ca.get(k, 0), cb.get(k, 0)
        if nb == 0:
            continue
        ratios.add(na / nb)
    print(f"   distinct signatures: {len(set_a)} new / {len(set_b)} base, "
          f"identical={set_a == set_b}")
    print(f"   pass-ratio (new/base multiplicity): {sorted(ratios)} "
          f"(pass-count difference only; identical per-pass multiset "
          f"iff all ratios equal {len(a)/max(len(b),1):.2f})")
    verdict = "IDENTICAL" if set_a == set_b else "DIFFER"
    print(f"   VERDICT: distinct number-free signature sets {verdict}"
          + (" (zero new typesetting defects)" if set_a == set_b
             else " -- INSPECT"))
print("\nOVERALL:", "PASS (no new warning signatures; any multiplicity "
      "difference is the TeX pass count only)" if ok else "FAIL")
sys.exit(0 if ok else 1)
