class Solution:
    def climbStairs(self, n: int) -> int:
        # n = 1, step = 1
        # n = 2, step = 2
        # n = 3, step = 3
        # n = 4, step = 5
        # fib sequence
        # f(n) = f(n - 1) + f(n - 2)

        if n == 1:
            return 1

        n1 = 0
        n2 = 1

        for i in range(n):
            result = n1 + n2
            n1 = n2
            n2 = result

        return result

def test1():
    solution = Solution()
    assert solution.climbStairs(2) == 2

def test2():
    solution = Solution()
    assert solution.climbStairs(3) == 3
    