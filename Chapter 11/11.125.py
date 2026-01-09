def main():
    # 11.125. Рост 35 человек. Сколько человек имеют максимальный рост?
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    h = arr[:35]
    if not h:
        print(0)
        return
    mx = max(h)
    cnt = sum(1 for x in h if x == mx)
    print(cnt)


if __name__ == "__main__":
    main()
