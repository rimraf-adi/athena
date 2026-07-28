import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_TEX = os.path.join(BASE_DIR, "cs-pyq.tex")
IMAGES_DIR = os.path.join(BASE_DIR, "images")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Target URLs of GATE EC Control Systems archive on practicepaper.in
TOPIC_URLS = [
    "https://practicepaper.in/gate-ec/control-systems",
    "https://practicepaper.in/gate-ec/basics-of-control-systems-block-diagram-and-sfgs",
    "https://practicepaper.in/gate-ec/time-response-analysis",
    "https://practicepaper.in/gate-ec/stability-analysis",
    "https://practicepaper.in/gate-ec/root-locus",
    "https://practicepaper.in/gate-ec/frequency-response-analysis",
    "https://practicepaper.in/gate-ec/compensators-and-controllers",
    "https://practicepaper.in/gate-ec/state-space-analysis",
]

ALL_URLS = TOPIC_URLS
