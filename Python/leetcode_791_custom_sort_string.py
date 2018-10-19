## 791. Custom Sort String
#
# S and T are strings composed of lowercase letters. In S, no letter occurs more than once.
#
# S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.
#
# Return any permutation of T (as a string) that satisfies this property.
#
# Example :
#
# Input:
#     S = "cba"
#     T = "abcd"
#
# Output: "cbad"
#
# Explanation:
# "a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
# Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.
#
# Note:
#
#     S has length at most 26, and no character is repeated in S.
#     T has length at most 200.
#     S and T consist of lowercase letters only.
##


# ## approach 2: using python standard library, count
# class Solution(object):
#     def customSortString(self, S, T):
#         """
#         :type S: str
#         :type T: str
#         :rtype: str
#         """
#         list1 = []
#         for character in S:
#             list1.append(character*T.count(character))
#         for character in T:
#             if character not in S:
#                 list1.append(character)
#         return "".join(list1)


## approach 1: my approach
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        if not S or not T:
            return ""

        dict1 = {}
        for character in T:
            if character not in dict1:
                dict1[character] = 1
            else:
                dict1[character] += 1

        result = ""

        for character in S:
            if character in dict1:
                while dict1[character] > 0:
                    result += character
                    dict1[character] -= 1
                del dict1[character]

        for character in dict1:
            while dict1[character] > 0:
                result += character
                dict1[character] -= 1
        return result


if __name__ == "__main__":
    S = "cba"
    T = "abcd"
    print(Solution().customSortString(S, T))
