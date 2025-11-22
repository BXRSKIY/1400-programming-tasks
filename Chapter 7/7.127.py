def main():
    # Непустая последовательность целых, оканчивающаяся 100.
    # Проверим, есть ли число больше 100; если есть — номер первого.
    idx = 0
    first_pos = 0
    while True:
        x = int(input())
        idx += 1
        if x == 100:
            break
        if first_pos == 0 and x > 100:
            first_pos = idx
    print(first_pos)


if __name__ == "__main__":
    main()
