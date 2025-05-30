import pytest
from typing import List


class Solution:
    # a ^ b gives sum. 0001 ^ 0010 = 0011
    # a & b << 1 gives carry. 0010 & 0010 = 0010, << 1 = 0100
    # this is pretty bad in Python the manual masking is too much
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) & MASK
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK
        
        return a if a <= MAX_INT else ~(a ^ MASK)

def test1():
    solution = Solution()
    assert solution.getSum(1, 2) == 3

def test2():
    solution = Solution()
    assert solution.getSum(2, 3) == 5

def test3():
    solution = Solution()
    assert solution.getSum(-1, 1) == 0