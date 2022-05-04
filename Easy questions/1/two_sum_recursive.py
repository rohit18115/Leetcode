import random


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = random.sample(range(len(nums)), k=2)
        return a if (nums[a[0]] + nums[a[1]]) == target else self.twoSum(nums, target)
