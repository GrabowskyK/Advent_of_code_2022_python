score = 0
k = 1
with open("data.txt") as file:
    for l in file:
        line = l.strip()
        elf = line[2]
        opponent = line[0]
        # x =lose, y = draw, z = win
        if line[0] == 'A' and line[2] == 'X': #lose, rock v scissors
            score += 3
        elif line[0] == 'A' and line[2] == 'Y': #draw, rock v rock
            score += 4
        elif line[0] == 'A' and line[2] == 'Z': #win, rock v paper
            score += 8
        elif line[0] == 'B' and line[2] == 'X': #lose, paper v rock
            score += 1
        elif line[0] == 'B' and line[2] == 'Y': #draw, paper v paper
            score += 5
        elif line[0] == 'B' and line[2] == 'Z': #win, paper v scissors
            score += 9
        elif line[0] == 'C' and line[2] == 'X': #lose, scissors v paper
            score += 2
        elif line[0] == 'C' and line[2] == 'Y': #draw, scicssors v scissors
            score += 6
        elif line[0] == 'C' and line[2] == 'Z': #win, scissors v rock
            score += 7


print(score)

