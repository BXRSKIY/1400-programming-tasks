def main():
    # 11.97. Известны оценки ученика по всем предметам за год (массив).
    # Некоторую оценку условимся считать «зачётом». Возможно ли,
    # что эта оценка есть средняя оценка учеников по всем предметам?
    #
    # Формат ввода: сначала число z (оценка-зачёт), затем оценки.
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 2:
        print("NO")
        return
    z = data[0]
    grades = data[1:]
    avg = sum(grades) / len(grades)
    print("YES" if abs(avg - z) < 1e-9 else "NO")


if __name__ == "__main__":
    main()
