def main():
    # Последовательность вещественных чисел, ввод
    # продолжается до первого нулевого значения.
    # Нужно количество чисел, предшествующих первому нулю.
    count = 0
    while True:
        try:
            x = float(input())
        except EOFError:
            break
        if x == 0.0:
            break
        count += 1
    print(count)


if __name__ == "__main__":
    main()
