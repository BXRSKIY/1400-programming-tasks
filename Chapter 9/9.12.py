def main():
    # Количество учеников в 4 классах за 3 года.
    # Формат: 4 строки по 3 целых.
    pupils = []
    for _ in range(4):
        row = list(map(int, input().split()))
        if len(row) != 3:
            raise ValueError("Для класса нужно 3 значения (по годам)")
        pupils.append(row)
    # а) на сколько увеличилось число учеников в каждом классе (год3 - год1)
    for i, row in enumerate(pupils, start=1):
        print(f"class_{i}_delta {row[2] - row[0]}")
    # б) для каждого года указать количество классов, в которых число учеников увеличилось
    for year in range(1, 3):
        cnt = 0
        for row in pupils:
            if row[year] > row[year-1]:
                cnt += 1
        print(cnt)


if __name__ == "__main__":
    main()
