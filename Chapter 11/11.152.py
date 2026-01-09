def main():
    # 11.152. Дан массив из четного числа элементов. Поменять местами:
    # а) его половины;
    # б) 1-й со 2-м, 3-й с 4-м, ...;
    # в) его половины следующим образом: 1-й с последним, 2-й с предпоследним, и т.д.
    import sys
    arr = sys.stdin.read().split()
    n = len(arr)
    if n % 2 != 0:
        # задача рассчитана на чётное число, но если нет — просто работаем как есть
        pass

    # a)
    a_arr = arr[:]
    half = n // 2
    a_arr = a_arr[half:] + a_arr[:half]
    print("a)", *a_arr)

    # b)
    b_arr = arr[:]
    for i in range(0, n-1, 2):
        b_arr[i], b_arr[i+1] = b_arr[i+1], b_arr[i]
    print("b)", *b_arr)

    # c)
    c_arr = arr[:]
    for i in range(n // 2):
        j = n - 1 - i
        c_arr[i], c_arr[j] = c_arr[j], c_arr[i]
    print("c)", *c_arr)


if __name__ == "__main__":
    main()
