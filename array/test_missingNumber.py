import pytest
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            while (nums[i] >= 0 and nums[i] < size and nums[i] != nums[nums[i]]):
                tmp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = tmp
        
        for i in range(size):
            if (nums[i] != i):
                return i
        
        return size
    
def test1():
    solution = Solution()
    assert solution.missingNumber([3,0,1]) == 2

def test2():
    solution = Solution()
    assert solution.missingNumber([0,1]) == 2

def test3():
    solution = Solution()
    assert solution.missingNumber([9,6,4,2,3,5,7,0,1]) == 8

def test4():
    solution = Solution()
    assert solution.missingNumber([1]) == 0
