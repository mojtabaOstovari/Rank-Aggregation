from sympy import *
import numpy as np
from fractions import Fraction
from sympy.calculus.util import *
import sys

n = 10

if(len(sys.argv) > 1):
    n = int(sys.argv[1])

beta = Fraction(55, 100)
alpha = Fraction(145, 100)

class J:
    def __init__(self, x1, x2, x3, w1, w2, w3):
        # self.X, self.Y = symbols("w_{ij}" + " " + "w_{jk}", real=True)

        self.x = np.zeros((4, 4), dtype=np.float64)
        self.set_x(x1, x2, x3)

        self.w = np.zeros((4, 4), dtype=np.float64)
        self.set_w(w1, w2, w3)

    
    def set_x(self, x1, x2, x3):
        self.x[1][2] = x1
        self.x[2][3] = x2
        self.x[3][1] = x3

        self.x[2][1] = 1 - self.x[1][2]
        self.x[3][2] = 1 - self.x[2][3]
        self.x[1][3] = 1 - self.x[3][1]

    def set_w(self, w1, w2, w3):
        self.w[1][2] = w1
        self.w[2][3] = w2
        self.w[3][1] = w3

        self.w[2][1] = 1 - self.w[1][2]
        self.w[3][2] = 1 - self.w[2][3]
        self.w[1][3] = 1 - self.w[3][1]

    def Pr(self, i, j):
        s = 3 * self.w[i][j] - 1
        s = 1 if s > 1 else s
        s = 0 if s < 0 else s
        return s

    def phi_l(self, i, j, k):
        return (self.Pr(i, j) * self.Pr(j, k) * self.w[k][i]) + (self.Pr(k, j) * self.Pr(j, i) * self.w[i][k])

    def mu_l(self, i, j, k):
        return (self.Pr(i, j) * self.Pr(j, k) + self.Pr(k, j) * self.Pr(j, i)) * (2 * self.w[i][k] * self.w[k][i])

    def psi_l(self, i, j, k):
        return (self.Pr(i, j) * self.Pr(j, k) + self.Pr(k, j) * self.Pr(j, i)) * (self.x[k][i] * self.w[i][k] + self.x[i][k] * self.w[k][i])

    def phi(self):
        return self.phi_l(1, 2, 3) + self.phi_l(3, 1, 2) + self.phi_l(2, 3, 1)

    def mu(self):
        return self.mu_l(1, 2, 3) + self.mu_l(3, 1, 2) + self.mu_l(2, 3, 1)

    def psi(self):
        return self.psi_l(1, 2, 3) + self.psi_l(3, 1, 2) + self.psi_l(2, 3, 1)

    def omega(self):
        return beta*self.phi() + (1-beta)*self.mu() - alpha*self.psi()
    


Max = -10
x1=1
x2=1
x3=0
p = (None, None, None)
for i in range(n+1):
    for j in range(i, n+1):
        for k in range(n+1):
            sum = i + j + k
            if n <= sum and sum <= 2*n:
                w1 = Fraction(i, n)
                w2 = Fraction(j, n)
                w3 = Fraction(k, n)
                o = J(x1, x2, x3, w1, w2, w3).omega()
                if Max < o:
                    Max = o
                    t = (w1, w2, w3)


print("Maximum value: ", Max)
print("w1, w2, w3: ", t[0]*1.0, ',', t[1]*1.0, ',', t[2]*1.0)
