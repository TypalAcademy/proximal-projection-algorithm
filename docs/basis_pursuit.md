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

Each algorithm is presented in this context below.


## Proximal Projection

$$
  \begin{align}
    \mathsf{x^{k+1}} & \mathsf{= z^k - A^\top (AA^\top)^{-1}(Az^k-b) }\\
    \mathsf{z^{k+1}} & \mathsf{= z^k + shrink(2x^{k+1} - z^k) - x^{k+1}}
  \end{align}
$$

::: src.basis_pursuit.methods.proximal_projection
    options:
      show_root_heading: false


## Linearized Bregman

::: src.basis_pursuit.methods.linearized_bregman
    options:
      show_root_heading: false


## Linearized Method of Multipliers

::: src.basis_pursuit.methods.linearized_method_multipliers
    options:
      show_root_heading: false


## Primal Dual Hybrid Gradient

::: src.basis_pursuit.methods.prial_dual_hybrid_gradient
    options:
      show_root_heading: false
