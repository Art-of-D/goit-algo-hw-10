import random
from graphic import f

def monte_carlo_simulation(b, num_experiments):
    """Виконує серію експериментів методом Монте-Карло."""
    average_area = 0

    for _ in range(num_experiments):
        points = [(random.uniform(0, b), random.uniform(0, f(b))) for _ in range(15000)]
        inside_points = [point for point in points if point[1] <= f(point[0])]

        M = len(inside_points)
        N = len(points)
        area = (M / N) * (b * f(b))

        average_area += area

    # Обчислення середньої площі
    average_area /= num_experiments
    return average_area