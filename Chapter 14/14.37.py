import sys
def share(s, ch):
    letters=[c for c in s if c!=" "]
    if not letters:
        return 0.0
    return 100.0*sum(1 for c in letters if c==ch)/len(letters)
def main():
    lines=sys.stdin.read().splitlines()
    if len(lines)<2:
        return
    p1=share(lines[0],"о")
    p2=share(lines[1],"о")
    if abs(p1-p2)<1e-12: print(0)
    elif p1>p2: print(1)
    else: print(2)
if __name__=="__main__":
    main()
