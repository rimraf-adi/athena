import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_TEX = os.path.join(BASE_DIR, "sns-pyq.tex")
IMAGES_DIR = os.path.join(BASE_DIR, "images")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 238 Questions of GATE EC Signals and Systems archive
TOPIC_URLS = [
    "https://practicepaper.in/gate-ec/signals-and-systems",
    "https://practicepaper.in/gate-ec/basics-of-signals-and-systems",
    "https://practicepaper.in/gate-ec/digital-filters",
    "https://practicepaper.in/gate-ec/dtfs-dtft-and-dft",
    "https://practicepaper.in/gate-ec/fourier-transforms-frequency-response-and-correlation",
    "https://practicepaper.in/gate-ec/lti-systems-continuous-and-discrete",
    "https://practicepaper.in/gate-ec/sampling",
    "https://practicepaper.in/gate-ec/laplace-transform",
    "https://practicepaper.in/gate-ec/z-transform",
    "https://practicepaper.in/gate-ec/fourier-series",
]

ALL_URLS = TOPIC_URLS
