import pytest
from typing import List


class Solution:
    def merge_intervals(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort first
        #  this is best O(nlogn) or O(n^2)
        intervals.sort()

        results = [intervals[0]]

        for start, end in intervals[1:]:

            if results[-1][1] >= start:
                # overlapping, find max and replace
                results[-1][1] = max(results[-1][1], end)
            else:
                results.append([start, end])

        return results

def test1():
    solution = Solution()
    assert solution.merge_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]

def test2():
    solution = Solution()
    assert solution.merge_intervals([[1,4],[4,5]]) == [[1,5]]

def test3():
    solution = Solution()
    assert solution.merge_intervals([[5,6],[1,3],[2,4]]) == [[1,4],[5,6]]
