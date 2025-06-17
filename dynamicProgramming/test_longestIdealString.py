from typing import List


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # 26 alphabets
        dp = [0] * 26

        for c in s:
            index = ord(c) - ord("a")
            best = 0
            for j in range(max(0, index - k), min(25, index + k) + 1):
                best = max(best, dp[j])
            dp[index] = best + 1

        return max(dp)


def test1():
    solution = Solution()
    [1, 3, 2, 4, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert solution.longestIdealString("acfgbd", 2) == 4

def test2():
    solution = Solution()
    assert solution.longestIdealString("abcd", 3) == 4
