class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        #return if first letter capital and the rest is lowercase
        def isCapital(word):
            if len(word)<=1: #if word empty or just one letter, will follow rules
                return True
            if word[0].isupper and word[1:].islower(): #first capital, rest lowercase
                return True
            return False #false otherwise
        
        if word.isupper():
            return True #true if completely uppercase
        if word.islower():
            return True #true if completely lowercase
        if isCapital(word):
            return True #true if first letter capitalized
        return False #false otherwise

'''
return true if the word is:
- completely capital
- completely noncapital
- only first letter is capital
'''
