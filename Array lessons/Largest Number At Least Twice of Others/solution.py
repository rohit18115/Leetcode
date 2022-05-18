class Solution:
    def dominantIndex(self, nums):
        max1 = 0
        max2 = 0
        idxOfMax1 = 0

        for i, n in enumerate(nums):
            if n >= max1:
                max2 = max1
                max1 = n
                idxOfMax1 = i
            elif n > max2:
                max2 = n

        return idxOfMax1 if max1 >= max2 * 2 else -1
