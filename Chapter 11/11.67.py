def main():
    # 11.67. Известно число жителей в каждом доме улицы.
    # Нумерация домов подряд, нечётные номера на одной стороне, чётные — на другой.
    # Определить, на какой стороне улицы проживает больше жителей.
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    # дом 1 -> arr[0] (нечётная сторона), дом 2 -> arr[1] (чётная), ...
    odd_side = sum(arr[0::2])
    even_side = sum(arr[1::2])
    if odd_side > even_side:
        print("ODD")
    elif even_side > odd_side:
        print("EVEN")
    else:
        print("EQUAL")


if __name__ == "__main__":
    main()
