# proximal-projection-algorithm
Numerical examples for the paper "Proximal Projection Method for Stable Linearly Constrained Optimization".

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
![Python Linting Badge](https://github.com/typalacademy/proximal-projection-algorithm/actions/workflows/python-linting.yml/badge.svg)
![Docs Website Badge](https://github.com/typalacademy/proximal-projection-algorithm/actions/workflows/docs-website.yml/badge.svg)

# Proximal Projection Algorithm

_Howard Heaton_

## Abstract

Many applications using large datasets require efficient methods for minimizing a proximable convex function subject to satisfying a set of linear constraints within a specified tolerance. For this task, we present a proximal projection (PP) algorithm, which is an instance of Douglas-Rachford splitting that directly uses projections onto the set of constraints. Formal guarantees are presented to prove convergence of PP estimates to optimizers. Unlike many methods that obtain feasibility asymptotically, each PP iterate is feasible. Numerically, we show PP either matches or outperforms alternatives (e.g. linearized Bregman, primal dual hybrid gradient, proximal augmented Lagrangian, proximal gradient) on problems in basis pursuit, stable matrix completion, stable principal component pursuit, and the computation of earth mover’s distances.

## Publication

_Proximal Projection Method for Stable Linearly Constrained Optimization_ [arXiv Link](https://arxiv.org/abs/2407.16998)
    
    @article{heaton2024proximal,
             title={{Proximal Projection Method for Stable Linearly Constrained Optimization}},
             author={Heaton, Howard},
             journal={{arXiv preprint}},
             year={2024}
    }

See the [documentation site](https://pp.research.typal.academy) for more details about code.
