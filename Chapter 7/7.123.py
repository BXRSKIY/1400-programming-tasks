def main():
    import sys
    # Рост 15 юношей в порядке строгого убывания, все различны.
    hs = list(map(float, sys.stdin.read().split()))
    if len(hs) < 15:
        raise ValueError("Ожидается 15 значений")
    hs = hs[:15]
    mx = hs[0]
    cnt = sum(1 for h in hs if h < mx)
    print(cnt)


if __name__ == "__main__":
    main()
