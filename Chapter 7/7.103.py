def main():
    import sys
    # Очки футбольных команд даны в порядке предполагаемого места.
    points = list(map(int, sys.stdin.read().split()))
    if not points:
        print("YES")
        return
    # Чем выше место, тем не меньше очков, чем у следующего.
    for i in range(1, len(points)):
        if points[i] > points[i-1]:
            print("NO")
            return
    print("YES")


if __name__ == "__main__":
    main()
