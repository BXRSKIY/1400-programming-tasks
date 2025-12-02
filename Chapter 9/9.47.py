def main():
    # 100 рублей, нужно купить 100 голов:
    # бык = 10 руб, корова = 5 руб, теленок = 0.5 руб.
    # b + c + t = 100
    # 10b + 5c + 0.5t = 100
    solutions = []
    for b in range(0, 101):
        for c in range(0, 101 - b):
            t = 100 - b - c
            cost = 10 * b + 5 * c + 0.5 * t
            if abs(cost - 100.0) < 1e-9:
                solutions.append((b, c, t))
    for b, c, t in solutions:
        print(b, c, t)


if __name__ == "__main__":
    main()
