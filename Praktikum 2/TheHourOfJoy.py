m = int(input())
n = int(input())

labirin = []
for i in range(0, m):
    l = list(map(str, input().split()))
    labirin.append(l)
labirin

def hourJoy(m, n, labirin):
    jalur = []
    pos = [0, 0]
    for i in range(0, m):
        for j in range(0, n):
            if (labirin[i][j] == 'O'):
                if (i == pos[0]):
                    if (j == pos[1] + 1):
                        jalur = jalur + ["RIGHT"]
                        pos = [i, j]
                else:
                    if (i == pos[0] + 1):
                        if (j == pos[1]):
                            jalur = jalur + ["DOWN"]
                            pos = [i, j]       
    return jalur

print(hourJoy(m, n, labirin))