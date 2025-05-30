import pytest
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}

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
                    return False
            
            # done
            visited[course] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
    
def test1():
    solution = Solution()
    assert solution.canFinish(2, [[1,0]]) == True

def test2():
    solution = Solution()
    assert solution.canFinish(2, [[1,0],[0,1]]) == False
