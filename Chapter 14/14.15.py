import sys, math
def trap_per(a,b,h):
    leg=math.sqrt(h*h+((a-b)/2)**2)
    return a+b+2*leg
def main():
    v=list(map(float, sys.stdin.read().split()))
    if len(v)<6:
        return
    p=trap_per(v[0],v[1],v[2])+trap_per(v[3],v[4],v[5])
    print(p)
if __name__=="__main__":
    main()
