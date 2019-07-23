
import numpy as np
import math
import pdb

# X of shape [2, ?, ?, ...], 2 means 2-dim
# def F(x):
#     return np.sin(x[0]) * (x[1] ** 3)

def F(x):
    return (x[0] ** 2) * (x[1] ** 3)

# calc
# predefined hyperparameters

X = np.array([1, 1])
ALPHA = [2,2]
N = 5

EPS = 10 ** - (14 / (ALPHA[0] + ALPHA[1]))

## filtering with q
### make K[0:1,i,j] = [i+1,j+1]
def _make_ks(N):
    ks = np.empty((2, N, N), dtype=int)
    for i in range(N):
        for j in range(N):
            ks[:,i,j] = [i+1, j+1]
    ks.reshape(2, N*N)
    return ks

### takes q[*,*], Fx[*,*] shaped as (N, N) calc a scalar
def filter_with_q(q, Fx):
    N = q.shape[0]
    ks = _make_ks(N)

    qs = q[(ks[0].reshape(N*N) - 1, ks[1].reshape(N*N) - 1)]

    ans = np.sum(Fx.reshape(N*N) * qs)
    return ans

### F_delta(k1, k2), ks = (k1-list, k2-list), returns value list of size (N,N)
def FX_neighbor(x, ks):
    # ks.shape = (2, N, N)
    return F(x.reshape(2,1,1) + EPS * ks)

### k^beta(k1, k2),  ks = (k1-list, k2-list), return value list of len (N,N)
def k_beta_s(ks, beta):
    # ks.shape = (2, N, N)
    return ks[0]**beta[0] * ks[1]**beta[1]

def check_order_of_sum_rules(q, alpha):
    alpha_mod = alpha[0] + alpha[1]
    ks = _make_ks(q.shape[0])

    for mod in range(0, alpha_mod):
        for b1 in range(mod + 1):
            b2 = mod - b1
            if b1 == alpha[0] and b2 == alpha[1]:
                continue
            filt = filter_with_q(q, k_beta_s(ks, [b1, b2]))
            print("filt = {}".format(filt))
            if abs(filt) > EPS:
                return False
    return True

def gen_filter_by_alpha(alpha, N):
    # generate a filter q_{alpha[0], alpha[1]} that has M(q)_{alpha[0], alpha[1]} = 1 others = 0
    # first: check alpha[0]+alpha[1] < N
    if alpha[0] + alpha[1] >= N: return None

    depend_vars = (2+alpha[0]+alpha[1]) * (1+alpha[0]+alpha[1]) // 2
    free_vars = N*N - depend_vars

    mat = []
    b = []
    alpha_mod = alpha[0] + alpha[1]
    for mod in range(0, alpha_mod+1):
        for b1 in range(mod + 1):
            b2 = mod - b1
            mat.append(k_beta_s(_make_ks(N), [b1, b2]).reshape(N*N))
            if b1 == alpha[0] and b2 == alpha[1]:
                b.append(math.factorial(b1) * math.factorial(b2))
            else:
                b.append(0)

    mat = np.array(mat)
    b = np.array(b)

    # select N*N - (1+2+...+|alpha|) free variables
    q_spec = np.matmul(np.linalg.pinv(mat), b)
    nullspace_basis = np.linalg.svd(mat)[2].transpose()[:,-free_vars:]
    comb = np.random.randn(free_vars)
    q_free = np.matmul(nullspace_basis, comb)

    return (q_spec + q_free).reshape(N, N)

# calculate F^(alpha1, alpha2)[X]
def calc(X, alpha, N, q=None):
    if q is None:
        q = gen_filter_by_alpha(alpha, N)
    if q is None:
        print("alpha beyond ability of rank-N filter")
        return None

    # check given q satisfies
    assert(check_order_of_sum_rules(q, alpha))

    print("Sigma = {}, |eps^alpha| = {}, C_alpha = {}".format(
        filter_with_q(q, FX_neighbor(X, _make_ks(N))), \
        EPS ** (alpha[0] + alpha[1]), \
        filter_with_q(q, k_beta_s(_make_ks(N), alpha)) / math.factorial(alpha[0]) / math.factorial(alpha[1])))

    ans =   filter_with_q(q, FX_neighbor(X, _make_ks(N)))\
          * math.factorial(alpha[0]) * math.factorial(alpha[1])\
          / EPS**(alpha[0] + alpha[1])\
          / filter_with_q(q, k_beta_s(_make_ks(N), alpha))

    return ans

if __name__ == '__main__':
    q = np.array([[1,-2,1,0,0],[1,-2,1,0,0],[1,-2,1,0,0],[1,-2,1,0,0],[1,-2,1,0,0]])
    diff = calc(X, ALPHA, N)
    print(diff)