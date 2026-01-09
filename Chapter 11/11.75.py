def main():
    # 11.75. В массиве записаны результаты 20 игр футбольной команды:
    # 3 — выигрыш, 1 — ничья, 0 — проигрыш.
    # Определить общее количество выигрышей и ничьих команды.
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    wins = sum(1 for x in arr if x == 3)
    draws = sum(1 for x in arr if x == 1)
    print(wins, draws)


if __name__ == "__main__":
    main()
