import sys, math
def has_real_roots(A,B,C):
    eps=1e-12
    if abs(A)<eps:
        if abs(B)<eps:
            return abs(C)<eps
        return True
    D=B*B-4*A*C
    return D>=-eps
def main():
    v=list(map(float, sys.stdin.read().split()))
    if len(v)<3:
        return
    a,b,c=v[:3]
    cnt=0
    if has_real_roots(a,b,c): cnt+=1
    if has_real_roots(b,a,c): cnt+=1
    if has_real_roots(c,a,b): cnt+=1
    print(cnt)
if __name__=="__main__":
    main()
