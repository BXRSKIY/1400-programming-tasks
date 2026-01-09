# 13.16. 20 учеников: фамилия, имя, отчество, дата рождения (год, месяц, число).
# Определить, есть ли ученики, у которых сегодня день рождения, и вывести их имя и фамилию.
# Ввод: текущий_месяц текущий_день, затем 20 строк: "фамилия имя отчество год месяц день"

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

cur_m, cur_d = map(int, input().split())
for _ in range(20):
    line = input().rstrip("\n")
    head, tail = parse_tail_ints(line, 3)  # year month day
    y, m, d = tail
    parts = head.split()
    surname, name = parts[0], parts[1]
    if m == cur_m and d == cur_d:
        print(name, surname)
