def main():
    import sys
    # Формат: n, m, q, затем n целых чисел a1..an.
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 3:
        raise ValueError("Ожидаются n, m, q")
    n, m, q = data[0], data[1], data[2]
    if len(data) < 3 + n:
        raise ValueError(f"Ожидается n={n} целых чисел a1..an")
    a = data[3:3+n]
    s = sum(x for x in a if x <= m)
    print("YES" if s > q else "NO")


if __name__ == "__main__":
    main()
