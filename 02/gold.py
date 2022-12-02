with open("input.txt", "r") as file:
    input = file.readlines()
    score = 0
    sRock, sPaper, sScissors, sLose, sDraw, sWin = 1, 2, 3, 0, 3, 6
    pLose, pDraw, pWin, eRock, ePaper, eScissors = "X", "Y", "Z", "A", "B", "C"

    for round in input:
        moves = round[:-1].split(" ")
        if moves[0] == eRock:
            if moves[1] == pLose:
                score += sScissors + sLose
            if moves[1] == pDraw:
                score += sRock + sDraw
            if moves[1] == pWin:
                score += sPaper + sWin
        elif moves[0] == ePaper:
            if moves[1] == pLose:
                score += sLose + sRock
            if moves[1] == pDraw:
                score += sDraw + sPaper
            if moves[1] == pWin:
                score += sWin + sScissors
        elif moves[0] == eScissors:
            if moves[1] == pLose:
                score += sLose + sPaper
            if moves[1] == pDraw:
                score += sDraw + sScissors
            if moves[1] == pWin:
                score += sWin + sRock
    print(score)
