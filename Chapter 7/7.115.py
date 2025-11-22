def main():
    import sys
    # Формат: m, n, затем m целых a1..am.
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 2:
        raise ValueError("Ожидаются m и n")
    m, n = data[0], data[1]
    if len(data) < 2 + m:
        raise ValueError(f"Ожидается m={m} чисел")
    a = data[2:2+m]
    vals = [x for x in a if x % n == 0]
    if not vals:
        print(0.0)
    else:
        print(sum(vals) / len(vals))


if __name__ == "__main__":
    main()
