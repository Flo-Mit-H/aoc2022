input = open("input.txt", "r").read()

for i in range(len(input)):
    letters = []
    for j in range(0, 14):
        letters.append(input[i + j])
    letter_set = set(letters)
    print(letters, letter_set)
    if len(letters) == len(letter_set):
        print(i + 14)
        break
