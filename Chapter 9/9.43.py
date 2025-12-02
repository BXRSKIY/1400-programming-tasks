from math import gcd

def main():
    # Дано n натуральных чисел. Найти их наибольший общий делитель.
    # Используем НОД(НОД(a,b), c)...
    data = list(map(int, input().split()))
    if not data:
        return
    n = data[0]
    nums = data[1:1+n]
    if len(nums) < n:
        # можно дочитать оставшиеся из stdin
        import sys
        extra = list(map(int, sys.stdin.read().split()))
        nums += extra
        nums = nums[:n]
    current = nums[0]
    for x in nums[1:]:
        current = gcd(current, x)
    print(current)


if __name__ == "__main__":
    main()
