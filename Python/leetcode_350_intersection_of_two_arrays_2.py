## 350. Intersection of Two Arrays II
#
# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
#     Input: nums1 = [1,2,2,1], nums2 = [2,2]
#     Output: [2,2]
#
# Example 2:
#
#     Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#     Output: [4,9]
#
# Note:
#
#     Each element in the result should appear as many times as it shows in both arrays.
#     The result can be in any order.
#
# Follow up:
#
#     What if the given array is already sorted? How would you optimize your algorithm?
#     What if nums1's size is small compared to nums2's size? Which algorithm is better?
#     What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
##


import collections


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ## approach 2: one dict and one original arr
        if not len(nums1) or not len(nums2):
            return []

        result1 = []

        dict1 = collections.Counter(nums1)
        for num in nums2:
            if num in dict1 and dict1[num] > 0:
                result1.append(num)
                dict1[num] -= 1
        return result1

        ## approach 1: two dicts and compare key
        # if not len(nums1) or not len(nums2):
        #     return []
        # dict1 = collections.Counter(nums1)
        # dict2 = collections.Counter(nums2)
        # result1 = []
        # for key in dict1:
        #     if key in dict2:
        #         repeatNum = min(dict1[key], dict2[key])
        #         for i in range(repeatNum):
        #             result1.append(key)
        # return result1


if __name__ == "__main__":
    arr1 = [1, 2, 2, 1]
    arr2 = [2, 2]
    print(Solution().intersect(arr1, arr2))
    arr1 = [4, 9, 5]
    arr2 = [9, 4, 9, 8, 4]
    print(Solution().intersect(arr1, arr2))
