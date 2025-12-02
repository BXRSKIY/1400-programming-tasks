def main():
    # Даны натуральные m и n. Вычислить 1^n + 2^n + ... + m^n.
    m, n = map(int, input().split())
    total = 0
    for k in range(1, m + 1):
        total += k ** n
    print(total)


if __name__ == "__main__":
    main()
