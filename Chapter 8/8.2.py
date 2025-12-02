def first_square_greater_than(n):
    k = 1
    while k * k <= n:
        k += 1
    return k * k


def main():
    # Среди чисел 1,4,9,16,25,... найти первое число, большее n.
    # Реализуем через цикл с условием (while).
    n = int(input())
    print(first_square_greater_than(n))


if __name__ == "__main__":
    main()
