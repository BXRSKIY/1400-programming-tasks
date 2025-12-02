def count_divisors(x: int) -> int:
    cnt = 0
    for d in range(1, int(x**0.5)+1):
        if x % d == 0:
            cnt += 1
            if d*d != x:
                cnt += 1
    return cnt


def main():
    a, b = map(int, input().split())
    best_n = a
    best_cnt = count_divisors(a)
    for n in range(a+1, b+1):
        c = count_divisors(n)
        if c > best_cnt:
            best_cnt = c
            best_n = n
    print(best_n, best_cnt)


if __name__ == "__main__":
    main()
