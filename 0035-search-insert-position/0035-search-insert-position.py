class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        def binary(arr, target, low, high):
            if low>high:
                return low #low and high cross; low is the index
            
            mid = (low+high)/2
            if target == arr[mid]:
                return mid
            
            elif target > arr[mid]:
                #target on right
                return binary(arr, target, mid+1, high)
            
            else:
                #target on left
                return binary(arr, target, low, mid-1)
        
        return binary(nums, target, 0, len(nums)-1)

#reused: https://leetcode.com/problems/binary-search/submissions/