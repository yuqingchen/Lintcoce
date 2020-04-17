import math
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def dropEggs(self, n):
        # write your code here
        m = int(math.sqrt(2 * n))
        if m * (m + 1) / 2 < n :
            m += 1 
        return m 