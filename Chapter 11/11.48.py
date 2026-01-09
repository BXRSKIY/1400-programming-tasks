def main():
    # 11.48. В массиве хранятся сведения о количестве осадков,
    # выпавших за каждый день июня.
    # Определить общее количество осадков, выпавших за каждую декаду месяца.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    days = arr[:30]
    if len(days) < 30:
        days += [0.0] * (30 - len(days))
    dec1 = sum(days[0:10])
    dec2 = sum(days[10:20])
    dec3 = sum(days[20:30])
    print(dec1, dec2, dec3)


if __name__ == "__main__":
    main()
