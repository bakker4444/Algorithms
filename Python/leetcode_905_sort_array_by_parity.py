## 905. Sort Array By Parity
#
# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
#
# You may return any answer array that satisfies this condition.
#
# Example 1:
#
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
#
# Note:
#
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000
##


class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A or len(A) <= 1:
            return A

        lastOddIndex = 0
        temp = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:   ## even
                temp = A[i]
                A[i] = A[lastOddIndex]
                A[lastOddIndex] = temp
                lastOddIndex += 1
        return A



if __name__ == "__main__":
    arr1 = [3, 1, 2, 4]
    print(Solution().sortArrayByParity(arr1))
    arr1 = None
    print(Solution().sortArrayByParity(arr1))
    arr1 = []
    print(Solution().sortArrayByParity(arr1))
    arr1 = [33, 11, 27, 43]
    print(Solution().sortArrayByParity(arr1))
    arr1 = [33, 12, 27, 43]
    print(Solution().sortArrayByParity(arr1))
