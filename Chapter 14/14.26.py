import sys
def digit_sum(n):
    s=0
    while n>0:
        s+=n%10
        n//=10
    return s
def main():
    a,b=map(int, sys.stdin.read().split()[:2])
    sa,sb=digit_sum(a),digit_sum(b)
    if sa>sb: print(1)
    elif sb>sa: print(2)
    else: print(0)
if __name__=="__main__":
    main()
