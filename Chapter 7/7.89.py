def main():
    import sys
    # Формат: m, p, затем m целых a1..am
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 2:
        raise ValueError("Ожидаются m и p")
    m, p = data[0], data[1]
    if len(data) < 2 + m:
        raise ValueError(f"Ожидается m={m} целых чисел")
    a = data[2:2+m]
    cnt = sum(1 for v in a if v > m)
    cond = (p != 0 and cnt % p == 0)
    print("YES" if cond else "NO")


if __name__ == "__main__":
    main()
