def main():
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 16:
        raise ValueError("Ожидается 15 чисел и n")
    y = data[:15]
    n = data[15]
    # а) сумма чисел < n
    s = sum(v for v in y if v < n)
    print(s)
    # б) найти пару, между которой находится n
    left_idx = right_idx = None
    for i in range(14):
        if y[i] < n < y[i+1]:
            left_idx = i
            right_idx = i+1
            break
    if left_idx is not None:
        print(left_idx+1, y[left_idx], right_idx+1, y[right_idx])
    else:
        print(0, 0.0, 0, 0.0)


if __name__ == "__main__":
    main()
