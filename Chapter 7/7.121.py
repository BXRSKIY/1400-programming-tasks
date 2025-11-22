def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    k = data[0]
    if len(data) < 1 + k:
        raise ValueError(f"Ожидается k={k} чисел")
    b = data[1:1+k]
    last = -1
    for i, v in enumerate(b, start=1):
        if v < 0:
            last = i
    print(last)


if __name__ == "__main__":
    main()
