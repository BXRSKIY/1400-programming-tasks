import math

def main():
    import sys
    # Площади кругов.
    areas = list(map(float, sys.stdin.read().split()))
    if not areas:
        print(0.0)
        return
    min_area = min(areas)
    r = math.sqrt(min_area / math.pi)
    print(r)


if __name__ == "__main__":
    main()
