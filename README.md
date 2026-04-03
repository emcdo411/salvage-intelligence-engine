# Salvage Intelligence Engine (SIE) v1.7

> **PhD-grade demolition and salvage bid intelligence for DFW and Texas.**
> Coined by Erwin Maurice McDonald (2026) | Epoch Frameworks LLC | DACR License v2.6

---

## What Is This?

SIE is a closed-loop decision advantage system that helps salvage operators identify,
score, and act on pre-demolition opportunities **before they hit the open market.**

It surfaces signals from public records (TDLR, Accela, TCAD, city zoning), scores
opportunity freshness, estimates material yield by structure era, calculates
risk-adjusted bid ranges, and — in v1.7 — automatically flags properties where the
General Contractor has not yet been identified via TDLR TABS filing.

**Built to rival iScrap as a full business intelligence platform for the salvage industry.**

---

## Framework Layers

| Layer | Name | Purpose |
|-------|------|---------|
| L0  | Access Probability Engine (APE) | Can you get this job? |
| L1  | Signal Detection | What public data says |
| L1A | **TDLR Watch Protocol** *(v1.7 NEW)* | GC identified? Flag if not. |
| L2  | Freshness Scoring | How close to actual demo |
| L3  | Seller Pressure Index (SPI) | How motivated is the owner |
| L4  | Structure Profile | What are we dealing with |
| L5  | Yield Estimation + Prior Access Discount | What materials are in this building |
| L6  | Yield Confidence Score (YCS) | How certain is the estimate |
| L7  | Bid Calculus + Crew Capacity Check | Floor / Optimal / Ceiling |
| L8  | Competition Intelligence (Bifurcated CPS) | Who else is circling |
| L9  | Strategic Play Engine | Smartest move, not just correct bid |
| L10 | Final Recommendation | Go / Monitor / Sub-Contract Pursue / Pass |
| L11 | Outcome Loop Preparation | Post-bid calibration hooks |

---

## Key Differentiators vs. iScrap

| Feature | iScrap | SIE |
|---------|--------|-----|
| Live scrap prices | ✅ | ✅ (reference table) |
| Pre-demo signal detection | ❌ | ✅ |
| TDLR / permit monitoring | ❌ | ✅ (L1A Watch) |
| GC identification & contact | ❌ | ✅ |
| Risk-adjusted bid range | ❌ | ✅ |
| Yield by structure era | ❌ | ✅ |
| Crew capacity modeling | ❌ | ✅ |
| Competition intelligence | ❌ | ✅ |
| Sub-contract play detection | ❌ | ✅ |

---

## Roadmap

- [ ] v1.7 — TDLR Watch Protocol (complete)
- [ ] v2.0 — Automated TDLR / Accela polling (scripts/tdlr-watcher)
- [ ] v2.1 — Facebook Marketplace + iScrap proxy signal scraper
- [ ] v2.5 — Plotly BI dashboard (property scoring + bid tracking)
- [ ] v3.0 — Full SaaS application with user accounts and deal pipeline

---

## Author

**Erwin Maurice McDonald**
GitHub: [@emcdo411](https://github.com/emcdo411)
Framework: Epoch Frameworks LLC | DACR License v2.6
Coined: 2026 | Fort Worth / Dallas, TX

---

## License

MIT — See [LICENSE](LICENSE)
