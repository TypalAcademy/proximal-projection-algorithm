---
title: Home
description: Documentation for code used in the paper for the Proximal Projection (PP) algorithm.

---

# Basis Pursuit

This page shows the numerical example for solving the problem

$$
    \mathsf{ \underset{x}{min} \ |x|_1 \quad s.t. \quad Ax=b. }
$$

::: src.basis_pursuit.methods.shrink
    options:
      show_root_heading: false

The update iteration for each benchmarked algorithm is in Appendix B.1 of the [paper](https://arxiv.org/abs/2407.16998). Code implementations are shown below.

::: src.basis_pursuit.methods.proximal_projection
    options:
      show_root_heading: false


::: src.basis_pursuit.methods.linearized_bregman
    options:
      show_root_heading: false


::: src.basis_pursuit.methods.linearized_method_multipliers
    options:
      show_root_heading: false


::: src.basis_pursuit.methods.prial_dual_hybrid_gradient
    options:
      show_root_heading: false
