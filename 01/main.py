with open("input.txt", "r") as file:
    input = file.readlines()
    max1, max2, max3, counter = 0, 0, 0, 0
    for line in input:
        if line != "\n":
            counter += int(line[:-1])
        else:
            if counter > max1:
                max1 = counter
            elif counter > max2:
                max2 = counter
            elif counter > max3:
                max3 = counter
            counter = 0
    print(max1 + max2 + max3)
