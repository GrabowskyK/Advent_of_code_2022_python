score = 0
k = 1
with open("data.txt") as file:
    for l in file:
        line = l.strip()
        elf = line[2]
        opponent = line[0]

        if line[0] == 'A' and line[2] == 'X': #rock v rock, draw
            score += 4
        elif line[0] == 'A' and line[2] == 'Y': #rock v paper, win
            score += 8
        elif line[0] == 'A' and line[2] == 'Z': #rock v scissors, lose
            score += 3
        elif line[0] == 'B' and line[2] == 'X': #paper v rock, lose
            score += 1
        elif line[0] == 'B' and line[2] == 'Y': #paper v paper, draw
            score += 5
        elif line[0] == 'B' and line[2] == 'Z': #paper v scissors, win
            score += 9
        elif line[0] == 'C' and line[2] == 'X': #scissors v rock, win
            score += 7
        elif line[0] == 'C' and line[2] == 'Y': #scissors v paper, lose
            score += 2
        elif line[0] == 'C' and line[2] == 'Z': #scissors v scissors, draw
            score += 6


print(score)

