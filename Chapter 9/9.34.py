def main():
    # Дано n (n < 100). Монеты 1,2,5 и купюры 10.
    # а) Число способов выплаты суммы n.
    # б) Все способы (кол-во купюр 10, монет 5,2,1).
    n = int(input())
    count = 0
    ways = []
    for c10 in range(0, n // 10 + 1):
        for c5 in range(0, (n - 10 * c10) // 5 + 1):
            for c2 in range(0, (n - 10 * c10 - 5 * c5) // 2 + 1):
                rest = n - 10 * c10 - 5 * c5 - 2 * c2
                if rest < 0:
                    continue
                c1 = rest
                count += 1
                ways.append((c10, c5, c2, c1))
    print(count)
    for c10, c5, c2, c1 in ways:
        print(f"10:{c10} 5:{c5} 2:{c2} 1:{c1}")


if __name__ == "__main__":
    main()
