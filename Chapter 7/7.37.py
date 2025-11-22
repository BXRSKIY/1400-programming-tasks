def main():
    import sys
    # Для каждого района: жители (тыс. чел.) и площадь (км^2).
    data = list(map(float, sys.stdin.read().split()))
    if len(data) % 2 != 0 or not data:
        raise ValueError("Ожидается четное количество чисел: пары жители-площадь")
    total_people = 0.0
    total_area = 0.0
    for i in range(0, len(data), 2):
        people = data[i]
        area = data[i+1]
        total_people += people
        total_area += area
    avg_density = total_people / total_area if total_area != 0 else 0.0
    print(avg_density)


if __name__ == "__main__":
    main()
