import numpy as np
import matplotlib.pyplot as plt

def perform_saturation(beta, a, b):
    V = np.linspace(0, 100, 100)

    plt.plot(V, beta*V, label='Лотка-Вольтерра (линейный)')
    plt.plot(V, (a*V)/(1 + b*V), label='Холлинг-II (нелинейный)')
    plt.xlabel('Плотность жертв (V)')
    plt.ylabel('Скорость потребления')
    plt.legend()
    plt.grid()
    plt.show()