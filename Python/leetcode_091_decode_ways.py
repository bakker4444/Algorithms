## 91. Decode Ways
#
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
#     'A' -> 1
#     'B' -> 2
#     ...
#     'Z' -> 26
#
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
# Example 1:
#
#     Input: "12"
#     Output: 2
#     Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#
# Example 2:
#
#     Input: "226"
#     Output: 3
#     Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
##


## Memo
## approach : Dynamic programming
## Point: save the number of ways to input string index
#
# example
#     input : 226
#     i = 0 ==> 2   : "A" ==> number of way to decode : 1
#     i = 1 ==> 22  : "A" or "V" ==> number of way to decode : 2 = (previous result) + 1
#     i = 2 ==> 226 : "AZ" or "VF" ==> number of way to decode : 3 = (previous result) + 1
#
# if two previous number is between 1 and 26, add one more way to decode
# otherwise, same as previous way
#     example 1 : "07" ==> "G", only one way to decode because number is not between 1 to 26
#     example 2 : "78" ==> "GH", only one way to decode because number is not between 1 to 26


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "" or s == "0":
            return 0

        number_of_way_to_idx = [ 0 for i in range(len(s)+1) ]
        number_of_way_to_idx[0] = 1

        for i in range(1, len(s)+1):
            if int(s[i-1]) != 0:
                number_of_way_to_idx[i] += number_of_way_to_idx[i-1]
            if i != 1 and int(s[i-2:i]) < 27 and int(s[i-2:i]) > 9:
                number_of_way_to_idx[i] += number_of_way_to_idx[i-2]

        print(number_of_way_to_idx)

        return number_of_way_to_idx[-1]


if __name__ == "__main__":
    s = "12"
    print(Solution().numDecodings(s))

    s = "226"
    print(Solution().numDecodings(s))

    s = "2026"
    print(Solution().numDecodings(s))

    s = "0"
    print(Solution().numDecodings(s))
