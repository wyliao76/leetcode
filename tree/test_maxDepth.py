from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeBuilder:
    def __init__(self, values: List[Optional[int]]):
        self.root = self.build(values)

    def build(self, values: List[Optional[int]]) -> Optional[TreeNode]:
        if not values or values[0] is None:
            return None

        root = TreeNode(values[0])
        queue = [root]
        i = 1

        while queue and i < len(values):
            current = queue.pop()

            # left first
            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1

            # right after
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1

        return root

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    
def test1():
    tree = TreeBuilder([3,9,20,None,None,15,7])
    solution = Solution()
    assert solution.maxDepth(tree.root) == 3

def test2():
    tree = TreeBuilder([1,None,2])
    solution = Solution()
    assert solution.maxDepth(tree.root) == 2
