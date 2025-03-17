"""Implement each method for benchmarking"""
import time

import numpy as np
from numpy.typing import NDArray

from src.basis_pursuit.stats import Stats


def shrink(xi: NDArray[np.float64], alpha: float) -> NDArray[np.float64]:
    """The proximal for $|x|_1$ is an element-wise shrink operation."""
    output: NDArray[np.float64] = np.sign(xi) * np.maximum(np.abs(xi) - alpha, 0)
    return output


def proximal_projection(A, b, alpha=1.0e-1, num_iters=2000):
    """Execute proximal projection algorithm"""
    start = time.time()
    z = np.zeros((A.shape[1], 1))
    x = np.zeros((A.shape[1], 1))
    stats = Stats(matrix=A, measurements=b)
    AAt = np.linalg.inv(A @ A.T)
    for _ in range(num_iters):
        x_p = x.copy()
        x = z - A.T @ (AAt @ (A @ z - b))
        z = z + shrink(2.0 * x - z, alpha) - x
        stats.add_stat(x, x_p)
    execution_time = time.time() - start
    return x, stats, execution_time


def linearized_bregman(A, b, mu=2.0, num_iters=2000):
    """Execute linearized bregman algorithm

    Note: This solves the problem
           min  mu * ||x||_1 + ||x||_2^2 / 2 * alpha,
            x

          subject to the linear constraint A @ x = b.
          So, mu must be chosen "large enough" to ensure
          the minimizer of the L1 norm is obtained.
    """
    x = np.zeros((A.shape[1], 1))
    v = np.zeros((A.shape[1], 1))
    stats = Stats(matrix=A, measurements=b)
    start = time.time()
    matrix_norm = np.linalg.norm(A @ A.T)
    alpha = 2.0 / matrix_norm
    mu *= matrix_norm
    for _ in range(num_iters):
        x_p = x.copy()
        v = v - A.T @ (A @ x - b)
        x = shrink(alpha * v, alpha * mu)
        stats.add_stat(x, x_p)
    execution_time = time.time() - start
    return x, stats, execution_time


def linearized_method_multipliers(A, b, lambd=100.0, num_iters=2000):
    """Execute linearized method of multipliers algorithm"""
    rows, cols = A.shape
    x = np.zeros((cols.shape[1], 1))
    v = np.zeros((rows.shape[0], 1))
    stats = Stats(matrix=A, measurements=b)
    start = time.time()
    lambd *= np.linalg.norm(A.T @ A)
    alpha = 1.0 / (lambd * np.linalg.norm(A.T @ A))
    for _ in range(num_iters):
        x_p = x.copy()
        x = shrink(x - alpha * A.T @ (v + lambd * (A @ x - b)), alpha)
        v = v + lambd * (A @ x - b)
        stats.add_stat(x, x_p)
    execution_time = time.time() - start
    return x, stats, execution_time


def prial_dual_hybrid_gradient(A, b, lambd=100.0, num_iters=2000):
    """Execute primal dual hybrid gradient algorithm"""
    stats = Stats(matrix=A, measurements=b)
    rows, cols = A.shape
    x = np.zeros((cols.shape[1], 1))
    v = np.zeros((rows.shape[0], 1))
    alpha = 1.0 / (lambd * np.linalg.norm(A.T @ A))
    start = time.time()
    for _ in range(num_iters):
        x_p = x.copy()
        x = shrink(x - alpha * A.T @ v, alpha)
        v = v + lambd * (A @ (2 * x - x_p) - b)
        stats.add_stat(x, x_p)
    execution_time = time.time() - start
    return x, stats, execution_time
