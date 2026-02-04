# src/model.py
import numpy as np
from src.config import BETA, LAMBDA_GEN, DECAY_CONST, RHO_STEP_1, RHO_STEP_2, RHO_STEP_3

def get_reactivity(t):
    """Piecewise constant reactivity function."""
    if t < 10.0:
        return RHO_STEP_1
    elif t < 20.0:
        return RHO_STEP_2
    else:
        return RHO_STEP_3

def point_kinetics_equations(t, y):
    """
    Point Kinetics Differential Equation System.
    y[0] = n(t) -> Neutron Density
    y[1] = C(t) -> Precursor Concentration
    """
    n, c = y
    rho = get_reactivity(t)

    dn_dt = ((rho - BETA) / LAMBDA_GEN) * n + DECAY_CONST * c
    dc_dt = (BETA / LAMBDA_GEN) * n - DECAY_CONST * c

    return np.array([dn_dt, dc_dt])
