def main():
    import sys
    # Осадки за каждый день месяца.
    # Найти общее количество осадков, выпавших 2-го, 4-го, 6-го и т.д.
    rains = list(map(float, sys.stdin.read().split()))
    total = 0.0
    for i, x in enumerate(rains, start=1):
        if i % 2 == 0:  # четные дни
            total += x
    print(total)


if __name__ == "__main__":
    main()
