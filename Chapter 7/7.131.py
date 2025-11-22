def main():
    import sys
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 20:
        raise ValueError("Ожидается 20 чисел")
    a = data[:20]
    # несколько подряд равных — найти количество таких чисел (максимальный блок)
    max_count = 1
    cur_count = 1
    for i in range(1, 20):
        if a[i] == a[i-1]:
            cur_count += 1
            if cur_count > max_count:
                max_count = cur_count
        else:
            cur_count = 1
    print(max_count)


if __name__ == "__main__":
    main()
