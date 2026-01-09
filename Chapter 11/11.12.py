def main():
    # 11.12. Заполнить массив из 20 элементов как на рис. 11.2:
    # 20 19 ... 1
    arr = list(range(20, 0, -1))
    print(*arr)


if __name__ == "__main__":
    main()
