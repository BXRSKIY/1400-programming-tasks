def main():
    # Напечатать в возрастающем порядке все трехзначные числа,
    # в десятичной записи которых нет одинаковых цифр.
    for a in range(1, 10):      # сотни
        for b in range(0, 10):  # десятки
            for c in range(0, 10):  # единицы
                if a != b and a != c and b != c:
                    print(a * 100 + b * 10 + c)


if __name__ == "__main__":
    main()
