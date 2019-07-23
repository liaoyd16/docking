### Neural PDE:

#### problem formulation:

given: {($x_1^{(1)}$, $x_2^{(1)}$, $u^{(1)}$), ...}

uncover: $\frac{\part u}{\part t}$ = G($u$, ​$\frac{\part u}{\part x_1}$, ​$\frac{\part u}{\part x_2}$, ​$\frac{\part^2 u}{\part^2 x_1}$,​$\frac{\part^2 u}{\part^2 x_2}$, ​$\frac{\part^2 u}{\part x_1 \part x_2}$, ...)

#### previous methods

i) Bongard & Lipson (2007), Schmidt& Lipson (2009)

ii) Sparse Regression -- Brunton et al. (2016), Schaeffer (2017), Rudy et al. (2017), Wu & Zhang (2017)

iii) determining parameterized models -- Raissi et al. (2017)

- physics informed neural networks 

#### Differentiation matrices & derivative

Matrices subject to certain constraints operated on image $u(x_1, x_2)$ can approximate $\frac{\part^{\alpha_1 + \alpha_2}}{\part^{\alpha_1}x_1 \part^{\alpha_2}x_2}u$. Denote the set of such filters $q$ as $D_{{\alpha_1}{\alpha_2}}$.

 $q \in D_{\alpha_1 \alpha_2}$ iff $M(q)_{i,j} = 1, when\ (i=\alpha_1+1) \and (j=\alpha_2+1); = 0, when\ others$.

#### Network architecture

![arch](/Users/liaoyuanda/Desktop/arch.jpeg)

#### Training method

Layer-wise training