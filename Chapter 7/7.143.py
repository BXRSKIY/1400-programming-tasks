def main():
    import sys
    # Для 16 государств: население (млн) и площадь (тыс. км^2).
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 32:
        raise ValueError("Ожидается 16 пар (население, площадь)")
    min_density = None
    for i in range(0, 32, 2):
        p = data[i]
        s = data[i+1]
        if s == 0:
            continue
        d = p / s
        if min_density is None or d < min_density:
            min_density = d
    print(min_density if min_density is not None else 0.0)


if __name__ == "__main__":
    main()
