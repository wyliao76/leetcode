import pytest
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ListNodeBuilder:
    def __init__(self, list: List):
        self.head = None
        self.prev = None

        for value in list:
            current = ListNode(value)
            if (self.head == None):
                self.head = current
            else:
                self.prev.next = current

            self.prev = current

    @staticmethod
    def return_list(head):
        current = head
        result = []
        while(current != None):
            result.append(current.val)
            current = current.next

        return result

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        prev = dummy
        for i in range(left - 1):
            prev = prev.next

        current = prev.next

        for i in range(right - left):
            next_node = current.next # Get the moving node
            current.next = next_node.next # link curr to next next
            next_node.next = prev.next # link moved node to prev next
            prev.next = next_node # link moved node to prev

        return dummy.next
    
    # We are moving the node after curr to right after prev node.
    # dummy -> p1 -> c2 -> 3 -> 4 -> 5
    # dummy -> p1 -> 3 -> c2 -> 4 -> 5
    # dummy -> p1 -> 4 -> 3 -> c2 -> 5

   
def test1():
    solution = Solution()
    left = 2
    right = 4
    linkedList = ListNodeBuilder([1,2,3,4,5])

    head = solution.reverseBetween(linkedList.head, left, right)

    assert linkedList.return_list(head) == [1,4,3,2,5]

def test2():
    solution = Solution()
    left = 1
    right = 1
    linkedList = ListNodeBuilder([5])

    head = solution.reverseBetween(linkedList.head, left, right)

    assert linkedList.return_list(head) == [5]

def test3():
    solution = Solution()
    left = 1
    right = 2
    linkedList = ListNodeBuilder([3, 5])

    head = solution.reverseBetween(linkedList.head, left, right)

    assert linkedList.return_list(head) == [5, 3]
