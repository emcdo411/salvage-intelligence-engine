"""
Proxy Signal Scanner — Facebook Marketplace + iScrap keyword monitor.
Watches for tenant-stripped materials appearing in target zip codes.

Erwin Maurice McDonald (2026) | Epoch Frameworks LLC
"""

WATCH_ZIPS   = ["76107"]
WATCH_KEYWORDS = [
    "Spring Hill", "Spring Glen", "Hamilton Ave", "Saint Juliet",
    "HVAC", "appliances", "doors", "windows", "fixtures", "copper pipe"
]

# TODO: Implement with Playwright (Facebook) and requests (iScrap public board)
# Signal: any listing matching keyword + zip = demo is 30-60 days out
# Trigger: flag to console + optional SMS/email alert

def scan():
    print("Marketplace proxy scan not yet implemented.")
    print("See docs/TDLR-Watch-Protocol.md for manual scan instructions.")

if __name__ == "__main__":
    scan()
