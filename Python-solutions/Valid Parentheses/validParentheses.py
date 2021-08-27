class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        openMap = {'(': ')', '{' : '}', '[' :']'}
        stack = []
        
        if ((len(s) % 2) != 0):
            return False
        for eachC in s:
            if eachC in openMap:
                stack.append(eachC)
            elif (len(stack) > 0):
                last = stack[-1]
                if openMap[last] == eachC:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return (stack == [])