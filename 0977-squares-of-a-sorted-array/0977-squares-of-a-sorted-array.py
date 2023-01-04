class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squared = [i**2 for i in nums]
        squared.sort()
        return squared