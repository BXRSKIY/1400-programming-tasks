def can_chain(dominoes):
    # домино представлены числами 0..66, например 24 -> (2,4)
    # строим неориентированный граф с вершинами 0..6
    from collections import defaultdict, deque
    deg = [0]*7
    adj = defaultdict(list)
    for v in dominoes:
        a = v // 10
        b = v % 10
        if not (0 <= a <= 6 and 0 <= b <= 6):
            continue
        deg[a] += 1
        deg[b] += 1
        adj[a].append(b)
        adj[b].append(a)
    # найдём любую вершину с ненулевой степенью
    start = None
    for i in range(7):
        if deg[i] > 0:
            start = i
            break
    if start is None:
        return True  # нет костей — тривиальная цепочка
    # проверка связности
    visited = [False]*7
    q = deque([start])
    visited[start] = True
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    for i in range(7):
        if deg[i] > 0 and not visited[i]:
            return False
    # условие Эйлерова пути: 0 или 2 вершины нечётной степени
    odd = sum(1 for d in deg if d % 2 == 1)
    return odd in (0, 2)


def main():
    import sys
    nums = list(map(int, sys.stdin.read().split()))
    if len(nums) < 20:
        raise ValueError("Ожидается 20 чисел")
    dominoes = nums[:20]
    # a) трактуем числа так же, условия существования цепочки те же, что и для (б)
    can_a = can_chain(dominoes)
    can_b = can_chain(dominoes)
    print("YES" if can_a else "NO")
    print("YES" if can_b else "NO")


if __name__ == "__main__":
    main()
