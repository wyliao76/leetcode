from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)

        # 0 coin to make up 0 amount
        dp[0] = 0
        
        for coin in coins:
            for j in range(coin, amount + 1):
                # we are looking for min number of coins to make up amount
                dp[j] = min(dp[j], dp[j - coin] + 1)
        
        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1
        

def test1():
    solution = Solution()
    # [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]
    assert solution.coinChange([1,2,5], 11) == 3

def test2():
    solution = Solution()
    assert solution.coinChange([2], 3) == -1

def test3():
    solution = Solution()
    assert solution.coinChange([1], 0) == 0
