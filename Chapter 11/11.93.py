def main():
    # 11.93. Известны стоимости нескольких марок легковых автомобилей.
    # Определить количество марок, стоимость которых превышает стоимость
    # самого дешёвого более чем в два раза.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    if not arr:
        print(0)
        return
    mn = min(arr)
    cnt = sum(1 for x in arr if x > 2 * mn)
    print(cnt)


if __name__ == "__main__":
    main()
