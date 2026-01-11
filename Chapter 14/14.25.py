def fact(n):
    r=1
    for i in range(2,n+1):
        r*=i
    return r
def main():
    val=(2*fact(5)+3*fact(8))/(fact(6)+fact(4))
    if abs(val-round(val))<1e-12:
        print(int(round(val)))
    else:
        print(val)
if __name__=="__main__":
    main()
