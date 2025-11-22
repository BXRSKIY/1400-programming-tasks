def main():
    import sys
    # Рост 12 юношей.
    data = list(map(float, sys.stdin.read().split()))
    if len(data) < 12:
        raise ValueError("Ожидается рост 12 юношей")
    heights = data[:12]
    count = sum(1 for h in heights if h < 165)
    print(count)


if __name__ == "__main__":
    main()
