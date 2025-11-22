def main():
    import sys
    # Формат: n, m, p, затем n целых чисел c1..cn.
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 3:
        raise ValueError("Ожидаются n, m, p")
    n, m, p = data[0], data[1], data[2]
    if len(data) < 3 + n:
        raise ValueError(f"Ожидается n={n} целых чисел c1..cn")
    c = data[3:3+n]
    s = sum(x for x in c if x <= m)
    # проверяем кратность p
    cond = (p != 0 and s % p == 0)
    print("YES" if cond else "NO")


if __name__ == "__main__":
    main()
