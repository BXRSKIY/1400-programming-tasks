def main():
    # Найти все натуральные решения x^2 + y^2 = k^2,
    # где x,y,k в [1,30], решения с перестановкой x и y считать совпадающими.
    for x in range(1, 31):
        for y in range(x, 31):
            s = x * x + y * y
            k_sq = s
            k = int(k_sq ** 0.5)
            if k * k == k_sq and 1 <= k <= 30:
                print(x, y, k)


if __name__ == "__main__":
    main()
