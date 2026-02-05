# ⚛️ Point Reactor Kinetics Analysis (Single Delayed Neutron Group)

🔭 Project Overview

This repository presents a rigorous analytical and numerical investigation of the Point Reactor Kinetics Equations using a single-group delayed neutron model. The project was developed within the scope of the NEM 394 – Engineering Project II course at Hacettepe University, Department of Nuclear Engineering.

The primary objective of this study is to analyze the transient behavior of a nuclear reactor subjected to piecewise constant reactivity insertions. Both exact analytical solutions and standard numerical integration techniques are implemented in order to examine reactor dynamics, numerical accuracy, stiffness characteristics, and error propagation mechanisms.

The point reactor kinetics formulation provides a simplified yet physically insightful framework by neglecting spatial effects and focusing exclusively on time-dependent behavior. Despite this simplification, the resulting system exhibits strong stiffness due to the large separation between neutron and precursor time scales. This project explicitly demonstrates these properties through mathematical analysis and computational results.

***

📌 Key Features

• Analytical Solution: Exact closed-form solution derived using matrix formulation and eigenvalue–eigenvector decomposition  
• Numerical Solvers: Implementation and comparison of Heun’s Method (Euler predictor–corrector) and the classical fourth-order Runge–Kutta (RK4) method  
• Error Quantification: Absolute and relative error analysis with respect to time step size and reactivity discontinuities  
• Stiffness Analysis: Quantitative demonstration of stiffness through eigenvalue ratios and time-derivative comparisons  

***

📘 Mathematical Model

The reactor dynamics are governed by the point reactor kinetics equations with one delayed neutron group, describing the evolution of neutron density n(t) and delayed neutron precursor concentration C(t):

dn/dt = ((ρ(t) − β) / Λ) n + λ C  
dC/dt = (β / Λ) n − λ C  

The parameters used throughout the simulations are:

• β = 0.007  (Delayed neutron fraction)  
• λ = 0.08 s⁻¹  (Delayed neutron precursor decay constant)  
• Λ = 1 × 10⁻³ s  (Neutron generation time)  

The applied reactivity function is piecewise constant and defined as follows:

• ρ(t) = +0.05β for 0 ≤ t < 10 s  
• ρ(t) = −0.05β for 10 ≤ t < 20 s  
• ρ(t) = 0 for t ≥ 20 s  

This configuration enables direct observation of prompt and delayed reactor responses under both positive and negative reactivity insertions.

***

📊 Visual Demonstration

The figure provided in simulation_result.png illustrates the analytical solution of neutron density and delayed neutron precursor concentration as functions of time.

The neutron density exhibits sharp and rapid changes immediately following reactivity insertions, whereas the precursor concentration evolves in a smooth and delayed manner. This contrast directly reflects the stabilizing role of delayed neutrons and provides a clear visual manifestation of the stiffness inherent in point reactor kinetics systems.

***

🚀 Installation & Usage

To execute the simulation locally, follow the steps below.

1. Prerequisites

Ensure that Python 3 is installed together with the required scientific computing libraries:

pip install numpy matplotlib

2. Clone and Run

Clone the repository and execute the main simulation script:

git clone https://github.com/yourusername/point-reactor-kinetics.git  
cd point-reactor-kinetics  
python main.py  

If the main execution file uses a different name, replace main.py accordingly.

***

✅ Results & Key Findings

The computational and analytical results lead to the following conclusions:

• Numerical Accuracy: The fourth-order Runge–Kutta (RK4) method demonstrates significantly superior accuracy and stability compared to Heun’s method. For a time step of h = 0.01 s, RK4 achieves absolute errors on the order of 10⁻⁸, while Heun’s method remains on the order of 10⁻³.  
• System Stiffness: Immediately after a reactivity step, the magnitude of dn/dt is approximately 143 times greater than that of dC/dt. Eigenvalue analysis of the system matrix yields a stiffness ratio of approximately 1620, confirming that the governing equations form a strongly stiff system requiring robust numerical solvers.  
• Physical Interpretation: The delayed neutron precursors introduce a smoothing and stabilizing effect on reactor dynamics, significantly moderating the prompt neutron response to reactivity changes.

***

🎓 License & Contact

Author: Emre Sakarya  
Affiliation: Hacettepe University – Department of Nuclear Engineering  
Date: January 2026  

This repository is intended for academic and educational use. Proper attribution is appreciated when this work is referenced or used in derivative studies.
