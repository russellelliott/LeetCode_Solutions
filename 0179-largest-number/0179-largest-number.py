class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        #lets say we hade ["10" , "2"]
        #the result should be "210"
        #"10"+"2" = "102"
        #"2"+"10" = "210"
        #should swap to produce 210
        def shouldSwap(one, two):
            return int(one+two) > int(two+one)
        
        
        #for each number, turn to a string
        strings = [str(i) for i in nums]
        
        #sort in decreasing order
        strings.sort(reverse=True)
        #modified version of insertion sort
        #if two numbers start with the same digit, the largest number wins
        while True:
		swapped = False
		for i in range(0, len(strings) - 1):
			if shouldSwap(strings[i+1], strings[i]):
				strings[i], strings[i+1] = strings[i+1], strings[i] # Swap elements that are out of order
				swapped = True

		if not swapped:
			break
        
        #merge all items into one string, no spaces
        result = ''.join(i for i in strings)
        
        #delete leading zeros, but. make sure one is left if only zero
        result = result.lstrip('0')
        if result == "":
            result = "0"
        
        return result

#easy; sort the numbers like words
#sort list: https://www.programiz.com/python-programming/methods/list/sort
#turn to single string: https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python
#insertion sort: https://www.geeksforgeeks.org/insertion-sort/
#remove leading zeros with lstrip: https://copyassignment.com/python-remove-leading-zeros-5-easy-methods/
#bubble sort: https://blogboard.io/blog/knowledge/python-sorted-lambda/