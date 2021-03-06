## 481. Magical String
#
# A magical string S consists of only '1' and '2' and obeys the following rules:
#
# The string S is magical because concatenating the number of contiguous occurrences of characters '1' and '2' generates the string S itself.
#
# The first few elements of string S is the following: S = "1221121221221121122……"
#
# If we group the consecutive '1's and '2's in S, it will be:
#
# 1 22 11 2 1 22 1 22 11 2 11 22 ......
#
# and the occurrences of '1's or '2's in each group are:
#
# 1 2	2 1 1 2 1 2 2 1 2 2 ......
#
# You can see that the occurrence sequence above is the S itself.
#
# Given an integer N as input, return the number of '1's in the first N number in the magical string S.
#
# Note: N will not exceed 100,000.
#
# Example 1:
#     Input: 6
#     Output: 3
#     Explanation: The first 6 elements of magical string S is "12211" and it contains three 1's, so return 3.
##


class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n <= 3:
            return 1

        head = 2
        tail = 3
        num = 1
        result = 1
        arr1 = [1, 2, 2]

        while tail < n:
            for i in range(arr1[head]):
                arr1.append(num)
                if num == 1 and tail < n:
                    result += 1
                tail += 1
            num = num ^ 3
            head += 1
        # print(arr1)
        return result


if __name__ == "__main__":
    print(Solution().magicalString(4))
    print(Solution().magicalString(14))
    print(Solution().magicalString(133))
    print(Solution().magicalString(277))
