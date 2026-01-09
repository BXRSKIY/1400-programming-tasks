def main():
    # 11.17. Заполнить массив десятью первыми числами Фибоначчи.
    n = 10
    fib = [0] * n
    fib[0] = 1
    fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i-1] + fib[i-2]
    print(*fib)


if __name__ == "__main__":
    main()
