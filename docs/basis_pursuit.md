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


## Proximal Projection

In this context, the scheme is as follows

$$
  \begin{align}
    \mathsf{x^{k+1}} & \mathsf{= z^k - A^\top (AA^\top)^{-1}(Az^k-b) }\\
    \mathsf{z^{k+1}} & \mathsf{= z^k + shrink(2x^{k+1} - z^k) - x^{k+1}}
  \end{align}
$$

It is implemented in the function below.

::: src.basis_pursuit.utils.proximal_projection
    options:
      show_root_heading: false


