class Solution:
    def isValid(self, s: str) -> bool:
        #1. Every parenthesis needs to have a closed parenthesis
        #2. The open and close parenthesis must be the same type
        #If both conditions met, return true. Otherwise, return false.
        
        stack = [] #make the stack
        
        lookup = {")":"(","]":"[","}":"{"} #hashtable; stores key of parenthesis
        
        for par in s:
            if stack and par in lookup: #if so; for sure it's closed
                if stack[-1]==lookup[par]: #if lat thing added is same type of parenthesis
                    stack.pop()
                else:
                    return False #two diff types
            else: #if par not closed, add to stack
                stack.append(par)
        
        return True if not stack else False