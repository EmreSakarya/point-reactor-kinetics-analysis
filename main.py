# main.py
import matplotlib.pyplot as plt
from src.config import N0, C0
from src.model import point_kinetics_equations
from src.solvers import rk4_solver, heun_solver

def run_simulation():
    print(">>> Starting Nuclear Reactor Kinetics Simulation...")

    # Simulation Settings
    t_final = 30.0
    dt = 0.01
    y_initial = [N0, C0]

    # 1. RK4 Solution
    print(f"Running RK4 Solver (dt={dt}s)...")
    t_rk4, y_rk4 = rk4_solver(point_kinetics_equations, (0, t_final), y_initial, dt)
    n_rk4 = y_rk4[:, 0]

    # 2. Heun Solution
    print(f"Running Heun Solver (dt={dt}s)...")
    t_heun, y_heun = heun_solver(point_kinetics_equations, (0, t_final), y_initial, dt)
    n_heun = y_heun[:, 0]

    # 3. Visualization
    plt.figure(figsize=(12, 7))

    plt.plot(t_rk4, n_rk4, 'b-', linewidth=2, label='Neutron Density (RK4)')
    plt.plot(t_heun, n_heun, 'r--', linewidth=1.5, label='Neutron Density (Heun)')

    plt.axvline(10, color='gray', linestyle=':', alpha=0.5)
    plt.axvline(20, color='gray', linestyle=':', alpha=0.5)

    ymax = max(n_rk4)
    plt.text(5, ymax*0.95, r'$\rho = +0.05\beta$', ha='center', bbox=dict(facecolor='white', alpha=0.8))
    plt.text(15, ymax*0.95, r'$\rho = -0.05\beta$', ha='center', bbox=dict(facecolor='white', alpha=0.8))
    plt.text(25, ymax*0.95, r'$\rho = 0$', ha='center', bbox=dict(facecolor='white', alpha=0.8))

    plt.title("Point Reactor Kinetics: Transient Response Analysis")
    plt.xlabel("Time (s)")
    plt.ylabel("Neutron Density $n(t)$")
    plt.legend()
    plt.grid(True, which='both', linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.savefig("simulation_result.png", dpi=300)
    print("Done! Plot saved as 'simulation_result.png'")
    plt.show()

if __name__ == "__main__":
    run_simulation()
