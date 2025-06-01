from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        nums.sort()

        for num in nums:
            newSets = []
            for item in result:
                newSet = item + [num]
                newSets.append(sorted(newSet))
            
            for newSet in newSets:
                if newSet not in result:
                    result.append(newSet)
        
        return result


def test1():
    solution = Solution()
    assert solution.subsetsWithDup([1,2,2]) == [[],[1],[2],[1,2],[2,2],[1,2,2]]

def test2():
    solution = Solution()
    assert solution.subsetsWithDup([0]) == [[],[0]]

def test3():
    solution = Solution()
    assert sorted(solution.subsetsWithDup([4,4,4,1,4])) == [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
