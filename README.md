<div align="center">

# 🏗️ Salvage Intelligence Engine

<img src="https://img.shields.io/badge/version-1.7.0-orange?style=for-the-badge&logo=git&logoColor=white" alt="Version"/>
<img src="https://img.shields.io/badge/status-Active%20Development-brightgreen?style=for-the-badge&logo=statuspage&logoColor=white" alt="Status"/>
<img src="https://img.shields.io/badge/license-MIT-blue?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="License"/>
<img src="https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/Platform-DFW%20%7C%20Texas-red?style=for-the-badge&logo=googlemaps&logoColor=white" alt="Platform"/>

<br/>
<br/>

<img src="https://img.shields.io/badge/Framework-Epoch%20Frameworks%20LLC-black?style=for-the-badge" alt="Epoch Frameworks"/>
<img src="https://img.shields.io/badge/License-DACR%20v2.6-purple?style=for-the-badge" alt="DACR"/>
<img src="https://img.shields.io/badge/Coined%20By-Erwin%20Maurice%20McDonald-gold?style=for-the-badge&logoColor=black" alt="Author"/>

<br/>
<br/>

> **PhD-grade demolition and salvage bid intelligence for DFW and Texas.**
> Coined by Erwin Maurice McDonald (2026) | Epoch Frameworks LLC | DACR License v2.6

<br/>

[![CI](https://img.shields.io/github/actions/workflow/status/emcdo411/salvage-intelligence-engine/ci.yml?branch=main&label=CI&style=flat-square&logo=githubactions&logoColor=white)](https://github.com/emcdo411/salvage-intelligence-engine/actions)
[![Last Commit](https://img.shields.io/github/last-commit/emcdo411/salvage-intelligence-engine?style=flat-square&logo=github&logoColor=white)](https://github.com/emcdo411/salvage-intelligence-engine/commits/main)
[![Repo Size](https://img.shields.io/github/repo-size/emcdo411/salvage-intelligence-engine?style=flat-square&logo=github)](https://github.com/emcdo411/salvage-intelligence-engine)
[![Issues](https://img.shields.io/github/issues/emcdo411/salvage-intelligence-engine?style=flat-square&logo=github)](https://github.com/emcdo411/salvage-intelligence-engine/issues)
[![Stars](https://img.shields.io/github/stars/emcdo411/salvage-intelligence-engine?style=flat-square&logo=github)](https://github.com/emcdo411/salvage-intelligence-engine/stargazers)

</div>

---

## 📌 What Is This?

SIE is a **closed-loop decision advantage system** that helps salvage operators identify,
score, and act on pre-demolition opportunities **before they hit the open market.**

It surfaces signals from public records (TDLR, Accela, TCAD, city zoning), scores
opportunity freshness, estimates material yield by structure era, calculates
risk-adjusted bid ranges, and — in v1.7 — automatically flags properties where the
General Contractor has not yet been identified via TDLR TABS filing.

> **Built to rival iScrap as a full business intelligence platform for the salvage industry.**

---

## 🧠 Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-4B8BBE?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

</div>

---

## 🗂️ Framework Layers

| Layer | Name | Purpose |
|:-----:|------|---------|
| `L0`  | Access Probability Engine (APE) | Can you get this job? |
| `L1`  | Signal Detection | What public data says |
| `L1A` | **TDLR Watch Protocol** *(v1.7 NEW)* | GC identified? Flag if not. |
| `L2`  | Freshness Scoring | How close to actual demo |
| `L3`  | Seller Pressure Index (SPI) | How motivated is the owner |
| `L4`  | Structure Profile | What are we dealing with |
| `L5`  | Yield Estimation + Prior Access Discount | What materials are in this building |
| `L6`  | Yield Confidence Score (YCS) | How certain is the estimate |
| `L7`  | Bid Calculus + Crew Capacity Check | Floor / Optimal / Ceiling |
| `L8`  | Competition Intelligence (Bifurcated CPS) | Who else is circling |
| `L9`  | Strategic Play Engine | Smartest move, not just correct bid |
| `L10` | Final Recommendation | Go / Monitor / Sub-Contract Pursue / Pass |
| `L11` | Outcome Loop Preparation | Post-bid calibration hooks |

---

## ⚔️ Key Differentiators vs. iScrap

| Feature | iScrap | SIE |
|---------|:------:|:---:|
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

## 📡 Signal Sources

<div align="center">

![TDLR](https://img.shields.io/badge/TDLR%20TABS-Signal%20★★★★-critical?style=flat-square)
![Accela](https://img.shields.io/badge/Fort%20Worth%20Accela-Signal%20★★★★★-red?style=flat-square)
![TCAD](https://img.shields.io/badge/Tarrant%20CAD-Tax%20%26%20Ownership-orange?style=flat-square)
![Dallas](https://img.shields.io/badge/City%20of%20Dallas-Signal%20★★★★★-red?style=flat-square)
![Marketplace](https://img.shields.io/badge/FB%20Marketplace-Proxy%20Signal-blue?style=flat-square&logo=facebook)
![iScrap](https://img.shields.io/badge/iScrap%20App-DFW%20Board-grey?style=flat-square)

</div>

---

## 🗺️ Roadmap

<div align="center">

![v1.7](https://img.shields.io/badge/v1.7-TDLR%20Watch%20Protocol-success?style=flat-square)
![v2.0](https://img.shields.io/badge/v2.0-Automated%20TDLR%20%2F%20Accela%20Polling-yellow?style=flat-square)
![v2.1](https://img.shields.io/badge/v2.1-Marketplace%20%2F%20iScrap%20Scraper-yellow?style=flat-square)
![v2.5](https://img.shields.io/badge/v2.5-Plotly%20BI%20Dashboard-orange?style=flat-square)
![v3.0](https://img.shields.io/badge/v3.0-Full%20SaaS%20Application-red?style=flat-square)

</div>

- [x] `v1.7` — TDLR Watch Protocol *(complete)*
- [ ] `v2.0` — Automated TDLR / Accela polling (`scripts/tdlr-watcher`)
- [ ] `v2.1` — Facebook Marketplace + iScrap proxy signal scraper
- [ ] `v2.5` — Plotly BI dashboard (property scoring + bid tracking)
- [ ] `v3.0` — Full SaaS application with user accounts and deal pipeline

---

## 📁 Project Structure

```
salvage-intelligence-engine/
├── engine/
│   ├── layers/              # L0–L11 intelligence layers
│   ├── models/              # PropertyData schema
│   └── sie_runner.py        # Orchestrates all layers
├── scripts/
│   ├── tdlr-watcher/        # TDLR TABS automated polling
│   ├── accela-watcher/      # Fort Worth permit monitor
│   └── marketplace-scan/    # FB Marketplace + iScrap proxy
├── data/
│   ├── sample-permits/      # Sample property JSON records
│   └── commodity-prices/    # DFW scrap spot prices
├── dashboard/               # Plotly / Streamlit BI app (v2.5)
├── docs/                    # Framework reference docs
├── tests/                   # Pytest unit + integration tests
└── .github/workflows/       # CI/CD pipeline
```

---

## ⚙️ Quick Start

```bash
# Clone the repo
git clone https://github.com/emcdo411/salvage-intelligence-engine.git
cd salvage-intelligence-engine

# Set up virtual environment
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ -v

# Run TDLR watcher
python scripts/tdlr-watcher/tdlr_watch.py
```

---

## 🧮 Core Formulas

```
APE     = (Relationship×0.35) + (PermitVis×0.25) + (OffMarket×0.25) + (Gatekeeper×0.15)
Fresh   = (Recency×0.40) + (StackDepth×0.30) + (Ownership×0.20) + (Zoning×0.10)
SPI     = (Distress×0.40) + (TimePressure×0.30) + (Condition×0.20) - (Sophistication×0.10)
Adj GMV = Pre-YCS GMV × (YCS / 100)
Net Val = Crew-Adj GMV − Labor − Haul − Tools − Disposal − MarginBuffer
Floor   = Net Value × 0.60
Optimal = Net Value × 0.75
Ceiling = Net Value × 0.88
APE-Adj = Bid Ceiling × 0.85   [if APE < 50]
```

---

## 👤 Author

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-emcdo411-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/emcdo411)
[![Location](https://img.shields.io/badge/Location-Fort%20Worth%20%2F%20Dallas%2C%20TX-red?style=for-the-badge&logo=googlemaps&logoColor=white)](https://github.com/emcdo411)
[![Framework](https://img.shields.io/badge/Epoch%20Frameworks%20LLC-2026-black?style=for-the-badge)](https://github.com/emcdo411)

**Erwin Maurice McDonald** — Coined 2026 | Fort Worth / Dallas, TX

</div>

---

## 📄 License

<div align="center">

[![MIT License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)
[![DACR](https://img.shields.io/badge/DACR%20License-v2.6-purple?style=for-the-badge)](LICENSE)

</div>

MIT — See [LICENSE](LICENSE)

---

<div align="center">

*Built with 🔩 by Erwin Maurice McDonald | Epoch Frameworks LLC | Fort Worth, TX*

</div>
