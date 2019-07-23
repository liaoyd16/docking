###Docking Problem: A Summary

#### 1. dataset description

Dataset website is at http://www.rcsb.org/pdb/. Each protein has its own protein file, whose name ends with ".cif". This correspondes to the representation of $P_i$.

#### 2. Problem Formulation & Solution

#####a) problem formulation

Build a transition generator which takes proteins' states $\{P_i\}$ and generates transitions of proteins $T(\{P_i\}) = \{T_{i}\}$. 

Given: $S = \{(P_i, P_j, T_{ij})\}$.

##### b) solution

i) Train:

a) a function $F$ that evaluates energy of a transition on a pair of proteins, 

b) a transition operator $T(\dot{}, \dot{})$ that operates:
$$
F[P_i, P_j, T(\dot{}, \dot{})] = F(P_i, T(P_i,P_j)(P_j))
$$
where $T$ is a transition operator that depends on two proteins $P_i$, $P_ j$ and returns the transition operation ($\Delta X_{ij}, \Delta Y_{ij}, \Delta Z_{ij}, \Delta \theta_{ij}, \Delta \omega_{ij}, \Delta \phi_{ij}$), (the latter three representing Euler angles of j-th element's transition). The $T(\dot{}, \dot{})$ may be a convolution network. This can be achieved by doing $argmin$ on loss function:
$$
argmin[\frac{1}{|S|}\Sigma_{i=1}^{|S|}F(P^{(i)}_{1}, T(P^{(i)}_{1}, P^{(i)}_{2}))]
$$
ii) Find the set of transitions of individual proteins $\{T_i\}$ that minimizes for a certain k:
$$
\Sigma_{i=1}^{M}||T^{(k)}_j(\dot{}){T_i^{(k)}}^{-1}(\dot{}) - T_{ij}(\dot{})||
$$

#### 3. Trying to simplify: image stitching

##### Image representation & answer representation

Images: 3 channels - rectangle images of size $(5472, 3648, 3)$. There are total 73 images. Note it as $\{I_i\}$, $I_i = (P_i, X_i,Y_i,\theta_i)$, and $P_i$ is a $(W, H, 3)$-shaped array representing the image.

Answer: $\{T_i^{(k)} = (\Delta X_i^{(k)}, \Delta Y_i^{(k)}, \Delta \theta_i^{(k)})\}$ where $\Delta \dot{}^{(k)}$ is the translation of i-th element with respect to k-th element.

#####Problem formulation & solution

TBD

### ODE-Net