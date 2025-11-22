def main():
    import sys
    heights = list(map(float, sys.stdin.read().split()))
    if not heights:
        print(0.0)
        return
    print(max(heights) - min(heights))


if __name__ == "__main__":
    main()
