# SIE SKILL.md — Surety Distinction Patch
# Insert this section into SKILL.md under Layer 1A documentation
# Version: v1.7.1 | Erwin Maurice McDonald (2026) | Epoch Frameworks LLC
# ─────────────────────────────────────────────────────────────────────

---

## ⚖️ Signal Certainty Tiers — What SIE Can and Cannot Claim

This is a foundational design principle of the SIE framework. Not all signals carry
equal certainty. SIE separates its confidence claims into two hard tiers based on
the verifiability of the underlying source.

### TIER 1 — HIGH CERTAINTY (Legally Required Public Filings)

These sources are mandatory, timestamped, publicly indexed, and binary.
Their absence is a meaningful, verified signal — not an assumption.

| Source | What Absence Means | Why It's Reliable |
|--------|-------------------|------------------|
| TDLR TABS filing | No asbestos abatement notification filed → no legal demo on pre-1978 structure | Texas law requires this filing BEFORE demolition begins. No exceptions. |
| Fort Worth Accela permit | No demolition permit pulled | City permit system is public and searchable. No permit = no authorized demo. |
| Fort Worth Zoning Commission | Rezoning status is a matter of public record | Zoning cases are publicly voted on and recorded. |
| City Council records | Developer and owner names are public | City Council votes and zoning cases identify parties by name. |

**SIE's primary confidence anchor is always TIER 1.**
When SIE says "authorized demolition has not commenced," it means a TDLR TABS filing
and an Accela demo permit are both absent from public records. That is a legally
grounded claim, not a market observation.

### TIER 2 — LOW CERTAINTY (Informal Markets — Manual Confirmation Required)

These sources are voluntary, anonymous, and cannot be auto-verified by SIE
from public records. Their absence is NOT a verified clean signal — it is
an unchecked assumption until the operator runs the proxy scan manually.

| Source | What Absence Means | Limitation |
|--------|-------------------|-----------|
| Facebook Marketplace | Unknown — scan not run | Listing is voluntary and anonymous. Tenant stripping can occur and be sold privately with no public trace. |
| iScrap App Fort Worth | Unknown — scan not run | Regional board is operator-reported. Not all activity is listed. |
| Google Street View delta | Unknown — visual check not run | Street View lags real-time conditions by weeks or months. |

**CRITICAL RULE:** SIE reports must NEVER imply that Tier 2 sources have been
verified unless the proxy scan has actually been executed. The correct language is:

  ✅ CORRECT: "Proxy scan not yet run — run before acting on this report."
  ❌ WRONG:   "No materials have appeared on Marketplace." (implies verification)
  ❌ WRONG:   "The opportunity is clean." (Tier 1 clean ≠ Tier 2 clean)

### How the Framework Bridges the Gap — The Prior Access Discount (L5)

Because SIE cannot verify Tier 2 sources automatically, the Prior Access Discount
in Layer 5 is the financial mechanism that prices in the uncertainty.

When tenants are being actively relocated:
  - Apply 15–25% reduction to copper and appliance line items
  - This assumes some stripping has already occurred, whether or not it is
    visible on Marketplace or iScrap
  - Running the proxy scan after this report either confirms the discount is
    sufficient OR indicates it should be raised to 30–40%

The Prior Access Discount converts an unverifiable risk into a quantified
financial buffer. This is more defensible than either:
  (a) Ignoring the risk entirely, or
  (b) Claiming the opportunity is clean based on Tier 1 silence alone

### Operator Checklist — Before Bidding

The following proxy scans are MANUAL STEPS the operator must complete
before treating any SIE report as bid-ready:

```
[ ] Facebook Marketplace — target ZIP code, property-specific keywords
    (HVAC, fixtures, doors, windows, copper pipe, appliances)

[ ] iScrap App — regional board for target city, bulk metal listings

[ ] Google Street View delta — compare current vs. 6-month-old imagery
    Look for: dumpsters, contractor vehicles, stripped rooftop HVAC,
    open/missing windows, debris piles

[ ] Adjust L5 Prior Access Discount if any proxy signal found:
    One signal found  → raise discount to 25–35%
    Multiple signals  → raise discount to 35–50%, reconsider YCS
    Active demo signs → escalate to emergency TDLR + Accela check
```

### Summary: The Two-Sentence Version for Any SIE Report

> "SIE's certainty that authorized demolition has not commenced is HIGH —
> it is grounded in the mandatory TDLR TABS filing and Fort Worth Accela
> permit record, both of which are absent as of this run date.
>
> SIE's certainty that no informal stripping or Marketplace activity has
> occurred is LOW — the proxy scan is a manual step the operator must run
> before bidding, and the Prior Access Discount in L5 prices in the risk
> until that scan is complete."

---

# Changelog
# v1.7.1 — Added Signal Certainty Tiers, Tier 1 / Tier 2 distinction,
#           Prior Access Discount surety rationale, operator proxy checklist,
#           and two-sentence summary for all SIE reports.
#           Closes surety gap identified during Spring Hill / Spring Glen POC run.
#           Erwin Maurice McDonald (2026) | Epoch Frameworks LLC
