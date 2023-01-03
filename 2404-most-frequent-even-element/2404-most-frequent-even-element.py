class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        evens = [i for i in nums if i % 2 == 0] #only have even numbers
        if len(evens)==0:
            return -1 #no evens
        
        #initalize empty dictionary
        freq = {}
        result = []
        
        #iterate through the list of numbers
        for i in evens:
            if i in freq:
                freq[i] = freq[i]+1
            else:
                freq[i] = 1
        
        
        #get max value
        #if there is a tie, return the number that is smallest
        #maxValue = max(freq, key=freq.get)
        curr = -1
        maxVal = -1
        for i in freq:
            #print(i, freq[i])
            #1. is it more frequent?
            if freq[i]>maxVal:
                curr = i
                maxVal = freq[i]
            #2. is it smaller if same frequency?
            if freq[i] == maxVal and i < curr:
                curr = i
                
        return curr
            
#find frequency of all elements.
#reused: https://leetcode.com/problems/top-k-frequent-elements/
#only even numbers: https://stackoverflow.com/questions/57161182/how-to-remove-even-numbers-from-a-list-in-python