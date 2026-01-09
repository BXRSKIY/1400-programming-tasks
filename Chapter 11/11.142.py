def main():
    # 11.142. Очки 20 футбольных команд (все очки различны).
    # Определить команды, занявшие первое и второе места.
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    pts = arr[:20]
    if len(pts) < 2:
        print(*range(1, len(pts)+1))
        return
    # первое место — максимум очков
    mx1 = max(pts)
    idx1 = pts.index(mx1) + 1
    # второй максимум
    tmp = pts.copy()
    tmp.remove(mx1)
    mx2 = max(tmp)
    # но индекс второго места нужно брать в исходном списке
    idx2 = pts.index(mx2) + 1
    print(idx1, idx2)


if __name__ == "__main__":
    main()
