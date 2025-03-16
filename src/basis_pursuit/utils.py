import numpy as np


def shrink(xi, alpha):
    """Execute element-wise soft-threshold"""
    return np.sign(xi) * np.maximum(np.abs(xi) - alpha, 0)


def update_stats(x, x_p, A, b, viol, obj, res, k):
    """Update arrays storing performance statistics."""
    viol[k] = np.linalg.norm(A @ x - b)
    obj[k] = np.linalg.norm(x, ord=1)
    res[k] = np.linalg.norm(x - x_p)
    return viol, obj, res
