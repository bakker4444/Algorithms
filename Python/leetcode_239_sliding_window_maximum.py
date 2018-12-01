## 239. Sliding Window Maximum
#
# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
#
# Example:
#
#     Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
#
#     Output: [3,3,5,5,6,7]
#
#     Explanation:
#
#         Window position                Max
#         --------------------------    -----
#         [1  3  -1] -3  5  3  6  7       3
#          1 [3  -1  -3] 5  3  6  7       3
#          1  3 [-1  -3  5] 3  6  7       5
#          1  3  -1 [-3  5  3] 6  7       5
#          1  3  -1  -3 [5  3  6] 7       6
#          1  3  -1  -3  5 [3  6  7]      7
#
# Note:
#     You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.
#
# Follow up:
#     Could you solve it in linear time?
##


## time complexity : O(n)
## https://www.youtube.com/watch?v=J6o_Wz-UGvc
from collections import deque
class Solution1(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dq = deque()
        result = []

        for i in range(len(nums)):
            if len(dq) != 0 and dq[0] == i - k:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result


## time complexity : O(n)
## https://leetcode.com/problems/sliding-window-maximum/discuss/111560/Python-O(n)-solution-using-deque-with-comments
from collections import deque
class Solution2:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # Checking for base case
        if not nums:
            return []
        if k == 0:
            return nums

        # Defining Deque and result list
        deq = deque()
        result = []

        # First traversing through K in the nums and only adding maximum value's index to the deque.
        # Note: We are olny storing the index and not the value.
        # Now, Comparing the new value in the nums with the last index value from deque,
        # and if new valus is less, we don't need it
        for i in range(k):
            while len(deq) != 0:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break

            deq.append(i)

        # Here we will have deque with index of maximum element for the first subsequence of length k.

        # Now we will traverse from k to the end of array and do 4 things
        # 1. Appending left most indexed value to the result
        # 2. Checking if left most is still in the range of k (so it only allows valid sub sequence)
        # 3. Checking if right most indexed element in deque is less than the new element found, if yes we will remove it
        # 4. Append i at the end of the deque  (Not: 3rd and 4th steps are similar to previous for loop)
        for i in range(k, len(nums)):
            result.append(nums[deq[0]])

            if deq[0] < i - k + 1:
                deq.popleft()

            while len(deq) != 0:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break

            deq.append(i)

        #Adding the maximum for last subsequence
        result.append(nums[deq[0]])

        return result


## time complexity : O(n)
## creative way to solve
"""
For Example: A = [2,1,3,4,6,3,8,9,10,12,56], w=4

1)  partition the array in blocks of size w=4. The last block may have less then w.
    2, 1, 3, 4 | 6, 3, 8, 9 | 10, 12, 56|

2)  Traverse the list from start to end and calculate max_so_far. Reset max after each block boundary (of w elements).
    left_max[] = 2, 2, 3, 4 | 6, 6, 8, 9 | 10, 12, 56

3)  Similarly calculate max in future by traversing from end to start.
    right_max[] = 4, 4, 4, 4 | 9, 9, 9, 9 | 56, 56, 56

4)  now, sliding max at each position i in current window, sliding-max(i) = max{right_max(i), left_max(i+w-1)}
    sliding_max = 4, 6, 6, 8, 9, 10, 12, 56
"""
class Solution3(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_left = [0] * len(nums)
        max_right = [0] * len(nums)

        for i in range(1, len(nums)):
            max_left[i] = nums[i] if i % k == 0 else max(max_left[i - 1], nums[i])

            j = len(nums) - i - 1

            if j & k == 0 :
                max_right[j] = nums[j]
            else:
                max_right[j] = max(max_right[j + 1], nums[j])

        sliding_max = [0] * (len(nums) - k + 1)
        j = 0
        for i in range(len(nums) - k + 1):
            sliding_max[j] = max(max_right[i], max_left[i + k - 1])
            j += 1

        return sliding_max




if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(Solution1().maxSlidingWindow(nums, k))
    print(Solution2().maxSlidingWindow(nums, k))
    print(Solution3().maxSlidingWindow(nums, k))