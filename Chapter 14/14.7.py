import sys
def swap(x, y):
    return y, x
def main():
    data=sys.stdin.read().split()
    if len(data)<4:
        return
    a,b,c,d=data[:4]
    a,b=swap(a,b)
    c,d=swap(c,d)
    sys.stdout.write(f"{a} {b} {c} {d}")
if __name__=="__main__":
    main()
