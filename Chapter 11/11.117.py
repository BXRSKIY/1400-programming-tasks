def main():
    # 11.117. Рост 25 человек. На сколько самый высокий выше самого низкого?
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    h = arr[:25]
    if not h:
        print(0.0)
    else:
        print(max(h) - min(h))


if __name__ == "__main__":
    main()
