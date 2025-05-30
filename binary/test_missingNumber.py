import pytest
from typing import List


class Solution:
    # # math solution
    # def missingNumber(self, nums: List[int]) -> int:
    #     size = len(nums)
    #     expected = sum(i for i in range(size + 1))
    #     actual = sum(nums)
    #     return expected - actual

    # # I like XOR since this is used in checksum
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        xor = 0
        for i in range(size):
            xor ^= i ^ nums[i]

        xor ^= size
        return xor
    
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
