def main():
    import sys
    # Формат: n, затем n чисел жителей по домам 1..n.
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    n = data[0]
    if len(data) < 1 + n:
        raise ValueError(f"Ожидается n={n} значений")
    people = data[1:1+n]
    odd_side = 0
    even_side = 0
    for i, x in enumerate(people, start=1):
        if i % 2 == 1:
            odd_side += x
        else:
            even_side += x
    # 1 - нечетная сторона, 2 - четная, 0 - одинаково
    if odd_side > even_side:
        print(1)
    elif even_side > odd_side:
        print(2)
    else:
        print(0)


if __name__ == "__main__":
    main()
