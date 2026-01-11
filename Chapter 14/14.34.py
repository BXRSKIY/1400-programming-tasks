import sys
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def main():
    data=list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n=data[0]
    arr=data[1:1+n]
    g=arr[0] if arr else 0
    for x in arr[1:]:
        g=gcd(g,x)
    print(g)
if __name__=="__main__":
    main()
