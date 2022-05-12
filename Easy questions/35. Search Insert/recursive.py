class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target <= nums[0]:
                return 0
            else:
                return 1
        elif target <= nums[int(len(nums) / 2) - 1]:
            return self.searchInsert(nums[0 : int(len(nums) / 2)], target)
        else:
            return int(len(nums) / 2) + self.searchInsert(
                nums[int(len(nums) / 2) :], target
            )
