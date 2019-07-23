####Validating that a convolution kernel 'q' that satisfies 'Order of Sum Rule' can approximate partial derivatives of multivariate functions

- "Order of sum rule" and differentiation property of linear filter: recap

  ![Screen Shot 2019-07-20 at 22.29.06](/Users/liaoyuanda/Desktop/Screen Shot 2019-07-20 at 22.29.06.png)

- Test using custom differentiation filter:

  - Tested functions: {$x^2y^3$, $sin(x)y^{3}$, }

  - Tested orders of derivatives: {$\frac{\part{f}}{\part{x}}$,$\frac{\part^2{f}}{\part{x}\part{y}}$, $\frac{\part^3{f}}{\part{x}\part^2{y}}$, $\frac{\part^3{f}}{\part^2{x}\part{y}}$}

  - Tested $(x,y) = (1,1)$

  - Result: (standard answer, calculation result)

|       |  ||
| ----- | ------ | ------ |
|       | x^2y^3 |sin(x)y^3|
| f_x   | (2, 2.005$\pm$0.005) |(0.5403, 0.5407$\pm$0.0016)|
| f_xy  | (6, 6.008$\pm$0.0035) |(1.6209, 1.6218$\pm$0.0013)|
| f_xyy | (12, 12.006$\pm$0.003) |(3.2418, 3.2402$\pm$0.0010)|
| f_xxy | (6, 6.003$\pm$0.002) |(-2.5244, -2.5273$\pm$0.0011)|

(use $\epsilon = 10^{-4}$, $N=4$)

####Solution to problem: generating a filter 'q' that satisfies momentum constraint (vanishing moments)

- Moment constraint problem description: 

  Solve matrix $q$ = {$q_{ij}, i,j < N$}, s.t. $\Sigma_i\Sigma_jq_{ij}i^{\beta_1}j^{\beta_2} = 0$ for moment of order $\beta=(\beta_1,\beta_2)$ that is constrained to be zero, $\Sigma_i\Sigma_jq_{ij}i^{\beta_1}j^{\beta_2} = \beta_1!\beta_2!$ for moment of order $\beta=(\beta_1,\beta_2)$ that is constrained to be zero.

- Conversion of the problem:

  Let {$i^{\beta_1}j^{\beta_2}$, $i,j \in Z_+, i,j < N$} be reshaped into a 1-dimension array, let $q$ = {$q_{ij}, i,j < N$} be reshaped into a 1-d array in the same manner. Every constraint becomes a linear equation having values in $\{0,1\}$. The problem becomes an $N^2$-dimensional, $k < N^2$-constraints linear equation.

- Converted problem: How to solve out all solutions that satisfy $Mq = b$, where $M.rows < M.columns$. Solutions can be represented as a function of DOF(degree of freedom)-number of free variables.

- Solution:

  1. Solve a specific $q_0$ that satisfies $Mq_0 = b$;

     This could be solve by solving $q_0 = M^{*}b$, where $M^*$ denotes pseudo-inverse of M, if $q_0$ exists;

  2. Solve the space of all $q_i$s that satisfy $Mq_i = 0$;

     This could be done using SVD to decompose $Nullspace(M)$ 's basis vectors

#### Numerical stability and convergence problem

- The formula does not perform ideally as $\epsilon$ goes to infinitely small. The approximation deteriorates dramatically and explodes as $\epsilon$ goes really small. Various calculations given entirely different and completely off-target results. 
- This could be problematic for future use in PDE-net. Solution to this is yet not worked out.
- Way-out:
  - The problem may be due to the numerical error in solving 'q' that shall satisfy vanishing moments constraints. When solving $q_0$ and $q_i$, they may not satisfy $Mq = b$. Instead, there may be some perturbations such that $Mq = b+\eta, \eta << 1$. Since all vanishing moment constraint has to satisfy $ \Sigma_i\Sigma_jq_{ij}=\Sigma_i\Sigma_jq_{ij}i^{0}j^{0} = 0$, which is the first constraint in $Mq = 0$, the q solved may end up having $Mq = \eta, \eta << 0$. In experiment, $\eta$ ~ $10^{-15}$.
  - When in experiment, let $\epsilon = 10 ^{- 14 / (\beta_1 + \beta_2)}$, and we constrain the derivative order to be $\alpha_0 \le 2, \alpha_1 \le 2$ and $N = 5$ the result will be satisfactory. The algorithm loses accuracy when calculating higher order partial derivatives.