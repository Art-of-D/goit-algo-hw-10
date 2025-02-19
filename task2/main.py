from graphic import b
from area_mk import monte_carlo_simulation
from check import *

num_experiments = 100


# Виконання симуляції
S = (b** 3) / 3
print(f"Теоретична площа трикутника: {S}")

average_area = monte_carlo_simulation(b, num_experiments)
print(f"Середня площа трикутника за {num_experiments} експериментів: {average_area}")

print_result()