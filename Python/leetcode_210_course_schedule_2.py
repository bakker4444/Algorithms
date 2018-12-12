## 210. Course Schedule II
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
#
# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
#
# Example 1:
#
#     Input: 2, [[1,0]]
#     Output: [0,1]
#     Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
#                 course 0. So the correct course order is [0,1] .
#
# Example 2:
#
#     Input: 4, [[1,0],[2,0],[3,1],[3,2]]
#     Output: [0,1,2,3] or [0,2,1,3]
#     Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
#                 courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
#                 So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
#
# Note:
#
# 1. The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
#     https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs
#
# 2. You may assume that there are no duplicate edges in the input prerequisites.
##


## Topological sort with DFS
## reference
## https://leetcode.com/problems/course-schedule-ii/discuss/59455/Fast-python-DFS-solution-with-inline-explanation
from collections import defaultdict
class Solution1(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # use DFS to parse the course structure
        self.graph = defaultdict(list) # a graph for all courses
        self.res = [] # start from empty
        for pair in prerequisites:
            self.graph[pair[0]].append(pair[1])
        self.visited = [0 for x in range(numCourses)] # DAG detection
        for x in range(numCourses):
            if not self.DFS(x):
                return []
             # continue to search the whole graph
        return self.res

    def DFS(self, node):
        if self.visited[node] == -1: # cycle detected
            return False
        if self.visited[node] == 1:
            return True # has been finished, and been added to self.res
        self.visited[node] = -1 # mark as visited
        for x in self.graph[node]:
            if not self.DFS(x):
                return False
        self.visited[node] = 1 # mark as finished
        self.res.append(node) # add to solution as the course depenedent on previous ones
        return True


## another approach : BFS
## https://leetcode.com/problems/course-schedule-ii/discuss/59321/Python-dfs-bfs-solutions-with-comments.
from collections import deque
class Solution2(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        dic = {i: set() for i in range(numCourses)}
        neigh = defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        # queue stores the courses which have no prerequisites
        queue = deque([i for i in dic if not dic[i]])
        count, res = 0, []
        while queue:
            node = queue.popleft()
            res.append(node)
            count += 1
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    queue.append(i)
        return res if count == numCourses else []


## another approach : BFS
## https://leetcode.com/problems/course-schedule-ii/discuss/59321/Python-dfs-bfs-solutions-with-comments.
class Solution3(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        dic = defaultdict(set)
        neigh = defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        stack = [i for i in range(numCourses) if not dic[i]]
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    stack.append(i)
            dic.pop(node)
        return res if not dic else []


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1,0]]
    print(Solution1().findOrder(numCourses, prerequisites))
    print(Solution2().findOrder(numCourses, prerequisites))
    print(Solution3().findOrder(numCourses, prerequisites))

    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(Solution1().findOrder(numCourses, prerequisites))
    print(Solution2().findOrder(numCourses, prerequisites))
    print(Solution3().findOrder(numCourses, prerequisites))
