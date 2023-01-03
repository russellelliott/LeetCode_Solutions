class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        for i in nums:
            if i in result:
                result.remove(i)
            else:
                result.append(i)
        
        return result[0]

#get frequency of each element
#hash table?
#reused: https://leetcode.com/problems/top-k-frequent-elements/