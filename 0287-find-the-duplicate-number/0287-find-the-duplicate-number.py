class Solution(object):
    def findDuplicate(self, nums):
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
        
        for i in freq:
            if freq[i]>=2:
                return i

#get frequency of each element
#hash table?
#reused: https://leetcode.com/problems/top-k-frequent-elements/
#reused: https://leetcode.com/problems/find-all-anagrams-in-a-string/