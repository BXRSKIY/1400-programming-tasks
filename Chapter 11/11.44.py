def main():
    # 11.44. В массиве хранятся сведения о количестве осадков,
    # выпавших за каждый день января.
    # Определить общее количество осадков за январь.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    days = arr[:31]
    if len(days) < 31:
        days += [0.0] * (31 - len(days))
    print(sum(days))


if __name__ == "__main__":
    main()
