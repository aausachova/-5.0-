board = list()
for i in range(8):
    board.append(list(input()))
for rw in range(8):
    for cl in range(8):
        if board[rw][cl] == "R":  # горизонталь/вертикаль
            for cli in range(cl - 1, -1, -1):
                if board[rw][cli] not in ["R", "B"]:
                    board[rw][cli] = "r"
                else:
                    break
            for cli in range(cl + 1, 8, 1):
                if board[rw][cli] not in ["R", "B"]:
                    board[rw][cli] = "r"
                else:
                    break
            for rwi in range(rw - 1, -1, -1):
                if board[rwi][cl] not in ["R", "B"]:
                    board[rwi][cl] = "r"
                else:
                    break
            for rwi in range(rw + 1, 8, 1):
                if board[rwi][cl] not in ["R", "B"]:
                    board[rwi][cl] = "r"
                else:
                    break
        if board[rw][cl] == "B":  # диагонали
            rwi = rw - 1
            cli = cl - 1
            while rwi>=0 and cli>=0:
                if board[rwi][cli] not in ["R", "B"]:
                    board[rwi][cli] = "b"
                    rwi-=1
                    cli-=1
                else:
                    break
            rwi = rw + 1
            cli = cl - 1
            while rwi<=7 and cli>=0:
                if board[rwi][cli] not in ["R", "B"]:
                    board[rwi][cli] = "b"
                    rwi+=1
                    cli-=1
                else:
                    break
            rwi = rw + 1
            cli = cl + 1
            while rwi<=7 and cli<=7:
                if board[rwi][cli] not in ["R", "B"]:
                    board[rwi][cli] = "b"
                    rwi+=1
                    cli+=1
                else:
                    break
            rwi = rw - 1
            cli = cl + 1
            while rwi>=0 and cli<=7:
                if board[rwi][cli] not in ["R", "B"]:
                    board[rwi][cli] = "b"
                    rwi-=1
                    cli+=1
                else:
                    break
safe=0
for i in range(8):
    safe+= board[i].count('*')
print(safe)
