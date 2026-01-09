# 12.8. Даны названия трех городов. Вывести самое длинное и самое короткое.
c1 = input().rstrip("\n")
c2 = input().rstrip("\n")
c3 = input().rstrip("\n")
cities = [c1, c2, c3]
# Если несколько одинаковых по длине — берём первое встретившееся.
longest = max(cities, key=len)
shortest = min(cities, key=len)
print(longest)
print(shortest)
