def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 20:
        raise ValueError("Ожидается 20 целых чисел a1..a20")
    a = data[:20]
    s = 0
    # Сумма a2 + a4 + ... (элементы с четными номерами).
    for i in range(len(a)):
        index = i + 1  # номер элемента
        if index % 2 == 0:
            s += a[i]
    print(s)


if __name__ == "__main__":
    main()
