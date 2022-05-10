class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        deletes = 0
        for i in range(len(nums)):
            if val == nums[i]:
                deletes += 1
            else:
                nums[i - deletes] = nums[i]

        return len(nums) - deletes
