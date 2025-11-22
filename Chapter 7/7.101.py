def main():
    # Последовательность вещественных чисел, заканчивается числом 10000.
    # Проверить упорядоченность по возрастанию (строго).
    # В случае нарушения вывести номер первого нарушающего элемента,
    # иначе вывести 0.
    nums = []
    idx = 0
    while True:
        try:
            x = float(input())
        except EOFError:
            break
        nums.append(x)
        idx += 1
        if x == 10000.0:
            break
    if len(nums) < 2:
        print(0)
        return
    # не учитываем последнее число-«сторож» в проверке
    for i in range(1, len(nums)-1):
        if nums[i] <= nums[i-1]:
            print(i+1)
            return
    print(0)


if __name__ == "__main__":
    main()
