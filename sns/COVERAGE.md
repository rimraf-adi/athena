# GATE EC — Signals & Systems: 26-Year PYQ Coverage Map

> **238 Questions · GATE EC 2001–2026 · Exhaustive topic, technique, and trap summary**

---

## 1. Topics Covered

### 1.1 Basics of Signals & Systems (~30 questions)
- **Signal classification**: continuous vs discrete, periodic vs aperiodic, energy vs power, deterministic vs random, even vs odd
- **Even/odd decomposition**: `x_e(t) = [x(t)+x(-t)]/2`, conjugate symmetric/anti-symmetric decomposition for complex sequences (Q214)
- **Periodicity**: fundamental period of sums of sinusoids via GCD/HCF of frequencies; condition `Ω₀/2π = rational` for discrete-time periodicity; non-periodic examples like `sin(π²n)` (Q139)
- **Standard signals**: `u(t)`, `δ(t)`, `r(t)`, signum, sinc, rect, tri — and their properties (sifting, scaling `δ(at) = δ(t)/|a|`)
- **Energy and power computation**: direct integration, Parseval's shortcut, scaling rule `E[x(at)] = E[x(t)]/|a|`; energy ratio `E[x(t)]/E[3x(-3t+5)]` (Q4); power of sum of sinusoids (Q205)
- **Orthogonality/orthonormality** of signals over an interval; harmonic relationships (Q1)
- **System properties testing**: linearity (superposition), time-invariance (delay-then-process vs process-then-delay), causality (`h(t)=0 for t<0`), BIBO stability (`∫|h(t)|dt < ∞` or `Σ|h[n]| < ∞`)
- **Piecewise-defined systems**: `y(n) = n|x[n]|` for some range, `x(n)-x(n-1)` otherwise (Q69); `y(t) = x(eᵗ)` which is non-causal + time-varying (Q30)
- **Non-linearity from constant bias**: `y = au + b` with `b≠0` breaks linearity (Q56)
- **Signal-spectrum duality table**: continuous-aperiodic ↔ continuous-aperiodic, continuous-periodic ↔ discrete-aperiodic, etc. (Q27, Q202)
- **Sampled signal periodicity**: `T/Tₛ` must be rational for sampled periodic signal to remain periodic (Q86)

### 1.2 LTI Systems — Continuous & Discrete (~35 questions)
- **Impulse response characterisation**: causal ⟺ `h(t)=0` for `t<0`; stable ⟺ absolutely integrable/summable
- **Convolution integral/sum**: analytical computation, graphical flip-and-slide, using delta-function sifting
- **Convolution with shifted impulses**: `x(t)*δ(t-a) = x(t-a)`; tricky variants like `x(-t)*δ(-t-t₀) = x(-t-t₀)` (Q111)
- **Cascade and parallel combinations**: `h = h₁*h₂` for cascade, `h = h₁+h₂` for parallel; computing overall system from block diagrams
- **Eigenfunctions of LTI systems**: `e^{st}` (continuous) and `z^n` (discrete) — `e^{jω₀t}` is eigenfunction, NOT `e^{jω₀t}u(t)` or `cos(ω₀t)` alone (Q87)
- **Frequency response from impulse response**: `H(e^{jω})` evaluation for filter type classification (BPF/LPF/HPF) (Q62, Q70)
- **Sinusoidal steady-state**: LTI system cannot change frequency of a sinusoidal input — used to identify non-LTI systems (Q32)
- **Time scaling of convolution**: `x(at)*h(at)` output is `(1/|a|)·y(at)` where `y=x*h` (Q20)
- **Impulse response from step response**: `h(t) = d/dt[s(t)]`; step response from impulse response via integration (Q95, Q159)
- **Output of max-type system**: `y[n] = max_{k≤n} |x[k]|` has impulse response `u[n]` (Q44)
- **White noise through LTI**: output PSD = `S_x(f)|H(f)|²`; output power via Parseval (Q21)
- **Minimum phase / non-minimum phase / mixed phase**: determined by zero locations relative to unit circle (Q19, Q132)
- **All-pass filters**: zero at `1/pole*` for discrete; constant magnitude response (Q40, Q55, Q125)
- **Non-LTI from bias injection**: system with `bδ[n]` additive constant in feedback is non-linear and time-varying (Q14)

### 1.3 Fourier Series (~15 questions)
- **Trigonometric and exponential** FS representations
- **Coefficient computation**: `aₖ = (1/T)∫x(t)e^{-jkω₀t}dt`
- **Conjugate symmetry**: `c₋ₙ = cₙ*` for real signals (Q226)
- **Half-wave symmetry** `x(t-T/2) = -x(t)` → only odd harmonics survive, all `a_{2m} = 0` (Q5, Q68)
- **Odd symmetry** → `aₙ = 0` (no cosine terms); even symmetry → `bₙ = 0` (no sine terms) (Q158)
- **Parseval's power theorem**: `P = Σ|aₖ|²`; computing average power from known coefficients (Q37)
- **Effect of time scaling on FS**: `f(αt)` has period `T₀/α` but same coefficients `dₖ = cₖ` (Q10, Q65)
- **Periodicity condition for valid FS**: ratio of component periods must be rational; `2cos(πt)+7cos(t)` is NOT periodic since `T₁/T₂ = 1/π` is irrational (Q232)
- **Changing period without changing coefficients**: if `T₀ = 10` is also considered `T' = 40`, then `Σ|bₖ| = Σ|aₖ|` unchanged (Q54)
- **Harmonic power ratio**: ratio of `n`-th to `m`-th harmonic power for square waves (Q130)
- **DC component of waveforms**: from graphical integration of one period (Q167)
- **Non-periodic signal** cannot have Fourier series: `e^{-|t|}sin(25t)` is aperiodic (Q210)

### 1.4 Fourier Transforms — Continuous Time (~45 questions)
- **Standard pairs**: `e^{-at}u(t) ↔ 1/(a+jω)`, rect ↔ sinc, Gaussian `e^{-at²} ↔ √(π/a)·e^{-ω²/4a}`, `t/(1+t²)² ↔ (π/2j)ωe^{-|ω|}` (Q28, Q34)
- **Properties**: linearity, time shift `e^{-jωt₀}`, frequency shift, scaling `x(at) ↔ (1/|a|)X(ω/a)`, differentiation `(-d/ds)`, integration, duality, convolution ↔ multiplication
- **Parseval's theorem**: `∫|x(t)|²dt = (1/2π)∫|X(ω)|²dω` — used to compute energy from spectrum (Q41, Q127)
- **Energy bandwidth**: 99% energy within `B Hz` requires solving `tan⁻¹(πB) = 0.495π` (Q3)
- **Magnitude bound**: `|F(ω)| ≤ ∫|f(t)|dt` always true (triangle inequality); `|F(ω)| ≤ ∫f(t)dt` is NOT always true (Q13)
- **Phase and group delay**: `Tₚ = -θ(ω)/ω`, `Tg = -dθ/dω`; linear phase → `Tₚ = Tg = const` (Q123, Q230); RC-LPF group delay computation (Q221)
- **Hilbert transform**: preserves energy, `∫|y(t)|² = ∫|x(t)|²` (Q53)
- **Modulation (multiplication by cosine)**: `x(t)cos(ω₀t) ↔ ½[X(ω-ω₀)+X(ω+ω₀)]`; energy halves if `ω₀ >> B` (Q29)
- **sinc convolved with sinc**: `sinc*sinc = sinc` because rect × rect = rect in frequency (Q75)
- **LTI filter output**: evaluating `H(ω)` at input frequencies, computing attenuation and phase shifts (Q24, Q60, Q63)
- **Time delay system**: `H(f) = e^{-j2πfτ}` → output is `x(t-τ)` (Q117, Q225)
- **Inverse FT of shifted/scaled transforms**: `X(3f+2)` inverse (Q200); Fourier transform of `x(2(t+1))` (Q211)
- **Integration property**: `∫_{-∞}^{t} g(τ)dτ ↔ G(jω)·[1/jω + πδ(ω)]` (Q136)
- **Area under signal = value of FT at ω=0**: `∫y(t)dt = Y(0)` (Q22, Q97)
- **Convolution of rectangular pulse with cosine²**: predicting output harmonics (Q215)
- **Network output from sinusoidal inputs**: an RLC network is LTI, so output has same frequencies as input but with different magnitudes and phases (Q82)
- **Distortionless transmission**: requires `φ(ω) = kω` (linear phase), magnitude can vary (Q197)

### 1.5 Laplace Transform (~25 questions)
- **Standard pairs and ROC**: right-sided `e^{-at}u(t) ↔ 1/(s+a)` with `Re(s) > -a`; left-sided with `Re(s) < -a`; both-sided (Q98)
- **Initial and final value theorems**: `f(0⁺) = lim_{s→∞} sF(s)`, `f(∞) = lim_{s→0} sF(s)` — FVT valid only if poles of `sF(s)` in LHP (Q156, Q163, Q227)
- **Partial fraction expansion**: systematic decomposition for inverse LT (Q49, Q162)
- **Forced vs natural response**: forced response = steady-state component (Q49)
- **Differential equation to transfer function**: `H(s) = Y(s)/X(s)` with zero ICs; with non-zero ICs using unilateral LT (Q133, Q141)
- **Cascading to make causal**: removing RHP poles by cascading with zero at that location (Q114)
- **ROC of finite-duration signal**: entire s-plane (Q104)
- **Bilateral LT of piecewise constant**: `u(t-a)-u(t-b) ↔ (e^{-as}-e^{-bs})/s` (Q106)
- **Laplace transform of periodic signals**: `F(s) = [1/(1-e^{-sT})]∫₀^T f(t)e^{-st}dt` (Q83)
- **Frequency differentiation**: `L[tf(t)] = -dF(s)/ds` (Q115, Q153)
- **Causal + stable** for CT systems: all poles in LHP; non-causal system CAN be BIBO stable with RHP poles (Q67, Q121, Q144)
- **Neither causal nor stable**: specific ROC selection giving anti-causal, unstable impulse response (Q100)
- **Integrator as H(s)=1/s**: output of integrator for `sin(t)/πt` input as `t→∞` gives `1/2` (Q58)
- **First-order system responses**: impulse, step, ramp responses matched to excitation signals (Q81)
- **Existence condition**: `Re(s) > a+2` for `e^{(a+2)t+5}` (Q204)

### 1.6 Z-Transform (~30 questions)
- **Standard pairs**: `aⁿu[n] ↔ 1/(1-az⁻¹)` with `|z|>|a|`; `−aⁿu[−n−1] ↔ 1/(1-az⁻¹)` with `|z|<|a|` (Q228)
- **ROC**: causal → exterior; anti-causal → interior; two-sided → annular ring (Q72, Q135, Q152, Q208)
- **ROC = empty set**: when right-sided ROC and left-sided ROC don't overlap, e.g. `2^|n|` (Q72)
- **Pole-zero analysis**: stability (poles inside unit circle), causality (ROC exterior including ∞)
- **Inverse Z-transform**: partial fractions, long division/binomial expansion `(1-2z⁻¹)⁻² → 1+4z⁻¹+12z⁻²+...` (Q120)
- **All-pass systems**: zero at `1/pole*`; `P(z) = H(z)H(1/z)` zero symmetry (Q50, Q125)
- **All-pass with poles outside unit circle**: stable only with two-sided impulse response (Q55)
- **Properties of `X(-z)`**: for `x[n] = δ[n-3]+2δ[n-5]` (all odd powers), `Y(z)=X(-z)` ⟹ `y[n]=-x[n]` (Q74)
- **Properties of `X(z⁻¹)`**: `x[-n] ↔ X(z⁻¹)`; if `x[n]=x[-n]` and zero at `z₀`, then zero also at `1/z₀` (Q131)
- **Difference equation → H(z)**: pole locations from characteristic equation (Q108, Q213)
- **Convolution of finite sequences**: using Z-transform multiplication or direct tabular convolution (Q66)
- **Accumulator**: `y[n] = Σₘ₌₀ⁿ x[m]` ↔ `Y(z) = X(z)·z/(z-1)` (Q103)
- **System function from block diagram**: reading SFG or block diagram to write H(z) (Q92, Q155)
- **Discrete-time stability conditions from difference equation coefficients**: `|α| < 2` for `2y[n] = αy[n-2] + ...` (Q213)

### 1.7 Sampling (~18 questions)
- **Nyquist theorem**: `fₛ ≥ 2fₘₐₓ`; sampling at exactly Nyquist rate is NOT valid (Q145)
- **Aliasing**: folded frequency computation; 7 kHz signal sampled at 9 kHz → aliases at 2 kHz and 11 kHz pass through LPF (Q59); 1 kHz sampled at 1.5 kHz → 0.5 kHz alias (Q216)
- **Nyquist rate of products**: `x₁(t)·x₂(t)` → bandwidth sums via convolution in frequency (Q138)
- **Nyquist rate with time scaling**: `y(t) = x(t)·x(1+t/2)` requires careful bandwidth analysis (Q39); `y(t) = x(2t+5)` doubles frequencies (Q76)
- **Reconstruction**: ideal sinc interpolation recovers `f(t)` (not `f(t-τ)`) even with delayed sampling `p(t) = Σδ(t-τ-nTₛ)` provided Nyquist condition met (Q11)
- **Non-ideal reconstruction filter**: when filter bandwidth differs from `fₛ/2`, minimum `fₛ` computed from `fₛ - fₘ ≥ f_cutoff` (Q52)
- **Sampling of signal with harmonics**: which harmonics survive after LPF of given cutoff (Q17, Q102, Q126, Q220)
- **Bandpass signal**: spectral components after sampling and filtering, identifying output sinusoid frequencies
- **System zero at input frequency** → output is zero for all sampling frequencies (Q168)
- **Convolution with impulse train**: `x(t) * Σδ(t-nT)` produces periodic spectrum (Q90)
- **Sample-and-hold**: increasing hold capacitor → droop rate ↓, acquisition time ↑ (Q119)

### 1.8 DTFS, DTFT & DFT (~28 questions)
- **DTFT existence**: requires absolute summability or ROC including unit circle (Q12)
- **DFT computation**: 4-point, 8-point DFT via matrix multiplication; hand computation (Q169)
- **Repeated DFT property**: `DFT(DFT(x)) = N·x(-k)` or with `1/√N` normalization → `DFT(DFT(x)) = x` for palindromic sequences (Q15, Q31, Q112)
- **Circular convolution**: matrix method; `z[k] = y[k]` at `k = N-1` when comparing N-point circular vs linear convolution of N-point sequences (Q38, Q99)
- **DFT of upsampled sequence**: inserting zeros → periodic repetition of DFT (Q42, Q77)
- **DTFS**: periodic extension of coefficients; `a₋₂ = a_{N-2}` (Q26, Q91, Q134)
- **Parseval's for DT**: `Σ|x[n]|² = (1/2π)∫|X(e^{jω})|²dω`; used to convert frequency-domain integrals to time-domain sums (Q80)
- **FFT complexity**: N/2·log₂N multiplications; max block size `N` from real-time processing constraint (Q71, Q164)
- **Decimation-in-frequency FFT**: 6-point FFT signal flow graph, twiddle factor identification (Q47)
- **Three-tap causal FIR filter design**: finding coefficients to null specific frequency (Q46)
- **Filter type identification from `H(e^{jω})`**: evaluate at `ω=0`, `ω=π`, `ω=π/2` to classify as LPF/HPF/BPF/BSF (Q62, Q70, Q171)
- **DFT of circular convolution = product of DFTs**: circular convolution matrix for 4-point (Q140)
- **Conjugate symmetry of DFT**: `X[k] = X*[N-k]` for real sequences → fills in unknown DFT values (Q154)

### 1.9 Digital Filters (~5 questions)
- **FIR filter design**: Parseval's-based optimal approximation (minimize error energy → truncate h[n]) (Q45)
- **FIR direct form structure**: reading coefficients from block diagram (Q70)
- **Impulse invariance method**: converting H(s) to H(z) by matching sampled impulse response (Q78)
- **Moving average filter**: null-at-zero-frequency condition → coefficients sum to zero (Q94)
- **Linear phase FIR**: symmetric/antisymmetric impulse response conditions

---

## 2. Problem-Solving Techniques

### Transform-Domain Methods
- Convolution in time ↔ multiplication in frequency
- Partial fraction decomposition for inverse Laplace / Z-transform
- Pole-zero plot interpretation (stability, causality, filter type)
- Polynomial long division / binomial expansion for inverse Z-transform

### Standard Integral & Series Results
- `∫₀^∞ e^{-at}dt = 1/a` ; `∫₀^∞ sin(t)/t dt = π/2`
- Geometric series: `Σ aⁿ = 1/(1-a)` for `|a|<1`; `Σ n·aⁿ = a/(1-a)²`
- `sinc²(at)` energy = `1/|a|` via Parseval's
- Trig product-to-sum identities for orthogonality checks: `2sinA·cosB = sin(A+B)+sin(A-B)`

### Graphical / Visual Techniques
- Graphical convolution (flip-and-slide)
- Spectrum sketching: sampling → periodic replication; modulation → frequency shift
- ROC sketching for Laplace/Z-transforms
- Reading filter type from `|H(e^{jω})|` plot at key frequencies

### Algebraic Manipulations
- Variable substitution `u = -3t+5 → du = -3dt` for time-scaled energy
- Factoring characteristic equations for pole locations
- L'Hôpital's rule for `lim_{s→0}` in final value computations

### Property-Testing for Systems
- **Linearity**: check superposition and homogeneity separately
- **Time-invariance**: compare `T[x(t-t₀)]` vs `y(t-t₀)`
- **Causality**: does output at any time depend on future input?
- **BIBO stability**: is `Σ|h[n]|` finite? Are all poles inside unit circle (DT) or in LHP (CT)?

---

## 3. Corner Cases, Traps & Gotchas

### Signals Basics
- **Non-periodic DT signal trap**: `sin(π²n)` — since `π²/2π = π/2` is irrational, NOT periodic (Q139)
- **Invalid Fourier series**: `2cos(πt)+7cos(t)` has `T₁/T₂ = 1/π` (irrational) → not periodic → no FS (Q232)
- **Constant bias breaks linearity**: `y = au + b` with `b≠0` fails zero-input test (Q56)
- **`y(t) = x(eᵗ)`**: at `t=0`, `y(0) = x(1)` → depends on future → non-causal AND time-varying (Q30)
- **`y(t) = ∫_{-∞}^t x(τ)cos(3τ)dτ`**: NOT time-invariant (cos(3τ) inside integral) and NOT stable (bounded input `cos(3τ)` gives unbounded output) (Q151)

### Fourier Analysis
- **Duality pitfall**: `F(t) ↔ 2πf(-ω)` — scaling factor 2π and sign of argument easy to mess up (Q34, Q231)
- **`|F(ω)| ≤ ∫|f(t)|dt` vs `|F(ω)| ≤ ∫f(t)dt`**: only the first is always true; the second fails for odd or sign-changing functions (Q13)
- **Modulation halves energy**: `E[m(t)cos(ω₀t)] = E/2` when `ω₀ >> B` (no spectral overlap) (Q29)
- **sinc * sinc = sinc**: rect × rect = rect in frequency → convolution of two identical sinc functions gives back the same sinc (Q75)
- **Hilbert transform preserves energy**: only phase changes, not magnitude spectrum (Q53)

### Laplace & Z-Transform
- **Same X(s)/X(z), different signal depending on ROC** — ALWAYS specify ROC
- **`h[n] = -5ⁿu[-n-1]`**: the minus sign is part of the standard left-sided pair definition; ROC is `|z| < 5` (Q228)
- **Causal + stable for DT**: need ROC = `|z| > |largest pole|` AND all poles inside unit circle
- **Causal + stable for CT**: all poles strictly in LHP; but a NON-causal system CAN be stable with RHP poles (Q67)
- **FVT trap**: only valid when `sF(s)` (or `(z-1)X(z)`) has all poles in stable region; applying FVT blindly to unstable systems gives wrong answers
- **`|s| < 1` ≠ stability for CT**: poles inside `|s|=1` includes RHP; CT stability requires Re(s)<0, not |s|<1 (Q144)
- **ROC = empty set**: `x[n] = 2^{|n|}` → right-sided ROC `|z|>2` and left-sided ROC `|z|<1/2` have no overlap → Z-transform doesn't exist (Q72)

### Sampling
- **Aliased frequency formula**: `|f - k·fₛ|` for integer k giving result in `[0, fₛ/2]`
- **Product of signals doubles bandwidth**: Nyquist rate of `x₁·x₂` = `2(f₁+f₂)` (Q138)
- **Delayed sampling still reconstructs f(t), not f(t-τ)**: the LPF undoes the delay effect (Q11)
- **Sampling at exactly Nyquist rate** is NOT valid — it's a strict inequality `fₛ > 2fₘ` (Q145)
- **Aliased frequency can match original**: `cos(πfₛt)` sampled at `fₛ` — all samples are ±1 → appears DC; `cos(100πt/40)` sampled at 40 Hz = same samples as `cos(20πt/40)` (Q8)

### DFT/FFT
- **Circular vs linear convolution**: equal only at `k = N-1` for two N-point sequences (Q38)
- **`DFT^4{x[n]} = N²·x[n]`** (with standard DFT normalization); with `1/√N` normalization → `DFT²{x} = x` only for palindromic sequences (Q15, Q31, Q112)
- **`X(z) = α`** for `x[n] = αδ[n]` → ROC = entire z-plane (no poles at all) (Q12)
- **Non-minimum-phase system**: zeros outside unit circle; initial value still computed via `lim_{z→∞} H(z)` (Q19)

---

## 4. All Variations Encountered (26-Year Panorama)

| Variation Theme | Examples Across Years |
|---|---|
| **Stability + Causality determination** | From `h(t)`, `h[n]`, pole locations, ROC — asked in almost every year |
| **Energy/Power computation** | Direct integration, Parseval's (time or freq), scaling (2001–2026) |
| **Convolution computation** | Analytical, graphical, via transforms, with δ-functions, circular (all years) |
| **Nyquist rate for modified signals** | Product, sum, time-scaled, squared signals (2004–2026) |
| **Aliased frequency identification** | After undersampling through LPF (2003, 2004, 2016, 2017) |
| **ROC determination** | Right-sided, left-sided, two-sided, empty ROC; relation to causality/stability (all years) |
| **Partial fractions + inverse transform** | Both Laplace and Z, forced/natural response separation (all years) |
| **Fourier series symmetry** | Half-wave, even, odd → which harmonics survive (2005, 2010, 2011, 2017, 2026) |
| **DFT properties** | Circular convolution, repeated DFT, conjugate symmetry, FFT complexity (2005–2024) |
| **All-pass / minimum-phase** | Zero-pole reciprocal relationship; mixed phase classification (2014–2020) |
| **Filter type from H(eʲω)** | Evaluate at ω=0, π, π/2 to classify as LPF/BPF/HPF/BSF (2009, 2016, 2017) |
| **Initial/Final value theorems** | Both s-domain and z-domain; when FVT is invalid (2001–2024) |
| **Time scaling in FT** | `x(at) ↔ (1/|a|)X(ω/a)` with composite shifts (2004, 2014, 2024) |
| **Group delay / Phase delay** | Linear phase systems, RC-LPF, passband signals (2003, 2014, 2022) |
| **Non-LTI system identification** | From block diagram, from input-output graph, from bias term (2015, 2022, 2024, 2025) |
| **Impulse invariance / Bilinear** | Converting CT filter to DT filter (2016) |
| **White noise through LTI** | Output PSD, output power (2023) |
| **System with `H(s) = eˢ + e⁻ˢ`** | Non-causal system, Fourier series of output (2016) |

---

*Generated after reading all 8559 lines of [sns-pyq.tex](file:///Users/adityakinjawadekar/Documents/sns-pyq/sns-pyq.tex) — 238 GATE EC Signals & Systems PYQs (2001–2026)*
