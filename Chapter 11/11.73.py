def main():
    # 11.73. Рост 22 учеников класса в виде массива.
    # Определить количество учеников, рост которых не превышает r.
    # Формат ввода: r, затем значения роста.
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if not data:
        return
    r = data[0]
    arr = data[1:]
    cnt = sum(1 for x in arr if x <= r)
    print(cnt)


if __name__ == "__main__":
    main()
