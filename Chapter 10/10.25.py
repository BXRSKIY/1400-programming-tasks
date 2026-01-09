import random

def rook_attacks(a,b,c,d):
    return a == c or b == d

def bishop_attacks(a,b,c,d):
    return abs(a-c) == abs(b-d)

def queen_attacks(a,b,c,d):
    return rook_attacks(a,b,c,d) or bishop_attacks(a,b,c,d)

def king_attacks(a,b,c,d):
    return max(abs(a-c), abs(b-d)) == 1

def knight_attacks(a,b,c,d):
    return (abs(a-c), abs(b-d)) in [(1,2),(2,1)]

def white_pawn_can_move(a,b,c,d):
    # Белые ходят снизу вверх: b -> b+1 (обычный ход) или диагональ вперёд при взятии
    if c == a and d == b+1:
        return True
    if d == b+1 and abs(c-a) == 1:
        return True
    return False

def black_pawn_can_move(a,b,c,d):
    # Чёрные ходят сверху вниз: b -> b-1
    if c == a and d == b-1:
        return True
    if d == b-1 and abs(c-a) == 1:
        return True
    return False

def random_cell():
    return random.randint(1,8), random.randint(1,8)

def main():
    # 10.25*. Случайные поля для:
    # а) белая пешка может пойти из (a,b) в (c,d)
    while True:
        a,b = random_cell()
        c,d = random_cell()
        if white_pawn_can_move(a,b,c,d):
            print("а) белая пешка:", (a,b), "->", (c,d))
            break
    # б) черная пешка может пойти из (a,b) в (c,d)
    while True:
        a,b = random_cell()
        c,d = random_cell()
        if black_pawn_can_move(a,b,c,d):
            print("б) черная пешка:", (a,b), "->", (c,d))
            break
    # в) конь угрожает полю (c,d)
    while True:
        a,b = random_cell()
        c,d = random_cell()
        if knight_attacks(a,b,c,d):
            print("в) конь угрожает:", (a,b), "->", (c,d))
            break


if __name__ == "__main__":
    main()
