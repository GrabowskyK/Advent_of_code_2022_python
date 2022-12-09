count = 0
score = 0
a = 1
y = 0
oppo = ["", "", ""]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
k = 1
with open("data.txt") as file:
    for l in file:
        line = l.strip()
        oppo[k-1] = line
        if(k % 3 == 0):
            #print(oppo[k-3] + " " + oppo[k-2] + " " + oppo[k-1])
            for i in range(len(oppo[k-3])):
                for j in range(len(oppo[k-2])):
                    if(oppo[k-3][i] == oppo[k-2][j] and oppo[k-1].find(oppo[k-3][i]) != -1):
                        #print(str(a) + ". " + oppo[k-3][i] + " " + str(score))
                        score += alphabet.index(oppo[k-3][i])+1
                        y = 1
                        break
                if(y == 1):
                    y = 0
                    break
            k = 0
        k += 1
        #a += 1
print(score)





