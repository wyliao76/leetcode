from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.result = 0
        def backtracking(index, string):
            if len(set(string)) < len(string):
                return
            
            # else update max
            self.result = max(self.result, len(string))

            # here we concat and move to next
            for i in range(index, len(arr)):
                backtracking(i + 1, string + arr[i])

        backtracking(0, "")

        return self.result


def test1():
    solution = Solution()
    assert solution.maxLength(["un","iq","ue"]) == 4

def test2():
    solution = Solution()
    assert solution.maxLength(["cha","r","act","ers"]) == 6

def test3():
    solution = Solution()
    assert solution.maxLength(["abcdefghijklmnopqrstuvwxyz"]) == 26

def test4():
    solution = Solution()
    assert solution.maxLength(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]) == 16