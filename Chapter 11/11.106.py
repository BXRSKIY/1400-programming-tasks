from collections import Counter

def main():
    # 11.106. Есть ли в массиве ровно одна пара одинаковых элементов.
    import sys
    arr = sys.stdin.read().split()
    c = Counter(arr)
    pairs = [k for k,v in c.items() if v == 2]
    others_ok = all(v in (1,2) for v in c.values())
    ok = (len(pairs) == 1 and others_ok)
    print("YES" if ok else "NO")


if __name__ == "__main__":
    main()
