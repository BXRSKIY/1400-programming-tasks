# 13.21. Известны возраст и пол каждого из 20 человек. Найти общий возраст мужчин.
# (В книге слово "массу" — очевидная опечатка; по смыслу суммируем возраст.)

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

total = 0
for _ in range(20):
    age_s, sex = input().split(maxsplit=1)
    age = int(age_s)
    if sex.strip().lower() in ('м', 'муж', 'мужской', 'male', 'm', 'man'):
        total += age
print(total)
