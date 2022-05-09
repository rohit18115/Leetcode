import functools


class Solution:
    def removeDuplicates(self, nums):
        p_el = nums[0]
        for i in nums[1:]:
            if p_el == i:
                nums.remove(p_el)
            p_el = i

        return len(nums)
