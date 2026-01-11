import sys, math
def tri_area(a,b,c):
    s=(a+b+c)/2
    return math.sqrt(max(0.0, s*(s-a)*(s-b)*(s-c)))
def main():
    v=list(map(float, sys.stdin.read().split()))
    if len(v)<7:
        return
    a,b,c,d,e,f,g=v[:7]
    area=tri_area(e,d,f)+tri_area(f,c,g)+tri_area(g,b,a)
    print(area)
if __name__=="__main__":
    main()
