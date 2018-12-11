## 38. Count and Say
#
# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
#     1.     1
#     2.     11
#     3.     21
#     4.     1211
#     5.     111221
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
#
# Note: Each term of the sequence of integers will be represented as a string.
#
# Example 1:
#
#     Input: 1
#     Output: "1"
#
# Example 2:
#
#     Input: 4
#     Output: "1211"
##


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"
        while (n > 1):
            result = self.helper(result)
            n -= 1
        return result

    def helper(self, str1):
        new_str, letter, count = "", str1[0], 0
        for i in range(len(str1)):
            if str1[i] == letter:
                count += 1
            else:
                new_str += str(count) + letter
                letter = str1[i]
                count = 1
        return new_str + str(count) + letter


if __name__ == "__main__":
    for i in range(1, 11):
        print(i, ":",Solution().countAndSay(i));
