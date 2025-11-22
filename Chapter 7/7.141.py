import math

def main():
    import sys
    # Площади квадратов. Найти длину диагонали самого большого из них.
    areas = list(map(float, sys.stdin.read().split()))
    if not areas:
        print(0.0)
        return
    max_area = max(areas)
    # сторона = sqrt(S), диагональ = сторона * sqrt(2)
    diag = math.sqrt(max_area) * math.sqrt(2.0)
    print(diag)


if __name__ == "__main__":
    main()
