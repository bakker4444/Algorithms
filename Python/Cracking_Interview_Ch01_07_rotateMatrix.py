## Rotate Matrix

# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

def rotateMatrix90degClockwise(nMatrix):
    if len(nMatrix) == 0 or len(nMatrix) != len(nMatrix[0]):
        return False
    n = len(nMatrix)
    for layer in range(round(n/2)):
        first = layer
        last = n-1-layer
        for i in range(first, last):
            ## offset = i - layer
            ## 0 operation
            temp = nMatrix[layer][i]
            ## 1 operation
            nMatrix[layer][i] = nMatrix[n - 1 - i][layer]
            ## 2 operation
            nMatrix[n - 1 - i][layer] = nMatrix[n - 1 - layer][n - 1 - i]
            ## 3 operation
            nMatrix[n - 1 - layer][n - 1 - i] = nMatrix[i][n - 1 - layer]
            ## 4 operation
            nMatrix[i][n - 1 - layer] = temp
    print(nMatrix)
    return nMatrix

a1 = [[1]]

a2 = [[1,2],
      [3,4]]

a3 = [[1,2,3],
      [4,5,6],
      [7,8,9]]

a4 = [[ 1, 2, 3, 4],
      [ 5, 6, 7, 8],
      [ 9,10,11,12],
      [13,14,15,16]]

print(a1)
rotateMatrix90degClockwise(a1)
print(a2)
rotateMatrix90degClockwise(a2)
print(a3)
rotateMatrix90degClockwise(a3)
print(a4)
rotateMatrix90degClockwise(a4)


# cracking coding interview book way
# def rotateMatrix(nMatrix):
#     if len(nMatrix) == 0 or len(nMatrix) != len(nMatrix[0]):
#         return False
#     n = len(nMatrix)
#     # print(round(n/2))
#     for layer in range(round(n/2)):
#         first = layer
#         last = n - 1 - layer
#         for i in range(first, last):
#             offset = i - first
#             top = nMatrix[first][i]
#             nMatrix[first][i] = nMatrix[last-offset][first]
#             nMatrix[last-offset][first] = nMatrix[last][last-offset]
#             nMatrix[last][last-offset] = nMatrix[i][last]
#             nMatrix[i][last] = top
#     print(nMatrix)
#     return nMatrix

# b1 = [[1]]

# b2 = [[1,2],
#       [3,4]]

# b3 = [[1,2,3],
#       [4,5,6],
#       [7,8,9]]

# b4 = [[ 1, 2, 3, 4],
#       [ 5, 6, 7, 8],
#       [ 9,10,11,12],
#       [13,14,15,16]]

# rotateMatrix(b1)
# rotateMatrix(b2)
# rotateMatrix(b3)
# rotateMatrix(b4)

# print(rotateMatrix90degClockwise(a1) == rotateMatrix(b1))
# print(rotateMatrix90degClockwise(a2) == rotateMatrix(b2))
# print(rotateMatrix90degClockwise(a3) == rotateMatrix(b3))
# print(rotateMatrix90degClockwise(a4) == rotateMatrix(b4))


