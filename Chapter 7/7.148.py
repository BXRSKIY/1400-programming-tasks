def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        print("NO")
        return
    mx = max(data)
    mn = min(data)
    print("YES" if mx - mn <= 25 else "NO")


if __name__ == "__main__":
    main()
