def main():
    # 11.47. В массиве хранится сопротивление каждого из 20 элементов
    # электрической цепи. Все элементы соединены параллельно.
    # Определить общее сопротивление цепи.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    elems = arr[:20]
    # При параллельном соединении: 1/R = sum(1/Ri).
    # Если есть нулевое сопротивление, общее сопротивление равно 0.
    if any(r == 0 for r in elems):
        print(0.0)
        return
    inv_sum = 0.0
    for r in elems:
        inv_sum += 1.0 / r
    if inv_sum == 0:
        print("INF")  # бесконечное сопротивление
    else:
        print(1.0 / inv_sum)


if __name__ == "__main__":
    main()
