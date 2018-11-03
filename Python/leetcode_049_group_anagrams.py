## 49. Group Anagrams
#
# Given an array of strings, group anagrams together.
#
# Example:
#
#     Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
#     Output:
#     [
#         ["ate","eat","tea"],
#         ["nat","tan"],
#         ["bat"]
#     ]
#
# Note:
#
# All inputs will be in lowercase.
# The order of your output does not matter.
##


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 0:
            return []
        if len(strs) == 1:
            return [strs]
        arr1 = []
        result = []

        for i in range(len(strs)):
            word_obj = self.analizeAnagrams(strs[i])
            if word_obj not in arr1:
                arr1.append(word_obj)
                arr2 = []
                arr2.append(strs[i])
                result.append(arr2)
            else:
                # print(arr1.index(word_obj))
                location = arr1.index(word_obj)
                result[location].append(strs[i])


        # print(result)
        return result


    def analizeAnagrams(self, str1):
        dict1 = {}
        if len(str1) == 0:
            return dict1
        for char1 in str1:
            # print(char1)
            if char1 not in dict1:
                dict1[char1] = 1
            else:
                dict1[char1] += 1
        return dict1



if __name__ == "__main__":
    arr1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(arr1))
