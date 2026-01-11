import sys
def in_arr(x, s):
    return x in s
def main():
    data=list(map(int, sys.stdin.read().split()))
    if len(data)<3:
        return
    i=0
    n1=data[i]; i+=1
    m1=data[i:i+n1]; i+=n1
    n2=data[i]; i+=1
    m2=data[i:i+n2]; i+=n2
    n3=data[i]; i+=1
    m3=data[i:i+n3]
    set3=set(m3)
    c1=sum(1 for x in m1 if in_arr(x,set3))
    c2=sum(1 for x in m2 if in_arr(x,set3))
    if c1>c2: print(1)
    elif c2>c1: print(2)
    else: print(0)
if __name__=="__main__":
    main()
