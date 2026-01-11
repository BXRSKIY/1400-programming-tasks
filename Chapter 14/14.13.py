import sys
def sign(a):
    if a<0: return -1
    if a>0: return 1
    return 0
def main():
    v=list(map(float, sys.stdin.read().split()))
    if len(v)<2: 
        return
    x,y=v[0],v[1]
    z=sign(x)+sign(y)
    print(int(z))
if __name__=="__main__":
    main()
