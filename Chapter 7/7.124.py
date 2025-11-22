def main():
    import sys
    # 20 значений очков и число N.
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 21:
        raise ValueError("Ожидается 20 очков и N")
    points = data[:20]
    N = data[20]
    pos = -1
    for i, v in enumerate(points, start=1):
        if v == N:
            pos = i
            break
    print(pos)


if __name__ == "__main__":
    main()
