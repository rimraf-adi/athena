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
    print("Generating COVERAGE.md for Control Systems...")
    topic_counts = {
        "Basics, Block Diagrams & SFGs": 0,
        "Time Response Analysis": 0,
        "Stability Analysis & Routh-Hurwitz": 0,
        "Root Locus Technique": 0,
        "Frequency Response Analysis": 0,
        "Compensators & Controllers": 0,
        "State Space Analysis": 0,
        "Miscellaneous & Combined": 0
    }

    for q in questions:
        tags_str = " ".join(q['tags']).lower()
        if "block" in tags_str or "sfg" in tags_str or "mason" in tags_str or "basic" in tags_str:
            topic_counts["Basics, Block Diagrams & SFGs"] += 1
        elif "time" in tags_str or "transient" in tags_str or "steady" in tags_str:
            topic_counts["Time Response Analysis"] += 1
        elif "stability" in tags_str or "routh" in tags_str:
            topic_counts["Stability Analysis & Routh-Hurwitz"] += 1
        elif "root locus" in tags_str:
            topic_counts["Root Locus Technique"] += 1
        elif "frequency" in tags_str or "bode" in tags_str or "nyquist" in tags_str or "polar" in tags_str:
            topic_counts["Frequency Response Analysis"] += 1
        elif "compensator" in tags_str or "controller" in tags_str or "lead" in tags_str or "lag" in tags_str or "pid" in tags_str:
            topic_counts["Compensators & Controllers"] += 1
        elif "state" in tags_str or "space" in tags_str or "controllab" in tags_str:
            topic_counts["State Space Analysis"] += 1
        else:
            topic_counts["Miscellaneous & Combined"] += 1

    total_q = len(questions)
    denom = max(total_q, 1)

    c_bd = topic_counts["Basics, Block Diagrams & SFGs"]
    c_tr = topic_counts["Time Response Analysis"]
    c_st = topic_counts["Stability Analysis & Routh-Hurwitz"]
    c_rl = topic_counts["Root Locus Technique"]
    c_fr = topic_counts["Frequency Response Analysis"]
    c_cc = topic_counts["Compensators & Controllers"]
    c_ss = topic_counts["State Space Analysis"]
    c_ms = topic_counts["Miscellaneous & Combined"]

    p_bd = f"{c_bd / denom * 100:.1f}%"
    p_tr = f"{c_tr / denom * 100:.1f}%"
    p_st = f"{c_st / denom * 100:.1f}%"
    p_rl = f"{c_rl / denom * 100:.1f}%"
    p_fr = f"{c_fr / denom * 100:.1f}%"
    p_cc = f"{c_cc / denom * 100:.1f}%"
    p_ss = f"{c_ss / denom * 100:.1f}%"
    p_ms = f"{c_ms / denom * 100:.1f}%"

    coverage_template = """# Module 3: Control Systems (`control-systems`) Topic Coverage Map

## 1. Topic Breakdown & Question Distribution (GATE EC 2001–2026)

| Topic | Primary Concepts Covered | Question Count | % of Total |
|---|---|---|---|
| **Basics, Block Diagrams & SFGs** | Block reduction, Mason's gain formula $T = \\frac{\\sum P_k \\Delta_k}{\\Delta}$, loop gains, forward paths | __C_BD__ | __P_BD__ |
| **Time Response Analysis** | 1st & 2nd order systems, $\\zeta, \\omega_n$, $t_r, t_p, M_p, t_s$, steady-state error $e_{ss}$, error constants $K_p, K_v, K_a$ | __C_TR__ | __P_TR__ |
| **Stability & Routh-Hurwitz** | Characteristic equation $1+G(s)H(s)=0$, RH array, auxiliary polynomial $A(s)$, RHP poles count | __C_ST__ | __P_ST__ |
| **Root Locus Technique** | Centroid $\\sigma_A$, asymptote angles $\\theta_A$, breakaway points $\\frac{dK}{ds}=0$, angle of departure/arrival | __C_RL__ | __P_RL__ |
| **Frequency Response Analysis** | Bode magnitude & phase plots, Nyquist stability criterion $N = Z - P$, polar plot, gain & phase margins | __C_FR__ | __P_FR__ |
| **Compensators & Controllers** | P, PI, PD, PID controllers, Lead compensator (phase advance), Lag compensator, Lag-Lead compensator | __C_CC__ | __P_CC__ |
| **State Space Analysis** | State model $\\dot{x}=Ax+Bu, y=Cx+Du$, State Transition Matrix $\\Phi(t)=e^{At}$, Controllability $Q_c$, Observability $Q_o$ | __C_SS__ | __P_SS__ |
| **Miscellaneous** | Non-minimum phase systems, time delay systems $e^{-sT}$ | __C_MS__ | __P_MS__ |
| **TOTAL** | **Complete GATE EC Control Systems Archive** | **__TOTAL_Q__** | **100%** |

---

## 2. Core Concepts & Essential Formulas

### 1. Block Diagrams & Signal Flow Graphs (SFGs)
- **Mason's Gain Formula:** $T(s) = \\frac{1}{\\Delta} \\sum_{k} P_k \\Delta_k$
  - $P_k$: $k$-th forward path gain
  - $\\Delta = 1 - \\sum L_1 + \\sum L_2 - \\sum L_3 + \\dots$
  - $\\Delta_k$: Value of $\\Delta$ for that part of the graph not touching the $k$-th forward path

### 2. Time Response Analysis (2nd Order Systems)
- **Standard Transfer Function:** $T(s) = \\frac{\\omega_n^2}{s^2 + 2\\zeta\\omega_n s + \\omega_n^2}$
- **Rise Time ($t_r$):** $t_r = \\frac{\\pi - \\beta}{\\omega_d}$, where $\\omega_d = \\omega_n \\sqrt{1-\\zeta^2}$ and $\\beta = \\tan^{-1}\\left(\\frac{\\sqrt{1-\\zeta^2}}{\\zeta}\\right)$
- **Peak Time ($t_p$):** $t_p = \\frac{\\pi}{\\omega_d}$
- **Peak Overshoot ($M_p$):** $M_p = e^{-\\frac{\\pi \\zeta}{\\sqrt{1-\\zeta^2}}} \\times 100\\%$
- **Settling Time ($t_s$):** $t_s = \\frac{4}{\\zeta \\omega_n}$ (2% tolerance band), $t_s = \\frac{3}{\\zeta \\omega_n}$ (5% tolerance band)
- **Steady-State Error ($e_{ss}$):** $e_{ss} = \\lim_{s \\to 0} \\frac{s R(s)}{1 + G(s)H(s)}$
  - Step Input: $e_{ss} = \\frac{1}{1 + K_p}$, $K_p = \\lim_{s \\to 0} G(s)H(s)$
  - Ramp Input: $e_{ss} = \\frac{1}{K_v}$, $K_v = \\lim_{s \\to 0} s G(s)H(s)$
  - Parabolic Input: $e_{ss} = \\frac{1}{K_a}$, $K_a = \\lim_{s \\to 0} s^2 G(s)H(s)$

### 3. Stability & Routh-Hurwitz Criterion
- **Characteristic Equation:** $a_n s^n + a_{n-1} s^{n-1} + \\dots + a_1 s + a_0 = 0$
- **Routh-Hurwitz Rule:** Number of sign changes in 1st column of RH array = Number of RHP (unstable) poles.
- **Row of Zeros:** Indicates symmetric poles ($\pm \\sigma$, $\pm j\\omega$). Form auxiliary polynomial $A(s)$ from preceding row and replace row of zeros with $\\frac{dA(s)}{ds}$.

### 4. Root Locus Technique
- **Angle Condition:** $\\angle G(s)H(s) = \\pm (2k+1) 180^\\circ$
- **Magnitude Condition:** $|G(s)H(s)| = 1 \\implies K = \\frac{1}{|G(s)H(s)|}$
- **Asymptote Centroid:** $\\sigma_A = \\frac{\\sum \\text{Poles} - \\sum \\text{Zeros}}{P - Z}$
- **Asymptote Angles:** \\theta_A = \\frac{(2k+1)180^\\circ}{P - Z}$
- **Breakaway Points:** Solutions to $\\frac{dK}{ds} = 0$ that lie on valid root locus segments.

### 5. Frequency Response & Nyquist Criterion
- **Nyquist Criterion:** $N = Z - P \\implies Z = N + P$
  - $N$: Number of counter-clockwise encirclements of $(-1 + j0)$ point
  - $P$: Number of open-loop RHP poles
  - $Z$: Number of closed-loop RHP (unstable) poles (Must be 0 for stability!)
- **Gain Margin (GM):** $GM = \\frac{1}{|G(j\\omega_{pc})H(j\\omega_{pc})|}$, where $\\angle G(j\\omega_{pc})H(j\\omega_{pc}) = -180^\\circ$
- **Phase Margin (PM):** $PM = 180^\\circ + \\angle G(j\\omega_{gc})H(j\\omega_{gc})$, where $|G(j\\omega_{gc})H(j\\omega_{gc})| = 1$

### 6. Compensators & Controllers
- **Phase Lead Compensator:** $G_c(s) = \\frac{s + 1/T}{s + 1/(\\alpha T)}$ with $\\alpha < 1$. Maximum phase lead $\\phi_m = \\sin^{-1}\\left(\\frac{1-\\alpha}{1+\\alpha}\\right)$ at $\\omega_m = \\frac{1}{T\\sqrt{\\alpha}}$.
- **Phase Lag Compensator:** $G_c(s) = \\frac{s + 1/T}{s + 1/(\\beta T)}$ with $\\beta > 1$. Increases low-frequency gain & reduces $e_{ss}$.
- **PID Controller:** $G_c(s) = K_p + \\frac{K_i}{s} + K_d s$. Increases stability margin ($K_d$) and eliminates $e_{ss}$ ($K_i$).

### 7. State Space Analysis
- **State Equations:** $\\dot{x}(t) = A x(t) + B u(t)$, $y(t) = C x(t) + D u(t)$
- **State Transition Matrix:** $\\Phi(t) = e^{At} = \\mathcal{L}^{-1}\\{(sI - A)^{-1}\\}$
  - Properties: $\\Phi(0) = I$, $\\Phi(-t) = \\Phi^{-1}(t)$, $\\Phi(t_1 + t_2) = \\Phi(t_1)\\Phi(t_2)$
- **Controllability Matrix:** $Q_c = \\begin{bmatrix} B & AB & A^2 B & \\dots & A^{n-1}B \\end{bmatrix}$ (Rank $= n$)
- **Observability Matrix:** $Q_o = \\begin{bmatrix} C \\\\ CA \\\\ CA^2 \\\\ \\vdots \\\\ CA^{n-1} \\end{bmatrix}$ (Rank $= n$)

---

## 3. Corner Cases, Traps & Gotchas

- **Non-Minimum Phase Systems**: Systems with zeros in the Right-Half Plane (RHP). Initial response goes in opposite direction to steady state; phase lag is higher than minimum-phase equivalent.
- **Transport Delay $e^{-sT}$**: Introduces infinite phase lag $\\Delta \\theta = -\\omega T$ without altering magnitude $|e^{-j\\omega T}| = 1$. Significantly reduces Phase Margin and compromises stability.
- **Routh-Hurwitz First Column Zero**: If the first element of a row is 0, replace with $\\epsilon > 0$ and proceed, taking $\\lim_{\\epsilon \\to 0^+}$.
- **Polar Plot Encirclement vs Touch**: If polar plot passes through $(-1 + j0)$, system is marginally stable (GM $= 0$ dB, PM $= 0^\\circ$).

---

## 4. 26-Year Panorama & Exam Pattern Analysis

- **2001–2010**: Focus on signal flow graphs (Mason's rule), second-order transient parameters ($M_p, t_s, \\zeta$), and Routh-Hurwitz stability limits.
- **2011–2018**: Increased weight on Bode plots (finding transfer function from asymptotic plot), Nyquist stability encirclement counts, and Lead/Lag compensator maximum phase shift calculations.
- **2019–2026**: Heavy emphasis on State Space Analysis (State Transition Matrix computation, controllability/observability matrices, matrix eigenvalues) and numerical NAT questions on steady-state error & Gain Margin.
"""

    coverage_content = coverage_template \
        .replace("__C_BD__", str(c_bd)).replace("__P_BD__", p_bd) \
        .replace("__C_TR__", str(c_tr)).replace("__P_TR__", p_tr) \
        .replace("__C_ST__", str(c_st)).replace("__P_ST__", p_st) \
        .replace("__C_RL__", str(c_rl)).replace("__P_RL__", p_rl) \
        .replace("__C_FR__", str(c_fr)).replace("__P_FR__", p_fr) \
        .replace("__C_CC__", str(c_cc)).replace("__P_CC__", p_cc) \
        .replace("__C_SS__", str(c_ss)).replace("__P_SS__", p_ss) \
        .replace("__C_MS__", str(c_ms)).replace("__P_MS__", p_ms) \
        .replace("__TOTAL_Q__", str(total_q))

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(coverage_content)
    print(f"COVERAGE.md generated at {output_path}")

async def run_pipeline():
    os.makedirs(IMAGES_DIR, exist_ok=True)

    print("Step 1 & 2: Scraping all Control Systems questions and downloading images...")
    questions, image_map = await collect_all_questions()

    raw_output_path = os.path.join(BASE_DIR, "raw_questions.txt")
    append_raw_questions_step1(questions, raw_output_path)

    print("Step 3: Formatting LaTeX document for Control Systems...")
    format_latex_step2(questions, image_map, OUTPUT_TEX)

    print("Step 4: Compiling PDF with pdflatex...")
    try:
        cmd = ["/Library/TeX/texbin/pdflatex", "-interaction=nonstopmode", "cs-pyq.tex"]
        res = subprocess.run(cmd, cwd=BASE_DIR, capture_output=True, text=True)
        if res.returncode == 0:
            print("PDF compiled successfully! Output: cs-pyq.pdf")
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
