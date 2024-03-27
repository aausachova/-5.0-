num_dots = int(input())
dots = [] 
set_dots = set()
for _ in range(num_dots): 
    x, y = map(int, input().split()) 
    dots.append((x, y)) 
    set_dots.add((x, y)) 
flag1 = True 
flag2 = True 
answer_dots = None 
for i in range(num_dots - 1): 
    if flag1 == False: 
        print(0) 
        break 
    for j in range(i+1, num_dots): 
        if dots[i][0] > dots[j][0]: 
            flag2 = False 
            i, j = j, i 
        center_x = (dots[i][0] + dots[j][0]) / 2 
        center_y = (dots[i][1] + dots[j][1]) / 2 
        diff_y = abs(dots[i][1] - dots[j][1]) / 2 
        diff_x = abs(dots[i][0] - dots[j][0]) / 2 
        if dots[i][1] > dots[j][1]: 
            third = (center_x + diff_y, center_y + diff_x) 
            fourth = (center_x - diff_y, center_y - diff_x) 
        else: 
            third = (center_x + diff_y, center_y - diff_x) 
            fourth = (center_x - diff_y, center_y + diff_x) 
        if flag2 == False: 
                i, j = j, i 
                flag2 = True 
        if third[0].is_integer() and third[1].is_integer() and fourth[0].is_integer() and fourth[1].is_integer(): 
            if third in set_dots and fourth in set_dots: 
                flag1 = False 
                break 
            elif third in set_dots: 
                if not answer_dots: 
                    answer_dots = [fourth] 
                elif len(answer_dots) == 2: 
                    answer_dots = [fourth] 
            elif fourth in set_dots: 
                if not answer_dots: 
                    answer_dots = [third] 
                elif len(answer_dots) == 2: 
                    answer_dots = [third] 
            elif not answer_dots: 
                answer_dots = [third, fourth] 
if flag1: 
    print(len(answer_dots)) 
    for dot in answer_dots: 
        print(int(dot[0]), int(dot[1]))
