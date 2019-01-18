## 315. Count of Smaller Numbers After Self
#
# You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
#
# Example:
#     Input: [5,2,6,1]
#     Output: [2,1,1,0]
#     Explanation:
#         To the right of 5 there are 2 smaller elements (2 and 1).
#         To the right of 2 there is only 1 smaller element (1).
#         To the right of 6 there is 1 smaller element (1).
#         To the right of 1 there is 0 smaller element.
##


## reference 1 : https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76584/Mergesort-solution
## reference 2 : https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76607/C++-O(nlogn)-Time-O(n)-Space-MergeSort-Solution-with-Detail-Explanation?page=1
## using mergesort, divide all the way down to length 1
## during merge stage, count smaller number from right side of array which merged to mergedArray
## time complexity : O(nlogn)
## space complexity : O(n)

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def sort(enum):
            half = int(len(enum) / 2)
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller


if __name__ == "__main__":
    nums = [5,2,6,1]
    print(Solution().countSmaller(nums))