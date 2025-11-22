def main():
    import sys
    # Последовательность целых чисел, первое число нечетное.
    # Найти сумму всех идущих подряд в начале последовательности
    # нечетных чисел.
    nums = list(map(int, sys.stdin.read().split()))
    if not nums:
        raise ValueError("Последовательность пуста")
    total = 0
    for x in nums:
        if x % 2 != 0:
            total += x
        else:
            break
    print(total)


if __name__ == "__main__":
    main()
