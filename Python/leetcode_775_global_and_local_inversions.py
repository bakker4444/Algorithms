## 775. Global and Local Inversions
#
# We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.
#
# The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].
#
# The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].
#
# Return true if and only if the number of global inversions is equal to the number of local inversions.
#
# Example 1:
#
#     Input: A = [1,0,2]
#     Output: true
#     Explanation: There is 1 global inversion, and 1 local inversion.
#
# Example 2:
#
#     Input: A = [1,2,0]
#     Output: false
#     Explanation: There are 2 global inversions, and 1 local inversion.
#
# Note:
#
#     A will be a permutation of [0, 1, ..., A.length - 1].
#     A will have length in range [1, 5000].
#     The time limit for this problem has been reduced.
##


class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # using index
        # if index is same as the value at the index, continue
        # if the difference between the index and the value at the index is 1, local inversion, also global inversion
        # if the difference between the index and the value at the index is more than 1, it is global inversion, not local inversion
        for i in range(len(A)):
            if abs(A[i]-i) > 1:
                return False
        return True

        ## using enumerate
        # for i, val in enumerate(A):
        #     if abs(val-i) > 1:
        #         return False
        # return True


if __name__ == "__main__":
    arr1 = [1, 0, 2]
    print(Solution().isIdealPermutation(arr1))

    arr1 = [1, 2, 0]
    print(Solution().isIdealPermutation(arr1))