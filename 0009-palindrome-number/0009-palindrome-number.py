class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #convert to string
        w = str(x)
        
        #reverse the string
        return w == w[::-1] # check if same front and back