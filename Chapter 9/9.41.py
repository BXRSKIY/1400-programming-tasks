def main():
    # Дано натуральное число n (n <= 27).
    # Найти все трехзначные числа, сумма цифр которых равна n.
    n = int(input())
    for a in range(1, 10):      # сотни
        for b in range(0, 10):  # десятки
            for c in range(0, 10):  # единицы
                if a + b + c == n:
                    value = a * 100 + b * 10 + c
                    print(value)


if __name__ == "__main__":
    main()
