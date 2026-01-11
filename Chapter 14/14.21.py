import sys, math
def is_square(n):
    if n<0: 
        return False
    r=int(math.isqrt(n))
    return r*r==n
def main():
    data=list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n=data[0]
    a=data[1:1+n]
    cnt=sum(1 for x in a if is_square(x))
    print(cnt)
if __name__=="__main__":
    main()
