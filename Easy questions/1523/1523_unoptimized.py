class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count = 0
        for i in range(low, high + 1):
            if i % 2 != 0:
                count = count + 1

        return count
