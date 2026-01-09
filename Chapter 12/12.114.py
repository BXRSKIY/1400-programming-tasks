# 12.114. Дано слово из 15 букв. Переставить в обратном порядке буквы между k-й и s-й (то есть (k+1)..(s-1)).
# Ввод: слово, затем k s (k < s), нумерация с 1.
word = input().rstrip("\n")
k, s = map(int, input().split())
i = k  # 0-based start for (k+1)
j = s-2  # 0-based end for (s-1)
mid = word[i:j+1][::-1] if i <= j else ""
print(word[:i] + mid + word[j+1:])
