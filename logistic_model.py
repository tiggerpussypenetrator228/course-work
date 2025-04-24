import numpy as np
import matplotlib.pyplot as plt

def logistic_growth(t, N0, r, K):
    return K * N0 * np.exp(r * t) / (K + N0 * (np.exp(r * t) - 1))

def perform_logistic_model(N0, r, K):
    t = np.linspace(0, 10, 100)

    # Решение
    N = logistic_growth(t, N0, r, K)

    # График
    plt.title("Ферхюльст–Перл")
    plt.plot(t, N, label=f"K={K}, r={r}")
    plt.xlabel("Время")
    plt.ylabel("Численность")
    plt.legend()
    plt.grid()
    plt.show()