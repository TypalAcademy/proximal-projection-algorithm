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
    & \mathsf{while stopping criteria not met} \\
    & \hspace*{5pt} x \leftarrow x + 1
  \end{align}
$$
