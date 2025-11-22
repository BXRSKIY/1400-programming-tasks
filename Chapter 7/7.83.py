def main():
    import sys
    nums = list(map(int, sys.stdin.read().split()))
    has_even = any(x % 2 == 0 for x in nums)
    print("YES" if has_even else "NO")


if __name__ == "__main__":
    main()
