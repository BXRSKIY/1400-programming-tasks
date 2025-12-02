def main():
    # Зарплата 12 работников за 3 месяца.
    # Формат ввода: 12 строк по 3 числа (можно вещественные).
    data = []
    for _ in range(12):
        row = list(map(float, input().split()))
        if len(row) != 3:
            raise ValueError("Каждому работнику должны соответствовать 3 значения")
        data.append(row)
    for i, row in enumerate(data, start=1):
        print(i, *row)


if __name__ == "__main__":
    main()
