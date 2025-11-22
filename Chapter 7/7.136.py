def main():
    import sys
    # Результаты лыжников приходят по очереди (время, меньше — лучше).
    # После каждого ввода выводить лучший результат.
    best = None
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        t = float(line)
        if best is None or t < best:
            best = t
        print(best)


if __name__ == "__main__":
    main()
