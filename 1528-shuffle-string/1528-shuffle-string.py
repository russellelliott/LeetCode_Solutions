class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        chars = []
        for i in range(len(indices)):
            #pair of the character and which index it should go in
            chars.append([indices[i], str(s[i])])
        
        chars = sorted(chars, key=lambda x: x[0])
        #print(chars)
        
        result = ""
        for i in chars:
            result += i[1]
        
        return result
    
#given a list of indices, produce word from chars at those indexes
#sort list of lists: https://stackoverflow.com/questions/36955553/sorting-list-of-lists-by-the-first-element-of-each-sub-list