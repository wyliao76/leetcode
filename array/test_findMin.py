from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # this is not normal because min should be in the left or mid itself
            # so if this is true, the min was rotated to the right half
            # and we only need to check right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        # eventually left == right
        return nums[left]
        

def test1():
    solution = Solution()
    assert solution.findMin([3,4,5,1,2]) == 1

def test2():
    solution = Solution()
    assert solution.findMin([4,5,6,7,0,1,2]) == 0

def test3():
    solution = Solution()
    assert solution.findMin([11,13,15,17]) == 11

def test4():
    solution = Solution()
    assert solution.findMin([2,3,4,5,1]) == 1

def test5():
    solution = Solution()
    assert solution.findMin([2,1]) == 1
