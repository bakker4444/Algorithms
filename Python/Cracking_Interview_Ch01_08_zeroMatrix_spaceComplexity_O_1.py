## Zero Matrix

# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

def zeroMatrix(mnMatrix):

    ## Approach
    # Using first row and first column as indicators for those line has zero

    # check first line of row and column
    # will nullify later

    if len(mnMatrix) == 0:
            return mnMatrix
    else:
        if len(mnMatrix[0]) == 0:
            return mnMatrix
        else:
            m = len(mnMatrix)
            n = len(mnMatrix[0])

            firstRowHasZero = False
            firstColHasZero = False

            # first column check
            for i in range(m):
                if mnMatrix[i][0] == 0:
                    firstColHasZero = True

            # first row check
            for j in range(n):
                if mnMatrix[0][j] == 0:
                    firstRowHasZero = True

            # Scan through array and record at first row and first col
            for i in range(1, m):
                for j in range(1, n):
                    if mnMatrix[i][j] == 0:
                        mnMatrix[i][0] = 0
                        mnMatrix[0][j] = 0

            # nullify row using first col
            for i in range(m):
                if mnMatrix[i][0] == 0:
                    mnMatrix[i] = [ 0 ] * n

            # nullify col using first row
            for j in range(n):
                if mnMatrix[0][j] == 0:
                    for i in range(m):
                        mnMatrix[i][j] = 0

            # check first col has zero
            if firstColHasZero == True:
                for i in range(m):
                    mnMatrix[i][0] = 0

            # check first row has zero
            if firstRowHasZero == True:
                mnMatrix[0] = [ 0 ] * n

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
