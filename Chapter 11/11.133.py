def main():
    # 11.133. Дана информация о дороге: длина каждого из 10 участков и
    # разрешённая скорость на каждом участке.
    # Найти длину всего пути и среднюю допустимую скорость.
    #
    # Формат ввода:
    # l1 v1 l2 v2 ... l10 v10
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 20:
        # дополним нулями
        data += [0.0] * (20 - len(data))
    lengths = data[0::2][:10]
    speeds = data[1::2][:10]
    total_length = sum(lengths)
    # среднюю допустимую скорость понимаем как средневзвешенную по длине
    total_time = 0.0
    for L, V in zip(lengths, speeds):
        if V > 0:
            total_time += L / V
    avg_speed = total_length / total_time if total_time > 0 else 0.0
    print(total_length, avg_speed)


if __name__ == "__main__":
    main()
