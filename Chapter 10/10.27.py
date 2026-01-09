import random
import math

def monte_carlo_half_sine(trials: int = 100000) -> float:
    # Площадь под y = sin x на [0, pi] (половина синусоиды)
    # Ограничающий прямоугольник: x in [0, pi], y in [0,1]
    inside = 0
    for _ in range(trials):
        x = random.random() * math.pi
        y = random.random()
        if y <= math.sin(x):
            inside += 1
    return inside / trials * (math.pi * 1.0)

def monte_carlo_parabola(trials: int = 100000) -> float:
    # Площадь под y = x^2 на [0,3]
    # Ограничающий прямоугольник: x in [0,3], y in [0,9]
    inside = 0
    for _ in range(trials):
        x = random.random() * 3.0
        y = random.random() * 9.0
        if y <= x*x:
            inside += 1
    return inside / trials * (3.0 * 9.0)

def main():
    # 10.27*. Метод Монте-Карло для площадей.
    trials = int(input("Число испытаний: ").strip() or "100000")
    print("Половина синусоиды, площадь ≈", monte_carlo_half_sine(trials))
    print("Под y = x^2 на [0,3], площадь ≈", monte_carlo_parabola(trials))


if __name__ == "__main__":
    main()
