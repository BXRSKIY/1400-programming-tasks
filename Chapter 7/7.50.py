def main():
    import sys
    # Число детей во всех первых, вторых, ..., одиннадцатых классах.
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 11:
        raise ValueError("Ожидается 11 чисел (1-11 классы)")
    classes = data[:11]
    total = 0
    # Сумма по нечетным номерам классов: 1, 3, 5, ...
    for i in range(len(classes)):
        klass = i + 1
        if klass % 2 == 1:
            total += classes[i]
    print(total)


if __name__ == "__main__":
    main()
