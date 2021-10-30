import numpy as np
import matplotlib.pyplot as plt
from math import e

# Mendefinisikan Fungsi
def f(x):
    return e**2*x-8*x**2

# Mendefinisikan Turunan Fungsi
def Df(x):
    return 2*x*e-16*x

# Metode Newton-Raphson
def newtonRaphson(x0,eps):
    step = 1
    print('\n\n*** --- Metode Newton Raphson --- ***')
    xn = x0
    for n in range(0,100): # Maksimal iterasi adalah 100
        fxn=f(xn)
        if abs(fxn) < eps:
            print('\n Akar Persamaan tersebut: %0.8f' % xn)
            return xn
        Dfxn=Df(xn)
        if Dfxn == 0:
            print('Solusi tidak ditemukan')
            return None
        xn=xn-(fxn/Dfxn)
        step = step + 1
        print('iterasi-%d, x = %0.8f dan f(x) = %0.8f;' % (step, xn, f(xn)))
    print('Iterasi maksimum, solusi tidak ditemukan')

# Sesi input nilai awal yang dikonversi ke pecahan
x0 = float(input('x0: '))
eps = float(input('epsilon: '))
newtonRaphson(x0,eps)