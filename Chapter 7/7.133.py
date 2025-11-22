def main():
    # Непустая неубывающая последовательность вещественных чисел,
    # оканчивающаяся 1000. Найти количество идущих подряд равных чисел,
    # составляющих один блок равных элементов.
    prev = None
    cur_count = 0
    max_block = 0
    while True:
        x = float(input())
        if prev is None:
            prev = x
            cur_count = 1
        else:
            if x == prev:
                cur_count += 1
            else:
                if cur_count > max_block:
                    max_block = cur_count
                cur_count = 1
                prev = x
        if x == 1000.0:
            if cur_count > max_block:
                max_block = cur_count
            break
    print(max_block)


if __name__ == "__main__":
    main()
