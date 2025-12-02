def main():
    # Оценки 15 учеников по 3 предметам.
    marks = []
    for _ in range(15):
        row = list(map(int, input().split()))
        if len(row) != 3:
            raise ValueError("Каждому ученику должно соответствовать 3 оценки")
        marks.append(row)
    # а) общее количество пятёрок
    total_5 = sum(1 for row in marks for x in row if x == 5)
    print(total_5)
    # б) количество троек у каждого ученика
    for i, row in enumerate(marks, start=1):
        c3 = sum(1 for x in row if x == 3)
        print(f"pupil_{i}_3s {c3}")
    # в) количество двоек по каждому предмету
    twos_per_subject = [0, 0, 0]
    for row in marks:
        for j in range(3):
            if row[j] == 2:
                twos_per_subject[j] += 1
    print(*twos_per_subject)


if __name__ == "__main__":
    main()
