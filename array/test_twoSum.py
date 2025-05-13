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


@pytest.fixture(scope="function")
def test1(self):
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    assert solution.twoSum(nums, target) == [0, 1]

@pytest.fixture(scope="function")
def test2(self):
    nums = [3, 2, 4]
    target = 6
    solution = Solution()
    assert solution.twoSum(nums, target) == [1, 2]

@pytest.fixture(scope="function")
def test3(self):
    nums = [3, 3]
    target = 6
    solution = Solution()
    assert solution.twoSum(nums, target) == [0, 1]
