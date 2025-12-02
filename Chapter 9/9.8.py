def main():
    # Оценки 14 студентов по 3 предметам.
    marks = []
    for _ in range(14):
        row = list(map(int, input().split()))
        if len(row) != 3:
            raise ValueError("Каждому студенту должно соответствовать 3 оценки")
        marks.append(row)
    # а) число студентов без двоек
    no_twos = 0
    for row in marks:
        if all(x != 2 for x in row):
            no_twos += 1
    print(no_twos)
    # б) количество предметов, по которым только 4 и 5
    good_subjects = 0
    for j in range(3):
        ok = True
        for i in range(14):
            if marks[i][j] not in (4, 5):
                ok = False
                break
        if ok:
            good_subjects += 1
    print(good_subjects)
    # в) количество двоек по каждому предмету
    twos_per_subject = [0, 0, 0]
    for row in marks:
        for j in range(3):
            if row[j] == 2:
                twos_per_subject[j] += 1
    print(*twos_per_subject)


if __name__ == "__main__":
    main()
