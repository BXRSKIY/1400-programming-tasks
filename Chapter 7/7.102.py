def main():
    import sys
    # Рост учащихся класса в том порядке, как в списке.
    heights = list(map(float, sys.stdin.read().split()))
    if not heights:
        print("YES")
        return
    # Проверяем порядок убывания (не возрастают).
    for i in range(1, len(heights)):
        if heights[i] > heights[i-1]:
            print("NO")
            return
    print("YES")


if __name__ == "__main__":
    main()
