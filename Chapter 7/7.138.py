def main():
    import sys
    temps = list(map(float, sys.stdin.read().split()))
    if not temps:
        print(0.0)
        return
    print(max(temps))


if __name__ == "__main__":
    main()
