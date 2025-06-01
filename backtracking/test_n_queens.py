from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        # {row : col}
        queens = {}
        # diagonal row - col are the same 0,1 1,2 2,3 = -1
        negative_diag = set()
        # diagonal row + col are the same 0,0 1,1 2,2 = 0
        positive_diag = set()
        cols = set()

        def backtrack(row):
            if row == n:
                broad = []
                for i in range(n):
                    string = ["."] * n
                    string[queens[i]] = "Q"
                    base = ""
                    for c in string:
                        base += c
                    broad.append(base)
                
                result.append(broad)    
                return    

            # try every col
            for col in range(n):
                # skip if not allowed
                if col in cols or (row - col) in negative_diag or (row + col) in positive_diag:
                    continue

                # place queen (do a move)
                queens[row] = col
                # record
                cols.add(col)
                negative_diag.add(row - col)
                positive_diag.add(row + col)

                # backtrack to next
                backtrack(row + 1)

                # undo a move
                del queens[row]
                # undo record
                cols.remove(col)
                negative_diag.remove(row - col)
                positive_diag.remove(row + col)

        backtrack(0)

        return result


def test1():
    solution = Solution()
    assert solution.solveNQueens(4) == [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

def test2():
    solution = Solution()
    assert solution.solveNQueens(1) == [["Q"]]
