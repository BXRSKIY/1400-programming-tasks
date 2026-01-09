def main():
    # 11.66. Осадки за каждый день февраля.
    # Верно ли, что по чётным числам выпало больше осадков,
    # чем по нечётным?
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    even_sum = sum(arr[1::2])   # дни 2,4,...
    odd_sum = sum(arr[0::2])    # дни 1,3,...
    print("YES" if even_sum > odd_sum else "NO")


if __name__ == "__main__":
    main()
