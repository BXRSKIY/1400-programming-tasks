import sys, math
def trap_per_area(a,b,h):
    leg=math.sqrt(h*h + ((a-b)/2)**2)
    p=a+b+2*leg
    s=(a+b)/2*h
    return p,s
def main():
    v=list(map(float, sys.stdin.read().split()))
    if len(v)<6:
        return
    p1,s1=trap_per_area(v[0],v[1],v[2])
    p2,s2=trap_per_area(v[3],v[4],v[5])
    print(p1+p2)
    print(s1+s2)
if __name__=="__main__":
    main()
