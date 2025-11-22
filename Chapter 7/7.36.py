def main():
    import sys
    # Для каждого района: площадь (га) и средняя урожайность (ц/га).
    data = list(map(float, sys.stdin.read().split()))
    if len(data) % 2 != 0 or not data:
        raise ValueError("Ожидается четное количество чисел: пары площадь-урожайность")
    total_area = 0.0
    total_wheat = 0.0
    for i in range(0, len(data), 2):
        area = data[i]
        yield_per_ha = data[i+1]
        total_area += area
        total_wheat += area * yield_per_ha
    avg_yield = total_wheat / total_area if total_area != 0 else 0.0
    print(total_wheat, avg_yield)


if __name__ == "__main__":
    main()
