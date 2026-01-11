import sys
def rep(ch, n):
    return ch * n
def main():
    data=sys.stdin.read()
    if not data:
        return
    parts=data.split()
    ch=parts[0]
    n=int(parts[1]) if len(parts)>1 else 0
    sys.stdout.write(rep(ch, n))
if __name__=="__main__":
    main()
