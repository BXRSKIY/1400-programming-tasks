def main():
    import sys
    # Рост каждого ученика двух классов, численность одинакова.
    heights = list(map(float, sys.stdin.read().split()))
    if not heights or len(heights) % 2 != 0:
        raise ValueError("Должно быть четное количество значений роста")
    n = len(heights) // 2
    class1 = heights[:n]
    class2 = heights[n:]
    avg1 = sum(class1) / n
    avg2 = sum(class2) / n
    print(avg1, avg2)


if __name__ == "__main__":
    main()
