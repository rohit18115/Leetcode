import math


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x = [int(a) for a in str(n)]
        return math.prod(x) - sum(x)
