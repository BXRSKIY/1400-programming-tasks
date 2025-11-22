def main():
    import sys
    # Последовательность чисел.
    nums = list(map(float, sys.stdin.read().split()))
    if len(nums) < 3:
        print(0)
        return
    cnt = 0
    for i in range(1, len(nums)-1):
        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
