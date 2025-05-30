from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            
            # corner case the left mid right are the same we need to skip
            # we can discard this value because it's NOT the target
            # so we shrink left right pointers
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue

            # check if left part is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # right part is sorted
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False


def test1():
    solution = Solution()
    assert solution.search([2,5,6,0,0,1,2], 0) == True

def test2():
    solution = Solution()
    assert solution.search([2,5,6,0,0,1,2], 3) == False

def test3():
    solution = Solution()
    assert solution.search([1,0,1,1,1], 0) == True
