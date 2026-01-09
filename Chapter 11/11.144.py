def main():
    # 11.144. Количество людей, живущих на каждом из 15 этажей.
    # Определить два этажа, на которых проживает меньше всего людей.
    import sys
    arr = list(map(int, sys.stdin.read().split()))
    people = arr[:15]
    if len(people) < 2:
        print(*range(1, len(people)+1))
        return
    mn1 = min(people)
    idx1 = people.index(mn1)
    tmp = people.copy()
    tmp.pop(idx1)
    mn2 = min(tmp)
    idx2 = people.index(mn2)
    print(idx1+1, idx2+1)


if __name__ == "__main__":
    main()
