def main():
    # Количество учеников в 4 классах за 3 года.
    pupils = []
    for _ in range(4):
        row = list(map(int, input().split()))
        if len(row) != 3:
            raise ValueError("Для класса нужно 3 значения (по годам)")
        pupils.append(row)
    # а) на сколько увеличилось общее количество учеников в школе (год3 - год1)
    total1 = sum(row[0] for row in pupils)
    total3 = sum(row[2] for row in pupils)
    print(total3 - total1)
    # б) в каком классе наибольшее увеличение
    best_delta = None
    best_class = 0
    for i, row in enumerate(pupils, start=1):
        d = row[2] - row[0]
        if best_delta is None or d > best_delta:
            best_delta = d
            best_class = i
    print(best_class)


if __name__ == "__main__":
    main()
