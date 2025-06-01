from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return nums[0]

        def rob_helper(nums: List[int]) -> int:
            prev1 = 0
            prev2 = 0

            for i in range(len(nums)):
                tmp = prev1
                prev1 = max(nums[i] + prev2, prev1)
                prev2 = tmp

            return prev1
        
        # rob from 0 to n - 1
        # rob from 1 to n
        # pick larger result    
        return max(
            rob_helper(nums[0: size - 1]),
            rob_helper(nums[1: size]),
        )
    

def test1():
    solution = Solution()
    assert solution.rob([2,3,2]) == 3

def test2():
    solution = Solution()
    assert solution.rob([1,2,3,1]) == 4

def test3():
    solution = Solution()
    assert solution.rob([1,2,3]) == 3

def test4():
    solution = Solution()
    assert solution.rob([2,1,1,2]) == 3
    