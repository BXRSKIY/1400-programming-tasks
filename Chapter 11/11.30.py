def main():
    # 11.30. В массиве хранится количество побед,
    # одержанных 20 футбольными командами.
    # Определить номера команд, имеющих меньше трех побед.
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    teams = arr[:20]
    res = [i + 1 for i, w in enumerate(teams) if w < 3]
    print(*res)


if __name__ == "__main__":
    main()
