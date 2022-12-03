with open("input.txt", "r") as file:
    input = file.readlines()
    sum = 0
    priorities = "#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    c = 3
    for rucksack in input:
        if c < 2:
            c += 1
            continue
        c = 0
        index = input.index(rucksack)
        rucksack = rucksack.replace("\n", "")

        for i in rucksack:
            if i in input[index + 1] and i in input[index + 2]:
                sum += priorities.index(i)
                break
    print(sum)