## 347. Top K Frequent Elements
#
# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#     Input: nums = [1,1,1,2,2,3], k = 2
#     Output: [1,2]
#
# Example 2:
#     Input: nums = [1], k = 1
#     Output: [1]
#
# Note:
#     - You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
#     - Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
##


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hm = {}
        freq = {}
        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1

        for key, value in hm.items():
            if value not in freq:
                freq[value] = [key]
            else:
                freq[value].append(key)

        result = []

        for i in range(len(nums), 0, -1):
            if i in freq:
                for val in freq[i]:
                    result.append(val)

        return result[:2]


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    print(Solution().topKFrequent(nums, 2))
    nums = [1]
    print(Solution().topKFrequent(nums, 1))