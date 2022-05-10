class Solution:
    def removeDuplicates(self, nums):
        i = 0
        while len(nums) != len(set(nums)):
            p_el = nums[i]
            for j in range(nums.count(p_el) - 1):
                nums.remove(p_el)
            i += 1

        return len(nums)
