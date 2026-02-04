# Point Reactor Kinetics Solver ⚛️

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

## 📌 Overview
This repository contains a numerical simulation framework for solving **Point Reactor Kinetics Equations (PKE)** with one group of delayed neutrons. The project was developed as part of the **NEM 394** course to analyze the transient behavior of nuclear reactors under various reactivity insertion scenarios (step, ramp, etc.).

The solver implements high-precision numerical integration methods (**Runge-Kutta 4th Order**) and benchmarks them against analytical solutions to evaluate error propagation and stability in stiff systems.

---

## ⚙️ Mathematical Model
The code solves the coupled system of stiff ordinary differential equations (ODEs) representing the neutron density ($n$) and precursor concentration ($C$):

$$
\frac{dn(t)}{dt} = \frac{\rho(t) - \beta}{\Lambda} n(t) + \lambda C(t)
$$

$$
\frac{dC(t)}{dt} = \frac{\beta}{\Lambda} n(t) - \lambda C(t)
$$

Where:
* $\rho(t)$: Reactivity insertion
* $\beta$: Delayed neutron fraction
* $\Lambda$: Neutron generation time
* $\lambda$: Precursor decay constant

---

## 🧮 Numerical Methods Implemented

The project explicitly compares two numerical integration schemes against the exact analytical solution (Eigenvalue/Eigenvector method):

1.  **Runge-Kutta 4th Order (RK4):**
    * Primary solver used for high-precision results.
    * Demonstrated global truncation error of $O(h^4)$.
    * Highly stable for standard transient analysis.

2.  **Heun’s Method (Predictor-Corrector):**
    * Implemented to demonstrate the Euler-based prediction logic.
    * Used for error comparison analysis against RK4.

### 📉 Stiffness Analysis
The project also investigates the **Stiffness Ratio** of the system. It demonstrates that for large reactivity insertions, the system becomes "stiff" due to the large difference between the prompt neutron lifetime and the precursor mean lifetime. The solver's time-step ($\Delta t$) sensitivity was analyzed to prevent numerical instability.

---

## 🚀 Key Results & Visualizations

*(Place your simulation plots here. Example: Neutron Density vs Time)*

### 1. Transient Response (Step Insertion)
The comparison between Analytical, RK4, and Heun methods shows excellent agreement for small $\Delta t$.

![Neutron Density Plot](relative_path_to_your_plot_image.png)
*(Example: Response to 0.003 $\delta k/k$ step input)*

### 2. Error Analysis
Comparison of relative error between numerical approximations and the exact analytical solution.

![Error Analysis](relative_path_to_your_error_plot.png)

---

## 💻 Installation & Usage

### Dependencies
The simulation relies on standard scientific Python libraries:
```bash
pip install numpy matplotlib scipy
