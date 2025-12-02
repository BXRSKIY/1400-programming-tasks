def main():
    # Число родившихся по месяцам (12 чисел).
    babies = list(map(int, input().split()))
    if len(babies) != 12:
        raise ValueError("Нужно 12 значений")
    print(sum(babies))
    max_val = max(babies)
    print(babies.index(max_val) + 1)


if __name__ == "__main__":
    main()
