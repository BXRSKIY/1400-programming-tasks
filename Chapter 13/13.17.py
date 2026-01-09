# 13.17. Записная книжка: 30 человек (фамилия, телефон). Определить:
# a) есть ли телефон заданного человека и вывести номер;
# b) есть ли человек с заданным телефоном и вывести фамилию.
# Ввод: 30 строк: "<фамилия> <телефон>", затем режим 'a'/'b', затем запрос (фамилия или телефон).

import re
from collections import defaultdict

def norm_phone(s: str) -> str:
    return "".join(ch for ch in s if ch.isdigit())

def truthy(s: str) -> bool:
    s = s.strip().lower()
    return s in {"1","да","yes","true","военнообязанный","женат","замужем","есть","м","муж","male","y"}

def parse_tail_ints(line: str, k: int):
    # Split line, take last k parts as ints, rest as leading text (joined with space)
    parts = line.strip().split()
    tail = list(map(int, parts[-k:]))
    head = " ".join(parts[:-k])
    return head, tail

book = []
for _ in range(30):
    line = input().rstrip("\n")
    parts = line.split()
    surname = parts[0]
    phone = norm_phone(parts[1])
    book.append((surname, phone))

mode = input().strip().lower()
query = input().rstrip("\n").strip()
if mode == "a":
    q = query
    for s, p in book:
        if s == q:
            print(p)
            break
    else:
        print("нет")
elif mode == "b":
    q = norm_phone(query)
    for s, p in book:
        if p == q:
            print(s)
            break
    else:
        print("нет")
else:
    raise SystemExit("mode must be a or b")
