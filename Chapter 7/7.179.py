def main():
    import sys
    nums = list(map(int, sys.stdin.read().split()))
    if not nums:
        print(0)
        return
    mx = max(nums)
    cnt = sum(1 for v in nums if v == mx)
    print(cnt)


if __name__ == "__main__":
    main()
