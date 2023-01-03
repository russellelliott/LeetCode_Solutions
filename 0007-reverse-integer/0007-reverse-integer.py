class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        factor = 1
        string = str(x) #turn to string
        if(string[0]=="-"):
            factor = -1
            string = string[1:]
        result = factor*int(string[::-1]) #flip string
        if result < -1* 2**31 or result > 2**31 - 1:
            result = 0 #0 if too big
        return result