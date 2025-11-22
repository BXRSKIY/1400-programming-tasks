def main():
    import sys
    # Формат: n, затем n вещественных чисел последовательности,
    # начинающейся с отрицательного числа.
    data = list(map(float, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    n = int(data[0])
    if len(data) < 1 + n:
        raise ValueError(f"Ожидается n={n} вещественных чисел")
    a = data[1:1+n]
    count = 0
    for x in a:
        if x < 0:
            count += 1
        else:
            break
    print(count)


if __name__ == "__main__":
    main()
