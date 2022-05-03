import random


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = [
            item
            for item in itertools.combinations(range(len(nums)), 2)
            if (nums[item[0]] + nums[item[1]]) == target
        ]
        return pairs[0]
