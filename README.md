# Athena: GATE EC Previous Year Questions Archive & Pipeline

A modular engine for scraping, parsing, formatting, and compiling GATE Electronics & Communication Engineering (EC) Previous Year Solved Questions into publication-ready LaTeX documents and PDFs.

---

## 📁 Repository Architecture

The project is organized into modular directories per subject/chapter to support scalable expansion across the entire GATE EC syllabus:

```text
athena/
├── README.md
├── pyproject.toml
├── uv.lock
├── .gitignore
└── sns/                        # Signals & Systems Module
    ├── main.py                 # Pipeline runner for Signals & Systems
    ├── sns-pyq.tex             # Complete LaTeX source (238 questions)
    ├── sns-pyq.pdf             # Compiled PDF document
    ├── COVERAGE.md             # 26-year topic, technique & corner-case map
    ├── images/                 # Downloaded question diagrams and schematics
    └── src/
        ├── config.py           # Configuration & topic URL targets
        ├── parser.py           # HTML scraping & question parser
        ├── converter.py        # HTML-to-LaTeX equation converter
        ├── downloader.py      # Async image downloader
        └── formatter.py        # Document generator & TOC formatter
```

---

## 📡 Module 1: Signals & Systems (`sns`)

### Overview
- **Questions Covered:** 238 Solved Questions (GATE EC 2001–2026)
- **Document Output:** [`sns/sns-pyq.pdf`](sns/sns-pyq.pdf) (~200 pages)
- **LaTeX Source:** [`sns/sns-pyq.tex`](sns/sns-pyq.tex)
- **Topic Coverage Map:** [`sns/COVERAGE.md`](sns/COVERAGE.md)

### Topics Included
1. **Basics of Signals & Systems** (Classification, Energy/Power, Periodicity, Systems Properties)
2. **LTI Systems** (Continuous & Discrete, Convolution, Stability & Causality, Eigenfunctions)
3. **Fourier Series** (Trigonometric & Exponential, Symmetry Properties, Parseval's Theorem)
4. **Fourier Transforms** (Properties, Group & Phase Delay, Energy Spectral Density, Modulation)
5. **Laplace Transform** (Bilateral/Unilateral, ROC Analysis, Initial & Final Value Theorems)
6. **Z-Transform** (ROC, Stability, All-pass Systems, Difference Equations)
7. **Sampling Theorem** (Nyquist Rate, Aliasing, Sinc Reconstruction, Bandpass Sampling)
8. **DTFS, DTFT & DFT** (Circular Convolution, FFT Algorithms, Spectral Analysis)
9. **Digital Filters** (FIR/IIR Filter Design, Impulse Invariance, Linear Phase Filters)

---

## 🚀 Running the Pipeline

### Prerequisites
- Python 3.12+
- [`uv`](https://github.com/astral-sh/uv) package manager
- `pdflatex` (TeX Live / MacTeX)

### Execution

1. **Install dependencies:**
   ```bash
   uv sync
   ```

2. **Run Signals & Systems Pipeline:**
   ```bash
   python3 sns/main.py
   ```

This will automatically scrape missing questions, download inline diagrams to `sns/images/`, construct `sns/sns-pyq.tex`, and run a 2-pass `pdflatex` compilation to produce `sns/sns-pyq.pdf`.

---

## 📡 Module 2: Electromagnetics & Transmission Lines (`emft`)

### Overview
- **Questions Covered:** 202 Solved Questions (GATE EC 2001–2026)
- **Document Output:** [`emft/emft-pyq.pdf`](emft/emft-pyq.pdf) (~177 pages)
- **LaTeX Source:** [`emft/emft-pyq.tex`](emft/emft-pyq.tex)
- **Topic Coverage Map:** [`emft/COVERAGE.md`](emft/COVERAGE.md)

### Topics Included
1. **Basics of Electromagnetics & Maxwell's Equations**
2. **Uniform Plane Waves & Polarization**
3. **Transmission Lines & Impedance Matching**
4. **Waveguides & Optical Fibers**
5. **Antennas & Radiating Systems**

---

## 🎛️ Module 3: Control Systems (`control-systems`)

### Overview
- **Questions Covered:** 210 Solved Questions (GATE EC 2001–2026)
- **Document Output:** [`control-systems/cs-pyq.pdf`](control-systems/cs-pyq.pdf) (~214 pages)
- **LaTeX Source:** [`control-systems/cs-pyq.tex`](control-systems/cs-pyq.tex)
- **Topic Coverage Map:** [`control-systems/COVERAGE.md`](control-systems/COVERAGE.md)

### Topics Included
1. **Basics, Block Diagrams & Signal Flow Graphs (SFGs)**
2. **Time Response Analysis**
3. **Stability Analysis & Routh-Hurwitz**
4. **Root Locus Technique**
5. **Frequency Response Analysis (Bode & Nyquist Plots)**
6. **Compensators & Controllers**
7. **State Space Analysis**

---

## 🔮 Future Modules (Upcoming)

- `analog/` — Analog Circuits & Electronics
- `digital/` — Digital Circuits
- `communications/` — Analog & Digital Communications

