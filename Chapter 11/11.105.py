def main():
    # 11.105. Есть ли в массиве одинаковые элементы?
    import sys
    arr = sys.stdin.read().split()
    seen = set()
    has_dup = False
    for x in arr:
        if x in seen:
            has_dup = True
            break
        seen.add(x)
    print("YES" if has_dup else "NO")


if __name__ == "__main__":
    main()
