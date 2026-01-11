import sys
def rook_att(c,d,x,y):
    return c==x or d==y
def bishop_att(c,d,x,y):
    return abs(c-x)==abs(d-y)
def queen_att(c,d,x,y):
    return rook_att(c,d,x,y) or bishop_att(c,d,x,y)
def knight_att(c,d,x,y):
    dx=abs(c-x); dy=abs(d-y)
    return (dx,dy) in ((1,2),(2,1))
def king_att(c,d,x,y):
    return max(abs(c-x),abs(d-y))==1
def safe(attacks, c,d, x,y):
    return not attacks(c,d,x,y)
def main():
    data=list(map(int, sys.stdin.read().split()))
    if len(data)<6:
        return
    a,b,c,d,e,f=data[:6]
    combos=[
        ("rook+queen", lambda: safe(lambda C,D,X,Y: rook_att(C,D,X,Y) or queen_att(C,D,X,Y), c,d,e,f)),
        ("rook+knight", lambda: safe(lambda C,D,X,Y: rook_att(C,D,X,Y) or knight_att(C,D,X,Y), c,d,e,f)),
        ("rook+king", lambda: safe(lambda C,D,X,Y: rook_att(C,D,X,Y) or king_att(C,D,X,Y), c,d,e,f)),
        ("bishop+queen", lambda: safe(lambda C,D,X,Y: bishop_att(C,D,X,Y) or queen_att(C,D,X,Y), c,d,e,f)),
        ("bishop+knight", lambda: safe(lambda C,D,X,Y: bishop_att(C,D,X,Y) or knight_att(C,D,X,Y), c,d,e,f)),
        ("bishop+rook", lambda: safe(lambda C,D,X,Y: bishop_att(C,D,X,Y) or rook_att(C,D,X,Y), c,d,e,f)),
        ("king+bishop", lambda: safe(lambda C,D,X,Y: king_att(C,D,X,Y) or bishop_att(C,D,X,Y), c,d,e,f)),
        ("king+queen", lambda: safe(lambda C,D,X,Y: king_att(C,D,X,Y) or queen_att(C,D,X,Y), c,d,e,f)),
        ("king+knight", lambda: safe(lambda C,D,X,Y: king_att(C,D,X,Y) or knight_att(C,D,X,Y), c,d,e,f)),
        ("king+rook", lambda: safe(lambda C,D,X,Y: king_att(C,D,X,Y) or rook_att(C,D,X,Y), c,d,e,f)),
    ]
    for name,fn in combos:
        print(name, "YES" if fn() else "NO")
if __name__=="__main__":
    main()
