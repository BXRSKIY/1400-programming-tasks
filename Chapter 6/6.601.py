a=int(input())
b=int(input())
if a<=b and a>0 and b>0:
    q=0
    r=b
    while r>=a:
        r-=a
        q+=1
    print(q,r)
else:
    print("Некорректные входные данные")
