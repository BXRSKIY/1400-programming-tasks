import sys
def count_n(s):
    return s.count("н")+s.count("Н")
def main():
    lines=sys.stdin.read().splitlines()
    if len(lines)<2:
        return
    print(count_n(lines[0])+count_n(lines[1]))
if __name__=="__main__":
    main()
