import sys
def count_ch(s, ch):
    return sum(1 for c in s if c==ch)
def main():
    lines=sys.stdin.read().splitlines()
    if not lines:
        return
    ch=lines[0].strip()
    ch=ch[0] if ch else ""
    total=0
    for s in lines[1:4]:
        total+=count_ch(s,ch)
    print(total)
if __name__=="__main__":
    main()
