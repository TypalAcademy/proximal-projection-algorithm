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

\begin{algorithm}
\caption{Example Algorithm}
\begin{algorithmic}[1]
    \STATE \textbf{Input:} $n$ (an integer)
    \STATE \textbf{Output:} Factorial of $n$
    \STATE $result \gets 1$
    \FOR{$i \gets 1$ to $n$}
        \STATE $result \gets result \times i$
    \ENDFOR
    \STATE \textbf{return} $result$
\end{algorithmic}
\end{algorithm}
