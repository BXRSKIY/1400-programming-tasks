def main():
    # Число родившихся по дням месяца (n дней).
    vals = list(map(int, input().split()))
    if not vals:
        print(0)
        return
    max_val = max(vals)
    day = vals.index(max_val) + 1
    print(day)


if __name__ == "__main__":
    main()
