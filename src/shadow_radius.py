import numpy as np
def shadow_radius(rph):
    rs = 2
    return rph / np.sqrt(
        1 - rs/rph
    )