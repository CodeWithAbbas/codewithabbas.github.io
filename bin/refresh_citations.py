#!/usr/bin/env python3
"""Refresh _data/citations.yml from Google Scholar.

Run this from an ordinary network connection, not from CI — Scholar blocks
datacenter IP ranges, which is why the GitHub Action cannot do it.

    python bin/refresh_citations.py

Then commit the change.  Standard library only; no dependencies.
"""
import datetime, html, os, re, sys, urllib.request

SCHOLAR_ID = "he1jXaIAAAAJ"
URL = "https://scholar.google.com/citations?user={}&hl=en&cstart=0&pagesize=100"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120 Safari/537.36")
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "_data", "citations.yml")


def fetch():
    req = urllib.request.Request(URL.format(SCHOLAR_ID), headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "ignore")


def main():
    page = fetch()
    if "captcha" in page.lower() or "unusual traffic" in page.lower():
        sys.exit("Scholar served a CAPTCHA. Try again later or from another network.")

    rows = re.findall(r'<tr class="gsc_a_tr">(.*?)</tr>', page, re.S)
    if not rows:
        sys.exit("No publications parsed — Scholar may have changed its markup.")

    papers = []
    for r in rows:
        cid = re.search(r"citation_for_view=([^\"&]+)", r)
        ttl = re.search(r'class="gsc_a_at"[^>]*>(.*?)</a>', r, re.S)
        cit = re.search(r'class="gsc_a_ac[^"]*"[^>]*>(\d*)</a>', r)
        yr = re.search(r'class="gsc_a_h[^"]*"[^>]*>(\d*)</span>', r)
        if not cid:
            continue
        papers.append((
            cid.group(1),
            int(cit.group(1)) if cit and cit.group(1) else 0,
            yr.group(1) if yr and yr.group(1) else "Unknown Year",
            html.unescape(re.sub("<[^>]+>", "", ttl.group(1))) if ttl else "",
        ))

    def q(s):
        return "'" + s.replace("'", "''") + "'"

    lines = ["metadata:", "  last_updated: '%s'" % datetime.date.today().isoformat(), "papers:"]
    for cid, c, y, t in sorted(papers):
        lines += ["  %s:" % cid, "    citations: %d" % c,
                  "    title: %s" % q(t), "    year: %s" % q(str(y))]

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    total = sum(p[1] for p in papers)
    print("Wrote %s" % OUT)
    print("%d publications, %d citations total" % (len(papers), total))


if __name__ == "__main__":
    main()
