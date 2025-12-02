def main():
    # Зарплата 12 работников за 3 месяца.
    data = []
    for _ in range(12):
        row = list(map(float, input().split()))
        if len(row) != 3:
            raise ValueError("Каждому работнику должны соответствовать 3 значения")
        data.append(row)
    # а) суммарная по каждому работнику
    for i, row in enumerate(data, start=1):
        print(f"worker_{i}_sum {sum(row)}")
    # б) суммарная по каждому месяцу
    month_sums = [0.0, 0.0, 0.0]
    for row in data:
        for j in range(3):
            month_sums[j] += row[j]
    print(*month_sums)


if __name__ == "__main__":
    main()
