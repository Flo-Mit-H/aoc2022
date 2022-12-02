with open("input.txt", "r") as file:
    input = file.readlines()
    score = 0
    sRock, sPaper, sScissors, sLose, sDraw, sWin = 1, 2, 3, 0, 3, 6
    yRock, yPaper, yScissors, eRock, ePaper, eScissors = "X", "Y", "Z", "A", "B", "C"

    for round in input:
        moves = round[:-1].split(" ")
        if moves[0] == eRock:
            if moves[1] == yRock:
                score += sRock + sDraw
            elif moves[1] == yPaper:
                score += sPaper + sWin
            elif moves[1] == yScissors:
                score += sScissors + sLose
        elif moves[0] == ePaper:
            if moves[1] == yRock:
                score += sRock + sLose
            elif moves[1] == yPaper:
                score += sPaper + sDraw
            elif moves[1] == yScissors:
                score += sScissors + sWin
        elif moves[0] == eScissors:
            if moves[1] == yRock:
                score += sRock + sWin
            elif moves[1] == yPaper:
                score += sPaper + sLose
            elif moves[1] == yScissors:
                score += sScissors + sDraw
    print(score)
