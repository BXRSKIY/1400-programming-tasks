def main():
    import sys
    times = list(map(float, sys.stdin.read().split()))
    if not times:
        print(0)
        return
    min_val = times[0]
    min_pos = 1
    for i, t in enumerate(times, start=1):
        if t < min_val:
            min_val = t
            min_pos = i
    print(min_pos)


if __name__ == "__main__":
    main()
