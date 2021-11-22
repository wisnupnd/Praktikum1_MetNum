from math import e 

# Definisikan fungsi yang akan di integralkan
def f(x):
     return e**x

# Implementasi Metode Trapezoidal
def trapezoidal(x0,xn,n):
    # Hitung ukuran h/ selisih xi dan xi+1
    h = (xn - x0) / n

    # Tentukan jumlah
    integration = f(x0) + f(xn)

    for i in range(1,n):
        k = x0 + i*h
        integration = integration + 2 * f(k)

    # Final Integrasi
    integration = integration * h/2

    return integration

# Sesi input
lower_limit = float(input("Masukkan Batas Bawah Daerah Integral: "))
upper_limit = float(input("Masukkan Batas Atas Daerah Integral: "))
sub_interval = int(input("Masukkan Jumlah Pias: "))

# Memanggil Trapezoidal
result = trapezoidal(lower_limit, upper_limit, sub_interval)
print("\nHasil Integral dengan Metode Trapezoidal : %0.6f" % (result) )