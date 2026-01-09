def main():
    # 11.132. Численность каждого из 40 классов школы.
    # Верно ли, что в самом многочисленном классе учится
    # на 10 учеников больше, чем в самом малочисленном?
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    classes = arr[:40]
    if not classes:
        print("NO")
        return
    mx = max(classes)
    mn = min(classes)
    ok = (mx == mn + 10)
    print("YES" if ok else "NO")


if __name__ == "__main__":
    main()
