def main():
    # 11.135. Известны очки (3, 1 или 0), полученные футбольной
    # командой за ряд игр в порядке их проведения.
    # Что было раньше: первый выигрыш (3 очка) или первый проигрыш (0 очков)?
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    first_win = None
    first_loss = None
    for i, x in enumerate(arr):
        if x == 3 and first_win is None:
            first_win = i
        if x == 0 and first_loss is None:
            first_loss = i
        if first_win is not None and first_loss is not None:
            break
    if first_win is None and first_loss is None:
        print("NONE")
    elif first_win is None:
        print("LOSS")
    elif first_loss is None:
        print("WIN")
    else:
        if first_win < first_loss:
            print("WIN")
        elif first_loss < first_win:
            print("LOSS")
        else:
            print("EQUAL")


if __name__ == "__main__":
    main()
