import numpy as np
def weak_deflection(gamma, lam):
    schwarzschild = 3.464
    correction = (
        gamma * lam * 0.1
    )
    return schwarzschild - correction