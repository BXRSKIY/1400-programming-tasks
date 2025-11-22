def main():
    # Непустая последовательность неотрицательных целых,
    # оканчивающаяся отрицательным числом.
    total = 0
    count = 0
    while True:
        try:
            x = int(input())
        except EOFError:
            break
        if x < 0:
            break
        total += x
        count += 1
    if count == 0:
        raise ValueError("Последовательность должна содержать хотя бы одно неотрицательное число")
    print(total / count)


if __name__ == "__main__":
    main()
