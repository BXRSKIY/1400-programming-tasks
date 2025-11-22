def main():
    import sys
    # Предполагаем формат ввода: n, p, затем n вещественных чисел d1..dn.
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 2:
        raise ValueError("Ожидаются n и p")
    n = int(data[0])
    p = data[1]
    if len(data) < 2 + n:
        raise ValueError(f"Ожидается n={n} вещественных чисел d1..dn")
    d = data[2:2+n]
    s = sum(x for x in d if x > 20.5)
    print("YES" if s < p else "NO")


if __name__ == "__main__":
    main()
