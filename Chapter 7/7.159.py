def main():
    import sys
    nums = list(map(int, sys.stdin.read().split()))
    if not nums:
        print(0)
        return
    max_val = nums[0]
    max_pos = 1
    for i, v in enumerate(nums, start=1):
        if v > max_val or v == max_val:
            max_val = v
            max_pos = i
    print(max_pos)


if __name__ == "__main__":
    main()
