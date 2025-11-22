def main():
    import sys
    # Оценки нескольких судей.
    scores = list(map(float, sys.stdin.read().split()))
    if len(scores) < 3:
        raise ValueError("Должно быть не менее трех оценок")
    mx = max(scores)
    mn = min(scores)
    # удалить ровно по одной максимальной и минимальной оценке
    removed_max = False
    removed_min = False
    remaining = []
    for s in scores:
        if s == mx and not removed_max:
            removed_max = True
            continue
        if s == mn and not removed_min:
            removed_min = True
            continue
        remaining.append(s)
    if not remaining:
        print(0.0)
        return
    result = sum(remaining) / len(remaining)
    print(result)


if __name__ == "__main__":
    main()
