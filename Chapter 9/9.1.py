def pattern_a():
    # 3x3 of 8
    for _ in range(3):
        print("8 8 8")


def pattern_b():
    # rows 1..7 of repeated digit i, 5 times each
    for i in range(1, 8):
        print(("{} ".format(i)) * 5)


def pattern_c():
    # rows 10,20,...,80 repeated 3 or 4 times as in sample
    for k in range(1, 9):
        val = 10 * k
        if k == 1:
            reps = 3
        else:
            reps = 4
        print(" ".join(str(val) for _ in range(reps)))


def pattern_d():
    # rows 12,22,...,82 repeated 3 or 4 times similar to (c)
    for k in range(1, 9):
        val = 10 * k + 2
        if k == 1:
            reps = 3
        else:
            reps = 4
        print(" ".join(str(val) for _ in range(reps)))


def main():
    # Выводим все четыре пункта через пустую строку
    pattern_a()
    print()
    pattern_b()
    print()
    pattern_c()
    print()
    pattern_d()


if __name__ == "__main__":
    main()
