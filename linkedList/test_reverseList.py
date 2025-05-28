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

    def return_list(self, head):
        current = head
        result = []
        while(current != None):
            result.append(current.val)
            current = current.next

        return result



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while(current != None):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev


def test1():
    solution = Solution()
    linkedList = ListNodeBuilder([1,2,3,4,5])

    head = solution.reverseList(linkedList.head)

    assert linkedList.return_list(head) == [5,4,3,2,1]

def test2():
    solution = Solution()
    linkedList = ListNodeBuilder([1,2])

    head = solution.reverseList(linkedList.head)

    assert linkedList.return_list(head) == [2,1]

def test3():
    solution = Solution()
    linkedList = ListNodeBuilder([])

    head = solution.reverseList(linkedList.head)

    assert linkedList.return_list(head) == []