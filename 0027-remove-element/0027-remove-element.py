class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        
        #while the number is in the array, remove it
        while val in nums:
            nums.remove(val)
            count+=1
        
        #now we have number of times "val" appeared
        print(nums)