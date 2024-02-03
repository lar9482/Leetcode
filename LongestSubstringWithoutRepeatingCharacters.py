class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        end = 0
        seenChars = {}
        maxLength = 0
        while (end < len(s)):
            if (seenChars.get(s[end]) is not None):
                maxLength = max(maxLength, len(list(seenChars.keys())))
                seenChars = {}
                start += 1
                end = start+1
                seenChars[s[start]] = 0
                
            else:
                seenChars[s[end]] = 0 
                end += 1
        maxLength = max(maxLength, len(list(seenChars.keys())))

        return maxLength
