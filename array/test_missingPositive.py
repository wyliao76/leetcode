import pytest
from typing import List


class Solution:
    def firstMissingPositive(self, A: List) -> int:
        size = len(A)
        for i in range(size):
            while (A[i] >= 1 and A[i] <= size and A[i] != A[A[i] - 1]):
                tmp = A[A[i] - 1]
                A[A[i] - 1] = A[i]
                A[i] = tmp
        
        for i in range(size):
            if (A[i] != i + 1):
                return i + 1
        
        return size + 1
    
def test1():
    solution = Solution()
    assert solution.firstMissingPositive([1, 3, 6, 4, 1, 2]) == 5

def test2():
    solution = Solution()
    assert solution.firstMissingPositive([1, 2, 3]) == 4

def test3():
    solution = Solution()
    assert solution.firstMissingPositive([-1, -3]) == 1

def test4():
    solution = Solution()
    assert solution.firstMissingPositive([0, 100]) == 1
