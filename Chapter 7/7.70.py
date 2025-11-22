def main():
    import sys
    # Количество осадков за каждый день мая (31 значение).
    # Нужно максимальное число подряд идущих дней без осадков (значение 0).
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 31:
        raise ValueError("Ожидается 31 значение осадков")
    rains = data[:31]
    max_streak = 0
    cur_streak = 0
    for val in rains:
        if val == 0:
            cur_streak += 1
            if cur_streak > max_streak:
                max_streak = cur_streak
        else:
            cur_streak = 0
    print(max_streak)


if __name__ == "__main__":
    main()
