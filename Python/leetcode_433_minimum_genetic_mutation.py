## 433. Minimum Genetic Mutation
#
# A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".
#
# Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.
#
# For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.
#
# Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.
#
# Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.
#
# Note:
#     1. Starting point is assumed to be valid, so it might not be included in the bank.
#     2. If multiple mutations are needed, all mutations during in the sequence must be valid.
#     3. You may assume start and end string is not the same.
#
# Example 1:
#     start: "AACCGGTT"
#     end:   "AACCGGTA"
#     bank: ["AACCGGTA"]
#
#     return: 1
#
# Example 2:
#     start: "AACCGGTT"
#     end:   "AAACGGTA"
#     bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
#
#     return: 2
#
# Example 3:
#     start: "AAAAACCC"
#     end:   "AACCCCCC"
#     bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
#
#     return: 3
##


## BFS with queue approach
## time complexity : O(L*4*N), for L:length of a gene, N: numver of genes in bank
## space complexity : O(N) for bank length
from collections import deque
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bank = set(bank)
        queue = deque()
        queue.append((start, 0))

        while queue:
            gene, dist = queue.popleft()

            if gene == end:
                return dist

            for i in range(len(gene)):
                for c in "ACGT":
                    temp_gene = gene[:i] + c + gene[i+1:]

                    if temp_gene in bank:
                        bank.remove(temp_gene)
                        queue.append((temp_gene, dist+1))

        return -1



import unittest
class Test(unittest.TestCase):
    def test_minMutation(self):
        test_input = [
            ["AACCGGTT", "AACCGGTA", ["AACCGGTA"]],
            ["AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]],
            ["AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]]
        ]
        test_result = [1, 2, 3]

        for i in range(len(test_input)):
            result = Solution().minMutation(test_input[i][0], test_input[i][1], test_input[i][2])
            self.assertEqual(result, test_result[i])
            print(result)



if __name__ == "__main__":
    unittest.main()
