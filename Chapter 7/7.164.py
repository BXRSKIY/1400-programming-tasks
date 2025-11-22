import math

def main():
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if not data:
        raise ValueError("Нет данных")
    n = int(data[0])
    if len(data) < 1 + 2*n:
        raise ValueError(f"Ожидается {n} пар чисел")
    vals = data[1:1+2*n]
    max_arith = None
    idx_max_arith = 0
    min_geom = None
    idx_min_geom = 0
    for i in range(n):
        a = vals[2*i]
        b = vals[2*i+1]
        ar = (a + b) / 2.0
        gm = math.sqrt(a * b)
        if max_arith is None or ar >= max_arith:
            max_arith = ar
            idx_max_arith = i + 1  # номер пары
        if min_geom is None or gm < min_geom:
            min_geom = gm
            idx_min_geom = i + 1
    print(idx_max_arith)
    print(idx_min_geom)


if __name__ == "__main__":
    main()
