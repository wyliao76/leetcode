import pytest
from typing import List


class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = result + (n & 1)
            n = n >> 1
        return result

def test1():
    solution = Solution()
    assert solution.hammingWeight(11) == 3

def test2():
    solution = Solution()
    assert solution.hammingWeight(128) == 1

def test3():
    solution = Solution()
    assert solution.hammingWeight(2147483645) == 30
