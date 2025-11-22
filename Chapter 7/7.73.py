def main():
    import sys
    # Формат: m, затем m целых чисел x1..xm.
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    m = data[0]
    if len(data) < 1 + m:
        raise ValueError(f"Ожидается m={m} целых чисел")
    xs = data[1:1+m]
    count3 = sum(1 for x in xs if x % 3 == 0)
    count7 = sum(1 for x in xs if x % 7 == 0)
    print(count3, count7)


if __name__ == "__main__":
    main()
