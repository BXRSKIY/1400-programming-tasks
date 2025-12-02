def main():
    # Оценки 12 учеников по 3 предметам.
    # Формат ввода: 12 строк по 3 целых числа.
    marks = []
    for _ in range(12):
        row = list(map(int, input().split()))
        if len(row) != 3:
            raise ValueError("Каждому ученику должно соответствовать 3 оценки")
        marks.append(row)
    # Просто печатаем таблицу в том же виде
    for i, row in enumerate(marks, start=1):
        print(i, *row)


if __name__ == "__main__":
    main()
