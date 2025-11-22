def main():
    import sys
    # Формат: n, затем n троек целых чисел a, b, c (a <= b <= c).
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    n = data[0]
    if len(data) < 1 + 3*n:
        raise ValueError(f"Ожидается 3*{n} целых чисел")
    vals = data[1:1+3*n]
    count = 0
    for i in range(0, len(vals), 3):
        a, b, c = vals[i], vals[i+1], vals[i+2]
        # Условие существования треугольника при a <= b <= c: a + b > c
        if a + b > c:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
