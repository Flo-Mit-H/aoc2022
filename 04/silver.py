import re

with open("input.txt", "r") as file:
    input = file.readlines()
    sum = 0

    for pair in input:
        pair = pair.replace("\n", "")
        p1low, p1high, p2low, p2high = [int(x) for x in re.split("[-,]", pair)]

        if (p1low <= p2low and p1high >= p2high) or (p2low <= p1low and p2high >= p1high):
            sum += 1
    print(sum)