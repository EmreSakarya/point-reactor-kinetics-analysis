
---

## Governing Equations

The point reactor kinetics equations with one delayed neutron group are given by:

dn(t)/dt = ((ρ(t) − β) / Λ) n(t) + λ C(t)

dC(t)/dt = (β / Λ) n(t) − λ C(t)

Where:
- n(t) is the neutron density
- C(t) is the delayed neutron precursor concentration
- ρ(t) is the reactivity
- β is the delayed neutron fraction
- Λ is the neutron generation time
- λ is the precursor decay constant

---

## Model Parameters

β = 0.007  
λ = 0.08 s⁻¹  
Λ = 1×10⁻³ s  
Initial neutron density n₀ = 10.0  

Initial equilibrium condition:

C(0) = β n₀ / (Λ λ)

---

## Reactivity Function

The applied reactivity is piecewise constant:

ρ(t) = 0.05β , 0 ≤ t < 10 s  
ρ(t) = −0.05β , 10 ≤ t < 20 s  
ρ(t) = 0 , t ≥ 20 s  

This reactivity scenario enables observation of prompt neutron response, delayed neutron smoothing effects, and the return to steady-state conditions.

---

## Solution Methods

### Analytical Solution
The system of equations is expressed in matrix form and solved analytically using eigenvalues and eigenvectors. Solutions are computed separately for each reactivity interval and matched using continuity conditions. The analytical solution serves as a reference for numerical error analysis.

### Heun Method (Euler Predictor–Corrector)
The Heun method is a second-order numerical integration technique. A predictor step is first computed using the forward Euler method, followed by a corrector step using the trapezoidal rule. Simulations are performed with multiple time step sizes to investigate convergence and error behavior.

### Runge–Kutta Method (RK4)
The fourth-order Runge–Kutta method provides higher accuracy and improved stability, particularly for stiff systems. Results show significantly smaller numerical errors compared to the Heun method for the same time step size.

---

## Error Analysis

Numerical solutions are compared against the analytical solution using absolute and relative error metrics:

Absolute error:
|n_num(t) − n_exact(t)|

Relative error:
|n_num(t) − n_exact(t)| / |n_exact(t)|

Results demonstrate that decreasing the time step reduces numerical error and that the RK4 method converges much faster than the Heun method.

---

## Physical Interpretation

Neutron density exhibits rapid and sharp changes in response to reactivity insertions, while delayed neutron precursor concentration evolves more smoothly and slowly. This behavior is caused by the large difference in characteristic time scales between neutron production and precursor decay.

Eigenvalue analysis reveals a stiffness ratio of approximately 1600, confirming that the system of equations is stiff and requires carefully selected numerical methods for accurate simulation.

---

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run the simulation:
python main.py

The script computes analytical and numerical solutions, performs error analysis, and generates plots of neutron density, precursor concentration, and error propagation.

---

## Report

A detailed academic report including mathematical derivations, numerical results, error analysis, and physical interpretation is provided in:

Point_Reactor_Kinetics_Report.pdf

---

## References

Duderstadt, J. J., & Hamilton, L. J. – Nuclear Reactor Analysis  
Lamarsh, J. R., & Baratta, A. J. – Introduction to Nuclear Engineering  
Stacey, W. M. – Nuclear Reactor Physics  
Chapra, S. C., & Canale, R. P. – Numerical Methods for Engineers  
IAEA (2011) – Reactor Kinetics and Control

---

## Author

Emre Sakarya  
Hacettepe University  
Department of Nuclear Engineering  

---

## License

This project is intended for academic and educational purposes only.
