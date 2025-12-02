def main():
    # Количество осадков по месяцам (12 чисел).
    rains = list(map(float, input().split()))
    if len(rains) != 12:
        raise ValueError("Нужно 12 значений осадков по месяцам")
    # а) общий годовой объём
    print(sum(rains))
    # б) номер месяца с максимальными осадками (первый, если несколько)
    max_val = max(rains)
    month = rains.index(max_val) + 1
    print(month)


if __name__ == "__main__":
    main()
