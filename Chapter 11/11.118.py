def main():
    # 11.118. Год рождения 30 человек.
    # На сколько лет самый старший старше самого младшего?
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    years = arr[:30]
    if not years:
        print(0)
    else:
        oldest = min(years)   # старший
        youngest = max(years) # младший
        print(youngest - oldest)


if __name__ == "__main__":
    main()
