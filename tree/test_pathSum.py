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
            current = queue.pop(0)

            # left first
            if i < len(values):
                if values[i] is not None:
                    current.left = TreeNode(values[i])
                    queue.append(current.left)
                i += 1

            # right after
            if i < len(values):
                if values[i] is not None:
                    current.right = TreeNode(values[i])
                    queue.append(current.right)
                i += 1

        return root

class Solution:
    # def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    #     if not root:
    #         return False

    #     if not root.left and not root.right and root.val == targetSum:
    #         return True
        
    #     left = self.hasPathSum(root.left, targetSum - root.val)
    #     right = self.hasPathSum(root.right, targetSum - root.val)

    #     return left or right

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        queue = [[root, targetSum]]

        while queue:
            item = queue.pop(0)
            node = item[0]
            target = item[1]

            if not node.left and not node.right and target - node.val == 0:
                return True

            if node.left:
                queue.append([node.left, target - node.val])
            
            if node.right:
                queue.append([node.right, target - node.val])

        return False

    
def test1():
    tree = TreeBuilder([5,4,8,11,None,13,4,7,2,None,None,None,1])
    solution = Solution()
    assert solution.hasPathSum(tree.root, 22) == True

def test2():
    tree = TreeBuilder([1,2,3])
    solution = Solution()
    assert solution.hasPathSum(tree.root, 5) == False

def test3():
    tree = TreeBuilder([])
    solution = Solution()
    assert solution.hasPathSum(tree.root, 0) == False
