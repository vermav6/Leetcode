class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

 
        isNegative = (x<0)
        x=abs(x)

        arr = []
        while x>0:
            onesPlace = x%10
            x = x//10
            arr.append(onesPlace)

        lenA = len(arr) 
        finalR = 0
        for i in range(len(arr)):
            power = lenA -i - 1
            finalR += arr[i] * (10**power)

        if isNegative:
            finalR = -1 * finalR

        if finalR <= pow(-2,31) or finalR >= (pow(2,31)):
            return 0;
        return finalR