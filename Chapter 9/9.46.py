def digital_root(n: int) -> int:
    # Цифровой корень: повторяем сумму цифр, пока не останется одна цифра.
    while n >= 10:
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        n = s
    return n


def main():
    n = int(input())
    print(digital_root(n))


if __name__ == "__main__":
    main()
