def main():
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 15:
        raise ValueError("Ожидается 15 вещественных чисел c1..c15")
    c = data[:15]
    s = 0.0
    # -c1 - c3 - c5 - ...
    for i in range(0, len(c), 2):
        s -= c[i]
    print(s)


if __name__ == "__main__":
    main()
