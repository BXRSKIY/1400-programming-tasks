# 13.5. 15 горных вершин: название и высота (м). Напечатать названия, чья высота > 3000.
for _ in range(15):
    line = input().rstrip("\n")
    if not line:
        continue
    head, tail = " ".join(line.split()[:-1]), int(line.split()[-1])
    name = head if head else line.split()[0]
    h = tail
    if h > 3000:
        print(name)
