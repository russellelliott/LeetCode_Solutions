class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #rotate = k
        length = len(nums)
        k = k % length
        
        
        #swap the two halves
        nums[length-k:], nums[:length-k] = nums[:length-k], nums[length-k:]
        