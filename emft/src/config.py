import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_TEX = os.path.join(BASE_DIR, "emft-pyq.tex")
IMAGES_DIR = os.path.join(BASE_DIR, "images")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Solved Questions of GATE EC Electromagnetics & Transmission Lines archive
TOPIC_URLS = [
    "https://practicepaper.in/gate-ec/electromagnetics",
    "https://practicepaper.in/gate-ec/basics-of-electromagnetics",
    "https://practicepaper.in/gate-ec/transmission-lines",
    "https://practicepaper.in/gate-ec/uniform-plane-waves",
    "https://practicepaper.in/gate-ec/waveguides",
    "https://practicepaper.in/gate-ec/miscellaneous-topics",
]

ALL_URLS = TOPIC_URLS
