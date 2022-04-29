class Solution:
    def hammingWeight(self, n: str) -> int:
        count = 0
        for i in range(32):

            if n % 2 != 0:
                count = count + 1
            n = n >> 1

        return count
