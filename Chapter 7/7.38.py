def main():
    import sys
    # Для каждого района: жители (тыс. чел.) и плотность (тыс. чел./км^2).
    data = list(map(float, sys.stdin.read().split()))
    if len(data) % 2 != 0 or not data:
        raise ValueError("Ожидается четное количество чисел: пары жители-плотность")
    total_area = 0.0
    for i in range(0, len(data), 2):
        people = data[i]
        density = data[i+1]
        if density == 0:
            raise ValueError("Плотность не должна быть равна нулю")
        total_area += people / density
    print(total_area)


if __name__ == "__main__":
    main()
