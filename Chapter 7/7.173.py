def main():
    import sys
    v = list(map(float, sys.stdin.read().split()))
    if len(v) < 12:
        raise ValueError("Ожидается 12 скоростей")
    v = v[:12]
    uniq = sorted(set(v))
    if len(uniq) < 2:
        # нет такого значения, берем максимум
        print(uniq[-1])
    else:
        print(uniq[-2])


if __name__ == "__main__":
    main()
