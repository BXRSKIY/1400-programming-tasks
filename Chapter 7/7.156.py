def main():
    import sys
    nums = list(map(float, sys.stdin.read().split()))
    if not nums:
        print(0)
        return
    max_len = 1
    cur_len = 1
    # sign: 1 for increasing, -1 for decreasing, 0 for undefined
    prev = nums[0]
    direction = 0
    for x in nums[1:]:
        if x > prev:
            if direction in (0, 1):
                cur_len += 1
            else:
                cur_len = 2
            direction = 1
        elif x < prev:
            if direction in (0, -1):
                cur_len += 1
            else:
                cur_len = 2
            direction = -1
        else:
            cur_len = 1
            direction = 0
        prev = x
        if cur_len > max_len:
            max_len = cur_len
    print(max_len)


if __name__ == "__main__":
    main()
