class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #first, get the length of the array
        length = len(nums)
        #make an array
        nums2 = []
        #for loop from 1 to lenth
        for i in range(length):
            #get subarray from 0 to 1
            current = nums[0:i+1]
            #get the sum of that array
            #nums2[i] = sum(current)
            nums2.append(sum(current))
        return nums2

#What is a "running sum?"
#[1, 2, 3, 4] -> [1, 1+2, 1+2+3, 1+2+3+4]
#get the subarray and add all those numbers together for that index

#first issue; first number is 0, but the other numbers sum as intended.
#arr[0:0] = nothing
#arr[0:1] = something