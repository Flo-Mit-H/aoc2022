with open("input.txt", "r") as file:
    input = file.readlines()
    stacks = [
        ["R", "P", "C", "D", "B", "G"],
        ["H", "V", "G"],
        ["N", "S", "Q", "D", "J", "P", "M"],
        ["P", "S", "L", "G", "D", "C", "N", "M"],
        ["J", "B", "N", "C", "P", "F", "L", "S"],
        ["Q", "B", "D", "Z", "V", "G", "T", "S"],
        ["B", "Z", "M", "H", "F", "T", "Q"],
        ["C", "M", "D", "B", "F"],
        ["F", "C", "Q", "G"]
    ]

    input = input[10:]
    for step in input:
        step = step.replace("\n", "").split(" ")
        amount, stack_from, stack_to = int(step[1]), int(step[3]), int(step[5])

        objs = stacks[stack_from - 1][-amount:]
        for i in range(amount):
            stacks[stack_from - 1].pop()

        for obj in objs:
            stacks[stack_to - 1].append(obj)

    for stack in stacks:
        print(stack[-1])
