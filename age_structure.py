import numpy as np
import matplotlib.pyplot as plt

def perform_age_structure_model(
    youngBornRate,
    adultBornRate,
    oldBornRate,
    youngLifeRate,
    adultLifeRate,
    oldLifeRate,
):
    # Параметры модели
    L = np.array([
        [youngBornRate, adultBornRate, oldBornRate],  # Плодовитость
        [youngLifeRate, 0, 0],     # Выживаемость молоди
        [0, adultLifeRate, oldLifeRate]      # Выживаемость взрослых
    ])

    print(L)

    n0 = np.array([100, 50, 10])  # Начальное распределение
    years = 20
    population = np.zeros((years, 3))

    # Моделирование
    for t in range(years):
        if t == 0:
            population[t] = n0
        else:
            population[t] = L @ population[t-1]

    # Визуализация
    plt.figure(figsize=(10, 5))
    plt.stackplot(range(years), population.T, labels=['Молодые', 'Взрослые', 'Старые'])
    plt.legend()
    plt.title('Динамика возрастной структуры')
    plt.xlabel('Годы')
    plt.ylabel('Численность')
    plt.show()