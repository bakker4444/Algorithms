## 08.02 Robot in a Grid
#
# Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
# The robot can only move in two directions, right and down, but certain cells are "off limits" such that
# the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
# the bottom right.
##


## depth for search from end point to origin
## time complexity : O(M*N)
## space complexity : O(max(M, N))
def getPath(arr):
    if not arr or not len(arr):
        return False

    path = list()
    failPoint = set()

    if findPath(arr, len(arr)-1, len(arr[0])-1, path, failPoint):
        return path
    return False


def findPath(arr, row, col, path, failPoint):
    if col < 0 or row < 0 or arr[row][col] == "#":
        return False

    if (row, col) in failPoint:
        return False

    if not row and not col or\
        findPath(arr, row, col-1, path, failPoint) or \
        findPath(arr, row-1, col, path, failPoint):
            path.append((row, col))
            return True
    failPoint.add((row, col))
    return False


if __name__ == "__main__":
    maze = [
        [" "," "," "," "," "," "," "," "," "," "],
        [" ","#","#","#","#"," ","#","#","#","#"],
        [" ","#"," "," ","#"," ","#"," "," ","#"],
        [" "," "," "," "," "," "," "," "," "," "],
        ["#"," ","#","#"," ","#"," ","#","#"," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" ","#"," ","#"," "," ","#"," ","#"," "],
        [" ","#"," "," "," "," ","#"," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "],
        ["#"," "," ","#"," ","#"," "," ","#"," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" ","#","#","#"," "," ","#"," ","#"," "],
        [" ","#"," "," "," "," ","#"," "," "," "],
        [" "," "," "," "," "," "," ","#"," "," "],
        ["#"," "," ","#","#","#"," "," ","#"," "],
        [" "," "," "," "," "," "," "," "," "," "],
        [" ","#"," ","#"," "," ","#"," ","#"," "],
        [" ","#"," "," ","#"," ","#"," "," ","#"],
        [" "," "," "," "," "," "," ","#"," "," "],
        ["#"," ","#","#"," ","#"," ","#","#"," "],
    ]
    print(getPath(maze))
