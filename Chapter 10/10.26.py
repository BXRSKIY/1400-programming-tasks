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

def attacks(piece, a,b, c,d):
    if piece == "ладья":
        return rook_attacks(a,b,c,d)
    if piece == "слон":
        return bishop_attacks(a,b,c,d)
    if piece == "ферзь":
        return queen_attacks(a,b,c,d)
    if piece == "конь":
        return knight_attacks(a,b,c,d)
    if piece == "король":
        return king_attacks(a,b,c,d)
    if piece == "белая пешка":
        return white_pawn_can_move(a,b,c,d)
    if piece == "черная пешка":
        return black_pawn_can_move(a,b,c,d)
    return False

def main():
    # 10.26*. Общая проверка:
    # Случайные клетки (a,b) белой фигуры, (c,d) черной, и цель (e,f).
    # Проверить, может ли белая фигура пойти на (e,f),
    # не попав под удар черной фигуры.
    white_piece = input("Белая фигура (ладья, слон, ферзь, конь, король, белая пешка): ").strip()
    black_piece = input("Черная фигура (ладья, слон, ферзь, конь, король, черная пешка): ").strip()
    a,b = random_cell()
    c,d = random_cell()
    e,f = random_cell()
    print("Белая фигура", white_piece, "на", (a,b))
    print("Черная фигура", black_piece, "на", (c,d))
    print("Цель белой:", (e,f))
    # может ли белая пойти?
    if not attacks(white_piece, a,b, e,f):
        print("Белая фигура не может пойти на это поле по правилам хода.")
        return
    # попадает ли под удар черной после хода?
    if attacks(black_piece, c,d, e,f):
        print("После хода белая фигура попадает под удар черной.")
    else:
        print("Ход возможен, белая фигура не под ударом.")


if __name__ == "__main__":
    main()
