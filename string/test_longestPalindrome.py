import pytest


class Solution:
    # time O(n^2)
    # space O(1)
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start = 0
        max_len = 1
        def helper(left: int, right: int):
            nonlocal start, max_len
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                if (right - left + 1 > max_len):
                    start = left
                    max_len = right - left + 1
                left -= 1
                right += 1

        for i in range(len(s)):
            helper(i, i) # odd
            helper(i, i + 1) # even

        return s[start:start + max_len]

# note:
# there is a Manacher’s Algorithm for O(n) time / space complexity solution
# but I think that's way to hard for me

def test1():
    solution = Solution()
    assert solution.longestPalindrome("babad") == "bab" or "aba"

def test2():
    solution = Solution()
    assert solution.longestPalindrome("cbbd") == "bb"

def test3():
    solution = Solution()
    assert solution.longestPalindrome("bb") == "bb"

def test4():
    solution = Solution()
    assert solution.longestPalindrome("abb") == "bb"
