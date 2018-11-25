## 4. Median of Two Sorted Arrays
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#
#     nums1 = [1, 3]
#     nums2 = [2]
#
#     The median is 2.0
#
# Example 2:
#
#     nums1 = [1, 2]
#     nums2 = [3, 4]
#
#     The median is (2 + 3)/2 = 2.5
##


## approach : merge two arrays
## time complexity : O(m+n)
## space complexity : O(m+n)
## can improve mergeArr part.
class Solution1(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        if not len(nums1):
            if not len(nums2):
                return 0
            else:
                # print(nums2)
                if len(nums2) % 2:
                    return nums2[len(nums2)//2]
                return (nums2[0] + nums2[len(nums2)-1]) / 2.0
        else:
            if not len(nums2):
                # print(nums2)
                if len(nums1) % 2:
                    return nums1[len(nums1)//2]
                return (nums1[0] + nums1[len(nums1)-1]) / 2.0
            else:
                result_arr = self.mergeArr(nums1, nums2)
                if len(result_arr) % 2:
                    return result_arr[len(result_arr)//2]
                return (result_arr[len(result_arr)//2] + result_arr[len(result_arr)//2-1]) / 2.0


    def mergeArr(self, nums1, nums2):
        if not len(nums1):
            return nums2
        if not len(nums2):
            return nums1

        i, j = 0, 0
        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                result.append(nums2[j])
                j += 1
            else:
                result.append(nums1[i])
                result.append(nums2[j])
                i += 1
                j += 1

        if i == len(nums1) and j < len(nums2):
            result += nums2[j:]
        elif i < len(nums1) and j == len(nums2):
            result += nums1[i:]
        # print(result)
        return result


## approach 2 : Binary Search
## time complexity : O(log(m+n))
## Space complexity : O(1)
## https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn))-solution-with-explanation
## https://youtu.be/LPFhl65R7ww
from math import inf
class Solution2(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        x = len(nums1)
        y = len(nums2)

        if y == 0:
            raise ValueError

        # print("Length :", x, y)

        low = 0
        high = x

        while low <= high:
            partitionX = (low + high)//2
            partitionY = (x + y + 1)//2 - partitionX

            # print("partition :", partitionX, partitionY)

            maxLeftX = -inf if partitionX == 0 else nums1[partitionX-1]
            minRightX = inf if partitionX == x else nums1[partitionX]

            maxLeftY = -inf if partitionY == 0 else nums2[partitionY-1]
            minRightY = inf if partitionY == y else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1

        return Exception


## same approach as Solution2
## leetcode solution
## time complexity : O(log(m+n))
## time complexity : O(1)
## https://leetcode.com/problems/median-of-two-sorted-arrays/solution/?page=3
class Solution3(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)

        ## len(nums1) < len(nums2)
        if m > n:
            nums1, nums2, m, n \
            = nums2, nums1, n, m

        ## both array cannot be empty
        ## which means larger array cannot empty
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2

        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j-1] > nums1[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0



if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]
    print("Problem 1")
    print(Solution1().findMedianSortedArrays(nums1, nums2))
    print(Solution2().findMedianSortedArrays(nums1, nums2))
    print(Solution3().findMedianSortedArrays(nums1, nums2))

    nums1 = [1, 2]
    nums2 = [3, 4]
    print("Problem 2")
    print(Solution1().findMedianSortedArrays(nums1, nums2))
    print(Solution2().findMedianSortedArrays(nums1, nums2))
    print(Solution3().findMedianSortedArrays(nums1, nums2))

    nums1 = []
    nums2 = [2,3]
    print("Problem 3")
    print(Solution1().findMedianSortedArrays(nums1, nums2))
    print(Solution2().findMedianSortedArrays(nums1, nums2))
    print(Solution3().findMedianSortedArrays(nums1, nums2))

    nums1 = [4,5,6,8,9]
    nums2 = []
    print("Problem 4")
    print(Solution1().findMedianSortedArrays(nums1, nums2))
    print(Solution2().findMedianSortedArrays(nums1, nums2))
    print(Solution3().findMedianSortedArrays(nums1, nums2))
