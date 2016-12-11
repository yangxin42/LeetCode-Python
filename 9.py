class Solution(object):
    # def isPalindrome(self, x):
    #     """
    #     :type x: int
    #     :rtype: bool
    #     """
    #     if x < 0 or x > (2<<30)-1:
    #         return False
    #     string_x = str(x)
    #     while len(string_x)>1:
    #         if string_x[0] == string_x[-1]:
    #             string_x = string_x[1:-1]
    #         else:
    #             break
    #     return True if len(string_x) <= 1 else False
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = 0
        temp = x
        while(temp>0):
            y *= 10
            y +=(temp%10)
            temp /=10
        return True if x == y else False
