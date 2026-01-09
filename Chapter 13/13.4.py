# 13.4. 16 сотрудников: фамилия и отношение к воинской службе (военнообязанный или нет). Напечатать фамилии военнообязанных.

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

for _ in range(16):
    line = input().rstrip("\n")
    parts = line.split()
    if len(parts) < 2:
        continue
    surname = parts[0]
    status = " ".join(parts[1:])
    if truthy(status):
        print(surname)
