import sys
def digits(n):
    c=0
    while n>0:
        c+=1
        n//=10
    return c
def main():
    a,b=map(int, sys.stdin.read().split()[:2])
    da,db=digits(a),digits(b)
    if da>db: print(1)
    elif db>da: print(2)
    else: print(0)
if __name__=="__main__":
    main()
