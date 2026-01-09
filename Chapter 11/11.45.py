def main():
    # 11.45. В массиве хранятся сведения о стоимости 12 различных предметов.
    # Определить общую стоимость всех предметов.
    import sys
    arr = list(map(float, sys.stdin.read().split()))
    items = arr[:12]
    print(sum(items))


if __name__ == "__main__":
    main()
