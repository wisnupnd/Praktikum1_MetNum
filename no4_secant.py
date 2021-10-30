import numpy as np
import matplotlib.pyplot as plt
from math import e

# Mendefinisikan fungsi
def f(x):
    return e**2*x-8*x**2

# Metode Secant
def Secant(x0,x1,eps,N):
    step = 1
    print('\n*** --- Metode Secant --- ***')
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Solusi tidak ditemukan')
            break

        x2 = x1 - ((f(x1)*(x1-x0))/(f(x1)-f(x0)))
        print('Iterasi-%d, x = %0.8f dan f(x) = %0.8f' % (step, x2, f(x2)))
        x0 = x1
        x1 = x2
        step = step + 1

        if step > N:
            print('Divergen')
            break

        condition = abs(f(x2)) > eps
    print('\n Akar persamaan tersebut : %0.8f' % x2)

# Sesi input nilai awal yang dikonversi ke pecahan
x0 = float(input('x0: '))
x1 = float(input('x1: '))
N = int(input('Max Iter: '))
eps = float(input('epsilon : '))
Secant(x0,x1,eps,N)