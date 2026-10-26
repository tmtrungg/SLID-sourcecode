# External owner audit (Section 6.3 of the paper)

Evidence backing the claim that 150 of the 3,117 heuristic-flagged pools are linked to 144 owner addresses carrying externally reported to be malicious, from third-party verificator of GoPlus Address Security feed, which attributes each record to its contributing providers: GoPlus, SlowMist, BlockSec.

## Included Files

| File | Content |
|---|---|
| `owner_audit_150.csv` | One row per qualified pool (150 rows): pool and creator address, indicator group (`scam-indicators-only` 128 / `both` 13 / `phishing-stealing-only` 9), the five indicator values, provider attribution (`data_source`), retrieval time, and the raw-response file backing the row |
| `owner_screen_2951.csv` | The full screen: one row per distinct creator address of any flagged pool (2,951 rows), qualified or not -- showing the 150 were not cherry-picked |
| `flagged_pools.csv` | Pool-to-creator mapping for the 3,117 flagged pools (join key) |
| `raw_responses/goplus_address/` | 2,951 cached API responses, one per creator address, retrieved 2026-09-21 (UTC); each file records the query, URL, retrieval time, and the unmodified response body |
| `build_audit_tables.py` | Rebuilds both CSVs from the raw responses and prints the totals (150 / 144 / 128-13-9) so the tables can be independently verified |
| `fetch_goplus_address.py` | The collection script, for provenance (re-running queries the live API, whose answers drift; the cached responses are the reported evidence) |
