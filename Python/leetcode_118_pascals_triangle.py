## 118. Pascal's Triangle
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#
#         1
#        1 1
#       1 2 1
#      1 3 3 1
#     1 4 6 4 1
#        ...
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
#     Input: 5
#
#     Output:
#         [
#                 [1],
#                [1,1],
#               [1,2,1],
#              [1,3,3,1],
#             [1,4,6,4,1]
#         ]
##


## my approach
class Solution1(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        if numRows == 0:
            return result
        result.append([1])
        if numRows == 1:
            return result
        result.append([1, 1])
        if numRows == 2:
            return result

        for i in range(2, numRows):
            temp_arr = [1]
            for j in range(len(result[i-1])-1):
                temp_arr.append(result[i-1][j] + result[i-1][j+1])
            temp_arr.append(1)
            result.append(temp_arr)

        return result


## map & lambda approach
## https://leetcode.com/problems/pascals-triangle/discuss/38128/Python-4-lines-short-solution-using-map.
class Solution2(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(1, numRows):
            res.append(list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])))

        return res[:numRows]


if __name__ == "__main__":
    import pprint
    pprint.pprint(Solution1().generate(5), width=20)
    pprint.pprint(Solution2().generate(5), width=20)
    pprint.pprint(Solution1().generate(10), width=40)
    pprint.pprint(Solution2().generate(10), width=40)
    pprint.pprint(Solution1().generate(15), width=80)
    pprint.pprint(Solution2().generate(15), width=80)
