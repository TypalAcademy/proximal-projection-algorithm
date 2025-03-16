"""Define basic operations used by all methods"""
import numpy as np


def shrink(xi, alpha):
    """Execute element-wise soft-threshold"""
    return np.sign(xi) * np.maximum(np.abs(xi) - alpha, 0)
