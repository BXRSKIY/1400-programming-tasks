def main():
    # 11.28. Дан массив целых чисел.
    # Найти номера элементов, оканчивающихся цифрой 0
    # (такие элементы в массиве есть).
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    # считаем, что нумерация элементов с 1
    idxs = [i + 1 for i, x in enumerate(arr) if x % 10 == 0]
    print(*idxs)


if __name__ == "__main__":
    main()
