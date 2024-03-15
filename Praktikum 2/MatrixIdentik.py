n = input().split()
nb = int(n[0])
nk = int(n[1])
matrix1 = [list(map(int, input().split())) for _ in range(nb)]

n = input().split()
nb = int(n[0])
nk = int(n[1])
matrix2 = [list(map(int, input().split())) for _ in range(nb)]

def isIdentik(matrix1, matrix2):
    return matrix1 == matrix2

def isRefleksionalHorizontal(matrix1, matrix2):
    return matrix1 == matrix2[::-1]

def isRefleksionalVertikal(matrix1, matrix2):
    return all(row1 == row2[::-1] for row1, row2 in zip(matrix1, matrix2))

def matrix(matrix1, matrix2):
    if isIdentik(matrix1, matrix2):
        return "identik"
    elif isRefleksionalHorizontal(matrix1, matrix2):
        return "horizontal"
    elif isRefleksionalVertikal(matrix1, matrix2):
        return "vertikal"
    else:
        return "tidak identik"

result = matrix(matrix1, matrix2)
print(result)
