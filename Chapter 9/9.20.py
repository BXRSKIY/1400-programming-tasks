def count_divisors(x: int) -> int:
    cnt = 0
    for d in range(1, int(x**0.5)+1):
        if x % d == 0:
            cnt += 1
            if d*d != x:
                cnt += 1
    return cnt


def main():
    n = int(input())
    for k in range(1, n+1):
        c = count_divisors(k)
        print(str(k) + "+"*c)


if __name__ == "__main__":
    main()
