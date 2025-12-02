def main():
    # Баллы 15 участников по 3 видам программы.
    # Формат: 15 строк по 3 вещественных.
    scores = []
    for _ in range(15):
        row = list(map(float, input().split()))
        if len(row) != 3:
            raise ValueError("Каждому спортсмену должно соответствовать 3 значения")
        scores.append(row)
    # а) среднее по каждому спортсмену
    for i, row in enumerate(scores, start=1):
        avg = sum(row) / 3.0
        print(f"athlete_{i}_avg {avg}")
    # б) среднее по каждому виду программы
    prog_sums = [0.0, 0.0, 0.0]
    for row in scores:
        for j in range(3):
            prog_sums[j] += row[j]
    for j in range(3):
        print(f"program_{j+1}_avg {prog_sums[j] / 15.0}")


if __name__ == "__main__":
    main()
