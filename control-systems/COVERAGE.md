# Module 3: Control Systems (`control-systems`) Topic Coverage Map

## 1. Topic Breakdown & Question Distribution (GATE EC 2001–2026)

| Topic | Primary Concepts Covered | Question Count | % of Total |
|---|---|---|---|
| **Basics, Block Diagrams & SFGs** | Block reduction, Mason's gain formula $T = \frac{\sum P_k \Delta_k}{\Delta}$, loop gains, forward paths | 21 | 10.0% |
| **Time Response Analysis** | 1st & 2nd order systems, $\zeta, \omega_n$, $t_r, t_p, M_p, t_s$, steady-state error $e_{ss}$, error constants $K_p, K_v, K_a$ | 39 | 18.6% |
| **Stability & Routh-Hurwitz** | Characteristic equation $1+G(s)H(s)=0$, RH array, auxiliary polynomial $A(s)$, RHP poles count | 27 | 12.9% |
| **Root Locus Technique** | Centroid $\sigma_A$, asymptote angles $\theta_A$, breakaway points $\frac{dK}{ds}=0$, angle of departure/arrival | 19 | 9.0% |
| **Frequency Response Analysis** | Bode magnitude & phase plots, Nyquist stability criterion $N = Z - P$, polar plot, gain & phase margins | 51 | 24.3% |
| **Compensators & Controllers** | P, PI, PD, PID controllers, Lead compensator (phase advance), Lag compensator, Lag-Lead compensator | 19 | 9.0% |
| **State Space Analysis** | State model $\dot{x}=Ax+Bu, y=Cx+Du$, State Transition Matrix $\Phi(t)=e^{At}$, Controllability $Q_c$, Observability $Q_o$ | 34 | 16.2% |
| **Miscellaneous** | Non-minimum phase systems, time delay systems $e^{-sT}$ | 0 | 0.0% |
| **TOTAL** | **Complete GATE EC Control Systems Archive** | **210** | **100%** |

---

## 2. Core Concepts & Essential Formulas

### 1. Block Diagrams & Signal Flow Graphs (SFGs)
- **Mason's Gain Formula:** $T(s) = \frac{1}{\Delta} \sum_{k} P_k \Delta_k$
  - $P_k$: $k$-th forward path gain
  - $\Delta = 1 - \sum L_1 + \sum L_2 - \sum L_3 + \dots$
  - $\Delta_k$: Value of $\Delta$ for that part of the graph not touching the $k$-th forward path

### 2. Time Response Analysis (2nd Order Systems)
- **Standard Transfer Function:** $T(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$
- **Rise Time ($t_r$):** $t_r = \frac{\pi - \beta}{\omega_d}$, where $\omega_d = \omega_n \sqrt{1-\zeta^2}$ and $\beta = \tan^{-1}\left(\frac{\sqrt{1-\zeta^2}}{\zeta}\right)$
- **Peak Time ($t_p$):** $t_p = \frac{\pi}{\omega_d}$
- **Peak Overshoot ($M_p$):** $M_p = e^{-\frac{\pi \zeta}{\sqrt{1-\zeta^2}}} \times 100\%$
- **Settling Time ($t_s$):** $t_s = \frac{4}{\zeta \omega_n}$ (2% tolerance band), $t_s = \frac{3}{\zeta \omega_n}$ (5% tolerance band)
- **Steady-State Error ($e_{ss}$):** $e_{ss} = \lim_{s \to 0} \frac{s R(s)}{1 + G(s)H(s)}$
  - Step Input: $e_{ss} = \frac{1}{1 + K_p}$, $K_p = \lim_{s \to 0} G(s)H(s)$
  - Ramp Input: $e_{ss} = \frac{1}{K_v}$, $K_v = \lim_{s \to 0} s G(s)H(s)$
  - Parabolic Input: $e_{ss} = \frac{1}{K_a}$, $K_a = \lim_{s \to 0} s^2 G(s)H(s)$

### 3. Stability & Routh-Hurwitz Criterion
- **Characteristic Equation:** $a_n s^n + a_{n-1} s^{n-1} + \dots + a_1 s + a_0 = 0$
- **Routh-Hurwitz Rule:** Number of sign changes in 1st column of RH array = Number of RHP (unstable) poles.
- **Row of Zeros:** Indicates symmetric poles ($\pm \sigma$, $\pm j\omega$). Form auxiliary polynomial $A(s)$ from preceding row and replace row of zeros with $\frac{dA(s)}{ds}$.

### 4. Root Locus Technique
- **Angle Condition:** $\angle G(s)H(s) = \pm (2k+1) 180^\circ$
- **Magnitude Condition:** $|G(s)H(s)| = 1 \implies K = \frac{1}{|G(s)H(s)|}$
- **Asymptote Centroid:** $\sigma_A = \frac{\sum \text{Poles} - \sum \text{Zeros}}{P - Z}$
- **Asymptote Angles:** \theta_A = \frac{(2k+1)180^\circ}{P - Z}$
- **Breakaway Points:** Solutions to $\frac{dK}{ds} = 0$ that lie on valid root locus segments.

### 5. Frequency Response & Nyquist Criterion
- **Nyquist Criterion:** $N = Z - P \implies Z = N + P$
  - $N$: Number of counter-clockwise encirclements of $(-1 + j0)$ point
  - $P$: Number of open-loop RHP poles
  - $Z$: Number of closed-loop RHP (unstable) poles (Must be 0 for stability!)
- **Gain Margin (GM):** $GM = \frac{1}{|G(j\omega_{pc})H(j\omega_{pc})|}$, where $\angle G(j\omega_{pc})H(j\omega_{pc}) = -180^\circ$
- **Phase Margin (PM):** $PM = 180^\circ + \angle G(j\omega_{gc})H(j\omega_{gc})$, where $|G(j\omega_{gc})H(j\omega_{gc})| = 1$

### 6. Compensators & Controllers
- **Phase Lead Compensator:** $G_c(s) = \frac{s + 1/T}{s + 1/(\alpha T)}$ with $\alpha < 1$. Maximum phase lead $\phi_m = \sin^{-1}\left(\frac{1-\alpha}{1+\alpha}\right)$ at $\omega_m = \frac{1}{T\sqrt{\alpha}}$.
- **Phase Lag Compensator:** $G_c(s) = \frac{s + 1/T}{s + 1/(\beta T)}$ with $\beta > 1$. Increases low-frequency gain & reduces $e_{ss}$.
- **PID Controller:** $G_c(s) = K_p + \frac{K_i}{s} + K_d s$. Increases stability margin ($K_d$) and eliminates $e_{ss}$ ($K_i$).

### 7. State Space Analysis
- **State Equations:** $\dot{x}(t) = A x(t) + B u(t)$, $y(t) = C x(t) + D u(t)$
- **State Transition Matrix:** $\Phi(t) = e^{At} = \mathcal{L}^{-1}\{(sI - A)^{-1}\}$
  - Properties: $\Phi(0) = I$, $\Phi(-t) = \Phi^{-1}(t)$, $\Phi(t_1 + t_2) = \Phi(t_1)\Phi(t_2)$
- **Controllability Matrix:** $Q_c = \begin{bmatrix} B & AB & A^2 B & \dots & A^{n-1}B \end{bmatrix}$ (Rank $= n$)
- **Observability Matrix:** $Q_o = \begin{bmatrix} C \\ CA \\ CA^2 \\ \vdots \\ CA^{n-1} \end{bmatrix}$ (Rank $= n$)

---

## 3. Corner Cases, Traps & Gotchas

- **Non-Minimum Phase Systems**: Systems with zeros in the Right-Half Plane (RHP). Initial response goes in opposite direction to steady state; phase lag is higher than minimum-phase equivalent.
- **Transport Delay $e^{-sT}$**: Introduces infinite phase lag $\Delta \theta = -\omega T$ without altering magnitude $|e^{-j\omega T}| = 1$. Significantly reduces Phase Margin and compromises stability.
- **Routh-Hurwitz First Column Zero**: If the first element of a row is 0, replace with $\epsilon > 0$ and proceed, taking $\lim_{\epsilon \to 0^+}$.
- **Polar Plot Encirclement vs Touch**: If polar plot passes through $(-1 + j0)$, system is marginally stable (GM $= 0$ dB, PM $= 0^\circ$).

---

## 4. 26-Year Panorama & Exam Pattern Analysis

- **2001–2010**: Focus on signal flow graphs (Mason's rule), second-order transient parameters ($M_p, t_s, \zeta$), and Routh-Hurwitz stability limits.
- **2011–2018**: Increased weight on Bode plots (finding transfer function from asymptotic plot), Nyquist stability encirclement counts, and Lead/Lag compensator maximum phase shift calculations.
- **2019–2026**: Heavy emphasis on State Space Analysis (State Transition Matrix computation, controllability/observability matrices, matrix eigenvalues) and numerical NAT questions on steady-state error & Gain Margin.
