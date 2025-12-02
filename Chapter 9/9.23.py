def count_divisors(x: int) -> int:
    cnt = 0
    for d in range(1, int(x**0.5)+1):
        if x % d == 0:
            cnt += 1
            if d*d != x:
                cnt += 1
    return cnt


def main():
    a, b, k = map(int, input().split())
    for n in range(a, b+1):
        if count_divisors(n) == k:
            print(n)


if __name__ == "__main__":
    main()
