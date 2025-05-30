import pytest
from typing import List, Optional
from heapq import heappop, heappush

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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        size = len(lists)
        if size == 1:
            return lists[0]
        if size == 0:
            return None
        
        mid = size // 2

        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
  
        def merge(left, right):
            dummy = ListNode(0)
            curr = dummy

            while left and right:
                if left.val < right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next

            if left:
                curr.next = left

            if right:
                curr.next = right

            return dummy.next

        return merge(left, right)


def test1():
    solution = Solution()
    lists = [
        ListNodeBuilder([1,4,5]).head,
        ListNodeBuilder([1,3,4]).head,
        ListNodeBuilder([2,6]).head
    ]
    head = solution.mergeKLists(lists)
    assert ListNodeBuilder.return_list(head) == [1,1,2,3,4,4,5,6]

def test2():
    solution = Solution()
    lists = []
    assert solution.mergeKLists(lists) == None

def test3():
    solution = Solution()
    lists = [[]]
    assert solution.mergeKLists(lists) == []
