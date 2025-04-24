import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def predator_prey(y, t, α, β, γ, δ):
    V, P = y
    dVdt = α*V - β*V*P
    dPdt = γ*β*V*P - δ*P
    return [dVdt, dPdt]

def perform_predator(alpha, beta, gamma, delta):
    # Параметры и начальные условия
    params = (alpha, beta, gamma, delta)
    y0 = [40, 9]
    t = np.linspace(0, 50, 1000)

    # Решение
    solution = odeint(predator_prey, y0, t, args=params)
    V, P = solution.T

    # Визуализация
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(t, V, label='Жертвы')
    plt.plot(t, P, label='Хищники')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(V, P)
    plt.xlabel('Жертвы')
    plt.ylabel('Хищники')
    plt.title('Фазовый портрет')
    plt.tight_layout()
    plt.show()