def main():
    # 11.101. Количество осадков за 15 лет.
    # Вычислить среднее и отклонения от среднего по годам.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    years = arr[:15]
    if len(years) < 15:
        years += [0.0] * (15 - len(years))
    avg = sum(years) / 15.0
    print("average:", avg)
    deviations = [x - avg for x in years]
    print("deviations:", *deviations)


if __name__ == "__main__":
    main()
