class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = 0
        if x < 0:
            negative = 1
            x = -x
        re = 0
        while (x != 0):
            re *= 10
            re += (x % 10)
            x /= 10
        if re > (2<<31 - 1):
            return 0
        return -re if negative else re
