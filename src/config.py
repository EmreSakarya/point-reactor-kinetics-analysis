# src/config.py

# --- PHYSICAL CONSTANTS ---
BETA = 0.007           # Delayed neutron fraction
LAMBDA_GEN = 1e-3      # Generation time [s]
DECAY_CONST = 0.08     # Decay constant [s^-1]

# Initial Conditions (Equilibrium)
N0 = 10.0              # Neutron Density
C0 = (BETA * N0) / (LAMBDA_GEN * DECAY_CONST)

# --- REACTIVITY SCENARIO (Step Functions) ---
RHO_STEP_1 = 0.05 * BETA   # 0 < t < 10
RHO_STEP_2 = -0.05 * BETA  # 10 < t < 20
RHO_STEP_3 = 0.0           # t > 20
