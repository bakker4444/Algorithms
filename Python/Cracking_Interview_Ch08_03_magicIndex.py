## Magic Index
# A magic index in an array A [e ... n -1] is defined to be an index such that A[i] = i.
# Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
# Follow up : What if the values are not distinct?
##


## Approach 1. Brute force
# time complexity : O(N)
# space complexity : O(1)
def magicIndex1(arr):
    for i in range(len(arr)):
        if arr[i] == i:
            return i
    return False


## Approach 2. Dynamic Programming. Binary Search
# condition : distinct integers in array
# time complexity : O(logN)
# space complexity : O(logN) - call stacks(maybe!?)
def magicIndex2(arr):
    if not arr:
        return -1
    return helper2(arr, 0, len(arr)-1)

def helper2(arr, start, end):
    if end < start:
        return -1
    mid = (start + end) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return helper2(arr, start, mid-1)
    else:
        return helper2(arr, mid+1, end)


## Approach 3: Dynamic Programming. Modified binary search
# condition : what if the values are not distinct?
def magicIndex3(arr):
    if not arr:
        return -1
    return helper3(arr, 0, len(arr)-1)

def helper3(arr, start, end):
    if end < start:
        return -1
    midIdx = (start + end) // 2
    midValue = arr[midIdx]
    if midValue == midIdx:
        return midIdx
    leftIdx = min(midIdx-1, midValue)
    left = helper3(arr, start, leftIdx)
    if left >= 0:
        return left
    rightIdx = max(midIdx+1, midValue)
    right = helper3(arr, rightIdx, end)

    return right



if __name__ == "__main__":
    print(magicIndex1([-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]))
    print(magicIndex2([-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]))
    print(magicIndex3([-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]))





