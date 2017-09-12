class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        #i=1,v=5,x=10,l=50,c=100,d=500,m=1000
        re = ""
        if num > 3999 or num < 1:
            return
        if type(num) != type(1):
            return
        m = num / 1000
        while m > 0:
            re += "M"
            m -= 1
        num = num % 1000

        c = num / 100
        if c == 9:
            re += "CM"
            c = 0
        elif c >=5:
            re += "D"
            c -= 5
        elif c == 4:
            re += "CD"
            c = 0
        while c > 0:
            re += "C"
            c -= 1
        num = num % 100

        x = num / 10
        if x == 9:
            re += "XC"
            x= 0
        elif x >= 5:
            re += "L"
            x-=5
        elif x == 4:
            re += "XL"
            x = 0
        while x > 0:
            re += "X"
            x -= 1
        num = num % 10

        i = num
        if i == 9:
            re += "IX"
            i = 0
        elif i >= 5:
            re += "V"
            i -= 5
        elif i == 4:
            re += "IV"
            i = 0
        while i > 0:
            re += "I"
            i -= 1
        
        return re
s = Solution()
print s.intToRoman(1893)





