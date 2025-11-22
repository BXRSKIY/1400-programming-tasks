def main():
    import sys
    # Формат: n, затем n целых чисел.
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    n = data[0]
    if len(data) < 1 + n:
        raise ValueError(f"Ожидается n={n} целых чисел")
    a = data[1:1+n]
    if n == 0:
        print(0)
        return
    first = a[0]
    count = 0
    for x in a:
        if x == first:
            count += 1
        else:
            break
    print(count)


if __name__ == "__main__":
    main()
