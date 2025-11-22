def main():
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    n = int(data[0])
    if n <= 0:
        raise ValueError("n должно быть положительным")
    if len(data) < 1 + n:
        raise ValueError(f"Ожидается n={n} чисел a1..an")
    a = data[1:1+n]
    # а) сумма модулей
    sum_abs = 0.0
    for x in a:
        if x < 0:
            sum_abs -= x
        else:
            sum_abs += x
    # б) произведение модулей
    prod_abs = 1.0
    for x in a:
        if x < 0:
            prod_abs *= -x
        else:
            prod_abs *= x
    # в) суммы соседних
    neighbor_sums = []
    for i in range(n-1):
        neighbor_sums.append(a[i] + a[i+1])
    # г) знакочередующаяся сумма
    alt_sum = 0.0
    sign = 1.0
    for x in a:
        alt_sum += sign * x
        sign = -sign
    # Вывод: каждая величина с новой строки
    print(sum_abs)
    print(prod_abs)
    if neighbor_sums:
        print(*neighbor_sums)
    else:
        print()
    print(alt_sum)


if __name__ == "__main__":
    main()
