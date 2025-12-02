def main():
    income = []
    for _ in range(3):
        row = list(map(float, input().split()))
        if len(row) != 12:
            raise ValueError("Для магазина нужно 12 значений")
        income.append(row)
    # а) средний месячный доход по каждому магазину
    for i, row in enumerate(income, start=1):
        print(f"store_{i}_avg {sum(row)/12.0}")
    # б) средний доход по каждому месяцу (по всем магазинам)
    for m in range(12):
        s = sum(income[i][m] for i in range(3))
        print(s / 3.0)


if __name__ == "__main__":
    main()
