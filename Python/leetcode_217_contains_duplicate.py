## 217. Contains Duplicate
#
# Given an array of integers, find if the array contains any duplicates.
#
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
#
# Example 1:
#
#     Input: [1,2,3,1]
#     Output: true
#
# Example 2:
#
#     Input: [1,2,3,4]
#     Output: false
#
# Example 3:
#
#     Input: [1,1,1,3,3,4,3,2,4,2]
#     Output: true
##


# ## approach 2: using dictionary
# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         dict1 = {}
#         for num in nums:
#             if num in dict1:
#                 return True
#             else:
#                 dict1[num] = True
#         return False


## approach 1: using python set and length
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        newSet = set(nums)
        if len(newSet) == len(nums):
            return False
        else:
            return True



if __name__ == "__main__":
    arr1 = [1, 2, 3, 1]
    print(Solution().containsDuplicate(arr1))
    arr1 = [1, 2, 3, 4]
    print(Solution().containsDuplicate(arr1))
    arr1 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(Solution().containsDuplicate(arr1))