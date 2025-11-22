def main():
    import sys
    # Вещественные числа a1..a12. Сумма тех, которые > 10.75.
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 12:
        raise ValueError("Ожидается 12 вещественных чисел")
    a = data[:12]
    s = 0.0
    for x in a:
        if x > 10.75:
            s += x
    print(s)


if __name__ == "__main__":
    main()
