# Neural PDE
import torch
import torch.nn as nn
import torch.nn.functional as F

class Diff(nn.Module):
    def __init__(self, momentum_constraint):
        pass

    def _shape_check(x):
        return True

    def forward(self, x):
        assert(_shape_check(x))
        pass


class WeightedSum_NonLinear_Func(nn.Module):
    def __init__(self, dim_in):
        pass

    def _shape_check(x):
        return True

    def forward(self, x):
        assert(_shape_check(x))
        pass


class Neural_PDE(nn.Module):
    def __init__(self, diff_orders, Func):
        pass

    def forward(self, x, steps):
        u_prime = x
        return u_prime

def train(U, timebin, timesteps):
    pass

if __name__ == "__main__":
    diff_orders = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
    neural_pde = Neural_PDE(diff_orders, )