def main():
    import sys
    # Оценки по 12 предметам.
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 12:
        raise ValueError("Ожидается 12 оценок")
    marks = data[:12]
    has_three = any(m == 3 for m in marks)
    print("YES" if not has_three else "NO")


if __name__ == "__main__":
    main()
