# Point Reactor Kinetics Simulation

**Course:** NEM 394 - Engineering Project II  
**Department:** Nuclear Engineering, Hacettepe University  
**Author:** Emre Sakarya

## 📌 Project Overview

This project simulates the time-dependent behavior of a nuclear reactor using the **Point Reactor Kinetics Equations** with a **single-group delayed neutron** approximation. The study investigates the reactor's response to piecewise constant reactivity changes (positive and negative steps).

The simulation implements three different solution methods to compare numerical accuracy, stability, and error propagation:
1.  **Analytical Solution:** Using matrix eigenvalues and eigenvectors (Reference solution).
2.  **Heun's Method:** Euler Predictor-Corrector (2nd order accuracy).
3.  **Runge-Kutta 4 (RK4):** 4th order numerical integration (high precision).

Additionally, the project analyzes the **stiffness** of the system, demonstrating the significant time-scale difference between neutron density changes and precursor concentration changes.

## ⚙️ Mathematical Model

The dynamics of the reactor are modeled using the following system of differential equations:

$$
\frac{dn(t)}{dt} = \left( \frac{\rho(t) - \beta}{\Lambda} \right) n(t) + \lambda C(t)
$$

$$
\frac{dC(t)}{dt} = \frac{\beta}{\Lambda} n(t) - \lambda C(t)
$$

### Parameters
* **$\beta$ (Delayed neutron fraction):** 0.007
* **$\Lambda$ (Neutron generation time):** $10^{-3}$ s
* **$\lambda$ (Decay constant):** $0.08$ s⁻¹
* **Initial Condition:** Equilibrium at $n_0 = 10.0$

### Reactivity Scenario ($\rho(t)$)
The system undergoes a positive reactivity step followed by a negative step:
* **0 s $\le t <$ 10 s:** $\rho = 0.05 \beta$ (Positive Step)
* **10 s $\le t <$ 20 s:** $\rho = -0.05 \beta$ (Negative Step)
* **$t \ge$ 20 s:** $\rho = 0$ (Return to zero)

## 📂 Repository Structure

```text
.
├── src/                                # Source code for solver algorithms (Heun, RK4, Analytical)
├── Point_Reactor_Kinetics_Report.pdf   # Full academic report with derivations and analysis
├── README.md                           # Project documentation
├── main.py                             # Main execution script for the simulation
├── requirements.txt                    # Python dependencies
└── simulation_result.png               # Output graph of the simulation
```

## 🚀 Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/EmreSakarya/Point-Reactor-Kinetics.git
    cd Point-Reactor-Kinetics
    ```

2.  **Install dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the simulation:**
    ```bash
    python main.py
    ```

## 📊 Key Results

* **Accuracy:** The RK4 method proved to be significantly more accurate than Heun's method. At a time step of $h=0.01s$, RK4 reduced the absolute error to the order of $10^{-8}$, whereas Heun's error was around $10^{-3}$.
* **Stiffness Analysis:** The system is identified as "stiff" with a stiffness ratio (eigenvalue ratio) of approximately **1620**.
* **Dynamics:** Neutron density ($n(t)$) responds almost instantaneously to reactivity changes (approx. 143 times faster rate of change), while precursor concentration ($C(t)$) acts as a stabilizing "inertia" with a delayed response.

![Simulation Results](simulation_result.png)
*(Figure: Comparison of Neutron Density and Precursor Concentration over time)*

## 📚 References

This project references standard nuclear engineering texts found in the report:
* *Lamarsh, J. R., & Baratta, A. J.* - Introduction to Nuclear Engineering
* *Hetrick, D. L.* - Dynamics of Nuclear Reactors
* *Stacey, W. M.* - Nuclear Reactor Physics
