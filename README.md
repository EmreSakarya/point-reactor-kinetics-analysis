# Point Reactor Kinetics Analysis (One Group Delayed Neutrons)

![Simulation Results](simulation_result.png)

## About the Project

This project implements the **Point Reactor Kinetic Equations** using the **Single-Group Delayed Neutron** approximation. It was developed as part of the *NEM 394 - Engineering Project II* course at **Hacettepe University, Department of Nuclear Engineering**.

The primary objective is to analyze the reactor's time-dependent behavior under piecewise constant reactivity changes. The project compares the **exact analytical solution** against two numerical integration methods: **Heun's Method** (Predictor-Corrector) and the **Runge-Kutta 4th Order (RK4)** method. Additionally, it provides a mathematical proof of the system's "stiffness" by analyzing the time scale differences between neutron density and precursor concentration.

## Features

* **Analytical Solution:** Exact solution of the differential equation system using matrix eigenvalue/eigenvector decomposition.
* **Numerical Methods:**
    * **Heun's Method:** Second-order accurate Euler predictor-corrector approach.
    * **Runge-Kutta 4 (RK4):** Fourth-order accurate method for high-precision simulations.
* **Error Analysis:** Calculation of absolute and relative errors for various time steps (h).
* **Stiffness Analysis:** Mathematical demonstration of the stiff nature of the equations by comparing the time derivatives (dn/dt vs dC/dt) and system eigenvalues.

## Mathematical Model

The dynamics of the reactor are modeled using the following system of differential equations:

$$
\frac{dn(t)}{dt} = \left( \frac{\rho(t) - \beta}{\Lambda} \right) n(t) + \lambda C(t)
$$

$$
\frac{dC(t)}{dt} = \frac{\beta}{\Lambda} n(t) - \lambda C(t)
$$

### Physical Parameters
* **Beta (Delayed Neutron Fraction):** 0.007
* **Lambda_decay (Decay Constant):** 0.08 1/s
* **Lambda_gen (Neutron Generation Time):** 0.001 s
* **n0 (Initial Neutron Density):** 10.0

### Reactivity Scenario
The system is subjected to a step reactivity function:
* **0 to 10 s:** Positive Step (0.05 * Beta)
* **10 to 20 s:** Negative Step (-0.05 * Beta)
* **20+ s:** Return to Equilibrium (0.0)

## Installation & Usage

To run this simulation on your local machine, you need Python installed along with standard scientific computing libraries.

### Prerequisites
* Python 3.x
* NumPy
* Matplotlib

### Setup
Clone the repository and install the dependencies:

    git clone https://github.com/yourusername/point-reactor-kinetics.git
    cd point-reactor-kinetics
    pip install numpy matplotlib

### Running the Simulation
Execute the main script to generate the data and plots:

    python main.py

*(Note: Ensure your script filename matches the command above, e.g., if your file is named `project_code.py`, run that instead.)*

## Results & Discussion

The analysis yielded the following key insights:

1.  **Accuracy:** The RK4 method demonstrated significantly higher accuracy than Heun's method. At a time step of h=0.01s, RK4 errors were on the order of 1e-8, whereas Heun errors were around 1e-3.
2.  **System Dynamics:** The neutron density n(t) responds instantly to reactivity steps (jumps), while the precursor concentration C(t) exhibits a delayed, smooth response due to the "inertia" effect.
3.  **Stiffness:** The analysis proved the system is stiff. Immediately after a reactivity step, the rate of change for neutrons (dn/dt) was found to be approximately **143 times faster** than that of the precursors (dC/dt). The eigenvalue ratio of the system matrix was calculated to be approximately **1620**, confirming the need for stable numerical solvers or small time steps.

## License & Contact

**Developer:** Emre Sakarya
**Institution:** Hacettepe University - Nuclear Engineering
**Date:** January 2026

This project is intended for educational and academic purposes.
