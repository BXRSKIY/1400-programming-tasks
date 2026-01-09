def main():
    # 11.98. Среднедневная температура воздуха каждого дня января на Янтарном берегу.
    # Определить количество дней, когда температура была ниже нуля,
    # а также на сколько градусов средняя температура этих дней
    # была меньше общей средней температуры за январь.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    temps = arr[:31]
    if len(temps) < 31:
        temps += [0.0] * (31 - len(temps))
    below = [t for t in temps if t < 0]
    cnt_below = len(below)
    if temps:
        avg_all = sum(temps) / len(temps)
    else:
        avg_all = 0.0
    if below:
        avg_below = sum(below) / len(below)
    else:
        avg_below = 0.0
    diff = avg_all - avg_below
    print(cnt_below, diff)


if __name__ == "__main__":
    main()
