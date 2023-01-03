class Solution(object):
    def factorial(n):
        for i in range(1, n+1):
            fact = fact * i
        return fact
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