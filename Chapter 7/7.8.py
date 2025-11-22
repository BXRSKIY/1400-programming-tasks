def main():
    # Непустая последовательность целых чисел, заканчивающаяся нулём.
    # Найти сумму и количество всех чисел (без последнего нуля).
    total = 0
    count = 0
    while True:
        try:
            x = int(input())
        except EOFError:
            break
        if x == 0:
            break
        total += x
        count += 1
    print(total, count)


if __name__ == "__main__":
    main()
