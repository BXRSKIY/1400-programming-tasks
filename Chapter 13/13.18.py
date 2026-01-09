# 13.18. 28 учеников: фамилия, имя, адрес, номер школы, класс.
# Фамилию, имя и адрес тех, кто учится в заданной школе в старших (10–11) классах, записать в отдельный массив.
# Практический вывод: печатаем подходящих учеников (Фамилия Имя Адрес), по одному в строке.
# Ввод: school_number, затем 28 строк: "фамилия имя <адрес...> школа класс"

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

target_school = input().strip()
records = []
for _ in range(28):
    line = input().rstrip("\n")
    head, tail = parse_tail_ints(line, 2)  # school, class
    school, klass = tail
    parts = head.split()
    surname, name = parts[0], parts[1]
    address = " ".join(parts[2:])
    if str(school) == target_school and klass in (10, 11):
        records.append((surname, name, address))
for r in records:
    print(r[0], r[1], r[2])
