def main():
    import sys
    # Сопротивления элементов, соединённых параллельно.
    resistances = list(map(float, sys.stdin.read().split()))
    if not resistances:
        print(0.0)
        return
    inv_sum = 0.0
    for r in resistances:
        if r == 0:
            # При нулевом сопротивлении общее сопротивление равно 0.
            print(0.0)
            return
        inv_sum += 1.0 / r
    print(1.0 / inv_sum)


if __name__ == "__main__":
    main()
