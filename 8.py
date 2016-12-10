class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        old_ = ''
        while str.__len__()>0 and (ord(str[0]) < ord('0') or ord(str[0]) > ord('9')):
            old_ = str[0]
            str = str[1:]
            if old_ == '+' or old_ == '-':
                break
            elif old_ != ' ':
                return 0

        if str.__len__() == 0:
            return 0

        if (old_ == '+' or old_ =='-') and (str[0]=='+' or str[0] == '-'):
            return 0

        negative = 0
        if old_ == '-':
            negative = 1

        re = 0
        while str.__len__() > 0:
            if ord(str[0]) < ord('0') or ord(str[0]) > ord('9'):
                break
            re *= 10
            re += int(str[0])
            str = str[1:]
        if re > (2<<30) -1:
            re = (2<<30)-1
            if negative:
                return - (2<<30)
        return -re if negative else re
