def main():
    import sys
    # длины 12 сторон 12-угольника
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 12:
        raise ValueError("Ожидается 12 длин сторон")
    sides = data[:12]
    print(sum(sides))


if __name__ == "__main__":
    main()
