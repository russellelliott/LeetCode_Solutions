class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        #find the smallest word
        strs = sorted(strs, key = len)
        #print(strs)
        
        prefixes = []
        
        for i in range(1, len(strs[0])+1):
            for word in strs:
                prefix = word[0:i]
                #print(prefix)
                prefixes.append(prefix)
        
        #we have a list of prefixes; check which ones appear for each word. use a hash map
        #initalize empty dictionary
        freq = {}
        result = []
        
        #iterate through the list of numbers
        for i in prefixes:
            if i in freq:
                freq[i] = freq[i]+1
            else:
                freq[i] = 1
        
        #print(freq)
        res = sorted(freq.items(), key=lambda x: (x[1],x[0]), reverse=True)

        #print(res)
        
        for i in res:
            word = i[0]
            frequency = i[1]
            #print("word: ", word, "frequency: ", frequency)
            if frequency == len(strs):
                return word #return first prefix shared; will be the longest due to the previous sorting
        
        #no words of that frequency, return empty string
        return ""

#common prefix is the first x letters that the words share
#get the prefix of each word and check if each word begins with that?
#sort list by length of strings: https://www.geeksforgeeks.org/python-sort-list-according-length-elements/
#substring in string: https://www.learndatasci.com/solutions/python-string-contains/

#reused: https://leetcode.com/problems/top-k-frequent-elements/submissions/
#reused: https://leetcode.com/problems/top-k-frequent-words/