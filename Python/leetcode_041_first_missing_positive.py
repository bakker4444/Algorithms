## 41. First Missing Positive
#
# Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1:
#     Input: [1,2,0]
#     Output: 3
#
# Example 2:
#     Input: [3,4,-1,1]
#     Output: 2
#
# Example 3:
#     Input: [7,8,9,11,12]
#     Output: 1
#
# Note:
#     Your algorithm should run in O(n) time and uses constant extra space.
##



## reference
## https://leetcode.com/problems/first-missing-positive/discuss/17080/Python-O(1)-space-O(n)-time-solution-with-explanation?page=3
## time complexity : O(n)
## space complexity : O(1)
class Solution1(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Basic idea:
        1. for any array whose length is l, the first missing positive must be in range [1,...,l+1],
            so we only have to care about those elements in this range and remove the rest.
        2. we can use the array index as the hash to restore the frequency of each number within
            the range [1,...,l+1]
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)): #delete those useless elements
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        for i in range(len(nums)): #use the index as the hash to record the frequency of each number
            nums[nums[i]%n]+=n
        for i in range(1,len(nums)):
            if nums[i]/n==0:
                return i
        return n



## reference
## https://leetcode.com/problems/first-missing-positive/discuss/17161/Python-O(n)-and-O(nlgn)-solutions.
## time complexity : O(n)
## space complexity : O(1)
class Solution2(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        for i in range(len(nums)):
            while (0 <= nums[i] < n) and (nums[nums[i]-1] != nums[i]):
                # approach 1
                temp = nums[i]-1
                nums[i], nums[temp] = nums[temp], nums[i]

                # # approach 2, be careful of switching order
                # temp = nums[nums[i]-1]
                # nums[nums[i]-1] = nums[i]
                # nums[i] = temp

        # print(nums)
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return n+1



if __name__ == "__main__":
    print(Solution1().firstMissingPositive([1,2,0]))
    print(Solution1().firstMissingPositive([3,4,-1,1]))
    print(Solution1().firstMissingPositive([7,8,9,10,11]))
    print(Solution2().firstMissingPositive([1,2,0]))
    print(Solution2().firstMissingPositive([3,4,-1,1]))
    print(Solution2().firstMissingPositive([7,8,9,10,11]))