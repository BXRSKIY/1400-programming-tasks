def main():
    import sys
    ages = list(map(int, sys.stdin.read().split()))
    if not ages:
        print("NONE")
        return
    max_age = max(ages)
    min_age = min(ages)
    first_max = None
    first_min = None
    for i, a in enumerate(ages, start=1):
        if a == max_age and first_max is None:
            first_max = i
        if a == min_age and first_min is None:
            first_min = i
        if first_max is not None and first_min is not None:
            break
    if first_max < first_min:
        print("OLDEST")
    elif first_min < first_max:
        print("YOUNGEST")
    else:
        print("EQUAL")


if __name__ == "__main__":
    main()
