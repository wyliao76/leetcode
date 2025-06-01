import pytest


class Solution:
    # we want to get last bit and put it to left most bit and repeat 32 times
    # well this is 32 bit integer
    def reverseBits(self, n: int) -> int:
        result = 0
        # extra last bit and put to left most of new int
        for i in range(32):
            result = (result << 1) | (n & 1)
            # drop last bit
            n = n >> 1

        return result

def test1():
    solution = Solution()
    assert solution.reverseBits(43261596) == 964176192

def test2():
    solution = Solution()
    assert solution.reverseBits(4294967293) == 3221225471
