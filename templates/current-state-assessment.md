# Current-State Assessment

A fast, evidence-based maturity assessment structured around the six NIST CSF 2.0 functions. Plan for 2–3 weeks. Score each area from **0 to 4** and **write down the evidence** behind every score.

| Score | Meaning |
|---|---|
| 0 | Not in place |
| 1 | Ad hoc: depends on individuals, undocumented |
| 2 | Defined: documented, but inconsistent or partial coverage |
| 3 | Managed: consistent, measured, covers critical assets |
| 4 | Optimised: automated, continuously improved, independently verified |

Target scores depend on your risk appetite. **3 is a good target** for most areas in most organisations.

## Assessment

| # | Function | Area | Key questions | Score (0–4) | Evidence | Target | Gap / note |
|---|---|---|---|---|---|---|---|
| 1 | Govern | Strategy, roles and reporting | Is there an approved strategy? Does the board get regular reporting? Are roles clear? | | | | |
| 2 | Govern | Risk management | Is there a risk register with business owners and an agreed appetite? | | | | |
| 3 | Govern | Policies | Are policies current, approved and acknowledged by staff? | | | | |
| 4 | Govern | Supplier risk | Are critical suppliers known, tiered and assessed? Do contracts include security clauses? | | | | |
| 5 | Govern | Legal and regulatory | Are obligations (privacy, sector rules, NIS2/DORA, customer contracts) mapped and owned? | | | | |
| 6 | Identify | Asset inventory | Do CMDB, EDR and cloud inventories agree? Are crown jewels identified? | | | | |
| 7 | Identify | Vulnerability management | Scan coverage? Critical vulnerabilities older than SLA on internet-facing systems? | | | | |
| 8 | Identify | Threat awareness | Do we know which threats target our sector, and use that to prioritise? | | | | |
| 9 | Protect | Identity and MFA | MFA coverage for all users and admins? Phishing-resistant MFA for admins? Legacy authentication blocked? | | | | |
| 10 | Protect | Privileged access | Separate admin accounts? Just-in-time access? Regular reviews? | | | | |
| 11 | Protect | Joiners / movers / leavers | Are leavers' accounts disabled within 24 hours? Evidence? | | | | |
| 12 | Protect | Endpoint and email security | EDR coverage %, email filtering, macro and attachment controls | | | | |
| 13 | Protect | Data protection | Classification, encryption, DLP; where does sensitive data live? | | | | |
| 14 | Protect | Secure development | Code review, pipeline scanning, secrets management, change control | | | | |
| 15 | Protect | Cloud and SaaS configuration | Baselines, posture management, admin controls | | | | |
| 16 | Protect | Awareness and culture | Training completion, phishing report rate, how staff view security | | | | |
| 17 | Detect | Logging and monitoring | Central logging? Who watches alerts out of hours? Mean time to detect? | | | | |
| 18 | Respond | Incident response | Tested plan? IR retainer? Insurance? Exec tabletop in the last 12 months? | | | | |
| 19 | Recover | Backup and recovery | Immutable or offline backups? Last restore test of a Tier 1 system and the time achieved? | | | | |
| 20 | Recover | Business continuity | BIA with RTO/RPO? Continuity plans for critical services? | | | | |

## Summary

| Function | Average score | Target | Biggest gap |
|---|---|---|---|
| Govern | | | |
| Identify | | | |
| Protect | | | |
| Detect | | | |
| Respond | | | |
| Recover | | | |

## Tips

- **Evidence beats interviews.** "We have MFA" isn't evidence; an enrolment report is.
- **Check coverage, not existence.** EDR on 70% of endpoints is a gap, not a tick.
- **Note what's good.** Credit existing strengths in your briefing; it builds trust.
- Map gaps to framework controls later if you need to (see [ciso-toolkit](https://github.com/Cyhelm-Vciso/ciso-toolkit)'s framework-mapper skill).
