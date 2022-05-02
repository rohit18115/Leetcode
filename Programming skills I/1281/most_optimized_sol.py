from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = [int(x) for x in str(n)]
        return reduce((lambda x, y: x * y), a) - reduce((lambda x, y: x + y), a)
