class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        #initalize empty dictionary
        freq = {}
        result = []
        
        #iterate through the list of numbers
        for i in words:
            if i in freq:
                freq[i] = freq[i]+1
            else:
                freq[i] = 1
                
        #sort dictionary by value and then key
        #https://stackoverflow.com/questions/7742752/sorting-a-dictionary-by-value-then-by-key
        #reverse_comparison = lambda (a1, a2), (b1, b2):cmp((b2, b1), (a2, a1))
        #res = sorted(freq.items(), cmp=reverse_comparison, reverse=True)
        res = sorted(freq.items(), key=lambda x: (x[1],x[0]), reverse=True)
        print(res)
        print(res[0][1])
        
        '''
        perform a form of bubble sort
        perform a swap if:
        1. the two words have the same frequency
        2. the two words are in reverse lexographic order
        '''
        #https://www.geeksforgeeks.org/bubble-sort/
        n = len(freq)
 
        # Traverse through all array elements
        for i in range(n):

            # Last i elements are already in place
            for j in range(0, n-i-1):

                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                #if result[j] > result[j+1]:
                if (res[j][1]==res[j+1][1] and res[j][0]>res[j+1][0]):
                    res[j], res[j+1] = res[j+1], res[j]
        
        print(res)
        #now words of the same frequency are in lexographic order
        #get the first k of them
        for i in range(k):
            result.append(res[i][0])
        
        print(result)
        return result
        
        
#same as top k frequent elements, but with words
#https://leetcode.com/problems/top-k-frequent-elements/submissions/