def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 20:
        raise ValueError("Ожидается число учеников в 20 классах")
    a = data[:20]
    print(max(a) - min(a))


if __name__ == "__main__":
    main()
