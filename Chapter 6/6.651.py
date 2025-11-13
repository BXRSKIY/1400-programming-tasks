n=input().strip()
k=int(input())
b=int(input())
x=input().strip()
y=input().strip()
a=int(input())
m=int(input())
digits=[int(ch) for ch in n]
print(sum(digits)>k and int(n)%2==0)
print(len(n)%2==0 and int(n)<=b)
print(n[0]==x and n[-1]==y)
p=1
for d in digits: p*=d
print(p<a and int(n)%b==0)
print(sum(digits)>m and int(n)%a==0)
