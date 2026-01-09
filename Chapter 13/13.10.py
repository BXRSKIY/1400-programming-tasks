# 13.10. 20 сотрудников: ФИО, адрес, дата поступления (месяц, год).
# Вывести ФИО и адрес тех, кто на сегодняшний день проработал >= 3 лет.
# День месяца не учитывать: если месяц поступления == месяцу текущего дня, считать что прошёл полный год.
# Ввод: текущий_месяц текущий_год, затем 20 строк: "фамилия имя отчество <адрес...> месяц год"

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

cur_m, cur_y = map(int, input().split())
for _ in range(20):
    line = input().rstrip("\n")
    head, tail = parse_tail_ints(line, 2)  # tail = [month, year]
    start_m, start_y = tail
    parts = head.split()
    surname, name, patronymic = parts[0], parts[1], parts[2]
    address = " ".join(parts[3:])
    years = cur_y - start_y
    if cur_m < start_m:
        years -= 1
    # если cur_m == start_m — полный год засчитывается (ничего не уменьшаем)
    if years >= 3:
        print(surname, name, patronymic, address)
