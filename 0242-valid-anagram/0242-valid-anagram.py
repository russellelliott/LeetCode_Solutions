class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #anagram = two words with sme letters/length
        
        #check for invalid words
        if len(s)!=len(t):
            return False #not anagram, need same length
        
        #track how many times you see each letter (dicitonary)
        lookup = {}
        
        for letter in s:
            if letter not in lookup:
                lookup[letter]=1
            else:
                lookup[letter]+=1
                
        
        for letter in t:
            if letter in lookup:
                lookup[letter]-=1 #decrease by 1 so we don't have to look at it again
                if lookup[letter]==0: #already seen letter
                    del lookup[letter]
                    
                    
        if len(lookup)>=1:
            return False
        else:
            return True