import pytest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in lookup:
                left = max(left, lookup[s[right]] + 1)
            
            lookup[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len


def test1():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3

def test2():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("bbbbb") == 1

def test3():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
