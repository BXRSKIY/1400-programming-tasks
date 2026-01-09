def main():
    # 11.115. Стоимость 1 кг 20 видов конфет.
    # Найти стоимость самых дешёвых конфет.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    kinds = arr[:20]
    if not kinds:
        print(0.0)
    else:
        print(min(kinds))


if __name__ == "__main__":
    main()
