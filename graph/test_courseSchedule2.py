import pytest
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        # the postOrder is the reverse of dead ends
        postOrder = []

        # I need sth like
        # {
        #   0: [],
        #   1: [],
        # }
        for i in range(numCourses):
            graph[i] = []

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # three states: 0, 1, 2 = unvisited, visiting, visited
        visited = [0] * numCourses

        def dfs(course):
            # course collision
            if visited[course] == 1:
                return False
            
            # already taken
            if visited[course] == 2:
                return True
            
            # taking
            visited[course] = 1
            
            # check prerequisites, if False there is collision
            for pre in graph[course]:
                if not dfs(pre):
                    return []
            
            # done
            visited[course] = 2
            postOrder.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return postOrder
    
def test1():
    solution = Solution()
    assert solution.findOrder(2, [[1,0]]) == [0,1]

def test2():
    solution = Solution()
    assert solution.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) == [0,1,2,3]

def test3():
    solution = Solution()
    assert solution.findOrder(1, []) == [0]
