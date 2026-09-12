#!/usr/bin/env python3
"""v8 citation fetch, part 2: Crossref (public API) + zbMATH plain-string retries.

Pins the journal-level data for the WAVE26 near-collision citations:
  - Guerra-Jana TAMS volume/pages/DOI
  - Korbas 2003 venue/DOI
  - Weber-Wojciechowski 2017 DOI
  - Matszangosz journal version?
  - Crabb 2022 journal version?
Every printed field comes from a saved live response.
"""
import json
import re
import ssl
import time
import urllib.parse
import urllib.request

OUT = "/home/z/my-project/scripts/novelty_pass"
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) citation-verification/1.0 (research)"}
CTX = ssl.create_default_context()


def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers=UA)
    try:
        r = urllib.request.urlopen(req, timeout=timeout, context=CTX)
        return {"status": r.status, "final_url": r.url,
                "body": r.read(400000).decode("utf-8", "ignore")}
    except urllib.error.HTTPError as e:
        try:
            body = e.read(8000).decode("utf-8", "ignore")
        except Exception:
            body = ""
        return {"status": e.code, "error": str(e.reason), "final_url": url, "body": body}
    except Exception as e:
        return {"status": None, "error": repr(e), "final_url": url, "body": ""}


CROSSREF = [
    ("cr_guerra_tams", "Cohomology of complete unordered flag manifolds Guerra Jana Transactions"),
    ("cr_korbas", "Korbas cup-length cohomology real flag manifolds"),
    ("cr_weber", "Weber Wojciechowski Pelczynski conjecture Auerbach bases"),
    ("cr_matszangosz", "Matszangosz cohomology rings real flag manifolds"),
    ("cr_crabb", "Crabb Borsuk-Ulam theorem cyclic p-groups"),
]

cr_parsed = {}
for fname, q in CROSSREF:
    url = ("https://api.crossref.org/works?rows=3&select=title,author,DOI,"
           "container-title,volume,page,issued,type"
           "&query.bibliographic=" + urllib.parse.quote(q))
    r = fetch(url)
    with open(f"{OUT}/{fname}.json", "w") as f:
        f.write(r.get("body", ""))
    items = []
    try:
        for it in json.loads(r.get("body", "{}")).get("message", {}).get("items", []):
            items.append({
                "title": (it.get("title") or [""])[0][:110],
                "authors": [f"{a.get('given','')} {a.get('family','')}".strip()
                            for a in it.get("author", [])][:6],
                "container": (it.get("container-title") or [""])[0],
                "volume": it.get("volume"), "page": it.get("page"),
                "year": (it.get("issued", {}).get("date-parts") or [[None]])[0][0],
                "DOI": it.get("DOI"), "type": it.get("type"),
            })
    except Exception as ex:
        items.append({"parse_error": repr(ex)})
    cr_parsed[fname] = {"status": r.get("status"), "items": items}
    print(f"[crossref] {fname}: status={r.get('status')}")
    for it in items:
        print("   ", json.dumps(it, ensure_ascii=False))
    time.sleep(2)

# zbMATH plain-string retries (the structured syntax 404'd)
ZB = [("zbm_v8_guerra_tams2", "Cohomology of complete unordered flag manifolds"),
      ("zbm_v8_korbas2", "cup-length of real flag manifolds")]
zb_parsed = {}
for fname, q in ZB:
    url = ("https://api.zbmath.org/v1/document/_search?"
           + urllib.parse.urlencode({"search_string": q}))
    r = fetch(url)
    with open(f"{OUT}/{fname}.json", "w") as f:
        f.write(r.get("body", ""))
    recs = []
    try:
        for d in json.loads(r.get("body", "{}")).get("result", [])[:4]:
            src = d.get("source", {})
            series = (src.get("series") or [{}])[0] if src.get("series") else {}
            recs.append({
                "authors": [a.get("name") for a in d.get("contributors", {}).get("authors", [])],
                "title": (d.get("title") or {}).get("title"),
                "source": src.get("source"), "volume": series.get("volume"),
                "year": series.get("year"), "pages": src.get("pages"),
                "dois": [l.get("identifier") for l in d.get("links", []) if l.get("type") == "doi"],
                "arxiv": [l.get("identifier") for l in d.get("links", []) if l.get("type") == "arxiv"],
            })
    except Exception as ex:
        recs.append({"parse_error": repr(ex), "status": r.get("status"),
                     "body_head": r.get("body", "")[:200]})
    zb_parsed[fname] = recs
    print(f"[zbMATH] {fname}: status={r.get('status')}")
    for rec in recs:
        print("   ", json.dumps(rec, ensure_ascii=False))
    time.sleep(3)

# Matszangosz full title from the saved abs page
html = open(f"{OUT}/abs_v8_1910.11149.html", encoding="utf-8", errors="ignore").read()
m = re.search(r'<h1 class="title mathjax">(.*?)</h1>', html, _ := re.S) if False else re.search(r'<h1 class="title mathjax">(.*?)</h1>', html, re.S)
full_title = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else "?"
full_title = " ".join(full_title.split())
print(f"[Matszangosz full title] {full_title}")

# If a TAMS DOI was found, probe its resolution
tams_doi = None
for rec in (zb_parsed.get("zbm_v8_guerra_tams2") or []) + cr_parsed.get("cr_guerra_tams", {}).get("items", []):
    for d in (rec.get("dois") or ([] if "dois" not in rec else rec["dois"])) or ([rec["DOI"]] if rec.get("DOI") else []):
        if d and "10.1090" in str(d):
            tams_doi = d
if tams_doi:
    r = fetch(f"https://doi.org/{tams_doi}")
    print(f"[TAMS DOI probe] https://doi.org/{tams_doi} -> status={r.get('status')} final={r.get('final_url')}")
    title = r.get("body", "")[:2000]
    print(f"    landing head: {title[:300]!r}")

with open(f"{OUT}/v8_citation_data.json", "w") as f:
    json.dump({"crossref": cr_parsed, "zbmath": zb_parsed,
               "matszangosz_full_title": full_title, "tams_doi": tams_doi}, f, indent=2)
print("\nSaved: v8_citation_data.json")
