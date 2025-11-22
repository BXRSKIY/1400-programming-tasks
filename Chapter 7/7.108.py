def main():
    import sys
    # Формат: m, n, затем m целых b1..bm.
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 2:
        raise ValueError("Ожидаются m и n")
    m, n = data[0], data[1]
    if len(data) < 2 + m:
        raise ValueError(f"Ожидается m={m} чисел")
    b = data[2:2+m]
    vals = [x for x in b if x % n == 0]
    if not vals:
        raise ValueError("По условию должны быть числа, кратные n")
    print(sum(vals) / len(vals))


if __name__ == "__main__":
    main()
