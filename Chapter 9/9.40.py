def main():
    # Дано натуральное n. Вычислить 1^1 + 2^2 + ... + n^n.
    n = int(input())
    total = 0
    for k in range(1, n + 1):
        total += k ** k
    print(total)


if __name__ == "__main__":
    main()
