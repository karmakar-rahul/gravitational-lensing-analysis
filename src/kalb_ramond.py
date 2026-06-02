def metric_function(r, M, gamma, lam):
    return (
        1
        - (2*M/r)
        + gamma/(r**(2/lam))
    )