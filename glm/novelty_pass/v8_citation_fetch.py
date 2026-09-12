#!/usr/bin/env python3
"""Wave 27 / v8 citation-integration fetch (2026-09-13).

Two jobs, both evidence-logged in this directory:
  (A) Live-verify the exact bibliographic data for the WAVE26 near-collision
      citations to be integrated into v8 (Guerra-Jana TAMS DOI, Korbas venue,
      Matszangosz journal data, the two Z_p-BU papers' authors/venues).
  (B) Probe MathSciNet access status for the user's task 3 (which articles
      can't be accessed from this environment) + the open/paywall status of
      the underlying journal versions of the near-collision line.

Nothing here is written from memory: every field printed below is parsed from
a live HTTP response saved in this directory.
"""
import json
import ssl
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

OUT = "/home/z/my-project/scripts/novelty_pass"
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) citation-verification/1.0 (research)"}
CTX = ssl.create_default_context()


def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers=UA)
    try:
        r = urllib.request.urlopen(req, timeout=timeout, context=CTX)
        return {"status": r.status, "final_url": r.url,
                "body": r.read(250000).decode("utf-8", "ignore")}
    except urllib.error.HTTPError as e:
        try:
            body = e.read(8000).decode("utf-8", "ignore")
        except Exception:
            body = ""
        return {"status": e.code, "error": str(e.reason), "final_url": url, "body": body}
    except Exception as e:
        return {"status": None, "error": repr(e), "final_url": url, "body": ""}


# ---------------------------------------------------------------------------
# (A) arXiv records. The export API was rate-limited (429) in the W26 session
# and is again here (recorded honestly below); the WEBSITE abs pages are a
# different endpoint and are used instead. 2309/2304 pages are already saved
# (abs_2309.html, abs_2304.html); the other three are fetched fresh.
# ---------------------------------------------------------------------------
import os
import re as _re

ARX_IDS = ["2309.00429", "2304.12990", "1910.11149", "1008.1134", "2211.08087"]
api_url = ("https://export.arxiv.org/api/query?"
           + urllib.parse.urlencode({"id_list": ",".join(ARX_IDS), "max_results": "50"}))
res = fetch(api_url)
api_note = {"api_url": api_url, "status": res.get("status"),
            "body_head": res.get("body", "")[:200]}
print(f"[arXiv API] status={res['status']} (rate limit recorded; "
      f"{'429 as in W26' if res.get('status') == 429 else ''})")


def parse_abs_html(html: str):
    """Parse an arXiv abstract page's citation metadata."""
    out = {}
    for key in ("citation_title", "citation_author", "citation_date",
                "citation_arxiv_id"):
        vals = _re.findall(rf'<meta name="{key}" content="([^"]*)"', html)
        out[key] = vals
    m = _re.search(r'<td class="tablecell jref">(.*?)</td>', html, _re.S)
    out["journal_ref"] = " ".join(m.group(1).split()) if m else ""
    m = _re.search(r'<td class="tablecell doi">.*?href="https://doi\.org/([^"]+)"', html, _re.S)
    out["doi"] = m.group(1) if m else ""
    return out


summary = []
for aid in ARX_IDS:
    local = f"{OUT}/abs_{aid.split('.')[0] if aid.startswith(('2309', '2304')) else 'v8_' + aid.replace('.', '_')}.html"
    if aid == "2309.00429" and os.path.exists(f"{OUT}/abs_2309.html"):
        html = open(f"{OUT}/abs_2309.html", encoding="utf-8", errors="ignore").read()
        src = "local (saved in W26)"
    elif aid == "2304.12990" and os.path.exists(f"{OUT}/abs_2304.html"):
        html = open(f"{OUT}/abs_2304.html", encoding="utf-8", errors="ignore").read()
        src = "local (saved in W26)"
    else:
        r = fetch(f"https://arxiv.org/abs/{aid}")
        html = r.get("body", "")
        with open(f"{OUT}/abs_v8_{aid}.html", "w") as f:
            f.write(html)
        src = f"live fetch status={r.get('status')}"
        time.sleep(4)
    meta = parse_abs_html(html)
    summary.append({"arxiv_id": aid, "source_of_record": src, **{
        k: (v if isinstance(v, list) else v) for k, v in meta.items()}})
    print(f"[abs {aid}] ({src})")
    print(f"    title:    {meta['citation_title'][:1] and meta['citation_title'][0]}")
    print(f"    authors:  {meta['citation_author']}")
    print(f"    jref:     {meta['journal_ref']!r}   doi: {meta['doi']!r}")
print(json.dumps(summary, indent=2))

# ---------------------------------------------------------------------------
# (B) zbMATH Open API: pin the TAMS record (DOI/volume/pages) and Korbas.
# ---------------------------------------------------------------------------
ZB_QUERIES = [
    ("zbm_v8_guerra_tams", "an:\"Guerra, Lorenzo\" AND ti:\"Cohomology of complete unordered flag manifolds\""),
    ("zbm_v8_korbas", "au:Korbas AND ti:cup-length"),
]
zb_parsed = {}
for fname, q in ZB_QUERIES:
    url = ("https://api.zbmath.org/v1/document/_search?"
           + urllib.parse.urlencode({"search_string": q}))
    r = fetch(url)
    with open(f"{OUT}/{fname}.json", "w") as f:
        f.write(r.get("body", ""))
    recs = []
    try:
        j = json.loads(r.get("body", "{}"))
        for d in j.get("result", [])[:5]:
            src = d.get("source", {})
            series = src.get("series", [{}])[0] if src.get("series") else {}
            recs.append({
                "authors": [a.get("name") for a in d.get("contributors", {}).get("authors", [])],
                "title": d.get("title", {}).get("title"),
                "source": src.get("source"),
                "volume": series.get("volume"),
                "year": series.get("year"),
                "pages": src.get("pages"),
                "dois": [l.get("identifier") for l in d.get("links", []) if l.get("type") == "doi"],
                "arxiv": [l.get("identifier") for l in d.get("links", []) if l.get("type") == "arxiv"],
            })
    except Exception as ex:
        recs.append({"parse_error": repr(ex)})
    zb_parsed[fname] = recs
    print(f"[zbMATH] {fname}: status={r['status']} records={len(recs)}")
    print(json.dumps(recs, indent=2))
    time.sleep(3)

# ---------------------------------------------------------------------------
# (C) Access probes: MathSciNet (task 3) + the journal versions of the line.
# ---------------------------------------------------------------------------
PROBES = [
    ("mathscinet_home", "https://mathscinet.ams.org/mathscinet/"),
    ("mathscinet_search",
     "https://mathscinet.ams.org/mathscinet/search/publications.html?pg4=AULL&s4=unordered+flag+manifold"),
    ("mathscinet_mrlookup", "https://mathscinet.ams.org/mrlookup"),
    ("ams_public", "https://www.ams.org/home/page"),
    ("arxiv_abs_2309", "https://arxiv.org/abs/2309.00429"),
    ("zbmath_open_record", "https://zbmath.org/7996963"),
    ("doi_topol_guerra_jana_maiti", "https://doi.org/10.1016/j.topol.2025.109279"),
]
MARKERS = ["log in", "login", "sign in", "subscribe", "subscription", "purchase",
           "purchase this article", "get access", "access denied", "credentials",
           "institutional access", "federation", "shibboleth"]
probe_results = {}
for name, url in PROBES:
    r = fetch(url)
    body = r.get("body", "")
    hits = [m for m in MARKERS if m in body.lower()]
    probe_results[name] = {
        "url": url,
        "status": r.get("status"),
        "final_url": r.get("final_url"),
        "error": r.get("error"),
        "gate_markers_found": hits,
        "title_hint": body[body.lower().find("<title>") + 7: body.lower().find("</title>")][:120]
        if "<title>" in body.lower() else body[:120],
    }
    print(f"[probe] {name}: status={r.get('status')} final={r.get('final_url')}")
    print(f"        markers={hits}  title={probe_results[name]['title_hint'][:100]!r}")
    time.sleep(2)

with open(f"{OUT}/v8_probe_results.json", "w") as f:
    json.dump({"arxiv_api_status": api_note, "arxiv_abs": summary,
               "zbmath": zb_parsed, "probes": probe_results}, f, indent=2)
print("\nSaved: v8_probe_results.json")
