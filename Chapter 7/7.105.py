def main():
    # Непустая последовательность целых, оканчивается отрицательным числом.
    nums = []
    while True:
        x = int(input())
        nums.append(x)
        if x < 0:
            break
    # сравниваем все числа, кроме последнего отрицательного «сторожа»
    core = nums[:-1]
    if not core:
        print("YES")
        return
    first = core[0]
    print("YES" if all(x == first for x in core) else "NO")


if __name__ == "__main__":
    main()
