import math


class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        if (high - low + 1) % 2 == 0:
            return (high - low + 1) / 2

        else:
            if high % 2 == 0 and low % 2 == 0:
                return int(math.floor((high - low + 1) / 2))
            elif high % 2 != 0 and low % 2 != 0:
                return int(math.ceil((high - low + 1) / 2) + 1)
