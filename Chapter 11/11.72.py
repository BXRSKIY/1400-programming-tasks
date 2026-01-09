def main():
    # 11.72. В массиве — общая стоимость товаров, проданных фирмой
    # за каждый день марта. Определить количество дней, в которые
    # стоимость проданных товаров превысила значение s.
    # Формат ввода: s, затем значения по дням.
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if not data:
        return
    s = data[0]
    arr = data[1:]
    cnt = sum(1 for x in arr if x > s)
    print(cnt)


if __name__ == "__main__":
    main()
