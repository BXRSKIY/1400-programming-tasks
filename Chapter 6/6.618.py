a=int(input())
b=int(input())
start=min(a,b)
end=max(a,b)
i=start-1
while True:
    i+=1
    print((i)**0.5)
    if i>=end:
        break
