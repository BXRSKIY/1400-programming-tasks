def main():
    import sys
    # Масса каждого предмета набора.
    masses = list(map(float, sys.stdin.read().split()))
    if not masses:
        raise ValueError("Не введено ни одной массы")
    print(sum(masses) / len(masses))


if __name__ == "__main__":
    main()
