def main():
    import sys
    # Расстояния до городов.
    ds = list(map(float, sys.stdin.read().split()))
    if not ds:
        print(0.0)
        return
    print(max(ds))


if __name__ == "__main__":
    main()
