def fib_sequence(limit=None):
    a, b = 1, 1
    while True:
        if limit is not None and a > limit:
            break
        yield a
        a, b = b, a + b


def first_fib_greater_than(n: int) -> int:
    a, b = 1, 1
    while a <= n:
        a, b = b, a + b
    return a


def main():
    # а) сумма всех чисел Фибоначчи, не превосходящих 1000
    s = sum(fib_sequence(1000))
    print(s)
    # б) первое число Фибоначчи, большее n (n > 1)
    n = int(input())
    print(first_fib_greater_than(n))


if __name__ == "__main__":
    main()
