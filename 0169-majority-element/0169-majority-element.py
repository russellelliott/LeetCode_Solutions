class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #initalize empty dictionary
        freq = {}
        result = []
        
        #iterate through the list of numbers
        for i in nums:
            if i in freq:
                freq[i] = freq[i]+1
            else:
                freq[i] = 1
        
        #print(freq)
        #get dictionary key with max value
        #we can assume the majority element always exists
        maxValue = max(freq, key=freq.get)
        return maxValue

#find frequency of all elements. find one that appeats more than floor(n/2) times
#reused: https://leetcode.com/problems/top-k-frequent-elements/