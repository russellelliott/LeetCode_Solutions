class Solution(object):
    def factorial(n):
        if n==0 or n==1:
            return 1
        return n * factorial(n-1)
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        number = factorial(n)
        
        string = str(number)
        result = string.rstrip('0')
        return len(string)-len(result)

#reused: https://leetcode.com/problems/largest-number/submissions/
#rstrip for trailing zeros