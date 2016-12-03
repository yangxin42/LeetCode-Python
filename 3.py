class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = 0;length = 0
        l = 0;r = 0
        pos = [-1 for i in range(255)]
        while r < len(s):
            if pos[ord(s[r])] == -1:
                #record the position or character
                pos[ord(s[r])] = r
                length += 1
            else:
                if length > maxLength:
                    maxLength = length
                    flag = 1
                old_l = l
                l = pos[ord(s[r])] + 1
                length = r - l + 1
                pos[ord(s[r])] = r
                #update the position
                for i in range(old_l,l):
                    if pos[ord(s[i])] < l:
                        pos[ord(s[i])] = -1
            r += 1

        if length > maxLength:
            maxLength = length
        return maxLength
