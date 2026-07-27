import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_TEX = os.path.join(BASE_DIR, "sns-pyq.tex")
IMAGES_DIR = os.path.join(BASE_DIR, "images")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

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

TAG_URLS = [
    "https://practicepaper.in/tag/basics-of-signals-and-systems",
    "https://practicepaper.in/tag/digital-filters",
    "https://practicepaper.in/tag/dtfs",
    "https://practicepaper.in/tag/dtft-and-dft",
    "https://practicepaper.in/tag/fourier-series",
    "https://practicepaper.in/tag/fourier-transforms",
    "https://practicepaper.in/tag/frequency-response-and-correlation",
    "https://practicepaper.in/tag/laplace-transform",
    "https://practicepaper.in/tag/lti-systems-continuous-and-discrete",
    "https://practicepaper.in/tag/sampling",
    "https://practicepaper.in/tag/z-transform",
]

YEAR_URLS = [
    "https://practicepaper.in/gate-ec/gate-ec-2026",
    "https://practicepaper.in/gate-ec/gate-ec-2025",
    "https://practicepaper.in/gate-ec/gate-ec-2024",
    "https://practicepaper.in/gate-ec/gate-ec-2023",
    "https://practicepaper.in/gate-ec/gate-ec-2022",
    "https://practicepaper.in/gate-ec/gate-ec-2021",
    "https://practicepaper.in/gate-ec/gate-ec-2020",
    "https://practicepaper.in/gate-ec/gate-ec-2019",
    "https://practicepaper.in/gate-ec/gate-ec-2018",
    "https://practicepaper.in/gate-ec/gate-ec-2017-set-1",
    "https://practicepaper.in/gate-ec/gate-ec-2017-set-2",
    "https://practicepaper.in/gate-ec/gate-ec-2016-set-1",
    "https://practicepaper.in/gate-ec/gate-ec-2016-set-2",
    "https://practicepaper.in/gate-ec/gate-ec-2016-set-3",
    "https://practicepaper.in/gate-ec/gate-ec-2015-set-1",
    "https://practicepaper.in/gate-ec/gate-ec-2015-set-2",
    "https://practicepaper.in/gate-ec/gate-ec-2015-set-3",
    "https://practicepaper.in/gate-ec/gate-ec-2014-set-1",
    "https://practicepaper.in/gate-ec/gate-ec-2014-set-2",
    "https://practicepaper.in/gate-ec/gate-ec-2014-set-3",
    "https://practicepaper.in/gate-ec/gate-ec-2014-set-4",
    "https://practicepaper.in/gate-ec/gate-ec-2013",
    "https://practicepaper.in/gate-ec/gate-ec-2012",
    "https://practicepaper.in/gate-ec/gate-ec-2011",
    "https://practicepaper.in/gate-ec/gate-ec-2010",
    "https://practicepaper.in/gate-ec/gate-ec-2009",
    "https://practicepaper.in/gate-ec/gate-ec-2008",
    "https://practicepaper.in/gate-ec/gate-ec-2007",
    "https://practicepaper.in/gate-ec/gate-ec-2006",
    "https://practicepaper.in/gate-ec/gate-ec-2005",
    "https://practicepaper.in/gate-ec/gate-ec-2004",
    "https://practicepaper.in/gate-ec/gate-ec-2003",
    "https://practicepaper.in/gate-ec/gate-ec-2002",
    "https://practicepaper.in/gate-ec/gate-ec-2001",
]

ALL_URLS = list(dict.fromkeys(TOPIC_URLS + TAG_URLS + YEAR_URLS))
