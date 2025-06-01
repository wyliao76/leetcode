import pytest
from typing import List
from collections import deque


class Solution:
    # remove node with no input, the 0 degree node, and then next degree
    # the order is the sorted order
    # topological sort
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        preOrder = []
        # I need sth like
        # {
        #   0: [],
        #   1: [],
        # }
        for i in range(numCourses):
            graph[i] = []

        # set every course degree to 0
        degrees = [0] * numCourses

        for course, prereq in prerequisites:
            # this is reversed because degree 0 node has no input arrow,
            # like prereq points to course
            # so the course has +1 degree
            graph[prereq].append(course)
            degrees[course] += 1

        # we need a queue to track nodes
        queue = deque()
        for i in range(numCourses):
            if degrees[i] == 0:
                queue.append(i)

        # use to check if schedule is valid or not
        taken = 0

        while queue:
            curr = queue.popleft()
            taken += 1
            # record order
            preOrder.append(curr)

            # check future courses
            for course in graph[curr]:
                # we need to decrease their degree because the prereq is done
                degrees[course] -= 1
                # add to queue if it reaches 0 degree!
                if degrees[course] == 0:
                    queue.append(course)

        # taken has to equal otherwise it's invalid schedule
        if taken == numCourses:
            return preOrder
        else:
            return []
        
    # def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     graph = {}
    #     # the postOrder is the reverse of dead ends
    #     postOrder = []

    #     # I need sth like
    #     # {
    #     #   0: [],
    #     #   1: [],
    #     # }
    #     for i in range(numCourses):
    #         graph[i] = []

    #     for course, prereq in prerequisites:
    #         graph[course].append(prereq)

    #     # three states: 0, 1, 2 = unvisited, visiting, visited
    #     visited = [0] * numCourses

    #     def dfs(course):
    #         # course collision
    #         if visited[course] == 1:
    #             return False
            
    #         # already taken
    #         if visited[course] == 2:
    #             return True
            
    #         # taking
    #         visited[course] = 1
            
    #         # check prerequisites, if False there is collision
    #         for pre in graph[course]:
    #             if not dfs(pre):
    #                 return []
            
    #         # done
    #         visited[course] = 2
    #         postOrder.append(course)
    #         return True
        
    #     for i in range(numCourses):
    #         if not dfs(i):
    #             return []
        
    #     return postOrder
    
def test1():
    solution = Solution()
    assert solution.findOrder(2, [[1,0]]) == [0,1]

def test2():
    solution = Solution()
    assert solution.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) == [0,1,2,3]

def test3():
    solution = Solution()
    assert solution.findOrder(1, []) == [0]
