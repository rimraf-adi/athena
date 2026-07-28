# Module 2: Electromagnetics & Transmission Lines (`emft`) Topic Coverage Map

## 1. Topic Breakdown & Question Distribution (GATE EC 2001–2026)

| Topic | Primary Concepts Covered | Question Count | % of Total |
|---|---|---|---|
| **Basics & Maxwell's Eqns** | Vector calculus, Coulomb/Gauss/Ampère laws, boundary conditions, displacement current | 40 | 19.8% |
| **Uniform Plane Waves** | Wave equations, intrinsic impedance $\eta$, polarization, Poynting vector, Snell's law | 45 | 22.3% |
| **Transmission Lines** | Characteristic impedance $Z_0$, reflection coefficient $\Gamma$, VSWR, stub matching, Smith chart | 51 | 25.2% |
| **Waveguides & Fibers** | Rectangular waveguides, TE/TM mode cutoff $f_c$, phase & group velocity ($v_p, v_g$), optical fiber NA | 28 | 13.9% |
| **Antennas & Radiation** | Hertzian dipole, half-wave dipole, quarter-wave monopole, gain, directivity, Friis equation, array factor | 27 | 13.4% |
| **Miscellaneous** | Combined EM problems, shielding, boundary conditions | 11 | 5.4% |
| **TOTAL** | **Complete GATE EC EMFT Archive** | **202** | **100%** |

---

## 2. Core Concepts & Essential Formulas

### Maxwell's Equations (Differential & Integral Form)
- **Gauss's Law (Electrostatics):** $\nabla \cdot \vec{D} = \rho_v \iff \oint \vec{D} \cdot d\vec{S} = Q_{\text{encl}}$
- **Gauss's Law (Magnetostatics):** $\nabla \cdot \vec{B} = 0 \iff \oint \vec{B} \cdot d\vec{S} = 0$ (No magnetic monopoles)
- **Faraday's Law:** $\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$
- **Ampère-Maxwell Law:** $\nabla \times \vec{H} = \vec{J} + \frac{\partial \vec{D}}{\partial t}$ (Displacement current density $\vec{J}_d = \frac{\partial \vec{D}}{\partial t}$)

### Boundary Conditions
- $E_{t1} = E_{t2} \implies (\vec{E}_1 - \vec{E}_2) \times \hat{n}_{12} = 0$
- $H_{t1} - H_{t2} = K_s \implies \hat{n}_{12} \times (\vec{H}_1 - \vec{H}_2) = \vec{K}_s$ (If perfect conductor, $H_t = K_s$)
- $D_{n1} - D_{n2} = \rho_s \implies (\vec{D}_1 - \vec{D}_2) \cdot \hat{n}_{12} = \rho_s$
- $B_{n1} = B_{n2} \implies (\vec{B}_1 - \vec{B}_2) \cdot \hat{n}_{12} = 0$

### Uniform Plane Waves & Polarization
- **Propagation Constant:** $\gamma = \alpha + j\beta = \sqrt{j\omega\mu(\sigma + j\omega\epsilon)}$
- **Intrinsic Impedance:** $\eta = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\epsilon}} \xrightarrow{\text{lossless}} \sqrt{\frac{\mu}{\epsilon}}$ (Free space: $\eta_0 \approx 120\pi \approx 377 \; \Omega$)
- **Phase Velocity & Group Velocity:** $v_p = \frac{\omega}{\beta}$, $v_g = \frac{d\omega}{d\beta}$, $v_p \cdot v_g = c^2$ (in lossless dispersionless media)
- **Poynting Vector:** $\vec{S} = \vec{E} \times \vec{H}$ (Average power density $\langle \vec{S} \rangle = \frac{1}{2} \text{Re}\{\vec{E} \times \vec{H}^*\}$)
- **Polarization Condition:** 
  - Linear: Equal/zero phase difference or one component zero
  - Circular: $E_x = E_y$ and $\Delta \phi = \pm 90^\circ$
  - Elliptical: General case ($E_x \neq E_y$ or $\Delta \phi \neq 90^\circ$)

### Transmission Lines
- **Characteristic Impedance:** $Z_0 = \sqrt{\frac{R + j\omega L}{G + j\omega C}} \xrightarrow{\text{lossless}} \sqrt{\frac{L}{C}}$
- **Reflection Coefficient:** $\Gamma = \frac{Z_L - Z_0}{Z_L + Z_0} = |\Gamma| e^{j\theta}$
- **Voltage Standing Wave Ratio (VSWR):** $S = \frac{1 + |\Gamma|}{1 - |\Gamma|} \implies |\Gamma| = \frac{S - 1}{S + 1}$
- **Input Impedance:** $Z_{\text{in}}(l) = Z_0 \frac{Z_L + j Z_0 \tan(\beta l)}{Z_0 + j Z_L \tan(\beta l)}$
  - Quarter-Wave Transformer ($l = \lambda/4$): $Z_{\text{in}} = \frac{Z_0^2}{Z_L}$
  - Half-Wave Line ($l = \lambda/2$): $Z_{\text{in}} = Z_L$

### Waveguides
- **Cutoff Frequency (Rectangular TE$_{mn}$ / TM$_{mn}$):** $f_c = \frac{c}{2} \sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}$
- **Dominant Mode (for $a > b$):** TE$_{10}$ mode with $f_{c10} = \frac{c}{2a}$
- **Guide Wavelength:** $\lambda_g = \frac{\lambda_0}{\sqrt{1 - (f_c/f)^2}}$
- **Phase & Group Velocities:** $v_p = \frac{c}{\sqrt{1 - (f_c/f)^2}} > c$, $v_g = c \sqrt{1 - (f_c/f)^2} < c$

### Antennas
- **Radiation Resistance ($R_{rad}$):** Half-wave dipole ($l = \lambda/2$): $R_{rad} \approx 73 \; \Omega$; Hertzian dipole ($dl \ll \lambda$): $R_{rad} = 80\pi^2 \left(\frac{dl}{\lambda}\right)^2 \; \Omega$
- **Directivity ($D$) & Gain ($G$):** $D = \frac{4\pi U_{\max}}{P_{\text{rad}}}$, $G = \eta_{\text{antenna}} \cdot D$
- **Friis Transmission Equation:** $\frac{P_r}{P_t} = G_t G_r \left(\frac{\lambda}{4\pi R}\right)^2$

---

## 3. Corner Cases, Traps & Gotchas

- **Phase velocity $v_p > c$ trap**: In waveguides, $v_p > c$ does NOT violate relativity because information travels at group velocity $v_g = c^2 / v_p < c$.
- **Intrinsic vs Wave Impedance**: Intrinsic impedance $\eta = \sqrt{\mu/\epsilon}$ is a medium property. Wave impedance $Z_{\text{wave}} = \eta / \sqrt{1 - (f_c/f)^2}$ for TE modes depends on frequency and mode.
- **Short-circuited vs Open-circuited stub**: A short stub ($Z_L = 0$) gives $Z_{\text{in}} = j Z_0 \tan(\beta l)$ (inductive for $l < \lambda/4$), open stub ($Z_L = \infty$) gives $Z_{\text{in}} = -j Z_0 \cot(\beta l)$.
- **Displacement Current in Conductor vs Dielectric**: Ratio $\frac{J_c}{J_d} = \frac{\sigma}{\omega \epsilon}$. Good conductor if $\sigma \gg \omega\epsilon$, good dielectric if $\sigma \ll \omega\epsilon$.
- **TM$_{10}$ and TM$_{01}$ modes DO NOT exist** in rectangular waveguides ($m, n \ge 1$ required for TM modes). TE$_{10}$ is the lowest mode when $a > b$.

---

## 4. 26-Year Panorama & Exam Pattern Analysis

- **2001–2010**: Heavy focus on transmission line input impedance, quarter-wave transformers, and electrostatics (Gauss's law, spherical/cylindrical charge distribution).
- **2011–2018**: Focus shifted toward wave polarization identification (linear vs circular/elliptical), wave impedance, Poynting vector calculations, and rectangular waveguide TE10 mode cutoff frequencies.
- **2019–2026**: High proportion of numerical answer type (NAT) questions on VSWR, Smith chart reflection coefficients, Friis transmission formula, and optical fiber acceptance angle / numerical aperture.
