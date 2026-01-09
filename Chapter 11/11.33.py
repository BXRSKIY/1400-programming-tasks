import math

def main():
    # 11.33. Дан массив вещественных чисел.
    # а) каждый элемент, больший 10, заменить его квадратным корнем;
    # б) элементы с четными номерами заменить модулем.
    # Номера считаем с 1: четные — индексы 1,3,5,...
    import sys
    arr = list(map(float, sys.stdin.read().split()))

    # a)
    a_arr = [math.sqrt(x) if x > 10 else x for x in arr]
    print("a)", *a_arr)

    # b)
    b_arr = arr[:]
    for i in range(1, len(b_arr), 2):
        b_arr[i] = abs(b_arr[i])
    print("b)", *b_arr)


if __name__ == "__main__":
    main()
