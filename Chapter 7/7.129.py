def main():
    # Непустая последовательность целых, оканчивающаяся -1.
    # Проверим, есть ли число, кратное 5; если есть — номер первого.
    idx = 0
    first = 0
    while True:
        x = int(input())
        idx += 1
        if x == -1:
            break
        if first == 0 and x % 5 == 0:
            first = idx
    print(first)


if __name__ == "__main__":
    main()
