from math import gcd

def main():
    n = int(input())
    res = []
    for k in range(1, n):
        if gcd(k, n) == 1:
            res.append(k)
    print(*res)


if __name__ == "__main__":
    main()
