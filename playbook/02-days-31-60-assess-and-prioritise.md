# Days 31–60: Assess and prioritise

**Goal:** turn what you've heard into an evidence-based picture of the current state, the top risks and the gaps. Deliver visible **quick wins** that build trust.

## Week 5–6: Current-state assessment

Use the [current-state assessment](../templates/current-state-assessment.md) to score maturity across the NIST CSF 2.0 functions (Govern, Identify, Protect, Detect, Respond, Recover). Base every score on **evidence**, not on interviews alone:

| Claim | Evidence to ask for |
|---|---|
| "We have MFA" | Identity provider report: % of users and admins enrolled; legacy authentication blocked? |
| "We patch regularly" | Scanner report: critical vulnerabilities older than 14 days on internet-facing systems |
| "We have backups" | Last restore test record for a Tier 1 system, and achieved restore time |
| "We know our assets" | Asset count from three sources (CMDB, EDR, cloud): do they agree? |
| "We review access" | Last quarterly privileged-access review, with removals |
| "We'd detect an attack" | Who looks at alerts at 3am on a Sunday? Show me the last 5 high-severity alerts and what happened |

Measure a few **baseline metrics** now, so you can show progress later:
- MFA coverage (all users / privileged users)
- Critical vulnerabilities older than the SLA, on internet-facing systems
- Endpoint protection (EDR) coverage
- Tier 1 systems with a restore test in the last 6 months
- Phishing simulation report rate vs click rate
- Critical suppliers assessed in the last 12 months

## Week 6–7: Top risks

Build a first [risk register](../templates/risk-register-starter.csv) with the **top 10 risks** in business language:

> *Because privileged accounts lack phishing-resistant MFA, an attacker could take over an admin account, leading to ransomware across our warehouses and several days of lost shipments.*

For each risk, record a business owner (not you), the likelihood and impact, the current controls, and whether it is within risk appetite. Validate the list with the risk owners. Their agreement matters more than precision.

## Weeks 5–8: Quick wins

Pick **3–5 quick wins** with the [quick-wins tracker](../templates/quick-wins-tracker.md). A good quick win:
- Visibly reduces a top risk
- Costs little and takes less than 4 weeks
- Makes life easier for someone (not only harder)

Typical candidates:

| Quick win | Why it works |
|---|---|
| Enforce MFA for all admins and remote access; block legacy authentication | Removes the most common breach path |
| Run (and fix) a restore test of the most critical system | Turns "we think" into "we know" for ransomware recovery |
| Fix offboarding: leavers' access removed within 24 hours | Common audit finding; easy with HR |
| Put the IR retainer, insurance and contact sheet on one page, and run a 60-minute exec tabletop | Highly visible readiness win for leadership |
| Add a "Report phishing" button, and thank reporters publicly | Positive security culture |
| Publish a short, approved list of AI tools staff *can* use | Turns "no" into "yes, safely" |
| Close the oldest critical external vulnerabilities | Shrinks the attack surface |

## Outputs by day 60

- [ ] Current-state assessment with evidence-based scores
- [ ] Top 10 risks agreed with business owners
- [ ] Baseline metrics captured
- [ ] 3–5 quick wins delivered or well under way, and **communicated**
- [ ] Draft target state: where we need to be in 12–36 months, and why

## Pitfalls

- **Assessing against a framework for its own sake.** The framework is a lens; the business risks are the point.
- **A 200-item gap list.** Nobody can act on it. Prioritise ruthlessly.
- **Quick wins nobody hears about.** Tell people what changed and why it matters.
