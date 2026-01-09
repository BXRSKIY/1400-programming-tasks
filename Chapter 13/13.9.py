# 13.9. 30 учеников: фамилия, класс, оценка по информатике. Вывести фамилии учеников 9-х классов с оценкой 5.
for _ in range(30):
    line = input().rstrip("\n")
    if not line:
        continue
    parts = line.split()
    if len(parts) < 3:
        continue
    surname = parts[0]
    klass = parts[1]
    grade = int(parts[2])
    # класс может быть '9', '9А', '9a' и т.п.
    is_9 = str(klass).startswith("9")
    if is_9 and grade == 5:
        print(surname)
