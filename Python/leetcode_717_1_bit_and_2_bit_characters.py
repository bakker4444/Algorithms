## 717. 1-bit and 2-bit Characters
#
# We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).
#
# Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.
#
# Example 1:
#     Input:
#         bits = [1, 0, 0]
#     Output: True
#     Explanation:
#         The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
#
# Example 2:
#     Input:
#         bits = [1, 1, 1, 0]
#     Output: False
#     Explanation:
#         The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
#
# Note:
#     - 1 <= len(bits) <= 1000.
#     - bits[i] is always 0 or 1.
##


## My approach
class Solution1(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        idx = 0
        while idx < len(bits) - 1:
            if bits[idx] == 1:
                idx += 2
            else:
                idx += 1
        if idx == len(bits) - 1:
            return True
        return False


## reference
## https://leetcode.com/articles/1-bit-and-2-bit-characters/
## Approach #1: Increment Pointer
class Solution2(object):
    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1



if __name__ == "__main__":
    bits = [1,0,0]
    print(Solution1().isOneBitCharacter(bits))
    print(Solution2().isOneBitCharacter(bits))

    bits = [0]
    print(Solution1().isOneBitCharacter(bits))
    print(Solution2().isOneBitCharacter(bits))

    bits = [1,1,0]
    print(Solution1().isOneBitCharacter(bits))
    print(Solution2().isOneBitCharacter(bits))

    bits = [1,0]
    print(Solution1().isOneBitCharacter(bits))
    print(Solution2().isOneBitCharacter(bits))

    bits = [1,1,1,0]
    print(Solution1().isOneBitCharacter(bits))
    print(Solution2().isOneBitCharacter(bits))
