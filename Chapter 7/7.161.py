def main():
    import sys
    pts = list(map(int, sys.stdin.read().split()))
    if not pts:
        print(0)
        return
    min_val = pts[0]
    min_pos = 1
    for i, v in enumerate(pts, start=1):
        if v < min_val:
            min_val = v
            min_pos = i
    print(min_pos)


if __name__ == "__main__":
    main()
