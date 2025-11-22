def main():
    import sys
    # Последовательность ненулевых целых чисел.
    nums = list(map(int, sys.stdin.read().split()))
    if not nums:
        print(0)
        return
    cnt = 0
    prev = nums[0]
    for x in nums[1:]:
        if (prev > 0 and x < 0) or (prev < 0 and x > 0):
            cnt += 1
        prev = x
    print(cnt)


if __name__ == "__main__":
    main()
