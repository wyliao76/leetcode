import pytest
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        for i in range(n + 1):
            # i >> 1 gives previous result!
            result[i] = result[i >> 1] + (i & 1)
    
        return result
    
    # def countBits(self, n: int) -> List[int]:
    #     result = [0] * (n + 1)
    #     for i in range(n + 1):
    #         k = i
    #         for j in range(32):
    #             result[k] += i & 1
    #             i = i >> 1

    #     return result

def test1():
    solution = Solution()
    assert solution.countBits(2) == [0,1,1]

def test2():
    solution = Solution()
    assert solution.countBits(5) == [0,1,1,2,1,2]
