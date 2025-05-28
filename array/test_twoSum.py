from typing import List
import pytest

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in dict:
                return [i, dict[remainder]]
            else:
                dict[num] = i
        return []


def test1():
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    assert sorted(solution.twoSum(nums, target)) == [0, 1]

def test2():
    nums = [3, 2, 4]
    target = 6
    solution = Solution()
    assert sorted(solution.twoSum(nums, target)) == [1, 2]

def test3():
    nums = [3, 3]
    target = 6
    solution = Solution()
    assert sorted(solution.twoSum(nums, target)) == [0, 1]
