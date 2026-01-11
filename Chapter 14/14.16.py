import sys, math
def dist(x1,y1,x2,y2):
    return math.hypot(x2-x1,y2-y1)
def main():
    v=list(map(float, sys.stdin.read().split()))
    if len(v)<6:
        return
    x1,y1,x2,y2,x3,y3=v[:6]
    p=dist(x1,y1,x2,y2)+dist(x2,y2,x3,y3)+dist(x3,y3,x1,y1)
    print(p)
if __name__=="__main__":
    main()
