class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        gauss = (len(nums) * (len(nums)+1))/2
        listSum = sum(nums)
        return gauss-listSum
        

#range 0 to num
#find sum of them, subtract by sum of array to get missing one
#gauss sum: https://dev.to/alisabaj/the-gauss-sum-and-solving-for-the-missing-number-996