def main():
    import sys
    pts = list(map(int, sys.stdin.read().split()))
    if len(pts) < 12:
        raise ValueError("Ожидается 12 значений очков")
    pts = pts[:12]
    uniq = sorted(set(pts))
    if len(uniq) < 2:
        print(uniq[-1])
    else:
        print(uniq[-2])


if __name__ == "__main__":
    main()
