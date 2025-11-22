def main():
    import sys
    # Для 20 тел: масса (кг) и объем (см^3).
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 40:
        raise ValueError("Ожидается 20 пар (масса, объем)")
    max_density = None
    for i in range(0, 40, 2):
        m = data[i]
        v = data[i+1]
        if v == 0:
            continue
        rho = m / v
        if max_density is None or rho > max_density:
            max_density = rho
    print(max_density if max_density is not None else 0.0)


if __name__ == "__main__":
    main()
