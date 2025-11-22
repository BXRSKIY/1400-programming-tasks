def main():
    import sys
    rains = list(map(float, sys.stdin.read().split()))
    if not rains:
        print(0)
        return
    max_val = rains[0]
    max_pos = 1
    for i, r in enumerate(rains, start=1):
        if r > max_val or r == max_val:
            max_val = r
            max_pos = i
    print(max_pos)


if __name__ == "__main__":
    main()
