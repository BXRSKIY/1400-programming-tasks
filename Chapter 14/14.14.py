import sys, math
def hyp(a,b):
    return math.sqrt(a*a+b*b)
def main():
    v=list(map(float, sys.stdin.read().split()))
    if len(v)<3:
        return
    AB,AD,CD=v[0],v[1],v[2]
    BD=hyp(AB,AD)
    BC=hyp(BD,CD)
    P=AB+BC+CD+AD
    print(P)
if __name__=="__main__":
    main()
