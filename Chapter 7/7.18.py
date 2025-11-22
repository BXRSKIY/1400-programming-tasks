def main():
    import sys
    # Дано n, затем b, затем x1..xn. Проверить, что сумма xi кратна b.
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 2:
        raise ValueError("Ожидается хотя бы n и b")
    n = data[0]
    if len(data) < 2 + n:
        raise ValueError(f"Ожидается n={n} чисел x1..xn")
    b = data[1]
    xs = data[2:2+n]
    s = sum(xs)
    if b == 0:
        # деление на 0 не имеет смысла, условие кратности не определено
        print("NO")
    else:
        print("YES" if s % b == 0 else "NO")


if __name__ == "__main__":
    main()
