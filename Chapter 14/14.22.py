import sys
def is_pow5(x):
    if x<1:
        return False
    while x%5==0:
        x//=5
    return x==1
def main():
    data=list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n=data[0]
    a=data[1:1+n]
    cnt=sum(1 for x in a if is_pow5(x))
    print(cnt)
if __name__=="__main__":
    main()
