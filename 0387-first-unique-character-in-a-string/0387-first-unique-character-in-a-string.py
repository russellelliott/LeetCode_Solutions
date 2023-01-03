class Solution(object):
    def firstUniqChar(self, words):
        """
        :type s: str
        :rtype: int
        """
        #initalize empty dictionary
        freq = {}
        result = []
        
        #iterate through the list of numbers
        for i in words:
            if i in freq:
                freq[i] = freq[i]+1
            else:
                freq[i] = 1
        
        freq2 = {}
        for i in freq:
            if freq[i]==1:
                freq2[i] = 1
        
        freq = freq2
        #if dictionary empty, there are no unique letters; return -1
        if len(freq)==0:
            return -1
        #no need to further sort; they are in order in which tyey are found
        #dictionary now has all unique letters
        #for i in freq:
            
        #find the unique one
        '''unique = ""
        for i in words:
            if freq[i]==1:
                unique = i'''
        
        #find where it is
        small = len(words) #fa word or the smallest index in which char appears once
        for i in freq:
            index = words.index(i)
            if index<small:
                small = index
        
        return small

#find first character with a frequency of 1
#reused: https://leetcode.com/problems/sort-characters-by-frequency/submissions/