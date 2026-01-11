import sys
def is_even(x):
    return x%2==0
def main():
    v=list(map(int, sys.stdin.read().split()))
    if len(v)<16:
        return
    a=v[:8]
    b=v[8:16]
    ce=sum(1 for x in a if is_even(x))
    co=sum(1 for x in b if not is_even(x))
    print(ce)
    print(co)
if __name__=="__main__":
    main()
