from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            newSets = []
            for item in result:
                newSet = item + [num]
                newSets.append(newSet)

            for newSet in newSets:
                result.append(newSet)

        return result


def test1():
    solution = Solution()
    assert solution.subsets([1,2,3]) == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

def test2():
    solution = Solution()
    assert solution.subsets([0]) == [[],[0]]
