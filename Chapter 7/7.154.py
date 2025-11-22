def main():
    import sys
    nums = list(map(float, sys.stdin.read().split()))
    if not nums:
        print(0)
        return
    max_len = 1
    cur = 1
    prev = nums[0]
    for x in nums[1:]:
        if x == prev:
            cur += 1
            if cur > max_len:
                max_len = cur
        else:
            cur = 1
            prev = x
    print(max_len)


if __name__ == "__main__":
    main()
