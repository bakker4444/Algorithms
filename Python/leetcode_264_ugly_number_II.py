## 264. Ugly Number II
#
# Write a program to find the n-th ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
#
# Example:
#     Input: n = 10
#     Output: 12
#     Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
#
# Note:  
#     1) 1 is typically treated as an ugly number.
#     2) n does not exceed 1690.
##



## three pointer approach
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0 or n > 1690:
            return False

        result = [1]
        cnt = 1

        p1, p2, p3 = 0, 0, 0

        while cnt < n:
            next_num = min(result[p1]*2, result[p2]*3, result[p3]*5)
            if next_num == result[p1]*2:
                p1 += 1
            if next_num == result[p2]*3:
                p2 += 1
            if next_num == result[p3]*5:
                p3 += 1
            
            result.append(next_num)
            cnt += 1
        
        return result[cnt-1]



import unittest

class Test(unittest.TestCase):
    def test_nthUglyNumber(self):
        test_input = [10, 3, 5, 7]
        test_output = [12, 3, 5, 8]
        sol = Solution()

        for i in range(len(test_input)):
            result = sol.nthUglyNumber(test_input[i])
            self.assertEqual(result, test_output[i])



if __name__ == "__main__":
    unittest.main()
        

