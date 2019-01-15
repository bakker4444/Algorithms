## 207. Course Schedule
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
# Example 1:
#     Input: 2, [[1,0]]
#     Output: true
#     Explanation: There are a total of 2 courses to take.
#                  To take course 1 you should have finished course 0. So it is possible.
#
# Example 2:
#     Input: 2, [[1,0],[0,1]]
#     Output: false
#     Explanation: There are a total of 2 courses to take.
#                  To take course 1 you should have finished course 0, and to take course 0 you should
#                  also have finished course 1. So it is impossible.
#
# Note:
#     1. The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
#     2. You may assume that there are no duplicate edges in the input prerequisites.
##


## reference : https://leetcode.com/problems/course-schedule/discuss/58586/Python-20-lines-DFS-solution-sharing-with-explanation
## time complexity : O(V+E)
## space complexity : O(V+E)
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.graph = [ [] for _ in range(numCourses) ]
        self.visit = [ 0 for _ in range(numCourses) ]
        for x, y in prerequisites:
            self.graph[x].append(y)
        for i in range(numCourses):
            if not self.dfs(i):
                return False
        return True

    def dfs(self, i):
        if self.visit[i] == -1:    ## node currently visiting and children need to check
            return False
        if self.visit[i] == 1:     ## node already visited and no more children need to check
            return True
        self.visit[i] = -1
        for j in self.graph[i]:
            if not self.dfs(j):
                return False
        self.visit[i] = 1
        return True


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1,0]]
    print(Solution().canFinish(numCourses, prerequisites))

    numCourses = 2
    prerequisites = [[1,0], [0,1]]
    print(Solution().canFinish(numCourses, prerequisites))
