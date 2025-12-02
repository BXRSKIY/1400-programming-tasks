def main():
    # Баллы 8 спортсменов по 5 видам спорта.
    # Формат: 8 строк по 5 вещественных.
    scores = []
    for _ in range(8):
        row = list(map(float, input().split()))
        if len(row) != 5:
            raise ValueError("Каждому спортсмену должно соответствовать 5 значений")
        scores.append(row)
    # а) максимальная из оценок в таблице
    max_score = max(max(row) for row in scores)
    print(max_score)
    # б) сколько баллов набрал победитель (по сумме)
    best_total = max(sum(row) for row in scores)
    print(best_total)


if __name__ == "__main__":
    main()
