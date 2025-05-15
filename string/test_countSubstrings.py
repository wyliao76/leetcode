import pytest


class Solution:
    # time O(n^2)
    # space O(1)
    def countSubstrings(self, s: str) -> int:
        count = 0
        start = 0
        max_len = 1
        def helper(left: int, right: int):
            nonlocal start, max_len, count
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                count += 1
                if (right - left + 1 > max_len):
                    start = left
                    max_len = right - left + 1
                left -= 1
                right += 1

        for i in range(len(s)):
            helper(i, i) # odd
            helper(i, i + 1) # even

        return count

def test1():
    solution = Solution()
    assert solution.countSubstrings("abc") == 3

def test2():
    solution = Solution()
    assert solution.countSubstrings("aaa") == 6

