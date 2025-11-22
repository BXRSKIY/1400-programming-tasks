def main():
    import sys
    # Результаты двух десятиборцев: сначала 10 чисел первого, затем 10 второго.
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 20:
        raise ValueError("Ожидается 20 чисел (10+10)")
    s1 = sum(data[:10])
    s2 = sum(data[10:20])
    # Выводим 1, если первый лучше, 2 — если второй, 0 — если равны.
    if s1 > s2:
        print(1)
    elif s2 > s1:
        print(2)
    else:
        print(0)


if __name__ == "__main__":
    main()
