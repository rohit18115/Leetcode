class Solution:
    # @param A, a list of integers
    # @return an integer
    # 6:57
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            print("cursum", curSum)
            maxSum = max(maxSum, curSum)
            print("maxsum", maxSum)

        return maxSum
