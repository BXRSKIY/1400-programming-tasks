import random
import math

def monte_carlo_pi(eps: float = 1e-4) -> float:
    # Метод Монте-Карло: площадь круга радиуса 1 в квадрате 2x2.
    # Оцениваем pi как 4 * (точек в круге / всех точек).
    inside = 0
    total = 0
    pi_est = 0.0
    # Будем увеличивать количество точек до достижения точности по разности
    while True:
        total += 1
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        if x*x + y*y <= 1.0:
            inside += 1
        pi_new = 4.0 * inside / total
        if total > 1000 and abs(pi_new - pi_est) < eps:
            pi_est = pi_new
            break
        pi_est = pi_new
    return pi_est, total

def main():
    # 10.28*. Вычисление числа pi методом Монте-Карло.
    pi_val, N = monte_carlo_pi(1e-4)
    print("pi ≈", pi_val, "после", N, "точек")


if __name__ == "__main__":
    main()
