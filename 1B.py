# B. Футбольный комментатор
g1, g2 = map(int, input().split(':'))
g1_2, g2_2 = map(int, input().split(':'))
l = int(input())
 
def ball_counter(g1, g2, g1_2, g2_2, l):
    x1 = g1 + g1_2 # общее кол-во мячей команды 1
    x2 = g2 + g2_2 # общее кол-во мячей команды 2
 
    if g1 > g2:
        if l == 1:
            if x1 > x2 and g1_2 > g2_2:
                return 0
            if g1 == g2_2 and g2 == g1_2:
                return 1
            elif g1 == g2_2:
                return abs(g2 - g1_2 + 1)
            elif g1 > g2_2:
                return abs(x2 - x1 + 1)
            else: 
                return max(x2 - x1, 0)
        elif l == 2:
            if g2_2 == g1_2 and x1 == x2 or g1 >= x2:
                return 0
            elif g1 == g2_2 and g2 == g1_2:
                return 1
            elif g1 == g2_2:
                return abs(g2 - g1_2) + 1
            elif g1 > g2_2 and x1 == x2:
                return 0
            elif g1 > g2_2:
                return abs(x2 - x1)
            else:
                return max(g2_2 - g1_2, 0)
    elif g1 == g2:
        if g1 == g2 == g1_2 == g2_2:
            return 1
        elif l == 1:
            if g2_2 > g1_2 and g1 >= g1_2 and x1 == x2:
                return max(g2_2 - g1_2 + 1, 0)
            elif g2_2 > g1_2 and g1 < g1_2:
                return max(g2_2 - g1_2 + 1, 0)
            elif g2_2 == g1_2 and g1 >= g1_2:
                return max(g2_2 - g1_2 + 1, 0)
            elif g2_2 == g1_2 and g1 < g1_2:
                return 0
            else: 
                return max(g2_2 - g1_2, 0)
        elif l == 2:
            if g2_2 == g1_2:
                return max(g2_2 - g1_2, 0)
            else: 
                return max(g2_2 - g1_2 + 1, 0)
    else:
        if l == 1:
            if g2_2 == g1_2:
                return max(g2_2 - g1_2 + 1, 0)
            elif x1 == x2 and g2 == g1_2:
                return 1
            elif x1 == x2 and g2 > g1_2:
                return 1
            else:
                return max(x2 - x1, 0)
        elif l == 2:
            if x1 == x2 and g1 > g2_2: 
                return 0
            else: 
                return max(x2 - x1 + 1, 0)
 
 
if g1 > 5 or g2 > 5 or g1_2 > 5 or g2_2 > 5 or l not in [1, 2]:
    print('Error')
else:
    print(ball_counter(g1, g2, g1_2, g2_2, l))
