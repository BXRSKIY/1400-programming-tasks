def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        print("NONE")
        return
    n = data[0]
    if len(data) < 1 + n:
        raise ValueError(f"Ожидается n={n} чисел")
    x = data[1:1+n]
    mx = max(x)
    mn = min(x)
    first_max = None
    first_min = None
    for i, v in enumerate(x, start=1):
        if v == mx and first_max is None:
            first_max = i
        if v == mn and first_min is None:
            first_min = i
        if first_max is not None and first_min is not None:
            break
    if first_max < first_min:
        print("MAX")
    elif first_min < first_max:
        print("MIN")
    else:
        print("EQUAL")


if __name__ == "__main__":
    main()
