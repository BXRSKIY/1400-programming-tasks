def main():
    # Последовательность целых, оканчивается 9999 (не менее двух чисел).
    prev = int(input())
    idx = 1
    while True:
        cur = int(input())
        idx += 1
        if cur == 9999:
            break
        if cur == prev:
            print(idx-1, idx)
            return
        prev = cur
    print(0, 0)


if __name__ == "__main__":
    main()
