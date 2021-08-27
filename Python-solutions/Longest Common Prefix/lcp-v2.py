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
 
        fs = ""
        for char in range(minLength):
            cMap = {}
            counter = 0
            for eachWord in strs:
                if eachWord[char] in cMap:
                    cMap[eachWord[char]] += 1
                else:
                    cMap[eachWord[char]] = 1
            for eachChar in cMap:
                if cMap[eachChar] == len(strs):
                    fs += eachChar
                    counter += 1
            if counter == 0:
                break
        return fs