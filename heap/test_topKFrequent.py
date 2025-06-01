import pytest
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        return [i for i, freq in freq.most_common(k)]


def test1():
    solution = Solution()
    assert solution.topKFrequent(nums = [1,1,1,2,2,3], k = 2) == [1,2]

def test2():
    solution = Solution()
    assert solution.topKFrequent(nums = [1], k = 1) == [1]
