## 56. Merge Intervals
#
# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
#     Input: [[1,3],[2,6],[8,10],[15,18]]
#     Output: [[1,6],[8,10],[15,18]]
#     Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#
# Example 2:
#
#     Input: [[1,4],[4,5]]
#     Output: [[1,5]]
#     Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
##


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def nestSort(param):
    return param.start

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals

        results = []

        ## sorted based on start value
        intervals.sort(key=nestSort)

        temp_interval = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i].start <= temp_interval.end:
                temp_interval.end = max(temp_interval.end, intervals[i].end)
            else:
                results.append(temp_interval)
                temp_interval = intervals[i]
        results.append(temp_interval)
        return results


if __name__ == "__main__":
    arr1 = [[1,3],[2,6],[8,10],[15,18]]
    arr2 = []
    for arr in arr1:
        arr2.append(Interval(arr[0], arr[1]))
    result = Solution().merge(arr2)
    result = [ [interval.start, interval.end] for interval in result ]
    print(result)
