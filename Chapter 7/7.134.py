def main():
    # Непустая невозрастающая последовательность вещественных чисел,
    # оканчивающаяся нулем. Найти количество различных чисел.
    prev = None
    distinct = 0
    while True:
        x = float(input())
        if prev is None or x != prev:
            distinct += 1
            prev = x
        if x == 0.0:
            break
    print(distinct)


if __name__ == "__main__":
    main()
