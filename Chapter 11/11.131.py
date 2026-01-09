def main():
    # 11.131. Известен вес каждого человека из группы.
    # Верно ли, что вес самого тяжёлого превышает массу самого лёгкого
    # более чем в 2 раза?
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    if not arr:
        print("NO")
        return
    mx = max(arr)
    mn = min(arr)
    # "превышает более чем в 2 раза": mx > 2 * mn
    ok = (mx > 2 * mn)
    print("YES" if ok else "NO")


if __name__ == "__main__":
    main()
