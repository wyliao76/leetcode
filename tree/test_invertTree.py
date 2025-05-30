import pytest
from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeBuilder:
    def __init__(self, values: List[int]):
        self.root: Optional[TreeNode] = None
        for value in values:
            self.insert(value)

    def insert(self, val: int):
        if not self.root:
            self.root = TreeNode(val)
            return

        curr = self.root
        while True:
            if val < curr.val:
                if curr.left is None:
                    curr.left = TreeNode(val)
                    return
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = TreeNode(val)
                    return
                curr = curr.right

    def pre_order(self, root: Optional['TreeNode'], result: List[int]) -> List[int]:
        if not root:
            return result
        
        result.append(root.val)
        self.pre_order(root.left, result)
        self.pre_order(root.right, result)

        return result
    
    def in_order(self, root: Optional['TreeNode'], result: List[int]) -> List[int]:
        if not root:
            return result

        self.in_order(root.left, result)
        result.append(root.val)
        self.in_order(root.right, result)

        return result
    
    def post_order(self, root: Optional['TreeNode'], result: List[int]) -> List[int]:
        if not root:
            return result
        
        self.post_order(root.left, result)
        self.post_order(root.right, result)
        result.append(root.val)

        return result
    
    def bfs(self, root: Optional['TreeNode'], result: List[int]) -> List[int]:
        if not root:
            return result
        
        queue = deque([root])
        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None

        tmp = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = tmp

        return root
    
def test1():
    tree = TreeBuilder([4,2,7,1,3,6,9])
    solution = Solution()
    assert tree.bfs(solution.invertTree(tree.root), []) == [4,7,2,9,6,3,1]

def test2():
    tree = TreeBuilder([2,1,3])
    solution = Solution()
    assert tree.bfs(solution.invertTree(tree.root), []) == [2, 3, 1]

def test3():
    tree = TreeBuilder([])
    solution = Solution()
    assert tree.bfs(solution.invertTree(tree.root), []) == []
