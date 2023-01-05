class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = [index for index in range(len(nums)) if nums[index] == target]
        if indices == []:
            return([-1, -1]) #not found, return [-1, -1]
        return [min(indices), max(indices)] #find first and last positions

#find all indexes, then return the smallest and biggest
#all indexes of substring in string: https://datagy.io/python-find-index-substring/
