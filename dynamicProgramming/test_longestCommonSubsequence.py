from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        # dp = []
        # for i in range(m + 1):
        #     dp.append([0] * (n + 1))
        
        dp = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # if current char matches, incre length
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                # backtrack if current char not match
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]
        


def test1():
    solution = Solution()
    assert solution.longestCommonSubsequence("abcde", "ace") == 3

def test2():
    solution = Solution()
    assert solution.longestCommonSubsequence("abc", "abc") == 3

def test3():
    solution = Solution()
    assert solution.longestCommonSubsequence("abc", "def") == 0

def test4():
    solution = Solution()
    assert solution.longestCommonSubsequence("abcba", "abcbcba") == 5
