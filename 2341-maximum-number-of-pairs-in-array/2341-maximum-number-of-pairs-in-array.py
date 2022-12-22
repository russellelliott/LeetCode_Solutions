class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #initalize empty dictionary
        freq = {}
        result = []
        
        size = len(nums)
        #iterate through the list of numbers
        for i in nums:
            if i in freq:
                freq[i] = freq[i]+1
            else:
                freq[i] = 1
        
        #count number of pairs
        numPairs = 0
        for i in freq.keys():
            if freq[i]>=2:
                numPairs+=1
                #remove number from list
                #round down then multiply by 2 to get number of pairs
                for j in range((freq[i]//2)*2):
                    nums.remove(i)
        
        numLeftOver = len(nums)
        numPairs = (size-numLeftOver)//2
        print(nums)
        return[numPairs, numLeftOver]
        
        

#number of pairs
#find numbers that have an even frequency
#use dictionary again
#left = number of pairs
#right = number of items left over