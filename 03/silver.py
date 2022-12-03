with open("input.txt", "r") as file:
    input = file.readlines()
    sum = 0
    priorities = "#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for rucksack in input:
        rucksack = rucksack.replace("\n", "")
        comp1 = rucksack[int((len(rucksack)) / 2):]
        comp2 = rucksack[:int((len(rucksack))/ 2)]

        for i in comp1:
            if i in comp2:
                sum += priorities.index(i)
                break
    print(sum)