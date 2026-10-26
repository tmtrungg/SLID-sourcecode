import csv, json, os, time, urllib.request

os.makedirs("raw_responses/goplus_address", exist_ok=True)
owners = sorted({r["owner_address"].lower() for r in csv.DictReader(open("flagged_pools.csv"))})
for i, a in enumerate(owners):
    out = f"raw_responses/goplus_address/{a}.json"
    if os.path.exists(out):
        continue
    url = f"https://api.gopluslabs.io/api/v1/address_security/{a}?chain_id=1"
    with urllib.request.urlopen(url, timeout=30) as resp:
        body = json.loads(resp.read().decode())
    json.dump({"_status": 200, "_body": body, "_url": url, "_query": a,
               "_retrieved_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())},
              open(out, "w"))
    if i % 50 == 0:
        print(f"{i}/{len(owners)}")
    time.sleep(1.2)
print("done")
