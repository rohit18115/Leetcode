class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        A = [0] + list(accumulate(nums)) + [0]
        print(A)
        total, n = sum(nums), len(nums)
        print(total, n)
        for i in range(n):
            if A[i] == total - A[i] - nums[i]:
                return i
        return -1
