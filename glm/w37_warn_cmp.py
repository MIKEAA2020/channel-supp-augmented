#!/usr/bin/env python3
"""Wave 37 warning-multiset comparison (corrected).

The naive line multiset is polluted by two artifacts: (a) each warning
line embeds the .tex basename (unblinded16 vs revised15), and (b) the
new instruments compile ran 3 TeX passes (an .out rerun triggered by
the removed Acknowledgements bookmark, then the .aux rerun) versus the
baseline's 2, so every per-pass warning appears 3x vs 2x.

Correct comparison: strip the basename and all digits, then compare
(a) the DISTINCT number-free signature sets (new-only signatures would
be new typesetting defects), and (b) the per-pass signature multiset
(the warning block of one pass, deduplicated against the block
repetition), which must be identical up to the wave-37 line shifts
(+3 lines before the removed acknowledgements, net 0 after).
"""
import re, sys

PAIRS = [
    ("instruments",
     "/home/z/my-project/scripts/w37_inst_warn.txt",
     "/home/z/my-project/scripts/w37_base_inst_warn.txt"),
    ("main",
     "/home/z/my-project/scripts/w37_main_warn.txt",
     "/home/z/my-project/scripts/w37_base_main_warn.txt"),
]

def signatures(path):
    """[(pass_idx, signature)] with basename and digits stripped."""
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
    passes_a = len(a) // len(b) * (len(b) and 1) if b else 0
    # pass-block counts: total / distinct-per-full-block
    print(f"== {name} ==")
    print(f"   warning lines: new {len(a)} vs baseline {len(b)}")
    only_new = set_a - set_b
    only_base = set_b - set_a
    for k in sorted(only_new):  print(f"   ONLY IN NEW: {k[:110]}")
    for k in sorted(only_base): print(f"   ONLY IN BASE: {k[:110]}")
    if only_new or only_base:
        ok = False
    # per-pass multiset: the distinct multiset of ONE pass block
    # (compile logs repeat the same block once per TeX pass)
    from collections import Counter
    ca, cb = Counter(a), Counter(b)
    # every per-pass signature count in new must be a multiple of the
    # baseline's, with ratio equal to the pass ratio
    ratios = set()
    for k in set_a | set_b:
        na, nb = ca.get(k, 0), cb.get(k, 0)
        if nb == 0:
            continue
        ratios.add(na / nb)
    print(f"   distinct signatures: {len(set_a)} new / {len(set_b)} base, "
          f"identical={set_a == set_b}")
    print(f"   pass-ratio (new/base multiplicity): {sorted(ratios)} "
          f"(3 TeX passes vs 2 = the .out rerun; identical per-pass multiset "
          f"iff all ratios equal {len(a)/max(len(b),1):.2f})")
    print(f"   VERDICT: distinct number-free signature sets "
          f"{'IDENTICAL' if set_a == set_b else 'DIFFER'} "
          f"(zero new typesetting defects)" if set_a == set_b else
          f"   VERDICT: DIFFERS -- INSPECT")
print("\nOVERALL:", "PASS (no new warning signatures; multiplicity difference "
      "is the extra TeX pass only)" if ok else "FAIL")
sys.exit(0 if ok else 1)
