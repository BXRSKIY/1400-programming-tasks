def main():
    import sys
    # Формат: n, затем n вещественных чисел.
    data = list(map(float, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    n = int(data[0])
    if len(data) < 1 + n:
        raise ValueError(f"Ожидается n={n} вещественных чисел")
    a = data[1:1+n]
    neg = 0
    pos = 0
    for x in a:
        if x < 0:
            neg += 1
        elif x > 0:
            pos += 1
    print(neg, pos)


if __name__ == "__main__":
    main()
