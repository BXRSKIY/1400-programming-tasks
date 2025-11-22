def main():
    import sys
    masses = list(map(float, sys.stdin.read().split()))
    if not masses:
        print("NO")
        return
    mx = max(masses)
    mn = min(masses)
    print("YES" if mx > 2 * mn else "NO")


if __name__ == "__main__":
    main()
