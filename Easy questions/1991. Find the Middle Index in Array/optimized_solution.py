class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)  # O(n)
        index = -1

        for key, num in enumerate(nums):  # O(n)

            if left_sum == right_sum - num:
                return key
            right_sum = right_sum - num
            left_sum += num
        return index
