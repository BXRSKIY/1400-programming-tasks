def main():
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 15:
        raise ValueError("Ожидается 15 вещественных чисел b1..b15")
    b = data[:15]
    vals = [x for x in b if x > 10]
    if not vals:
        print(0.0)
    else:
        print(sum(vals) / len(vals))


if __name__ == "__main__":
    main()
