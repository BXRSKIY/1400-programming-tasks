def main():
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    n = int(data[0])
    if len(data) < 1 + n:
        raise ValueError(f"Ожидается n={n} чисел m1..mn и далее пороги")
    # После m1..mn ожидаем два порога: 25.5 и 20, но в условии они
    # зашиты константами, поэтому дополнительных данных не нужно.
    m = data[1:1+n]
    sum_lt_25_5 = sum(x for x in m if x < 25.5)
    sum_le_20 = sum(x for x in m if x <= 20)
    cond_a = (sum_lt_25_5 <= 50)
    # Для кратности трём сумму нужно трактовать как целое.
    cond_b = (int(sum_le_20) % 3 == 0)
    print("YES" if cond_a else "NO")
    print("YES" if cond_b else "NO")


if __name__ == "__main__":
    main()
