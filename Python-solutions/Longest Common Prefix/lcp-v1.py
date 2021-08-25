class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        minLength = len(strs[0])
        for eachWord in range(1, len(strs)):
            if len(strs[eachWord]) < minLength:
                minLength = len(strs[eachWord])
        
        i = 0
        fs = ""
        while i < minLength:
            firstChar = strs[0][i]
            for eachWord in range(1, len(strs)):
                if strs[eachWord][i] != firstChar:
                    return fs
            fs += firstChar
            i += 1
        return fs