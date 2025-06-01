from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # build degree
        degrees = {}
        for r1, r2 in roads:
            degrees[r1] = degrees.get(r1, 0) + 1
            degrees[r2] = degrees.get(r2, 0) + 1

        # sort desc
        degreeList = sorted(degrees.items(), key = lambda x: x[1], reverse = True)
        
        # assign importance
        importance = {}
        value = n
        for i, degree in degreeList:
            importance[i] = value
            value -= 1
        
        # sum
        total = 0
        for r1, r2 in roads:
            total += importance[r1] + importance[r2]
            
        return total


def test1():
    solution = Solution()
    assert solution.maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]) == 43

def test2():
    solution = Solution()
    assert solution.maximumImportance(5, [[0,3],[2,4],[1,3]]) == 20
