score = 0
with open("data.txt") as file:
    for l in file:
        line = l.strip().split(",")
        line[0] = line[0].split("-")
        line[1] = line[1].split("-")
        if(int(line[0][0]) <= int(line[1][0]) and int(line[0][1]) >= int(line[1][1])):
            score += 1
            #print("1. " + line[0][0] + " " + line[0][1] + " " + line[1][0] + " " + line[1][1])
        elif(int(line[0][0]) >= int(line[1][0]) and int(line[0][1]) <= int(line[1][1])):
            score += 1
            #print("2. " + line[0][0] + " " + line[0][1] + " " + line[1][0] + " " + line[1][1])

print(score)





