import sys
def last_pos(s, ch):
    i=s.rfind(ch)
    return i+1
def main():
    lines=sys.stdin.read().splitlines()
    if len(lines)<2:
        return
    p1=last_pos(lines[0],"й")
    p2=last_pos(lines[1],"й")
    if p1==p2: print(0)
    elif p1>p2: print(1)
    else: print(2)
if __name__=="__main__":
    main()
