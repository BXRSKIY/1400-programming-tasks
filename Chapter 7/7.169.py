def main():
    import sys
    times = list(map(float, sys.stdin.read().split()))
    if not times:
        print(0, 0, "NO")
        return
    min_time = times[0]
    max_time = times[0]
    min_pos = 1
    max_pos = 1
    for i, t in enumerate(times, start=1):
        if t < min_time:
            min_time = t
            min_pos = i
        if t > max_time:
            max_time = t
            max_pos = i
    print(min_pos, max_pos)
    print("YES" if min_pos < max_pos else "NO")


if __name__ == "__main__":
    main()
