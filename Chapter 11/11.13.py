def main():
    # 11.13. Заполнить массив степенями числа 2 (от 2^1 до 2^n).
    n = int(input())
    arr = [2 ** k for k in range(1, n+1)]
    print(*arr)


if __name__ == "__main__":
    main()
