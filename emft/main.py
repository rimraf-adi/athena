import asyncio
import os
import sys
import subprocess

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
if MODULE_DIR not in sys.path:
    sys.path.insert(0, MODULE_DIR)

from src.config import OUTPUT_TEX, IMAGES_DIR, BASE_DIR
from src.parser import collect_all_questions
from src.formatter import append_raw_questions_step1, format_latex_step2

def generate_coverage_md(questions, output_path):
    print("Generating COVERAGE.md for EMFT...")
    topic_counts = {
        "Basics of Electromagnetics & Maxwell's Equations": 0,
        "Uniform Plane Waves": 0,
        "Transmission Lines": 0,
        "Waveguides & Optical Fibers": 0,
        "Antennas & Radiating Systems": 0,
        "Miscellaneous & Combined": 0
    }

    for q in questions:
        tags_str = " ".join(q['tags']).lower()
        if "basic" in tags_str or "maxwell" in tags_str or "electrostatic" in tags_str or "magnetostatic" in tags_str:
            topic_counts["Basics of Electromagnetics & Maxwell's Equations"] += 1
        elif "transmission" in tags_str or "smith" in tags_str:
            topic_counts["Transmission Lines"] += 1
        elif "uniform" in tags_str or "plane wave" in tags_str or "propagation" in tags_str:
            topic_counts["Uniform Plane Waves"] += 1
        elif "waveguide" in tags_str or "mode" in tags_str or "fiber" in tags_str:
            topic_counts["Waveguides & Optical Fibers"] += 1
        elif "antenna" in tags_str or "radiation" in tags_str or "dipole" in tags_str:
            topic_counts["Antennas & Radiating Systems"] += 1
        else:
            topic_counts["Miscellaneous & Combined"] += 1

    total_q = len(questions)
    denom = max(total_q, 1)

    c_bm = topic_counts["Basics of Electromagnetics & Maxwell's Equations"]
    c_pw = topic_counts["Uniform Plane Waves"]
    c_tl = topic_counts["Transmission Lines"]
    c_wg = topic_counts["Waveguides & Optical Fibers"]
    c_an = topic_counts["Antennas & Radiating Systems"]
    c_ms = topic_counts["Miscellaneous & Combined"]

    p_bm = f"{c_bm / denom * 100:.1f}%"
    p_pw = f"{c_pw / denom * 100:.1f}%"
    p_tl = f"{c_tl / denom * 100:.1f}%"
    p_wg = f"{c_wg / denom * 100:.1f}%"
    p_an = f"{c_an / denom * 100:.1f}%"
    p_ms = f"{c_ms / denom * 100:.1f}%"

    coverage_template = """# Module 2: Electromagnetics & Transmission Lines (`emft`) Topic Coverage Map

## 1. Topic Breakdown & Question Distribution (GATE EC 2001–2026)

| Topic | Primary Concepts Covered | Question Count | % of Total |
|---|---|---|---|
| **Basics & Maxwell's Eqns** | Vector calculus, Coulomb/Gauss/Ampère laws, boundary conditions, displacement current | __C_BM__ | __P_BM__ |
| **Uniform Plane Waves** | Wave equations, intrinsic impedance $\\eta$, polarization, Poynting vector, Snell's law | __C_PW__ | __P_PW__ |
| **Transmission Lines** | Characteristic impedance $Z_0$, reflection coefficient $\\Gamma$, VSWR, stub matching, Smith chart | __C_TL__ | __P_TL__ |
| **Waveguides & Fibers** | Rectangular waveguides, TE/TM mode cutoff $f_c$, phase & group velocity ($v_p, v_g$), optical fiber NA | __C_WG__ | __P_WG__ |
| **Antennas & Radiation** | Hertzian dipole, half-wave dipole, quarter-wave monopole, gain, directivity, Friis equation, array factor | __C_AN__ | __P_AN__ |
| **Miscellaneous** | Combined EM problems, shielding, boundary conditions | __C_MS__ | __P_MS__ |
| **TOTAL** | **Complete GATE EC EMFT Archive** | **__TOTAL_Q__** | **100%** |

---

## 2. Core Concepts & Essential Formulas

### Maxwell's Equations (Differential & Integral Form)
- **Gauss's Law (Electrostatics):** $\\nabla \\cdot \\vec{D} = \\rho_v \\iff \\oint \\vec{D} \\cdot d\\vec{S} = Q_{\\text{encl}}$
- **Gauss's Law (Magnetostatics):** $\\nabla \\cdot \\vec{B} = 0 \\iff \\oint \\vec{B} \\cdot d\\vec{S} = 0$ (No magnetic monopoles)
- **Faraday's Law:** $\\nabla \\times \\vec{E} = -\\frac{\\partial \\vec{B}}{\\partial t}$
- **Ampère-Maxwell Law:** $\\nabla \\times \\vec{H} = \\vec{J} + \\frac{\\partial \\vec{D}}{\\partial t}$ (Displacement current density $\\vec{J}_d = \\frac{\\partial \\vec{D}}{\\partial t}$)

### Boundary Conditions
- $E_{t1} = E_{t2} \\implies (\\vec{E}_1 - \\vec{E}_2) \\times \\hat{n}_{12} = 0$
- $H_{t1} - H_{t2} = K_s \\implies \\hat{n}_{12} \\times (\\vec{H}_1 - \\vec{H}_2) = \\vec{K}_s$ (If perfect conductor, $H_t = K_s$)
- $D_{n1} - D_{n2} = \\rho_s \\implies (\\vec{D}_1 - \\vec{D}_2) \\cdot \\hat{n}_{12} = \\rho_s$
- $B_{n1} = B_{n2} \\implies (\\vec{B}_1 - \\vec{B}_2) \\cdot \\hat{n}_{12} = 0$

### Uniform Plane Waves & Polarization
- **Propagation Constant:** $\\gamma = \\alpha + j\\beta = \\sqrt{j\\omega\\mu(\\sigma + j\\omega\\epsilon)}$
- **Intrinsic Impedance:** $\\eta = \\sqrt{\\frac{j\\omega\\mu}{\\sigma + j\\omega\\epsilon}} \\xrightarrow{\\text{lossless}} \\sqrt{\\frac{\\mu}{\\epsilon}}$ (Free space: $\\eta_0 \\approx 120\\pi \\approx 377 \\; \\Omega$)
- **Phase Velocity & Group Velocity:** $v_p = \\frac{\\omega}{\\beta}$, $v_g = \\frac{d\\omega}{d\\beta}$, $v_p \\cdot v_g = c^2$ (in lossless dispersionless media)
- **Poynting Vector:** $\\vec{S} = \\vec{E} \\times \\vec{H}$ (Average power density $\\langle \\vec{S} \\rangle = \\frac{1}{2} \\text{Re}\\{\\vec{E} \\times \\vec{H}^*\\}$)
- **Polarization Condition:** 
  - Linear: Equal/zero phase difference or one component zero
  - Circular: $E_x = E_y$ and $\\Delta \\phi = \\pm 90^\\circ$
  - Elliptical: General case ($E_x \\neq E_y$ or $\\Delta \\phi \\neq 90^\\circ$)

### Transmission Lines
- **Characteristic Impedance:** $Z_0 = \\sqrt{\\frac{R + j\\omega L}{G + j\\omega C}} \\xrightarrow{\\text{lossless}} \\sqrt{\\frac{L}{C}}$
- **Reflection Coefficient:** $\\Gamma = \\frac{Z_L - Z_0}{Z_L + Z_0} = |\\Gamma| e^{j\\theta}$
- **Voltage Standing Wave Ratio (VSWR):** $S = \\frac{1 + |\\Gamma|}{1 - |\\Gamma|} \\implies |\\Gamma| = \\frac{S - 1}{S + 1}$
- **Input Impedance:** $Z_{\\text{in}}(l) = Z_0 \\frac{Z_L + j Z_0 \\tan(\\beta l)}{Z_0 + j Z_L \\tan(\\beta l)}$
  - Quarter-Wave Transformer ($l = \\lambda/4$): $Z_{\\text{in}} = \\frac{Z_0^2}{Z_L}$
  - Half-Wave Line ($l = \\lambda/2$): $Z_{\\text{in}} = Z_L$

### Waveguides
- **Cutoff Frequency (Rectangular TE$_{mn}$ / TM$_{mn}$):** $f_c = \\frac{c}{2} \\sqrt{\\left(\\frac{m}{a}\\right)^2 + \\left(\\frac{n}{b}\\right)^2}$
- **Dominant Mode (for $a > b$):** TE$_{10}$ mode with $f_{c10} = \\frac{c}{2a}$
- **Guide Wavelength:** $\\lambda_g = \\frac{\\lambda_0}{\\sqrt{1 - (f_c/f)^2}}$
- **Phase & Group Velocities:** $v_p = \\frac{c}{\\sqrt{1 - (f_c/f)^2}} > c$, $v_g = c \\sqrt{1 - (f_c/f)^2} < c$

### Antennas
- **Radiation Resistance ($R_{rad}$):** Half-wave dipole ($l = \\lambda/2$): $R_{rad} \\approx 73 \\; \\Omega$; Hertzian dipole ($dl \\ll \\lambda$): $R_{rad} = 80\\pi^2 \\left(\\frac{dl}{\\lambda}\\right)^2 \\; \\Omega$
- **Directivity ($D$) & Gain ($G$):** $D = \\frac{4\\pi U_{\\max}}{P_{\\text{rad}}}$, $G = \\eta_{\\text{antenna}} \\cdot D$
- **Friis Transmission Equation:** $\\frac{P_r}{P_t} = G_t G_r \\left(\\frac{\\lambda}{4\\pi R}\\right)^2$

---

## 3. Corner Cases, Traps & Gotchas

- **Phase velocity $v_p > c$ trap**: In waveguides, $v_p > c$ does NOT violate relativity because information travels at group velocity $v_g = c^2 / v_p < c$.
- **Intrinsic vs Wave Impedance**: Intrinsic impedance $\\eta = \\sqrt{\\mu/\\epsilon}$ is a medium property. Wave impedance $Z_{\\text{wave}} = \\eta / \\sqrt{1 - (f_c/f)^2}$ for TE modes depends on frequency and mode.
- **Short-circuited vs Open-circuited stub**: A short stub ($Z_L = 0$) gives $Z_{\\text{in}} = j Z_0 \\tan(\\beta l)$ (inductive for $l < \\lambda/4$), open stub ($Z_L = \\infty$) gives $Z_{\\text{in}} = -j Z_0 \\cot(\\beta l)$.
- **Displacement Current in Conductor vs Dielectric**: Ratio $\\frac{J_c}{J_d} = \\frac{\\sigma}{\\omega \\epsilon}$. Good conductor if $\\sigma \\gg \\omega\\epsilon$, good dielectric if $\\sigma \\ll \\omega\\epsilon$.
- **TM$_{10}$ and TM$_{01}$ modes DO NOT exist** in rectangular waveguides ($m, n \\ge 1$ required for TM modes). TE$_{10}$ is the lowest mode when $a > b$.

---

## 4. 26-Year Panorama & Exam Pattern Analysis

- **2001–2010**: Heavy focus on transmission line input impedance, quarter-wave transformers, and electrostatics (Gauss's law, spherical/cylindrical charge distribution).
- **2011–2018**: Focus shifted toward wave polarization identification (linear vs circular/elliptical), wave impedance, Poynting vector calculations, and rectangular waveguide TE10 mode cutoff frequencies.
- **2019–2026**: High proportion of numerical answer type (NAT) questions on VSWR, Smith chart reflection coefficients, Friis transmission formula, and optical fiber acceptance angle / numerical aperture.
"""

    coverage_content = coverage_template \
        .replace("__C_BM__", str(c_bm)).replace("__P_BM__", p_bm) \
        .replace("__C_PW__", str(c_pw)).replace("__P_PW__", p_pw) \
        .replace("__C_TL__", str(c_tl)).replace("__P_TL__", p_tl) \
        .replace("__C_WG__", str(c_wg)).replace("__P_WG__", p_wg) \
        .replace("__C_AN__", str(c_an)).replace("__P_AN__", p_an) \
        .replace("__C_MS__", str(c_ms)).replace("__P_MS__", p_ms) \
        .replace("__TOTAL_Q__", str(total_q))

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(coverage_content)
    print(f"COVERAGE.md generated at {output_path}")

async def run_pipeline():
    os.makedirs(IMAGES_DIR, exist_ok=True)

    print("Step 1 & 2: Scraping all EMFT questions and downloading images...")
    questions, image_map = await collect_all_questions()

    raw_output_path = os.path.join(BASE_DIR, "raw_questions.txt")
    append_raw_questions_step1(questions, raw_output_path)

    print("Step 3: Formatting LaTeX document for EMFT...")
    format_latex_step2(questions, image_map, OUTPUT_TEX)

    print("Step 4: Compiling PDF with pdflatex...")
    try:
        cmd = ["/Library/TeX/texbin/pdflatex", "-interaction=nonstopmode", "emft-pyq.tex"]
        res = subprocess.run(cmd, cwd=BASE_DIR, capture_output=True, text=True)
        if res.returncode == 0:
            print("PDF compiled successfully! Output: emft-pyq.pdf")
        else:
            print("pdflatex completed with warnings/errors. Running second pass...")
            subprocess.run(cmd, cwd=BASE_DIR, capture_output=True, text=True)
            print("Second pass complete.")
    except Exception as e:
        print(f"Error running pdflatex: {e}")

    coverage_path = os.path.join(BASE_DIR, "COVERAGE.md")
    generate_coverage_md(questions, coverage_path)

def main():
    asyncio.run(run_pipeline())

if __name__ == "__main__":
    main()
