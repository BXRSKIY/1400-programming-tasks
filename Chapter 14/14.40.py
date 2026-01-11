import sys
def is_leap(y):
    return y%400==0 or (y%4==0 and y%100!=0)
def dim(y,m):
    if m in (1,3,5,7,8,10,12): return 31
    if m in (4,6,9,11): return 30
    return 29 if is_leap(y) else 28
def next_day(y,m,d):
    d+=1
    if d>dim(y,m):
        d=1
        m+=1
        if m>12:
            m=1
            y+=1
    return y,m,d
def prev_day(y,m,d):
    d-=1
    if d<1:
        m-=1
        if m<1:
            m=12
            y-=1
        d=dim(y,m)
    return y,m,d
def main():
    y,m,d=map(int, sys.stdin.read().split()[:3])
    py,pm,pd=prev_day(y,m,d)
    ny,nm,nd=next_day(y,m,d)
    print(py,pm,pd)
    print(ny,nm,nd)
if __name__=="__main__":
    main()
