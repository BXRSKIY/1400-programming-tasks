def main():
    import sys
    # Стоимости восьми предметов в двух наборах: 8 чисел первого набора, затем 8 второго.
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 16:
        raise ValueError("Ожидается 16 чисел (8+8)")
    set1 = data[:8]
    set2 = data[8:16]
    s1 = sum(set1)
    s2 = sum(set2)
    # Выводим 1, если первый набор дешевле, 2 — если второй, 0 — если равны.
    if s1 < s2:
        print(1)
    elif s2 < s1:
        print(2)
    else:
        print(0)


if __name__ == "__main__":
    main()
