def main():
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 15:
        raise ValueError("Ожидается 15 вещественных чисел")
    xs = data[:15]
    cnt = sum(1 for x in xs if x <= 33.2)
    print("YES" if cnt % 4 == 0 else "NO")


if __name__ == "__main__":
    main()
