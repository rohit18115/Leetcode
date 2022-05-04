class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = []
        for i in range(len(nums)):
            sec = target - nums[i]
            if sec in nums:
                pairs.append([nums.index(sec), i])
        pairs = [p for p in pairs if p[0] != p[1]]
        return pairs[0]
