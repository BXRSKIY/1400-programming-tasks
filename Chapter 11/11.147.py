def main():
    # 11.147*. Изменить знак у максимального по модулю элемента массива.
    # Минимальный элемент массива при этом не определять.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    if not arr:
        return
    # максимальный по модулю
    max_abs = max(arr, key=lambda x: abs(x))
    idx = arr.index(max_abs)
    arr[idx] = -arr[idx]
    print(*arr)


if __name__ == "__main__":
    main()
