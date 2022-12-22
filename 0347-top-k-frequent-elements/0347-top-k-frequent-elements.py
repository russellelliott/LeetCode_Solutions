class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #initalize empty dictionary
        freq = {}
        result = []
        
        #iterate through the list of numbers
        for i in nums:
            if i in freq:
                freq[i] = freq[i]+1
            else:
                freq[i] = 1
        
        #print(freq)
        #for k times, find the largest iten
        for i in range(k):
            #get dictionary key with max value
            maxValue = max(freq, key=freq.get)
            #print(max_value)
            #add max value to list and remove it from dictionary
            result.append(maxValue)
            freq.pop(maxValue)
            
        #return result list
        return result

#to find the k most frequent elements, we can use a hash tableDictionary