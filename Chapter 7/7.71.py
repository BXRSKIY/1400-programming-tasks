def main():
    import sys
    # Формат: n, затем по два балла для каждого студента (два экзамена).
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    n = data[0]
    if len(data) < 1 + 2*n:
        raise ValueError(f"Ожидается 2*{n} оценок")
    vals = data[1:1+2*n]
    count = 0
    for i in range(0, len(vals), 2):
        e1 = vals[i]
        e2 = vals[i+1]
        if e1 == 2 or e2 == 2:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
