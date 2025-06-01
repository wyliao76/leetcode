from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0

        for i in range(len(nums)):
            tmp = prev1
            prev1 = max(nums[i] + prev2, prev1)
            prev2 = tmp

        return prev1
        

def test1():
    solution = Solution()
    assert solution.rob([1,2,3,1]) == 4

def test2():
    solution = Solution()
    assert solution.rob([2,7,9,3,1]) == 12

def test3():
    solution = Solution()
    assert solution.rob([1,1]) == 1
