def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    m = data[0]
    if len(data) < 1 + m:
        raise ValueError(f"Ожидается m={m} чисел")
    d = data[1:1+m]
    max_val = d[0]
    min_val = d[0]
    max_pos = 1
    min_pos = 1
    for i in range(2, m+1):
        v = d[i-1]
        if v > max_val or v == max_val:
            max_val = v
            max_pos = i
        if v < min_val or v == min_val:
            # для минимального по условию тоже последняя позиция
            if v < min_val:
                min_val = v
            min_pos = i
    print(max_pos, min_pos)


if __name__ == "__main__":
    main()
