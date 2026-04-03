# SIE Framework Reference — v1.7

Complete layer-by-layer documentation for the Salvage Intelligence Engine.
See individual layer files in engine/layers/ for implementation details.

## Version History
- v1.7 — TDLR Watch Protocol (L1A): auto-flags early-stage properties
- v1.6 — Prior Access Discount (L5), Crew Capacity Ceiling (L7),
          SPI Confidence Flag (L3), Bifurcated CPS (L8)

## Core Formula References
- APE = (Relationship×0.35) + (PermitVis×0.25) + (OffMarket×0.25) + (Gatekeeper×0.15)
- Freshness = (Recency×0.40) + (StackDepth×0.30) + (Ownership×0.20) + (Zoning×0.10)
- SPI = (Distress×0.40) + (TimePressure×0.30) + (Condition×0.20) - (Sophistication×0.10)
- Adjusted GMV = Pre-YCS GMV × (YCS / 100)
- Crew-Adjusted GMV = Adjusted GMV × Capacity Factor
- Net Value = Crew-Adjusted GMV - Labor - Haul - Tools - Disposal - MarginBuffer
- Bid Floor = Net Value × 0.60
- Optimal Bid = Net Value × 0.75
- Bid Ceiling = Net Value × 0.88
- APE-Adjusted Ceiling = Bid Ceiling × 0.85  [if APE < 50]
