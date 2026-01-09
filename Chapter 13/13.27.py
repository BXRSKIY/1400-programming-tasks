# 13.27. 20 учеников: фамилия и оценки по 12 предметам.
# Найти среднюю оценку каждого ученика и всего класса, вывести фамилии учеников со средней оценкой выше средней по классу.
students = []
for _ in range(20):
    parts = input().split()
    surname = parts[0]
    grades = list(map(int, parts[1:13]))
    avg = sum(grades) / 12
    students.append((surname, avg))
class_avg = sum(a for _, a in students) / len(students)
for s, a in students:
    if a > class_avg:
        print(s)
