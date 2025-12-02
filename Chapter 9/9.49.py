from math import gcd

def main():
    n = int(input())
    # простые делители n
    res = []
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            res.append(d)
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:
        res.append(temp)
    res = sorted(set(res))
    print(*res)


if __name__ == "__main__":
    main()
