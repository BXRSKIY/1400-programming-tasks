def main():
    # Доходы 3 магазинов за 12 месяцев.
    # Формат: 3 строки по 12 чисел.
    income = []
    for _ in range(3):
        row = list(map(float, input().split()))
        if len(row) != 12:
            raise ValueError("Для магазина нужно 12 значений")
        income.append(row)
    # а) годовой доход каждого магазина
    for i, row in enumerate(income, start=1):
        print(f"store_{i}_year {sum(row)}")
    # б) доход по каждому месяцу (сумма по магазинам)
    for m in range(12):
        s = sum(income[i][m] for i in range(3))
        print(f"month_{m+1}_sum {s}")


if __name__ == "__main__":
    main()
