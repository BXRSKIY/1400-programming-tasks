# 13.7. 25 человек: фамилия, адрес, телефон. Найти фамилии и адреса тех, чей телефон начинается с 8905.
# Телефон может быть: 10-значным числом или вида 8-905-123-45-7. Сравнение делаем по цифрам.

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
    phone_raw = parts[-1]
    phone = norm_phone(phone_raw)
    surname = parts[0]
    address = " ".join(parts[1:-1])
    if phone.startswith("8905"):
        print(surname, address)
