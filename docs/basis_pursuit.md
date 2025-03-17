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
    \mathsf{ \underset{x}{min} \ |x|_1 \quad s.t. \quad Ax=b. }
$$

::: src.basis_pursuit.methods.shrink
    options:
      show_root_heading: false

The update iteration benchmarked algorithm for solving the above problem is listed below and is followed by the function implementing it.


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

INSERT UPDATES.

Note: 
    This method solves the problem
    
    $$
    \mathsf{ \underset{x}{min}\ |x|_1 + \alpha \frac{|x|_2^2}{2} \quad s.t. \quad Ax=b.}
    $$

    Consequently, the parameter $\mu$ must be chosen "large enough" to ensure the minimizer of the $\mathsf{\ell_1}$ norm is obtained.

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
