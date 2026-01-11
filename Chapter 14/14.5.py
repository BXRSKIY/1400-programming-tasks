def frame(w, h):
    if w<=0 or h<=0:
        return
    if h==1:
        print("*"*w)
        return
    print("*"*w)
    for _ in range(h-2):
        if w==1:
            print("*")
        else:
            print("*" + " "*(w-2) + "*")
    print("*"*w)
def main():
    frame(60, 20)
if __name__=="__main__":
    main()
