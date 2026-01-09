def main():
    # 11.58. Оценки фигуриста (в баллах) хранятся в массиве из 18 элементов.
    # Предполагаем, что:
    #  - элементы 0..5  — оценки за первую программу,
    #  - элементы 6..11 — за вторую программу,
    #  - элементы 12..17 — за третью программу.
    # Определить, по какому виду программы спортсмен показал лучший результат.
    import sys
    scores = list(map(float, sys.stdin.read().split()))
    if len(scores) < 18:
        scores += [0.0] * (18 - len(scores))
    sums = [
        sum(scores[0:6]),
        sum(scores[6:12]),
        sum(scores[12:18]),
    ]
    best = 1 + max(range(3), key=lambda i: sums[i])
    print(best)


if __name__ == "__main__":
    main()
