def main():
    # 11.78. Дан массив целых чисел.
    # Определить количество четных элементов и элементов, оканчивающихся на цифру 5.
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    even_cnt = sum(1 for x in arr if x % 2 == 0)
    end5_cnt = sum(1 for x in arr if x % 10 == 5 or x % 10 == -5)
    print("even:", even_cnt)
    print("end5:", end5_cnt)


if __name__ == "__main__":
    main()
