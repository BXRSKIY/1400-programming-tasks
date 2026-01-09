# 13.8. 25 человек: фамилия, семейное положение (женат/замужем или нет) и наличие детей (есть или нет).
# Вывести фамилии женатых/замужних, имеющих детей.

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

for _ in range(25):
    line = input().rstrip("\n")
    if not line:
        continue
    parts = line.split()
    # ожидаем: surname married children
    if len(parts) < 3:
        continue
    surname = parts[0]
    married = parts[1]
    kids = parts[2]
    if truthy(married) and truthy(kids):
        print(surname)
