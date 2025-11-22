def main():
    # Положительные целые числа, оканчивающиеся нулём.
    # Вывести: a1, a1*a2, a1*a2*a3, ..., 0.
    products = []
    prod = 1
    while True:
        try:
            x = int(input())
        except EOFError:
            break
        if x == 0:
            break
        prod *= x
        products.append(prod)
    products.append(0)
    # Выводим через пробел в одной строке.
    print(*products)


if __name__ == "__main__":
    main()
