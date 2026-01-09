def main():
    # 11.46. В массиве хранится сопротивление каждого из 20 элементов
    # электрической цепи. Все элементы соединены последовательно.
    # Определить общее сопротивление цепи.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    elems = arr[:20]
    print(sum(elems))


if __name__ == "__main__":
    main()
