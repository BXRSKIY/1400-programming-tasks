def main():
    # 11.43. Дан массив a. Определить знакопеременную сумму
    # a[1] – a[2] + a[3] – a[4] + … .
    # Условный оператор и операцию возведения в степень не использовать.
    #
    # В Python считаем, что a[0] = a[1], a[1] = a[2] и т. д. (1-базная нумерация задачи).
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    s = 0.0
    sign = 1.0
    for x in arr:
        s += sign * x
        sign = -sign
    print(s)


if __name__ == "__main__":
    main()
