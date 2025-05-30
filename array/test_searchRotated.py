from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # left is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False


def test1():
    solution = Solution()
    assert solution.search([4,5,6,7,0,1,2], 0) == 4

def test2():
    solution = Solution()
    assert solution.search([4,5,6,7,0,1,2], 3) == -1

def test3():
    solution = Solution()
    assert solution.search([1], 0) == -1

def test4():
    solution = Solution()
    assert solution.search([3, 1], 1) == 1
