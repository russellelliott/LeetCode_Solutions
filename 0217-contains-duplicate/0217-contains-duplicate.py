class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
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
                return True

#return true or false if a duplicate is detected
#use a hashmap for counting frequencies
#reused hashmap code from
#max number of pairs: https://leetcode.com/problems/maximum-number-of-pairs-in-array/submissions/
#top k frequent words: https://leetcode.com/problems/top-k-frequent-words/submissions/