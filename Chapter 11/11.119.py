def main():
    # 11.119. Оценки восьми судей.
    # Выбросить одну максимальную и одну минимальную, усреднить остальные.
    import sys
    scores = list(map(float, sys.stdin.read().split()))
    scores = scores[:8]
    if len(scores) < 3:
        print(0.0)
        return
    mx = max(scores)
    mn = min(scores)
    tmp = scores.copy()
    tmp.remove(mx)
    tmp.remove(mn)
    avg = sum(tmp) / len(tmp)
    print(avg)


if __name__ == "__main__":
    main()
