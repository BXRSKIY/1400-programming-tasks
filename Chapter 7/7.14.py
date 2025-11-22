def main():
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    n = int(data[0])
    if len(data) < 1 + n:
        raise ValueError(f"Ожидается n={n} вещественных чисел")
    arr = data[1:1+n]
    s = sum(x*x for x in arr)
    print(s)


if __name__ == "__main__":
    main()
