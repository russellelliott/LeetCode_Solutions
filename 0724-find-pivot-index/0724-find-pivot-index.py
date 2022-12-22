class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        total = sum(nums)
        half = total//2
        for i in range(0, length):
            index = i+1
            left = nums[0: index-1] #arr[0:0] = nothing, #arr[0:1] = arr[0]
            leftSum = sum(left)
            #print("left subarray: ", left)
            #print("left sum: ", leftSum)
            right = nums[index+1-1:length] #skip over index
            rightSum = sum(right)
            #print("right subarray: ", right)
            #print("right sum: ", rightSum)
            
            #check if the sums match. if so, return index
            if(leftSum==rightSum):
                #return the INDEX
                return i
                '''if(i==0):
                    return 0 #edge case where the pivot is at the beginning
                #return(nums[i-1]) #return number at index i
                return i'''
            
        
        return -1

#what is finding the pivot index?
#it is an index such that the numbers on the left of it equal the numbers on the right.
#1. find sum of array
#2. find index such that everything left of it is half of the sum