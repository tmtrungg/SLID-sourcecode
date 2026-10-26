import csv, glob, json

IND = ["honeypot_related_address", "number_of_malicious_contracts_created",
       "phishing_activities", "stealing_attack", "blacklist_doubt"]

pools_by_owner = {}
for r in csv.DictReader(open("flagged_pools.csv")):
    pools_by_owner.setdefault(r["owner_address"].lower(), []).append(r["pool_address"])

owners_rows, audit_rows = [], []
for p in sorted(glob.glob("raw_responses/goplus_address/*.json")):
    d = json.load(open(p))
    res = (d.get("_body") or {}).get("result") or {}
    owner = d.get("_query") or ""
    vals = {}
    for k in IND:
        try: vals[k] = int(res.get(k) or 0)
        except (TypeError, ValueError): vals[k] = 0
    scam = vals[IND[0]] or vals[IND[1]]
    ps = vals[IND[2]] or vals[IND[3]] or vals[IND[4]]
    group = ("scam-indicators-only" if (scam and not ps) else
             "both" if (scam and ps) else
             "phishing-stealing-only" if ps else "")
    ref = "raw_responses/goplus_address/" + p.split("/")[-1]
    base = [res.get("data_source", ""), d.get("_retrieved_at", ""), ref]
    owners_rows.append([owner, 1 if group else 0] + [vals[k] for k in IND] + base)
    if group:
        for pool in pools_by_owner.get(owner.lower(), []):
            audit_rows.append([pool, owner, group] + [vals[k] for k in IND] + base)

with open("owner_screen_2951.rebuilt.csv", "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["owner_address", "qualified"] + IND + ["data_source", "retrieved_at", "raw_response"])
    w.writerows(sorted(owners_rows))
with open("owner_audit_150.rebuilt.csv", "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["pool_address", "owner_address", "indicator_group"] + IND + ["data_source", "retrieved_at", "raw_response"])
    w.writerows(sorted(audit_rows))

from collections import Counter
print("owners screened:", len(owners_rows), "| qualified pools:", len(audit_rows),
      "| distinct owners:", len({r[1] for r in audit_rows}))
print("groups:", dict(Counter(r[2] for r in audit_rows)))
