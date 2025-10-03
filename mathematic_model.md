# Electric Vehicle Engineering: Mathematical Models and Equations
## A Comprehensive Reference for Simulation and Analysis

**Version:** 1.0
**Last Updated:** 2025
**Companion Document:** See `references.md` for complete bibliography
**Intended for:** Master's students, researchers, and engineers in EV development

---

## Table of Contents

1. [Introduction](#introduction)
2. [How to Use This Guide](#how-to-use-this-guide)
3. [Nomenclature and Symbols](#nomenclature-and-symbols)
4. [Vehicle Dynamics and Performance](#1-vehicle-dynamics-and-performance)
5. [Electric Machine Models](#2-electric-machine-models)
6. [Energy Storage Systems](#3-energy-storage-systems)
7. [Braking Performance](#4-braking-performance)
8. [Solar Powered Charging Stations](#5-solar-powered-charging-stations)
9. [Environmental Impact Calculations](#6-environmental-impact-calculations)
10. [Tire-Road Interaction](#7-tire-road-interaction)
11. [Torque Vectoring and Direct Yaw Moment Control](#8-torque-vectoring-and-direct-yaw-moment-control)
12. [Lateral Vehicle Dynamics](#9-lateral-vehicle-dynamics)
13. [Advanced Energy Consumption Models](#10-advanced-energy-consumption-models)
14. [Battery State Estimation and Thermal Management](#11-battery-state-estimation-and-thermal-management)
15. [Control and Optimization Frameworks](#12-control-and-optimization-frameworks)
16. [Advanced Regenerative Braking](#13-advanced-regenerative-braking)
17. [Power Management](#14-power-management)
18. [Vehicle-to-Grid (V2G) and Smart Charging](#15-vehicle-to-grid-v2g-and-smart-charging)
19. [Suspension and Ride Dynamics](#16-suspension-and-ride-dynamics)
20. [Multi-Objective Optimization for EV Design](#17-multi-objective-optimization-for-ev-design)
21. [Drive Cycle Analysis and Testing](#18-drive-cycle-analysis-and-testing)
22. [Electromagnetic Compatibility and Power Quality](#19-electromagnetic-compatibility-and-power-quality)
23. [Safety and Fault Detection](#20-safety-and-fault-detection)
24. [MATLAB Implementation Guide](#matlab-implementation-guide)
25. [Quick Reference Tables](#quick-reference-tables)

---

## Introduction

This document provides a comprehensive collection of mathematical models and equations for electric vehicle (EV) engineering, carefully extracted from leading textbooks, peer-reviewed journal papers, and international standards. Each equation is accompanied by:

- **Source attribution** with references to the companion `references.md` file
- **Variable definitions** with appropriate SI units
- **Application context** and typical values
- **Implementation notes** for simulation and analysis

### Scope and Organization

The models are organized into 20 technical categories covering:

- **Fundamental Dynamics:** Longitudinal, lateral, and vertical vehicle motion
- **Powertrain Components:** Electric machines, batteries, ultracapacitors
- **Advanced Control:** MPC, DYC, torque vectoring, energy management
- **System Integration:** V2G, charging infrastructure, thermal management
- **Safety and Standards:** ISO 26262, fault detection, power quality

### Prerequisites

Users should have knowledge of:
- Classical mechanics and dynamics
- Electrical engineering fundamentals
- Control systems theory
- Numerical methods and MATLAB/Simulink

---

## How to Use This Guide

### For Simulation and Modeling

1. **Identify your application area** from the table of contents
2. **Review the mathematical models** with all variable definitions
3. **Check the source references** in `references.md` for detailed theory
4. **Implement in MATLAB/Simulink** using the implementation guide (Section 24)
5. **Validate with standard test cases** (see Section 18 for drive cycles)

### For Research and Development

- **Literature review:** Cross-reference equations with source papers in `references.md`
- **Model development:** Build upon existing equations for new applications
- **Validation:** Compare results with published experimental data
- **Standards compliance:** Check against ISO/SAE standards (Section 20)

### Navigation Tips

- **Equation numbering:** Each section uses hierarchical numbering (e.g., 1.1, 1.2)
- **Cross-references:** Look for `[See references.md: Paper #X]` for detailed sources
- **MATLAB notes:** Implementation tips marked with 💻
- **Important assumptions:** Marked with ⚠️

---

## Nomenclature and Symbols

### Latin Symbols

| Symbol | Description | Units |
|--------|-------------|-------|
| A | Vehicle frontal area | m² |
| a | Acceleration | m/s² |
| C_d | Aerodynamic drag coefficient | - |
| C_α | Cornering stiffness | N/rad |
| E | Energy | J or kWh |
| F | Force | N |
| f_r | Rolling resistance coefficient | - |
| g | Gravitational acceleration (9.81) | m/s² |
| h | Height of center of gravity | m |
| I | Current / Moment of inertia | A / kg⋅m² |
| i_t, i_0 | Transmission/differential gear ratio | - |
| L | Wheelbase | m |
| l_f, l_r | Distance from CG to front/rear axle | m |
| m | Vehicle mass | kg |
| P | Power | W |
| Q | Battery capacity | Ah |
| R | Resistance | Ω |
| r | Tire radius | m |
| s | Slip ratio | - |
| T | Torque / Temperature | Nm / K or °C |
| t | Time / Track width | s / m |
| V | Voltage / Velocity | V / m/s |

### Greek Symbols

| Symbol | Description | Units |
|--------|-------------|-------|
| α | Tire slip angle | rad |
| β | Vehicle sideslip angle | rad |
| γ | Angle (motor control) | rad or ° |
| δ | Steering angle / Mass factor | rad / - |
| η | Efficiency | - |
| θ | Road angle / Rotor position | rad |
| λ | Wheel slip ratio | - |
| μ | Friction coefficient | - |
| ρ | Air density | kg/m³ |
| σ | Slip ratio (Pacejka) | - |
| φ | Roll angle / Power factor angle | rad |
| ω | Angular speed | rad/s |

### Subscripts and Abbreviations

- **_f, _r** = Front, Rear
- **_x, _y, _z** = Longitudinal, Lateral, Vertical/Yaw
- **_regen** = Regenerative
- **_max, _min** = Maximum, Minimum
- **SOC** = State of Charge
- **SOH** = State of Health
- **THD** = Total Harmonic Distortion
- **MPC** = Model Predictive Control
- **DYC** = Direct Yaw Moment Control
- **V2G** = Vehicle-to-Grid

---

## 1. Vehicle Dynamics and Performance

### 1.1 Longitudinal Vehicle Motion

**Reference:** [Advanced Electric Drive Vehicles, Chapter 2] → See references.md: Textbook #7

**Total Tractive Force Equation:**

$$ma = F_t - F_w - F_g - F_r$$

**Where:**
- m = vehicle mass (kg)
- a = acceleration (m/s²)
- F_t = total tractive force (N)
- F_w = aerodynamic drag force (N)
- F_g = grading resistance force (N)
- F_r = rolling resistance force (N)

**Application:** Fundamental equation for vehicle performance simulation, range prediction, and powertrain sizing.

---

### 1.2 Aerodynamic Drag

**Reference:** [Advanced Electric Drive Vehicles, Chapter 2] → See references.md: Textbook #7

$$F_w = \frac{1}{2} \rho C_d A (V + V_w)^2$$

**Where:**
- ρ = air density (kg/m³) [Standard: 1.2 kg/m³ at sea level, 20°C]
- C_d = aerodynamic drag coefficient [Typical: 0.25-0.35 for modern EVs]
- A = effective vehicle frontal area (m²) [Typical: 2.0-2.5 m²]
- V = vehicle longitudinal speed (m/s)
- V_w = wind speed (m/s) [positive = headwind]

**⚠️ Assumption:** Headwind adds to vehicle speed; for tailwind, use negative V_w

**💻 MATLAB Note:** For energy calculations, integrate F_w × V over drive cycle

---

### 1.3 Grading Resistance

**Reference:** [Advanced Electric Drive Vehicles, Chapter 2] → See references.md: Textbook #7

$$F_g = mg \sin(\theta)$$

**For small angles (θ < 15°):**

$$F_g \approx mg \tan(\theta) = mgG$$

**Where:**
- m = vehicle mass (kg)
- g = gravitational acceleration (9.81 m/s²)
- θ = road angle (radians)
- G = slope of the grade [Grade (%) = tan(θ) × 100]

**Example:** 10% grade → G = 0.1 → θ ≈ 5.7°

---

### 1.4 Rolling Resistance

**Reference:** [Advanced Electric Drive Vehicles, Chapter 2] → See references.md: Textbook #7

$$F_r = F_z \cdot f_r \cdot \cos(\theta)$$

**Where:**
- F_z = normal load (N)
- f_r = rolling resistance coefficient [Typical: 0.008-0.015]
- θ = road angle (radians)

**Typical f_r values:**
- High-performance tires: 0.008
- Standard passenger car tires: 0.010-0.012
- Off-road/winter tires: 0.015-0.020

---

### 1.5 Normal Forces on Front and Rear Axles

**Reference:** [Advanced Electric Drive Vehicles, Chapter 2] → See references.md: Textbook #7

**Front axle normal force:**

$$F_{zf} = \frac{mg \cdot l_r \cdot \cos(\theta) + mg \cdot h \cdot \sin(\theta) - F_w \cdot h - ma \cdot h}{l_f + l_r}$$

**Rear axle normal force:**

$$F_{zr} = \frac{mg \cdot l_f \cdot \cos(\theta) - mg \cdot h \cdot \sin(\theta) + F_w \cdot h + ma \cdot h}{l_f + l_r}$$

**Where:**
- l_f = distance from front axle to center of gravity (m)
- l_r = distance from rear axle to center of gravity (m)
- h = height of vehicle center of gravity (m)

**Application:** Critical for traction limit analysis, brake force distribution, and vehicle stability

---

### 1.6 Maximum Vehicle Speed

**Reference:** [Advanced Electric Drive Vehicles, Chapter 2] → See references.md: Textbook #7

At maximum speed conditions (a = 0, θ = 0):

$$\frac{T_{en} \cdot i_t \cdot i_0 \cdot \eta_p}{r_d} = mgf_r + \frac{1}{2} \rho A C_d V^2$$

**Solving for maximum speed V:**

$$V_{max} = \sqrt{\frac{2\left(\frac{T_{en} \cdot i_t \cdot i_0 \cdot \eta_p}{r_d} - mgf_r\right)}{\rho A C_d}}$$

**Where:**
- T_en = engine/motor torque (Nm)
- i_t = transmission gear ratio
- i_0 = differential gear ratio
- η_p = powertrain efficiency [Typical: 0.85-0.95 for EVs]
- r_d = effective tire radius (m)

**💻 MATLAB Tip:** Plot V_max vs. gear ratio to optimize top speed

---

### 1.7 Gradeability

**Reference:** [Advanced Electric Drive Vehicles, Chapter 2] → See references.md: Textbook #7

$$G_{max} = \frac{\frac{T_{en} \cdot i_t \cdot i_0 \cdot \eta_p}{r_d} - mgf_r - \frac{1}{2} \rho A C_d V^2}{mg}$$

**Application:** Determines maximum climbable grade at given speed

**Example:** For 30% grade at 50 km/h, verify T_en is sufficient

---

### 1.8 Acceleration Performance

**Reference:** [Advanced Electric Drive Vehicles, Chapter 2] → See references.md: Textbook #7

**Acceleration:**

$$a = \frac{\frac{T_{en} \cdot i_t \cdot i_0 \cdot \eta_p}{r_d} - mgf_r - \frac{1}{2} \rho A C_d V^2}{\delta \cdot m}$$

**Where:** δ = mass factor accounting for rotating components inertia [Typical: 1.03-1.10]

**Time to reach speed V₂ from V₁:**

$$t = \delta m \int_{V_1}^{V_2} \frac{dV}{\frac{T_{en} \cdot i_t \cdot i_0 \cdot \eta_p}{r_d} - mgf_r - \frac{1}{2}\rho A C_d V^2}$$

**Distance to reach speed V₂ from V₁:**

$$S = \delta m \int_{V_1}^{V_2} \frac{V \cdot dV}{\frac{T_{en} \cdot i_t \cdot i_0 \cdot \eta_p}{r_d} - mgf_r - \frac{1}{2}\rho A C_d V^2}$$

**💻 MATLAB Implementation:** Use `trapz()` or `integral()` for numerical integration

---

## 2. Electric Machine Models

### 2.1 DC Machine Back-EMF and Torque

**Reference:** [Electric and Hybrid Vehicles: Design Fundamentals, Chapter 6] → See references.md: Textbook #6

**Back-EMF (Induced Voltage):**

$$E_a = K_m \cdot \phi \cdot \omega_m$$

**Electromagnetic Torque:**

$$T_e = K_m \cdot \phi \cdot I_a$$

**Where:**
- K_m = machine constant = N_t × P / (π × a)
- φ = magnetic flux (Wb)
- ω_m = motor speed (rad/s)
- I_a = armature current (A)
- N_t = number of turns
- P = number of poles
- a = number of parallel paths

**Application:** DC motor modeling for simple EV powertrains (less common in modern EVs)

---

### 2.2 DC Machine Voltage Balance

**Reference:** [Electric and Hybrid Vehicles: Design Fundamentals, Chapter 6] → See references.md: Textbook #6

$$V_A = R_A \cdot i_A + L_{AA} \frac{di_A}{dt} + e_A$$

**Where:**
- V_A = armature voltage (V)
- R_A = armature resistance (Ω)
- L_AA = armature self-inductance (H)
- e_A = back-EMF (V)

**💻 MATLAB State-Space:** Use for dynamic simulation with current as state variable

---

### 2.3 Induction Motor Torque (Simplified)

**Reference:** [Electric and Hybrid Vehicles: Design Fundamentals, Chapter 6] → See references.md: Textbook #6

**For linear region operation:**

$$T_e = K_{IM} \cdot \omega_{slip}$$

**Where:**
- K_IM = induction motor constant (Nm⋅s/rad)
- ω_slip = slip speed = ω_e - ω_m (rad/s)
- ω_e = synchronous speed (rad/s)
- ω_m = rotor speed (rad/s)

**Slip Ratio:**

$$s = \frac{\omega_e - \omega_m}{\omega_e}$$

**Typical slip at rated torque:** 2-5%

---

### 2.4 Permanent Magnet Synchronous Motor (PMSM) Torque

**Reference:** [Electric and Hybrid Vehicles: Design Fundamentals, Chapter 6] → See references.md: Textbook #6

$$T_e = \frac{3}{2} \cdot \frac{P}{2} \cdot L_m \cdot I_F \cdot I_S \cdot \sin(\gamma)$$

**Where:**
- P = number of poles [Typical: 4-8 for EV traction motors]
- L_m = magnetizing inductance (H)
- I_F = equivalent magnet current (A)
- I_S = stator RMS current (A)
- γ = angle between stator current and magnet flux

**Maximum torque occurs at γ = 90°** (field-oriented control)

**Application:** Most common motor type in modern EVs (Tesla, Nissan Leaf, etc.)

---

### 2.5 Switched Reluctance Motor (SRM)

**Reference:** [Electric and Hybrid Vehicles: Design Fundamentals, Chapter 6] → See references.md: Textbook #6

**Torque (linear assumption):**

$$T_{ph}(i,\theta) = \frac{1}{2} i_{ph}^2 \frac{dL_{ph}(\theta)}{d\theta}$$

**Where:**
- i_ph = phase current (A)
- L_ph(θ) = phase inductance as function of rotor position (H)
- θ = rotor angle (rad)

**Voltage Balance:**

$$V_{ph} = i_{ph} \cdot R_s + \frac{d\lambda_{ph}}{dt}$$

**Where:**
- V_ph = phase voltage (V)
- R_s = winding resistance (Ω)
- λ_ph = flux linkage (Wb-turns)

**Application:** Simple, rugged motor for cost-sensitive applications

---

## 3. Energy Storage Systems

### 3.1 Battery Models

**Reference:** [Advanced Electric Drive Vehicles, Chapter 8] → See references.md: Textbook #7

**C-Rate Definition:**

$$\text{C-rate} = \frac{\text{Discharge Current}}{\text{Rated Capacity}}$$

**Example:** For a 75 kWh / 300V battery (250 Ah):
- 1C = 250 A (75 kW)
- 2C = 500 A (150 kW) [typical fast charging]
- 4C = 1000 A (300 kW) [ultra-fast charging limit]

**Energy Stored in Battery:**

$$E_{battery} = V_{nominal} \times Q_{capacity}$$

**Where:**
- V_nominal = nominal voltage (V)
- Q_capacity = capacity (Ah)

---

### 3.2 Ultracapacitor Energy

**Reference:** [Advanced Electric Drive Vehicles, Chapter 8] → See references.md: Textbook #7

**Energy Stored:**

$$E_{UC} = \frac{1}{2} C V^2$$

**Where:**
- C = capacitance (F) [Typical: 3000-5000 F for EV modules]
- V = voltage (V)

**Energy Released (V₁ to V₂):**

$$\Delta E = \frac{1}{2} C (V_1^2 - V_2^2)$$

**Voltage during constant current discharge:**

$$V(t) = V_{initial} - \frac{I \cdot t}{C}$$

**Where:**
- I = discharge current (A)
- t = time (s)

**Power Loss:**

$$P_{loss} = I^2 \times ESR_{DC}$$

**Where:** ESR_DC = equivalent series resistance (Ω) [Typical: 0.5-2 mΩ]

**Application:** Hybridization with batteries for peak power and regenerative braking

---

### 3.3 Hybrid ESS Power Density

**Reference:** [Advanced Electric Drive Vehicles, Chapter 8 Problems] → See references.md: Textbook #7

**Combined Power Density:**

$$P_{density,hybrid} = \frac{P_{battery} + P_{UC}}{m_{battery} + m_{UC}}$$

**Where:** masses and powers are in consistent units (kg, W)

**Application:** Optimize battery/ultracapacitor mass ratio for performance targets

---

## 4. Braking Performance

### 4.1 Braking Force

**Reference:** [Advanced Electric Drive Vehicles, Chapter 2] → See references.md: Textbook #7

$$F_b = \frac{T_b - I \cdot \alpha_{an}}{r}$$

**Where:**
- T_b = applied brake torque (Nm)
- I = rotating inertia (kg⋅m²)
- α_an = angular deceleration (rad/s²)
- r = tire rolling radius (m)

---

### 4.2 Normal Forces During Braking

**Reference:** [Advanced Electric Drive Vehicles, Chapter 2] → See references.md: Textbook #7

**Front axle:**

$$F_{zf} = \frac{mg \cdot l_r + h \frac{a}{g}}{l_f + l_r}$$

**Rear axle:**

$$F_{zr} = \frac{mg \cdot l_f - h \frac{a}{g}}{l_f + l_r}$$

**Where:**
- a = braking deceleration (m/s²) [Typical: 0.3-0.9g for normal braking]
- h = height of center of gravity (m)

**Note:** During braking, load transfers to front axle (F_zf increases, F_zr decreases)

---

## 5. Solar Powered Charging Stations

### 5.1 Daily Energy Generation

**Reference:** [Solar Powered Charging Infrastructure for Electric Vehicles, Chapter 3] → See references.md: Textbook #19

**Typical generation per parking space (Kansas example):**

$$E_{daily} \approx 16 \text{ kWh/day per parking space}$$

**Total potential generation:**

$$E_{total} = N_{spaces} \times E_{daily}$$

**Example:** 200 million spaces × 16 kWh/day = 3.2 billion kWh/day

**Application:** Solar carport sizing for workplace/public charging

---

### 5.2 EV Charging Economics

**Reference:** [Solar Powered Charging Infrastructure for Electric Vehicles, Chapter 3] → See references.md: Textbook #19

**Daily charging cost:**

$$\text{Cost}_{daily} = E_{used} \times \text{Price}_{kWh}$$

**Example:** 13.3 kWh × $0.12/kWh = $1.60/day

**Levelized cost per parking space:**

$$\text{Cost}_{per\ day} = \frac{\text{Installation Cost}}{\text{Days/year} \times \text{Years of operation}}$$

**Example:** $10,000 / (250 days/year × 20 years) = $2.00/day

---

## 6. Environmental Impact Calculations

### 6.1 Oil Consumption Projection

**Reference:** [Modern Electric, Hybrid Electric, and Fuel Cell Vehicles, Chapter 1] → See references.md: Textbook #9

**Annual consumption with growth:**

$$C(t) = C_0 (1 + r)^t$$

**Where:**
- C₀ = initial consumption
- r = annual growth rate [e.g., 0.013 for 1.3%]
- t = time in years

---

### 6.2 Reserves/Production Ratio

**Reference:** [Modern Electric, Hybrid Electric, and Fuel Cell Vehicles, Chapter 1] → See references.md: Textbook #9

$$\text{R/P ratio} = \frac{\text{Proved Reserves}}{\text{Annual Production}}$$

**This gives the number of years reserves will last at current production rates.**

---

### 6.3 Fuel Efficiency Improvement

**Reference:** [Modern Electric, Hybrid Electric, and Fuel Cell Vehicles, Chapter 1] → See references.md: Textbook #9

**Fuel consumption reduction factors:**
- HEV: 25% reduction → Factor = 0.75
- BEV/Fuel Cell: 50% reduction → Factor = 0.50

**Annual consumption with technology:**

$$C_{tech}(t) = C_0 (1 + r)^t \times \text{Efficiency Factor}$$

---

## 7. Tire-Road Interaction

### 7.1 Pacejka Tire Model (Magic Formula)

**Reference:** [Advanced Electric Drive Vehicles, Chapter 2] → See references.md: Textbook #7

$$\mu_{f/r} = D \sin\left[C \arctan\left(B\sigma_{f/r} - E\left(B\sigma_{f/r} - \arctan(B\sigma_{f/r})\right)\right)\right]$$

**Where:**
- μ_f/r = friction coefficient
- σ_f/r = slip ratio
- B, C, D, E = tire coefficients (depend on road conditions)

**Typical values (dry asphalt):**
- B ≈ 10 (stiffness factor)
- C ≈ 1.9 (shape factor)
- D ≈ 1.0 (peak friction)
- E ≈ 0.97 (curvature factor)

**Slip Ratio (acceleration):**

$$\sigma_r = \frac{\omega_{wr} r_{wr} - V}{\omega_{wr} r_{wr}}$$

$$\sigma_f = \frac{\omega_{wf} r_{wf} - V}{\omega_{wf} r_{wf}}$$

**Where:**
- ω_w = wheel angular speed (rad/s)
- r_w = wheel radius (m)
- V = vehicle speed (m/s)

---

## 8. Torque Vectoring and Direct Yaw Moment Control

### 8.1 Differential Torque Distribution

**Reference:** [Vehicle Dynamics and Control (Rajesh Rajamani, 2nd Edition, 2012)] → See references.md: Textbook #4

**Total Yaw Moment from Torque Vectoring:**

$$M_{z,TV} = \frac{(T_{RL} - T_{RR}) \cdot t_r}{2} + \frac{(T_{FL} - T_{FR}) \cdot t_f}{2}$$

**Where:**
- M_z,TV = yaw moment from torque vectoring (Nm)
- T_RL, T_RR = rear left/right motor torque (Nm)
- T_FL, T_FR = front left/right motor torque (Nm)
- t_r, t_f = rear/front track width (m) [Typical: 1.5-1.6 m]

**Application:** Essential for in-wheel motor EVs and four-motor platforms

---

### 8.2 Direct Yaw Moment Control (DYC)

**Reference:** [IEEE Transactions on Vehicular Technology (Deng et al., 2015)] → See references.md: Paper #4

**Desired Yaw Moment:**

$$M_{z,desired} = K_p(\beta_{desired} - \beta) + K_d(\dot{r}_{desired} - \dot{r})$$

**Where:**
- β = vehicle sideslip angle (rad)
- ṙ = yaw rate (rad/s)
- K_p, K_d = control gains [Tune via pole placement or LQR]

**Optimal Torque Distribution (Quadratic Programming):**

$$\min \sum (T_i - T_{i,nominal})^2$$

**Subject to:**
- $\sum (T_i \times r_i) = M_{z,desired}$
- $T_{i,min} \leq T_i \leq T_{i,max}$

**💻 MATLAB:** Use `quadprog()` for real-time optimization

---

### 8.3 Yaw Rate Response

**Reference:** [Fundamentals of Vehicle Dynamics (Thomas Gillespie, 1992)] → See references.md: Textbook #5

**Desired Yaw Rate (Steady State):**

$$\dot{r}_{desired} = \frac{V \cdot \delta_f}{L (1 + K_{us} V^2)}$$

**Where:**
- δ_f = front wheel steering angle (rad)
- L = wheelbase (m)
- K_us = understeer coefficient (s²/m²)
- V = vehicle speed (m/s)

**Understeer Coefficient:**

$$K_{us} = \frac{m}{L^2} \left(\frac{l_f}{C_r} - \frac{l_r}{C_f}\right)$$

**Where:**
- m = vehicle mass (kg)
- C_f, C_r = front/rear cornering stiffness (N/rad) [Typical: 50,000-80,000 N/rad per axle]
- l_f, l_r = distance from CG to front/rear axle (m)

**Interpretation:**
- K_us > 0: Understeer (stable)
- K_us = 0: Neutral steer
- K_us < 0: Oversteer (unstable at high speed)

---

### 8.4 Stability Region

**Reference:** [Vehicle Handling Dynamics (Masato Abe, 2015)] → See references.md: Textbook #6

**Phase Plane Stability Boundary:**

$$\beta_{max} = \arctan\left(\frac{\mu g}{V^2 / R}\right)$$

**Where:**
- μ = friction coefficient
- g = gravitational acceleration (m/s²)
- R = turning radius (m)

**Critical Sideslip Angle:**

$$\beta_{critical} \approx \pm(3-5)° \text{ for passenger vehicles}$$

**Application:** ESC (Electronic Stability Control) intervention threshold

---

### 8.5 Torque Vectoring Energy Efficiency

**Reference:** [IEEE Transactions on Transportation Electrification (De Novellis et al., 2014)] → See references.md: Paper #9

**Energy Loss from Torque Difference:**

$$P_{loss,TV} = \sum \left[(T_i \times \omega_i) \times (1 - \eta_i)\right]$$

**Where:**
- P_loss,TV = power loss due to torque vectoring (W)
- ω_i = wheel angular speed (rad/s)
- η_i = individual motor efficiency [Function of T_i and ω_i]

**Efficiency-Aware Torque Distribution:**

$$\max \sum [T_i \times \omega_i \times \eta_i(T_i, \omega_i)]$$

**Subject to:** $\sum (T_i \times r_i) = M_{z,desired}$

---

## 9. Lateral Vehicle Dynamics

### 9.1 Bicycle Model (2-DOF)

**Reference:** [Vehicle Dynamics and Control (Rajesh Rajamani, 2nd Edition, 2012)] → See references.md: Textbook #4

**Lateral Force Equation:**

$$m V (\dot{\beta} + \dot{r}) = F_{yf} + F_{yr}$$

**Yaw Moment Equation:**

$$I_z \ddot{r} = l_f F_{yf} - l_r F_{yr} + M_{z,ext}$$

**Where:**
- I_z = yaw moment of inertia (kg⋅m²) [Typical: 1500-3000 kg⋅m² for sedans]
- F_yf, F_yr = front/rear lateral tire forces (N)
- M_z,ext = external yaw moment (Nm) [from torque vectoring]
- β = sideslip angle (rad)

---

### 9.2 Linear Tire Model

**Reference:** [Fundamentals of Vehicle Dynamics (Thomas Gillespie, 1992)] → See references.md: Textbook #5

**Lateral Tire Force:**

$$F_y = -C_\alpha \alpha$$

**Where:**
- C_α = cornering stiffness (N/rad)
- α = tire slip angle (rad)

**Slip Angles:**

$$\alpha_f = \delta_f - \left(\beta + \frac{l_f \dot{r}}{V}\right)$$

$$\alpha_r = -\left(\beta - \frac{l_r \dot{r}}{V}\right)$$

**Application:** Valid for small slip angles (< 3-5°)

---

### 9.3 Magic Formula (Lateral)

**Reference:** [Tire and Vehicle Dynamics (Hans Pacejka, 3rd Edition, 2012)] → See references.md: Textbook #7

**Lateral Force (Pure Slip):**

$$F_y = D \sin\left[C \arctan\left\{B\alpha - E(B\alpha - \arctan(B\alpha))\right\}\right]$$

**Where:**
- D = peak value (N)
- C = shape factor
- B = stiffness factor (1/rad)
- E = curvature factor

**Load Sensitivity:**

$$D = \mu_y F_z$$

$$B = \frac{C_\alpha}{C \cdot D}$$

---

### 9.4 Combined Slip (Pacejka Model)

**Reference:** [Tire and Vehicle Dynamics (Hans Pacejka, 3rd Edition, 2012)] → See references.md: Textbook #7

**Combined Longitudinal Force:**

$$F_{x,combined} = F_{x0} \times G_{x\alpha}$$

**Combined Lateral Force:**

$$F_{y,combined} = F_{y0} \times G_{y\kappa}$$

**Weighting Functions:**

$$G_{x\alpha} = \cos[C_{x\alpha} \arctan(B_{x\alpha} \alpha)]$$

$$G_{y\kappa} = \cos[C_{y\kappa} \arctan(B_{y\kappa} \kappa)]$$

**Where:** κ = longitudinal slip ratio

**Application:** Critical for combined braking/cornering maneuvers

---

### 9.5 Roll Dynamics

**Reference:** [Race Car Vehicle Dynamics (Milliken & Milliken, 1995)] → See references.md: Textbook #8

**Roll Angle:**

$$\phi = \frac{m h a_y}{K_{\phi f} + K_{\phi r} - mgh}$$

**Where:**
- φ = roll angle (rad)
- h = CG height (m)
- a_y = lateral acceleration (m/s²)
- K_φf, K_φr = front/rear roll stiffness (Nm/rad)

**Lateral Load Transfer:**

$$\Delta F_z = \frac{m a_y h K_\phi}{t (K_{\phi f} + K_{\phi r})}$$

---

## 10. Advanced Energy Consumption Models

### 10.1 Drive Cycle Energy Consumption

**Reference:** [Electric and Hybrid Vehicles: Technologies, Modeling and Control (Sabri et al., 2018)] → See references.md: Textbook #10

**Total Energy Consumption:**

$$E_{total} = \int_{t_0}^{t_f} P(t) \, dt = \int_{t_0}^{t_f} [F_{traction}(t) \times V(t)] \, dt$$

**Tractive Power:**

$$P_{traction} = V \left[ma + mgf_r\cos(\theta) + mg\sin(\theta) + \frac{1}{2}\rho C_d A V^2\right]$$

**💻 MATLAB Implementation:**
```matlab
E_total = trapz(t, P_traction); % [J]
E_kWh = E_total / 3.6e6; % Convert to kWh
```

---

### 10.2 Regenerative Braking Energy Recovery

**Reference:** [IEEE Transactions on Vehicular Technology (Gao et al., 2008)] → See references.md: Paper #1

**Recoverable Braking Energy:**

$$E_{regen} = \int_{t_0}^{t_f} \eta_{regen} P_{brake}(t) \, dt$$

**Where:**
- η_regen = regenerative efficiency [Typical: 0.6-0.8]
- P_brake = braking power (W)

**Maximum Regenerative Torque:**

$$T_{regen,max} = \min\left(T_{motor,max}, \frac{F_z \cdot r \cdot f_{brake}}{i_{total}}\right)$$

**Where:**
- f_brake = brake force distribution factor
- i_total = total gear ratio

**Blended Braking Strategy:**

$$T_{mechanical} = T_{total} - T_{regen}$$

**Subject to:** $T_{regen} \leq T_{regen,max}$

---

### 10.3 Motor Efficiency Map Model

**Reference:** [SAE Technical Paper 2013-01-1462] → See references.md: Standard #2

**Efficiency as Function of Torque and Speed:**

$$\eta_{motor}(T,\omega) = \frac{P_{out}}{P_{out} + P_{copper} + P_{iron} + P_{mech}}$$

**Copper Loss:**

$$P_{copper} = 3 I^2(T,\omega) R_s$$

**Iron Loss:**

$$P_{iron} = K_h f B^2 + K_e f^2 B^2$$

**Where:**
- K_h = hysteresis coefficient
- K_e = eddy current coefficient
- f = frequency (Hz)
- B = flux density (T)

**💻 MATLAB:** Create lookup table η(T,ω) from test data using `interp2()`

---

### 10.4 Battery Power Losses

**Reference:** [Journal of Power Sources (Seaman et al., 2014)] → See references.md: Paper #29

**Internal Resistance Model:**

$$P_{loss,battery} = I^2 R_{int}(SOC, T)$$

**Voltage-Current Relationship:**

$$V_{terminal} = V_{oc}(SOC) - I \cdot R_{int}(SOC,T)$$

**Temperature-Dependent Resistance:**

$$R_{int}(T) = R_{ref} [1 + \alpha(T - T_{ref})]$$

**Typical values:**
- α ≈ 0.005-0.015 /°C
- R_int increases 2-3× from 25°C to -20°C

---

### 10.5 HVAC and Auxiliary Loads

**Reference:** [Applied Energy Journal (Kambly & Bradley, 2014)] → See references.md: Paper #36

**Total Auxiliary Power:**

$$P_{aux} = P_{HVAC} + P_{electronics} + P_{steering} + P_{lighting}$$

**Cabin Heating/Cooling Power:**

$$P_{HVAC} = \frac{\dot{m} c_p \Delta T}{COP}$$

**Where:**
- ṁ = air mass flow rate (kg/s)
- c_p = specific heat capacity [1005 J/kg⋅K for air]
- COP = coefficient of performance [Heating: 2-4, Cooling: 1.5-3]

**Range Impact:**

$$\text{Range}_{reduction} = \frac{E_{battery} - E_{aux}}{E_{nominal} / \text{Range}_{nominal}}$$

**Example:** 3 kW HVAC for 1 hour = 3 kWh → ~20 km range loss (for 150 Wh/km consumption)

---

## 11. Battery State Estimation and Thermal Management

### 11.1 State of Charge (SOC) Estimation

**Reference:** [IEEE Transactions on Industrial Electronics (Plett, 2004)] → See references.md: Paper #17

**Coulomb Counting:**

$$SOC(t) = SOC(t_0) - \frac{1}{Q_{nom}} \int_{t_0}^{t} \eta_{coulombic} I(\tau) \, d\tau$$

**Where:**
- Q_nom = nominal capacity (Ah)
- η_coulombic = coulombic efficiency [~0.99 for Li-ion]

**Extended Kalman Filter (EKF) SOC Estimation:**

**State equation:**

$$SOC(k+1) = SOC(k) - \frac{\eta T_s I(k)}{3600 Q_{nom}}$$

**Measurement equation:**

$$V_{terminal}(k) = OCV(SOC(k)) - R_{int} I(k)$$

**💻 MATLAB:** Implement EKF using `extendedKalmanFilter()` or custom code

---

### 11.2 State of Health (SOH) Estimation

**Reference:** [Journal of Energy Storage (Hu et al., 2020)] → See references.md: Paper #32

**Capacity Fade:**

$$SOH = \frac{Q_{current}}{Q_{initial}} \times 100\%$$

**Resistance Increase:**

$$SOH_R = \frac{R_{initial}}{R_{current}} \times 100\%$$

**Aging Model (Calendar + Cycle):**

$$Q_{fade} = Q_{fade,calendar} + Q_{fade,cycle}$$

$$Q_{fade,calendar} = A \exp\left(\frac{-E_a}{RT}\right) t^z$$

$$Q_{fade,cycle} = B (Ah_{throughput})^z$$

**Where:**
- E_a = activation energy (J/mol) [Typical: 20,000-30,000 J/mol]
- R = gas constant (8.314 J/mol⋅K)
- z = aging exponent [Typical: 0.5-0.75]

---

### 11.3 Battery Thermal Model

**Reference:** [Applied Thermal Engineering (Saw et al., 2016)] → See references.md: Paper #37

**Lumped Thermal Model:**

$$m_{cell} c_p \frac{dT}{dt} = Q_{gen} - Q_{conv} - Q_{rad}$$

**Heat Generation:**

$$Q_{gen} = I^2 R_{int} + IT\frac{dOCV}{dT}$$

**Where:** the second term is reversible entropic heat [typically small]

**Convective Heat Transfer:**

$$Q_{conv} = h A_{surface} (T_{cell} - T_{ambient})$$

**Where:** h = heat transfer coefficient [Air cooling: 5-25 W/m²⋅K, Liquid: 50-500 W/m²⋅K]

---

### 11.4 Equivalent Circuit Model (2RC)

**Reference:** [Journal of Power Sources (He et al., 2011)] → See references.md: Paper #28

**Voltage Equation:**

$$V_{terminal} = OCV - R_0 I - V_1 - V_2$$

**RC Network Dynamics:**

$$\frac{dV_1}{dt} = -\frac{V_1}{R_1 C_1} + \frac{I}{C_1}$$

$$\frac{dV_2}{dt} = -\frac{V_2}{R_2 C_2} + \frac{I}{C_2}$$

**Where:**
- R_0 = ohmic resistance (Ω)
- R_1, C_1 = charge transfer resistance/capacitance
- R_2, C_2 = diffusion resistance/capacitance

**💻 MATLAB State-Space:**
```matlab
A = [-1/(R1*C1) 0; 0 -1/(R2*C2)];
B = [1/C1; 1/C2];
C = [-1 -1];
D = -R0;
sys = ss(A,B,C,D);
```

---

### 11.5 Thermal Runaway Prevention

**Reference:** [Journal of the Electrochemical Society (Spotnitz & Franklin, 2003)] → See references.md: Paper #27

**Critical Temperature Criterion:**

$$\left.\frac{dT}{dt}\right|_{max} = \frac{Q_{gen,max}}{m c_p} < \text{Threshold}$$

**Safe Operating Area:**

$$T_{min} < T_{cell} < T_{max}$$

**Typical:** 15°C < T < 45°C (optimal: 20-30°C)

**⚠️ Safety Limits:**
- T > 60°C: Accelerated aging
- T > 80°C: Safety concern (SEI breakdown)
- T > 130°C: Thermal runaway risk

---

## 12. Control and Optimization Frameworks

### 12.1 Model Predictive Control (MPC) for Energy Management

**Reference:** [IEEE Transactions on Control Systems Technology (Borhan et al., 2012)] → See references.md: Paper #22

**Cost Function:**

$$J = \sum_{k=0}^{N-1} \left[\alpha m_{fuel}(k) + \beta \Delta T_{eng}^2(k) + \gamma (SOC(k) - SOC_{ref})^2\right]$$

**Constraints:**

$$SOC_{min} \leq SOC(k) \leq SOC_{max}$$
$$T_{motor,min} \leq T_{motor}(k) \leq T_{motor,max}$$
$$P_{battery,min} \leq P_{battery}(k) \leq P_{battery,max}$$

**State Update:**

$$SOC(k+1) = SOC(k) - \frac{P_{battery}(k) \Delta t}{V_{battery} Q_{nom}}$$

**💻 MATLAB:** Use MPC Toolbox with `mpc()` and `mpcobj()`

---

### 12.2 Optimal Torque Distribution

**Reference:** [IEEE Transactions on Vehicular Technology (Chen & Wang, 2014)] → See references.md: Paper #2

**Multi-Objective Optimization:**

$$\min J = w_1 P_{loss} + w_2 |M_z - M_{z,desired}|$$

**Constraints:**

$$T_{FL} + T_{FR} + T_{RL} + T_{RR} = T_{total}$$
$$|T_i| \leq T_{i,max}$$
$$F_{x,i} \leq \mu F_{z,i}$$ (traction limit)

**Lagrangian Method:**

$$\mathcal{L} = J + \lambda_1(\sum T_i - T_{total}) + \lambda_2(\sum T_i r_i - M_{z,desired})$$

---

### 12.3 Energy-Optimal Velocity Planning

**Reference:** [Transportation Research Part C (Sciarretta et al., 2014)] → See references.md: Paper #38

**Pontryagin's Minimum Principle:**

$$\mathcal{H} = P_{traction}(v,a) + \lambda(t) a$$

**Optimal Control Law:**

$$u^*(t) = \arg\min \mathcal{H}(x, u, \lambda, t)$$

**Costate Equation:**

$$\frac{d\lambda}{dt} = -\frac{\partial \mathcal{H}}{\partial x}$$

---

### 12.4 Adaptive Cruise Control (ACC) with Energy Optimization

**Reference:** [IEEE Transactions on Intelligent Transportation Systems (Li et al., 2017)] → See references.md: Paper #23

**Safe Following Distance:**

$$d_{safe} = d_{min} + \tau v_{ego} + \frac{v_{ego}^2 - v_{lead}^2}{2 a_{max}}$$

**Energy-Optimal Spacing Policy:**

$$v_{optimal} = \arg\min \int_{t_0}^{t_f} P(v,a) \, dt$$

**Subject to:** $d(t) \geq d_{safe}(t)$

---

### 12.5 Convex Optimization for Power Splitting

**Reference:** [Optimal Control Applications and Methods (Sundstrom & Guzzella, 2009)] → See references.md: Paper #46

**Convex Problem Formulation:**

$$\min \int_{t_0}^{t_f} [P_{loss,motor} + P_{loss,battery}] \, dt$$

**Subject to:**
- $P_{motor} + P_{battery} = P_{demand}$
- $SOC(t_f) \geq SOC_{target}$

**Power Loss Convex Approximation:**

$$P_{loss} \approx aP^2 + bP + c$$

(quadratic approximation)

---

## 13. Advanced Regenerative Braking

### 13.1 Maximum Regenerative Power

**Reference:** [IEEE Transactions on Vehicular Technology (Ko et al., 2014)] → See references.md: Paper #3

**Battery Power Limit:**

$$P_{regen,max,battery} = \min(V_{oc} I_{max,charge}, SOC_{factor} P_{rated})$$

**SOC-Dependent Limit:**

$$SOC_{factor} = \begin{cases}
1.0 & \text{if } SOC < 0.8 \\
\frac{1-SOC}{0.2} & \text{if } 0.8 \leq SOC < 1.0 \\
0 & \text{if } SOC \geq 1.0
\end{cases}$$

**Application:** Prevents overcharging at high SOC

---

### 13.2 Cooperative Braking Control

**Reference:** [Vehicle System Dynamics (Xu et al., 2015)] → See references.md: Paper #41

**Total Braking Force Distribution:**

$$F_{brake,total} = F_{regen} + F_{friction}$$

**Ideal Braking Force Distribution:**

$$F_{brake,front} = F_{brake,total} \frac{l_r + \mu h}{l_f + l_r}$$

$$F_{brake,rear} = F_{brake,total} \frac{l_f - \mu h}{l_f + l_r}$$

**ECE Regulation (Front Priority):**

$$F_{brake,front} = F_{brake,total} \times \phi$$
$$F_{brake,rear} = F_{brake,total} \times (1 - \phi)$$

**Where:** $\phi = 0.07 + 0.85 \times \frac{F_{brake,total}}{mg}$

---

### 13.3 Energy Recovery Efficiency

**Reference:** [Applied Energy (Zhang et al., 2013)] → See references.md: Paper #35

**Overall Regenerative Efficiency:**

$$\eta_{overall} = \eta_{motor} \times \eta_{inverter} \times \eta_{battery,charge}$$

**Recovered Energy per Braking Event:**

$$E_{recovered} = \int_{t_0}^{t_f} \eta_{overall} T_{regen}(t) \omega(t) \, dt$$

**Regenerative Coefficient:**

$$RC = \frac{E_{recovered}}{0.5 m v_0^2} \times 100\%$$

**Typical RC values:**
- City driving: 20-30%
- Highway: 5-10%
- Aggressive driving: 35-45%

---

### 13.4 Anti-Lock Braking System (ABS) Integration

**Reference:** [Control Engineering Practice (Tanelli et al., 2007)] → See references.md: Paper #42

**Slip Ratio Control:**

$$\lambda_{target} = 0.1 - 0.2$$ (optimal slip for maximum braking)

**Regenerative Torque Modulation:**

$$T_{regen}(k+1) = T_{regen}(k) - K_p(\lambda - \lambda_{target}) - K_d \Delta\lambda$$

**Wheel Slip:**

$$\lambda = \frac{v_{vehicle} - v_{wheel}}{v_{vehicle}}$$

---

### 13.5 Predictive Regenerative Braking

**Reference:** [IEEE Transactions on Transportation Electrification (Sandrini et al., 2017)] → See references.md: Paper #10

**Look-Ahead Braking Strategy:**

$$T_{regen,planned}(s) = f(v_{current}, v_{target}(s), \text{road grade}(s))$$

**Where:** s = position along route

**Optimal Deceleration Profile:**

$$a_{optimal}(s) = -\frac{v_{target}^2(s) - v^2(s)}{2 \Delta s}$$

**Subject to:** $a_{min} \leq a \leq a_{comfort}$

---

## 14. Power Management

### 14.1 Powertrain Efficiency

**Reference:** [Advanced Electric Drive Vehicles, Chapter 2] → See references.md: Textbook #7

**Traction torque from powertrain:**

$$T_p = T_{en} \times i_t \times i_0 \times \eta_p$$

**Where:**
- T_en = engine/motor torque (Nm)
- i_t = transmission ratio
- i_0 = differential ratio
- η_p = total efficiency [EV: 0.85-0.95, ICE: 0.15-0.30]

---

### 14.2 Energy Ratio (for SRM)

**Reference:** [Electric and Hybrid Vehicles: Design Fundamentals, Chapter 6] → See references.md: Textbook #6

$$ER = \frac{W}{W + R}$$

**Where:**
- W = energy converted to mechanical work
- R = energy returned to source (with regenerative converter)

---

## 15. Vehicle-to-Grid (V2G) and Smart Charging

### 15.1 Bidirectional Power Flow

**Reference:** [IEEE Transactions on Smart Grid (Yilmaz & Krein, 2013)] → See references.md: Paper #21

**Charging Power:**

$$P_{charge}(t) = V_{grid}(t) I_{charge}(t) \eta_{charger} \cos(\phi)$$

**Discharging Power:**

$$P_{discharge}(t) = V_{battery} I_{discharge}(t) \eta_{inverter} \eta_{charger}$$

**Where:**
- φ = power factor angle
- η_charger = charger efficiency [0.90-0.95]
- η_inverter = inverter efficiency [0.92-0.96]

---

### 15.2 Optimal Charging Schedule

**Reference:** [Applied Energy (Sortomme & El-Sharkawi, 2011)] → See references.md: Paper #34

**Cost Minimization:**

$$\min J = \sum_{t=1}^{T} [c(t) P_{charge}(t) \Delta t]$$

**Subject to:**
- $SOC(T) = SOC_{target}$
- $P_{min} \leq P_{charge}(t) \leq P_{max}$
- $SOC_{min} \leq SOC(t) \leq SOC_{max}$

**Where:** c(t) = electricity price at time t ($/kWh)

**💻 MATLAB:** Use `fmincon()` or `linprog()` for time-of-use optimization

---

### 15.3 Battery Degradation Cost

**Reference:** [Journal of Energy Storage (Xu et al., 2018)] → See references.md: Paper #31

**Degradation Cost per kWh:**

$$C_{deg} = \frac{C_{battery}}{L_{cycle} \times DOD \times Q_{nom}} \times k_{temp} \times k_{rate}$$

**Where:**
- C_battery = battery replacement cost ($) [Typical: $150-200/kWh in 2024]
- L_cycle = cycle life (cycles) [Typical: 1000-3000 at 80% DOD]
- DOD = depth of discharge
- k_temp = temperature degradation factor
- k_rate = C-rate degradation factor

**Total Cost Function:**

$$C_{total} = C_{electricity} + C_{degradation}$$

---

### 15.4 Grid Services Revenue

**Reference:** [IEEE Transactions on Power Systems (Kempton & Tomic, 2005)] → See references.md: Paper #24

**Frequency Regulation Revenue:**

$$R_{reg} = P_{capacity} \times \text{Price}_{capacity} + E_{delivered} \times \text{Price}_{energy}$$

**Peak Shaving Value:**

$$V_{peak} = (P_{peak,without} - P_{peak,with}) \times \text{Price}_{demand} \times N_{months}$$

---

### 15.5 Smart Charging Power Limit

**Reference:** [Electric Power Systems Research (Clement-Nyns et al., 2010)] → See references.md: Paper #45

**Transformer Capacity Constraint:**

$$\sum_{i=1}^{N} P_{charge,i}(t) \leq P_{transformer,max} - P_{baseline}(t)$$

**Voltage Drop Constraint:**

$$\Delta V = \frac{R \cdot P + X \cdot Q}{V_{nom}} \leq \Delta V_{max}$$

**Where:**
- R, X = line resistance and reactance (Ω)
- P, Q = active and reactive power (W, VAR)

---

## 16. Suspension and Ride Dynamics

### 16.1 Quarter Car Model

**Reference:** [Vehicle Dynamics and Control (Rajesh Rajamani, 2nd Edition, 2012)] → See references.md: Textbook #4

**Sprung Mass Dynamics:**

$$m_s \ddot{z}_s = -k_s(z_s - z_u) - c_s(\dot{z}_s - \dot{z}_u)$$

**Unsprung Mass Dynamics:**

$$m_u \ddot{z}_u = k_s(z_s - z_u) + c_s(\dot{z}_s - \dot{z}_u) - k_t(z_u - z_r)$$

**Where:**
- m_s = sprung mass (kg) [~90% of vehicle mass]
- m_u = unsprung mass (kg) [~10% of vehicle mass]
- k_s = suspension stiffness (N/m) [15,000-30,000 N/m typical]
- c_s = damping coefficient (N⋅s/m)
- k_t = tire stiffness (N/m) [150,000-250,000 N/m]
- z_r = road input (m)

---

### 16.2 Active Suspension Control

**Reference:** [Automatica (Hrovat, 1997)] → See references.md: Paper #47

**Skyhook Control Law:**

$$F_{active} = -c_{sky} \dot{z}_s$$

**LQR Optimal Control:**

$$F_{active} = -K [z_s - z_u,\ \dot{z}_s - \dot{z}_u,\ z_u - z_r,\ \dot{z}_u]^T$$

**💻 MATLAB:** Design K using `lqr(A,B,Q,R)`

---

### 16.3 Road Disturbance PSD

**Reference:** [ISO 8608:2016] → See references.md: Standard #10

**Power Spectral Density:**

$$S(\Omega) = S(\Omega_0) \left(\frac{\Omega}{\Omega_0}\right)^{-w}$$

**Where:**
- Ω = spatial frequency (cycles/m)
- Ω₀ = reference spatial frequency (0.1 cycles/m)
- w = waviness [typically 2]
- S(Ω₀) = road roughness coefficient

**Road Classes:**

| Class | Quality | S(Ω₀) [×10⁻⁶ m³] |
|-------|---------|------------------|
| A | Very good | 16 |
| B | Good | 64 |
| C | Average | 256 |
| D | Poor | 1024 |
| E | Very poor | 4096 |

---

## 17. Multi-Objective Optimization for EV Design

### 17.1 Pareto Optimality

**Reference:** [Structural and Multidisciplinary Optimization (Marler & Arora, 2004)] → See references.md: Textbook #17

**Multi-Objective Problem:**

$$\min \mathbf{F}(\mathbf{x}) = [f_1(\mathbf{x}), f_2(\mathbf{x}), \ldots, f_n(\mathbf{x})]$$

**Subject to:**
- $g_i(\mathbf{x}) \leq 0$
- $h_j(\mathbf{x}) = 0$

**Typical EV Objectives:**

$$f_1(\mathbf{x}) = \text{Energy Consumption}$$
$$f_2(\mathbf{x}) = -\text{Acceleration Performance}$$
$$f_3(\mathbf{x}) = \text{Total Cost}$$
$$f_4(\mathbf{x}) = \text{Battery Degradation}$$

---

### 17.2 Weighted Sum Method

**Reference:** [Engineering Optimization (Rao, 2009)] → See references.md: Textbook #18

**Combined Objective:**

$$J = w_1 \frac{E}{E_{ref}} + w_2 \frac{t_{accel}}{t_{ref}} + w_3 \frac{\text{Cost}}{\text{Cost}_{ref}}$$

**Subject to:** $\sum w_i = 1,\ w_i \geq 0$

---

### 17.3 Genetic Algorithm for EV Optimization

**Reference:** [IEEE Transactions on Evolutionary Computation (Deb et al., 2002)] → See references.md: Paper #26

**Design Variables:**

$$\mathbf{x} = [P_{motor}, Q_{battery}, m_{vehicle}, C_d, i_{gear}]$$

**Fitness Function:**

$$\text{Fitness} = \frac{1}{1 + J(\mathbf{x})}$$

**Constraints Handling:**

$$\text{Penalty} = \sum \max(0, g_i(\mathbf{x}))^2$$
$$F_{penalized} = F(\mathbf{x}) + r_{penalty} \times \text{Penalty}$$

**💻 MATLAB:** Use Global Optimization Toolbox with `ga()` or `gamultiobj()`

---

## 18. Drive Cycle Analysis and Testing

### 18.1 Standard Drive Cycles

**Reference:** [SAE J1634 Standard] → See references.md: Standard #1

**UDDS (Urban Dynamometer Driving Schedule):**
- Distance: 11.99 km
- Duration: 1372 s
- Average Speed: 31.5 km/h
- Maximum Speed: 91.2 km/h
- Idle time: 18%

**HWFET (Highway Fuel Economy Test):**
- Distance: 16.45 km
- Duration: 765 s
- Average Speed: 77.4 km/h
- Maximum Speed: 96.4 km/h
- No idle time

**WLTP (Worldwide Harmonized Light Vehicles Test Procedure):**
- Distance: 23.27 km
- Duration: 1800 s
- Average Speed: 46.5 km/h
- Maximum Speed: 131.3 km/h

---

### 18.2 Energy Consumption Calculation

**Reference:** [SAE J1634 (2012)] → See references.md: Standard #1

**Range on Full Charge:**

$$\text{Range} = \frac{E_{usable} \times \eta_{overall}}{E_{cycle}}$$

**Where:**
- E_usable = usable battery energy (kWh)
- E_cycle = energy consumed per cycle (kWh)

**Equivalent Fuel Economy:**

$$\text{MPGe} = \frac{33.7 \text{ kWh/gal}}{E_{consumption} \text{ in kWh/mile}}$$

**Example:**
- E_consumption = 0.25 kWh/mile → MPGe = 135

---

### 18.3 Aggressive Driving Factor

**Reference:** [Transportation Research Part D (De Vlieger et al., 2000)] → See references.md: Paper #39

**Energy Increase:**

$$E_{aggressive} = E_{normal} (1 + k_{accel} \times RPA + k_{brake} \times RPA)$$

**Where:**
- RPA = Relative Positive Acceleration
- k_accel, k_brake = sensitivity factors [Typical: 0.5-1.5]

**RPA Calculation:**

$$RPA = \frac{\sum [v(t) \times a(t)]}{\text{Distance}}$$ (for a(t) > 0)

---

### 18.4 Real-World Range Adjustment

**Reference:** [Environmental Science & Technology (Fiori et al., 2016)] → See references.md: Paper #40

**Adjusted Range:**

$$\text{Range}_{real} = \text{Range}_{test} \times f_{temp} \times f_{terrain} \times f_{HVAC} \times f_{traffic}$$

**Temperature Factor:**

$$f_{temp} = 1 - k_{temp} |T_{ambient} - T_{optimal}|^2$$

**Typical:**
- k_temp = 0.0001 /°C²
- T_optimal = 21.5°C

**Example Factors:**
- f_temp @ -10°C ≈ 0.70
- f_HVAC (heating) ≈ 0.80
- f_terrain (hilly) ≈ 0.90
- **Total: 0.70 × 0.80 × 0.90 = 0.50** (50% range reduction in winter!)

---

## 19. Electromagnetic Compatibility and Power Quality

### 19.1 Total Harmonic Distortion (THD)

**Reference:** [IEEE Standard 519-2014] → See references.md: Standard #16

**Voltage THD:**

$$THD_V = \frac{\sqrt{\sum_{h=2}^{\infty} V_h^2}}{V_1} \times 100\%$$

**Current THD:**

$$THD_I = \frac{\sqrt{\sum_{h=2}^{\infty} I_h^2}}{I_1} \times 100\%$$

**Where:** h = harmonic order

**IEEE 519 Limits:**
- Voltage THD: < 5% at PCC (Point of Common Coupling)
- Current THD: < 8% for I_sc/I_L < 20
- Current THD: < 15% for I_sc/I_L > 1000

---

### 19.2 Power Factor

**Reference:** [Electric Power Systems (Weedy et al., 2012)] → See references.md: Textbook #20

**Total Power Factor:**

$$PF = \frac{P}{S} = \frac{P}{\sqrt{P^2 + Q^2}}$$

**Displacement Power Factor:**

$$DPF = \cos(\phi) = \frac{P_1}{S_1}$$

**Distortion Power Factor:**

$$\text{Distortion PF} = \frac{1}{\sqrt{1 + THD_I^2}}$$

**Relationship:**

$$PF = DPF \times \text{Distortion PF}$$

---

### 19.3 EMI Filter Design

**Reference:** [IEEE Transactions on Electromagnetic Compatibility (Nave, 1991)] → See references.md: Paper #25

**Common-Mode Impedance:**

$$Z_{CM} = j\omega L_{CM} + \frac{1}{j\omega C_{CM}}$$

**Differential-Mode Impedance:**

$$Z_{DM} = j\omega L_{DM} + \frac{1}{j\omega C_{DM}}$$

**Cutoff Frequency:**

$$f_{cutoff} = \frac{1}{2\pi\sqrt{LC}}$$

**Typical Design:**
- f_cutoff ≈ 10-30 kHz (below switching frequency)
- L_CM: 1-10 mH
- C_CM: 1-10 nF (X-capacitors, class X2)

---

## 20. Safety and Fault Detection

### 20.1 Battery Safety Monitoring

**Reference:** [Journal of Power Sources (Dey et al., 2019)] → See references.md: Paper #30

**Voltage Consistency Check:**

$$\sigma_{voltage} = \sqrt{\frac{\sum (V_i - V_{avg})^2}{N}}$$

**Alert if:** $\sigma_{voltage} > V_{threshold}$ [Typical: 50-100 mV]

**Temperature Gradient:**

$$\Delta T_{max} = \max|T_i - T_j|$$ for all cells i,j

**Alert if:** $\Delta T_{max} > \Delta T_{threshold}$ [typically 5°C]

---

### 20.2 Insulation Resistance Monitoring

**Reference:** [ISO 6469-3:2018] → See references.md: Standard #8

**Minimum Insulation Resistance:**

$$R_{iso,min} = \begin{cases}
100 \text{ Ω/V} \times V_{system} & \text{for } V_{system} \leq 500V \\
500 \text{ Ω/V} \times V_{system} & \text{for } V_{system} > 500V
\end{cases}$$

**Insulation Fault Detection:**

$$R_{iso} = \frac{V_{battery}}{I_{leakage}}$$

**Alert if:** $R_{iso} < R_{iso,min}$

**Example:** 400V system → R_iso,min = 40 kΩ

---

### 20.3 Motor Fault Detection

**Reference:** [IEEE Transactions on Industrial Electronics (Benbouzid, 2000)] → See references.md: Paper #16

**Current Signature Analysis:**

$$I_{spectrum} = \text{FFT}(i_{phase}(t))$$

**Fault Indicators:**

**Bearing fault frequency:**
$$f_{bearing} = \frac{f_e N_{balls}}{2} \left(1 - \frac{d}{D} \cos(\alpha)\right)$$

**Rotor bar fault frequency:**
$$f_{rotor\ bar} = f_e (1 \pm s) N_{bars}$$

**Where:**
- f_e = electrical frequency
- s = slip
- N_balls, N_bars = number of balls/bars

---

### 20.4 Functional Safety (ISO 26262)

**Reference:** [ISO 26262:2018] → See references.md: Standard #9

**Automotive Safety Integrity Level (ASIL):**

$$\text{ASIL} = f(\text{Severity}, \text{Exposure}, \text{Controllability})$$

**Failure Rate Target:**

$$\lambda_{target} < \begin{cases}
10^{-8} \text{ failures/hour} & \text{for ASIL D} \\
10^{-7} \text{ failures/hour} & \text{for ASIL C}
\end{cases}$$

**Diagnostic Coverage:**

$$DC = \frac{\lambda_{detected}}{\lambda_{total}} \times 100\%$$

**ASIL Requirements:**
- **ASIL D:** DC > 99% (safety-critical: braking, steering)
- **ASIL C:** DC > 97%
- **ASIL B:** DC > 90%
- **ASIL A:** DC > 60%

---

## MATLAB Implementation Guide

### General Workflow

1. **Define Vehicle Parameters**
```matlab
% Vehicle parameters
m = 1500;        % kg
Cd = 0.28;       % -
A = 2.3;         % m^2
fr = 0.010;      % -
rho = 1.2;       % kg/m^3
```

2. **Load Drive Cycle**
```matlab
% Load UDDS cycle
load('udds.mat'); % Contains time, speed vectors
t = udds.time;
V = udds.speed / 3.6; % Convert km/h to m/s
```

3. **Calculate Forces**
```matlab
% Resistance forces
a = gradient(V) ./ gradient(t);
F_aero = 0.5 * rho * Cd * A * V.^2;
F_roll = m * 9.81 * fr;
F_trac = m * a + F_aero + F_roll;
```

4. **Calculate Energy**
```matlab
% Power and energy
P_trac = F_trac .* V;
E_total = trapz(t, P_trac) / 3.6e6; % kWh
fprintf('Energy: %.2f kWh\n', E_total);
```

### Advanced: Battery SOC Simulation

```matlab
% Battery parameters
Q_nom = 75;      % kWh
V_nom = 400;     % V
SOC0 = 1.0;      % Initial SOC

% Coulomb counting
Ah_nom = Q_nom * 1000 / V_nom; % Ah
I = P_trac / V_nom;            % Current
SOC = SOC0 - cumtrapz(t, I) / (3600 * Ah_nom);

% Plot
plot(t, SOC * 100);
xlabel('Time (s)');
ylabel('SOC (%)');
```

### Simulink Implementation Tips

1. **Use Simscape for physical modeling** (motor, battery)
2. **Implement controllers in MATLAB Function blocks**
3. **Use Lookup Tables for efficiency maps** (motor, battery)
4. **Enable fixed-step solver** for real-time applications
5. **Log signals to workspace** for post-processing

### Useful MATLAB Functions

| Function | Application |
|----------|-------------|
| `ode45()` | Solve differential equations (dynamics) |
| `lsim()` | Linear system simulation |
| `interp1()` / `interp2()` | Lookup tables (efficiency maps) |
| `fmincon()` | Constrained optimization (MPC, torque distribution) |
| `ga()` | Genetic algorithm (design optimization) |
| `extendedKalmanFilter()` | State estimation (SOC, SOH) |

---

## Quick Reference Tables

### Typical EV Parameters

| Parameter | Symbol | Typical Range | Units |
|-----------|--------|---------------|-------|
| Vehicle mass | m | 1200-2500 | kg |
| Drag coefficient | C_d | 0.22-0.35 | - |
| Frontal area | A | 2.0-2.8 | m² |
| Rolling resistance | f_r | 0.008-0.015 | - |
| Motor power | P_motor | 50-350 | kW |
| Battery capacity | E_battery | 40-100 | kWh |
| Battery voltage | V_battery | 300-800 | V |
| Motor efficiency | η_motor | 0.90-0.96 | - |
| Inverter efficiency | η_inverter | 0.95-0.98 | - |

### Common Constants

| Constant | Symbol | Value | Units |
|----------|--------|-------|-------|
| Gravitational acceleration | g | 9.81 | m/s² |
| Air density (sea level, 20°C) | ρ | 1.2 | kg/m³ |
| Energy per gallon gasoline | - | 33.7 | kWh |
| Gas constant | R | 8.314 | J/mol⋅K |
| Specific heat of air | c_p | 1005 | J/kg⋅K |

### Unit Conversions

| From | To | Multiply by |
|------|-----|-------------|
| km/h | m/s | 1/3.6 |
| mph | m/s | 0.447 |
| kWh | J | 3.6×10⁶ |
| Ah | C (Coulombs) | 3600 |
| hp | kW | 0.746 |
| lb-ft | Nm | 1.356 |

### Performance Benchmarks

| Metric | Compact EV | Mid-size EV | Performance EV |
|--------|------------|-------------|----------------|
| 0-100 km/h | 8-10 s | 6-8 s | 2-4 s |
| Top speed | 140-160 km/h | 160-180 km/h | 200-250 km/h |
| Range (WLTP) | 200-300 km | 300-450 km | 400-600 km |
| Energy consumption | 13-16 kWh/100km | 16-20 kWh/100km | 18-25 kWh/100km |
| DC fast charging | 50-100 kW | 100-150 kW | 150-350 kW |

---

## Notes on Usage and Assumptions

### 1. Consistent Units
⚠️ **All equations require consistent SI units unless otherwise specified.**
- Mass: kg
- Force: N
- Power: W
- Energy: J (or kWh where noted)
- Speed: m/s
- Torque: Nm

### 2. Standard Conditions
Unless specified, assume:
- Air density: ρ = 1.2 kg/m³ (sea level, 20°C)
- Gravitational acceleration: g = 9.81 m/s²
- Battery temperature: 25°C
- Powertrain efficiency: η_p = 0.90 for EVs

### 3. Model Validity
- **Linear tire models:** Valid for |α| < 5° (low lateral acceleration)
- **Pacejka models:** Valid for full range, but requires parameter identification
- **Steady-state equations:** Valid when dV/dt ≈ 0
- **Battery models:** Valid within SOC 10-90% for linear approximations

### 4. Numerical Integration
Equations requiring integration (energy, SOC, acceleration time):
- Use `trapz()` for discrete data
- Use `integral()` for continuous functions
- Use `ode45()` for differential equations
- Recommended time step: Δt ≤ 0.1 s for drive cycles

### 5. Safety Margins
For design and validation:
- **Thermal limits:** Use 80% of max continuous rating
- **Current limits:** Peak = 2-3× continuous
- **Voltage limits:** Stay within ±10% of nominal
- **SOC operating window:** 10-90% for longevity

### 6. Temperature Effects
Battery and motor performance degrades with temperature:
- **-20°C:** 40-50% capacity loss, 2-3× resistance increase
- **0°C:** 20-30% capacity loss, 1.5× resistance increase
- **25°C:** Nominal performance (reference temperature)
- **45°C:** Accelerated aging, reduced power capability
- **>60°C:** Safety concern, require active cooling

### 7. Model Hierarchies
Choose model complexity based on application:

**Level 1 - Conceptual Design:**
- Quasi-static models (1.1-1.8)
- Average efficiencies
- Drive cycle energy (10.1)

**Level 2 - System Simulation:**
- Dynamic models (2.1-2.5, 9.1-9.5)
- Lookup table efficiencies (10.3)
- Thermal models (11.3)

**Level 3 - Real-Time Control:**
- Reduced-order models
- MPC/optimization (12.1-12.5)
- State estimation (11.1-11.2)

**Level 4 - Detailed Analysis:**
- High-fidelity FEA (not covered here)
- Transient thermal (11.3 extended)
- Detailed chemistry models

---

## Revision History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2025 | Initial professional compilation | EV Research Team |

---

## Acknowledgments

This mathematical reference guide synthesizes equations from:
- **20 leading textbooks** in vehicle dynamics and EV engineering
- **73 peer-reviewed journal papers** from IEEE, Elsevier, and others
- **31 international standards** (SAE, ISO, IEC, IEEE, UN ECE)

See `references.md` for complete bibliography with ISBNs, DOIs, and access information.

Special thanks to the global EV research community for advancing the theoretical foundations that make this compilation possible.

---

## For Questions and Contributions

- **Technical clarifications:** Consult original sources in `references.md`
- **MATLAB implementation help:** See Section 24 and code examples
- **Errata and updates:** Submit via academic repository
- **Additional models:** Suggest via institutional channels

---

**Document Status:** Publication-Ready for Master's Level Education
**Coverage:** Comprehensive EV engineering mathematics (1992-2025)
**Companion Document:** `references.md` (124 sources)
**MATLAB Compatibility:** R2020b and later recommended

---

**End of Mathematical Models Guide**
