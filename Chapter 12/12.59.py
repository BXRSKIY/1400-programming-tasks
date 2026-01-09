# 12.59. Дано предложение. Определить число вхождений в него некоторого символа.
s = input().rstrip("\n")
ch = input().rstrip("\n")
target = ch[0] if ch else ""
print(sum(1 for c in s if c == target))
