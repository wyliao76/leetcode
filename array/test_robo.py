from typing import List


class Solution:
    # state
    # 0 to 4
    # origin is 0
    # set to 0 if next pos is the origin, else incre
    # if state == 3 and next pos is the origin, set to 4, else set to 3
    # if state == 4 and next move, set to 1
    def rectangle(self, moves: str) -> int:
        x = 0
        y = 0
        state = 0
        for move in moves:
            if move == '^':
                y += 1
            elif move == 'v':
                y -= 1
            elif move == '>':
                x += 1
            elif move == '<':
                x -= 1
            else:
                print("Invalid input!")

            if state == 3:
                if (x == 0 and y == 0):
                    state = 4
                else:
                    state = 3
            elif state == 4:
                state = 1
            else:
                if (x == 0 and y == 0):
                    state = 0
                else:
                    state += 1
            
        return x == 0 and y == 0 and state == 4

def test1():
    solution = Solution()
    assert solution.rectangle("^^>>vv<<") == True

def test2():
    solution = Solution()
    assert solution.rectangle("^v") == False

def test3():
    solution = Solution()
    assert solution.rectangle("^v><") == False
