def main():
    # 11.130. Дан массив вещественных чисел. Выяснить, верно ли, что:
    # а) максимальный элемент превышает минимальный не более чем на 25;
    # б) минимальный элемент меньше максимального более чем в 2 раза.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    if not arr:
        print("a) NO")
        print("b) NO")
        return
    mx = max(arr)
    mn = min(arr)
    a_ok = (mx - mn <= 25)
    # "меньше более чем в 2 раза" — интерпретируем как mn * 2 < mx
    b_ok = (mn * 2 < mx)
    print("a)", "YES" if a_ok else "NO")
    print("b)", "YES" if b_ok else "NO")


if __name__ == "__main__":
    main()
