import math

def main():
    # 11.32. Дан массив вещественных чисел.
    # а) каждый отрицательный элемент заменить его модулем;
    # б) элементы с нечетными номерами заменить квадратным корнем.
    # Номера считаем с 1, поэтому нечетные — индексы 0,2,4,...
    import sys
    arr = list(map(float, sys.stdin.read().split()))

    # a)
    a_arr = [abs(x) if x < 0 else x for x in arr]
    print("a)", *a_arr)

    # b)
    b_arr = arr[:]
    for i in range(0, len(b_arr), 2):
        if b_arr[i] >= 0:
            b_arr[i] = math.sqrt(b_arr[i])
        else:
            # для отрицательных корень не определён в вещественных;
            # оставим как есть
            b_arr[i] = b_arr[i]
    print("b)", *b_arr)


if __name__ == "__main__":
    main()
