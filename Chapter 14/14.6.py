import sys
def rep(ch, n):
    return ch*n
def frame(w, h):
    if w<=0 or h<=0:
        return
    if h==1:
        print(rep("*", w))
        return
    print(rep("*", w))
    for _ in range(h-2):
        if w==1:
            print("*")
        else:
            print("*"+rep(" ", w-2)+"*")
    print(rep("*", w))
def main():
    data=sys.stdin.read().split()
    if len(data)<2:
        return
    w=int(data[0]); h=int(data[1])
    frame(w,h)
if __name__=="__main__":
    main()
