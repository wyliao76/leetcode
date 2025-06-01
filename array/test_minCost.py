from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        size = len(colors)

        left = 0
        total = 0

        # we need to deal with consecutive same colors
        # put them in a subset using two pointers left and right
        # only keep the local max
        # this is greedy algorithm
        while left < size:
            groupSum = neededTime[left]
            groupMax = neededTime[left]

            right = left + 1

            while right < size and colors[left] == colors[right]:
                groupSum += neededTime[right]
                groupMax = max(groupMax, neededTime[right])
                right += 1
            
            total += groupSum - groupMax

            left = right
        
        return total



def test1():
    solution = Solution()
    assert solution.minCost("abaac", [1,2,3,4,5]) == 3

def test2():
    solution = Solution()
    assert solution.minCost("abc", [1,2,3]) == 0

def test3():
    solution = Solution()
    assert solution.minCost("aabaa", [1,2,3,4,1]) == 2
