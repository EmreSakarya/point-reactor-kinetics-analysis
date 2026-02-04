# src/solvers.py
import numpy as np

def rk4_solver(func, t_span, y0, dt):
    """4th Order Runge-Kutta Method (High Precision)"""
    t_start, t_end = t_span
    n_steps = int(np.round((t_end - t_start) / dt))

    t_vals = np.linspace(t_start, t_end, n_steps + 1)
    y_vals = np.zeros((n_steps + 1, len(y0)))
    y_vals[0] = y0

    for i in range(n_steps):
        t = t_vals[i]
        y = y_vals[i]
        h = dt

        k1 = func(t, y)
        k2 = func(t + 0.5*h, y + 0.5*h*k1)
        k3 = func(t + 0.5*h, y + 0.5*h*k2)
        k4 = func(t + h, y + h*k3)

        y_vals[i+1] = y + (h/6.0) * (k1 + 2*k2 + 2*k3 + k4)

    return t_vals, y_vals

def heun_solver(func, t_span, y0, dt):
    """Heun's Predictor-Corrector Method"""
    t_start, t_end = t_span
    n_steps = int(np.round((t_end - t_start) / dt))

    t_vals = np.linspace(t_start, t_end, n_steps + 1)
    y_vals = np.zeros((n_steps + 1, len(y0)))
    y_vals[0] = y0

    for i in range(n_steps):
        t = t_vals[i]
        y = y_vals[i]
        dt_k = t_vals[i+1] - t_vals[i]

        slope1 = func(t, y)
        y_predict = y + dt_k * slope1

        slope2 = func(t_vals[i+1], y_predict)
        y_vals[i+1] = y + (dt_k / 2.0) * (slope1 + slope2)

    return t_vals, y_vals
