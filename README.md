# Point Reactor Kinetics Analysis ⚛️

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat&logo=python&logoColor=white)
![Scientific Computing](https://img.shields.io/badge/Scientific%20Computing-NumPy%20%7C%20SciPy-orange)
![License](https://img.shields.io/badge/License-MIT-green)

This project investigates the **time-dependent behavior of a nuclear reactor** using the **point reactor kinetics equations** with a **single group of delayed neutrons**.

The system is solved using both **analytical** and **numerical methods** (RK4, Heun) to study **reactor transients, numerical accuracy, stiffness, and error propagation** under piecewise-constant reactivity insertions.

---

## 📊 Simulation Results
![Reactor Transient Response](simulation_result.png)
*Figure 1: Comparison of Neutron Density response under step reactivity changes (Positive -> Negative -> Zero).*

---

## 🎯 Objectives
- **Model** the reactor dynamics using coupled differential equations (Neutrons & Precursors).
- **Implement** numerical solvers (RK4 & Heun) from scratch.
- **Analyze** the "Stiffness" of the system ($\Lambda$ vs $\lambda$ time scales).
- **Validate** stability limits of explicit methods against Analytical Benchmark.

---

## 🔬 Physical Model (Point Kinetics)

The governing coupled differential equations derived in the report:

$$
\frac{dn(t)}{dt} = \frac{\rho(t) - \beta}{\Lambda} n(t) + \lambda C(t)
$$

$$
\frac{dC(t)}{dt} = \frac{\beta}{\Lambda} n(t) - \lambda C(t)
$$

**Parameters:**
- $\beta = 0.007$ (Delayed Neutron Fraction)
- $\Lambda = 10^{-3} s$ (Generation Time)
- $\lambda = 0.08 s^{-1}$ (Decay Constant)

---

## 📁 Repository Structure

The project uses a modular architecture for scalability:

```text
point-reactor-kinetics-analysis/
│
├── src/
│   ├── config.py       # Physical constants & Reactivity scenario parameters
│   ├── model.py        # Implementation of Point Kinetics differential equations
│   └── solvers.py      # Numerical algorithms (RK4, Heun)
│
├── main.py             # Main execution script (Simulation & Visualization)
├── Pointkinetic.pdf    # Full Project Report & Analytical Derivation
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
