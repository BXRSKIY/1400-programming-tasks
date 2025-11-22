def main():
    import sys
    # 28 оценок по информатике.
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 28:
        raise ValueError("Ожидается 28 оценок")
    marks = data[:28]
    has_two = any(m == 2 for m in marks)
    print("YES" if has_two else "NO")


if __name__ == "__main__":
    main()
