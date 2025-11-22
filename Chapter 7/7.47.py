def main():
    import sys
    # Стоимость каждого товара. Сумма тех, что > 1000 рублей.
    prices = list(map(float, sys.stdin.read().split()))
    s = 0.0
    for p in prices:
        if p > 1000:
            s += p
    print(s)


if __name__ == "__main__":
    main()
