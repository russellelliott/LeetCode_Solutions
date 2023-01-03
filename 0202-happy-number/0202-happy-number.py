class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        obtained = [] #results obtained
        #helper function
        
        def happy(number):
            result = sum([int(x)**2 for x in str(number)])
            obtained.append(number) #add number to list of obtained
            return result
        
        #check if n is 1 and not in cycle
        while n!=1 and n not in obtained:
            n = happy(n)
        
        return n==1
            
#split list into digits: https://bobbyhadz.com/blog/python-split-integer-into-digits
#sum list: https://www.geeksforgeeks.org/sum-function-python/

#note; if we see a number repeated, we know for sure it's false
#resued: https://leetcode.com/problems/binary-tree-inorder-traversal