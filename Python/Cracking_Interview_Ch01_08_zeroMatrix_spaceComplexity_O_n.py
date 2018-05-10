## Zero Matrix

# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

def zeroMatrix(mnMatrix):
    if len(mnMatrix) == 0:
        return mnMatrix
    else:
        if len(mnMatrix[0]) == 0:
            return mnMatrix
        else:
            rowArray = [ False ] * len(mnMatrix)
            colArray = [ False ] * len(mnMatrix[0])

            # first scan to check the flag of row and col
            for i in range(len(mnMatrix)):
                for j in range(len(mnMatrix[0])):
                    if mnMatrix[i][j] == 0:
                        rowArray[i] = True
                        colArray[j] = True

            # MxN Matrix conversion loop
            for i in range(len(mnMatrix)):
                for j in range(len(mnMatrix[0])):
                    if rowArray[i] == True or colArray[j] == True:
                       mnMatrix[i][j] = 0

            print(mnMatrix)
            return mnMatrix

a1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
]

resultA = [
    [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

zeroMatrix(a1)
print(a1 == resultA)

b1 = [
    [],
    []
]

resultB = [
    [],
    []
]

zeroMatrix(b1)
print(b1 == resultB)
