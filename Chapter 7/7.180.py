def main():
    import sys
    temps = list(map(float, sys.stdin.read().split()))
    if not temps:
        print(0)
        return
    mn = min(temps)
    cnt = sum(1 for t in temps if t == mn)
    print(cnt)


if __name__ == "__main__":
    main()
