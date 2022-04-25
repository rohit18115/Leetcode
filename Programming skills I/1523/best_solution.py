class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """

        return (high - low + 1) // 2 + (high % 2 and low % 2)
