count = 0
score = 0
a = 1
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

with open("data.txt") as file:
    for l in file:
        line = l.strip()
        x = len(line)/2
        lineFirst = line[:int(x)]
        lineLast = line[int(x):]
        for j in range(int(x)):
            count = 0
            for i in range(int(x)):
                if(lineFirst[j] == lineLast[i]):
                    count += 1
            if(count >= 1):
                score += alphabet.index(lineFirst[j])+1
                #print(str(a) +": Add " + str(score) + " " + str(lineFirst[j]))
                break
        #a += 1
print(score)




