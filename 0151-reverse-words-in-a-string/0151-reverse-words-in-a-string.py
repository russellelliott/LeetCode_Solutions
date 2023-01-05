class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #need to remove leading and trailing spaces
        
        #split the string into list of words
        wordsList = s.split(" ") #words seperated by spaces
        #reverse the list and join them together
        wordsList = wordsList[::-1] #reverse
        #remove all extra spaces for each word
        #represented as unique items
        wordsList = [i for i in wordsList if i!= ""] #remove empty elements
        
        result = " ".join(wordsList) #join
        return result