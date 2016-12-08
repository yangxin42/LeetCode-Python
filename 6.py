class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        re = ""
        if numRows == 1 :
            return s
        for row in range(numRows):
            index = row
            flag = 0
            while index < len(s):
                re += s[index]
                if row == numRows -1 or row == 0:
                    index += 2*numRows - 2
                else:
                    if flag % 2 == 0:
                        index += 2*(numRows - 1 - row) 
                    else:
                        index += 2*row
                    flag += 1
        return re
