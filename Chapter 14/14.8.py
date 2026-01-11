import sys, math
def tri_per_area(a,b,c):
    p=a+b+c
    s=p/2
    area=math.sqrt(max(0.0, s*(s-a)*(s-b)*(s-c)))
    return p, area
def main():
    v=list(map(float, sys.stdin.read().split()))
    if len(v)<6:
        return
    p1,a1=tri_per_area(v[0],v[1],v[2])
    p2,a2=tri_per_area(v[3],v[4],v[5])
    print(p1+p2)
    print(a1+a2)
if __name__=="__main__":
    main()
