def row(k):
    return " ".join(["*"]*k)
def main():
    for k in range(1,11):
        print(row(k))
    print()
    for k in list(range(1,7))+list(range(5,0,-1)):
        print(row(k))
if __name__=="__main__":
    main()
