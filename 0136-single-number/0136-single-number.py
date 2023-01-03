class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        for i in nums:
            if i in result:
                result.remove(i) #remove if duplicate
            else:
                result.append(i) #add if doesn't exist
        
        return result[0] #return the sole unique element

#get frequency of each element
#hash table?
#reused: https://leetcode.com/problems/top-k-frequent-elements/