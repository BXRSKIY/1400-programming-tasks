import sys, math
def tri_area(x1,y1,x2,y2,x3,y3):
    return abs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))/2
def main():
    v=list(map(float, sys.stdin.read().split()))
    if len(v)<10:
        return
    pts=[(v[i],v[i+1]) for i in range(0,10,2)]
    (x1,y1)=pts[0]
    area=0.0
    for i in range(1,4):
        x2,y2=pts[i]
        x3,y3=pts[i+1]
        area+=tri_area(x1,y1,x2,y2,x3,y3)
    print(area)
if __name__=="__main__":
    main()
