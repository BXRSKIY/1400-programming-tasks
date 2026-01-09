def main():
    # 11.96. Известны годовые расходы семьи за 10 лет (массив).
    # Определить расходы за первые 5 лет и за последние 5 лет.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    years = arr[:10]
    if len(years) < 10:
        years += [0.0] * (10 - len(years))
    first5 = sum(years[:5])
    last5 = sum(years[5:10])
    print(first5, last5)


if __name__ == "__main__":
    main()
