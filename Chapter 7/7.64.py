def main():
    import sys
    # Годы рождения людей.
    years = list(map(int, sys.stdin.read().split()))
    before_1990 = sum(1 for y in years if y < 1990)
    after_2000 = sum(1 for y in years if y > 2000)
    print(before_1990, after_2000)


if __name__ == "__main__":
    main()
