---
hide:
  - navigation
  - toc
title: Home
description: Documentation for code used in the paper for the Proximal Projection (PP) algorithm.

---

# Proximal Projection Algorithm

This website provides documentation for code used in the paper for the Proximal Projection (PP) algorithm.

!!! abstract "Abstract"
  
    Many applications using large datasets require efficient methods for minimizing a proximable convex function subject to satisfying a set of linear constraints within a specified tolerance. For this task, we present a proximal projection (PP) algorithm, which is an instance of Douglas-Rachford splitting that directly uses projections onto the set of constraints. Formal guarantees are presented to prove convergence of PP estimates to optimizers. Unlike many methods that obtain feasibility asymptotically, each PP iterate is feasible. Numerically, we show PP either matches or outperforms alternatives (e.g. linearized Bregman, primal dual hybrid gradient, proximal augmented Lagrangian, proximal gradient) on problems in basis pursuit, stable matrix completion, stable principal component pursuit, and the computation of earth mover's distances.

## Key Results

__Problem__: For a convex function $\mathsf{f\colon\mathbb{R}^n \rightarrow \overline{\mathbb{R}}}$, a matrix $\mathsf{A \in \mathbb{R}^{m\times n}}$, a vector $\mathsf{b\in \mathbb{R}^m}$, and a scalar $\mathsf{\varepsilon \geq 0}$, we consider the problem

$$
\mathsf{
  \underset{x}{\mathsf{min}} \ f(x) \quad\mathsf{s.t.}\quad \|Ax-b\|\leq \varepsilon.
}
$$

We refer to this as a _stable linearly constrained optimization problem_ and below set $\mathsf{\mathcal{C} = \{ x : \|Ax-b\|\leq\varepsilon\}}$.
The key conditions used in this work are as follows.

  - [x] the function $f\colon\mathbb{R}^n\rightarrow \overline{\mathbb{R}}$ is closed, convex, and proper;
  - [x] either the matrix $A$ has full row-rank or $\varepsilon > 0$;
  - [x] there is $y \in \mathbb{R}^n$ such that, if $\varepsilon = 0$, then $Ay = b$ and, if $\varepsilon > 0$, then  $\|Ay-b\| < \varepsilon$; 
  - [x] the above condition holds for $y \in \mbox{ri}(\mbox{dom}(f))$.    
  - [x] either $f$ is coercive or $\mathcal{C}$ is bounded; 


__Proposition__: If the conditions above hold, then projection onto $\mathcal{C}$ is given by
$$
\mathsf{\sP_{\mathcal{C}}(x)}
$$
where, if $\mathsf{\|Ax-b\|>\varepsilon}$, the scalar $\mathsf{\tau_x}$ is the unique positive solution to 
$$
  \mathsf{1 = \tau \| (AA^\top +\varepsilon \tau \II)^{-1} (Ax-b) \|.}
$$

We can use the above projection formula with Douglas-Rachford Splitting (DRS) to obtain the PP algorithm.

__Theorem__: If the listed conditions hold, then PP converges to a solution of the stable linearly constrained optimization problem.

## Publication Reference

_Proximal Projection Method for Stable Linearly Constrained Optimization_
    
    @article{heaton2024proximal,
             title={{Proximal Projection Method for Stable Linearly Constrained Optimization}},
             author={Heaton, Howard},
             journal={{arXiv preprint}},
             year={2024}
    }

<br>

<center>
  
  [arXiv Prerint :simple-arxiv:](https://arxiv.org/abs/2407.16998){ .md-button  }
  [Github Repo :simple-github:](https://github.com/TypalAcademy/proximal-projection-algorithm){ .md-button  }
  [Contact Us :material-chat-processing:](https://form.jotform.com/TypalAcademy/contact-form){ .md-button }
   
</center>

<br>
