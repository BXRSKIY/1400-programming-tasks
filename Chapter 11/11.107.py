def main():
    # 11.107. В массиве имеется только два одинаковых элемента.
    # Найти их значение и позиции.
    import sys
    arr = sys.stdin.read().split()
    pos = {}
    val = None
    i1 = i2 = None
    for i, x in enumerate(arr):
        if x in pos:
            val = x
            i1 = pos[x]
            i2 = i
            break
        pos[x] = i
    if val is None:
        return
    print("value:", val)
    print("positions:", i1+1, i2+1)


if __name__ == "__main__":
    main()
