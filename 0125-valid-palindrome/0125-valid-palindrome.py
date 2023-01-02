class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        #only alphanumberic
        w = ""
        for i in range(len(s)):
            if(s[i].isalnum()): #if alphanumeric
                w+=s[i]
        
        #make lowercase
        w = w.lower()
        
        return w == w[::-1] # check if same front and back