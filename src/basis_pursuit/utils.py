"""Define basic operations used by all methods"""
import time

import numpy as np
from numpy.typing import NDArray

from src.basis_pursuit.stats import Stats


def shrink(xi: NDArray[np.float64], alpha: float) -> NDArray[np.float64]:
    """Execute element-wise soft-threshold"""
    output: NDArray[np.float64] = np.sign(xi) * np.maximum(np.abs(xi) - alpha, 0)
    return output


def proximal_projection(matrix, b, alpha=1.0e-1, num_iters=2000):
    """Execute proximal projection algorithm"""
    start = time.time()
    z = np.zeros((matrix.shape[1], 1))
    x = np.zeros((matrix.shape[1], 1))
    stats = Stats(matrix=matrix, measurements=b)
    matrix_matrix_transpose = np.linalg.inv(matrix @ matrix.T)
    for _ in range(num_iters):
        x_p = x.copy()
        x = z - matrix.T @ (matrix_matrix_transpose @ (matrix @ z - b))
        z = z + shrink(2.0 * x - z, alpha) - x
        stats.add_stat(x, x_p)
    execution_time = time.time() - start
    return x, stats, execution_time


def linearized_bregman(matrix, b, mu=2.0, num_iters=2000):
    """Execute linearized bregman algorithm

    Note: This solves the problem
           min  mu * ||x||_1 + ||x||_2^2 / 2 * alpha,
            x

          subject to the linear constraint A @ x = b.
          So, mu must be chosen "large enough" to ensure
          the minimizer of the L1 norm is obtained.
    """
    x = np.zeros((matrix.shape[1], 1))
    v = np.zeros((matrix.shape[1], 1))
    stats = Stats(matrix=matrix, measurements=b)
    start = time.time()
    matrix_norm = np.linalg.norm(matrix @ matrix.T)
    alpha = 2.0 / matrix_norm
    mu *= matrix_norm
    for _ in range(num_iters):
        x_p = x.copy()
        v = v - matrix.T @ (matrix @ x - b)
        x = shrink(alpha * v, alpha * mu)
        stats.add_stat(x, x_p)
    execution_time = time.time() - start
    return x, stats, execution_time


def linearized_method_multipliers(matrix, b, lambd=100.0, num_iters=2000):
    """Execute linearized method of multipliers algorithm"""
    rows, cols = matrix.shape
    x = np.zeros((cols.shape[1], 1))
    v = np.zeros((rows.shape[0], 1))
    stats = Stats(matrix=matrix, measurements=b)
    start = time.time()
    lambd *= np.linalg.norm(matrix.T @ matrix)
    alpha = 1.0 / (lambd * np.linalg.norm(matrix.T @ matrix))
    for _ in range(num_iters):
        x_p = x.copy()
        x = shrink(x - alpha * matrix.T @ (v + lambd * (matrix @ x - b)), alpha)
        v = v + lambd * (matrix @ x - b)
        stats.add_stat(x, x_p)
    execution_time = time.time() - start
    return x, stats, execution_time


def prial_dual_hybrid_gradient(matrix, b, lambd=100.0, num_iters=2000):
    """Execute primal dual hybrid gradient algorithm"""
    stats = Stats(matrix=matrix, measurements=b)
    rows, cols = matrix.shape
    x = np.zeros((cols.shape[1], 1))
    v = np.zeros((rows.shape[0], 1))
    alpha = 1.0 / (lambd * np.linalg.norm(matrix.T @ matrix))
    start = time.time()
    for _ in range(num_iters):
        x_p = x.copy()
        x = shrink(x - alpha * matrix.T @ v, alpha)
        v = v + lambd * (matrix @ (2 * x - x_p) - b)
        stats.add_stat(x, x_p)
    execution_time = time.time() - start
    return x, stats, execution_time
