class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        def makeDict(word):
            #split word into chars
            letters = word.split()
            #initalize empty dictionary
            freq = {}

            #iterate through the list of numbers
            for i in word:
                if i in freq:
                    freq[i] = freq[i]+1
                else:
                    freq[i] = 1
            
            return freq

        #make a dictionary for each of the characters of word1 and word2
        #compare frequencies of each
        dict1 = makeDict(word1) #frequencies in word1
        dict2 = makeDict(word2) #frequencies in word2
        allLetters = makeDict(word1+word2) #all letters across all words
        
        def getFrequency(dictionary, word):
            #print(word)
            if word in dictionary: #if it exits
                return dictionary[word]
            return 0
        for letter in allLetters:
            freq1 = getFrequency(dict1, letter)
            freq2 = getFrequency(dict2, letter)
            #print(letter, freq1, freq2)
            if abs(freq1-freq2) >3:
                return False
        
        #false never invoked, return true
        return True

#reused: https://leetcode.com/problems/top-k-frequent-elements/submissions/