def digit_sum(k: int) -> int:
    s = 0
    while k > 0:
        s += k % 10
        k //= 10
    return s


def main():
    # Даны натуральные m и n.
    # Получить все натуральные числа, меньшие n, квадрат суммы
    # цифр которых равен m.
    m, n = map(int, input().split())
    for x in range(1, n):
        s = digit_sum(x)
        if s * s == m:
            print(x)


if __name__ == "__main__":
    main()
