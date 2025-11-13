n=input().strip()
d=input().strip()
cnt=n.count(d)
first=(n.find(d)+1) if d in n else 0
last=(n.rfind(d)+1) if d in n else 0
print(cnt)
print(first)
print(last)
