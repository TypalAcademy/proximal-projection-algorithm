---
hide:
  - navigation
  - toc
title: Home
description: Documentation for code used in the paper for the Proximal Projection (PP) algorithm.

---

# Basis Pursuit

This page shows the numerical example for solving the problem

$$
    \mathsf{ \underset{x}{min} \ \|x\|_1 \quad s.t. \quad Ax=b. }
$$

::: src.basis_pursuit.utils.proximal_projection
    options:
      show_root_heading: false

$$
  \begin{align}
    & \mathsf{while\ \ stopping\ \  criteria\ \ not\ \ met} \\
    & \quad\quad \mathsf{if \ \|Az-b\|\leq \varepsilon} \\
    & \quad\quad\quad\quad \mathsf{x \leftarrow z} \\
    & \quad\quad \mathsf{else} \\
    & \quad\quad\quad\quad \mathsf{\tau \leftarrow solution\big( 1 = \tau \|AA^\top + \varepsilon I)^{-1}(Az-b)} \\
    & \quad\quad\quad\quad \mathsf{x \leftarrow z - A^\top (AA^\top+\varepsilon I)^{-1}(Az-b) } \\
    & \quad\quad \mathsf{z \leftarrow z + prox_{\alpha f}(2x - z) - x}
  \end{align}
$$
