class Solution(object):
    #rewrite n to base b
    def toBase(self, n, b):
        if n == 0:
            return '0'
        nums = []
        while n:
            n, r = divmod(n, b)
            nums.append(str(r))
        return ''.join(reversed(nums))
    
    #check if number is palindrone
    def isPalindrome(self, w):
        """
        :type x: int
        :rtype: bool
        """
        #already a string
        
        #reverse the string
        return w == w[::-1] # check if same front and back
    
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(2, (n-2)+1):
            number = self.toBase(n, i)
            if not self.isPalindrome(number):
                return False
        
        return True
        

#convert number into given base by divide that base and add the remainder as a digit
#https://stackoverflow.com/questions/34559663/convert-decimal-to-ternarybase3-in-python

#reused: https://leetcode.com/problems/palindrome-number/submissions/