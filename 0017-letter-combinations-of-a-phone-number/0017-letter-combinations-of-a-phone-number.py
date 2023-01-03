class Solution(object):
    def flatten(self, B):    # function needed for code below;
        A = [] #put into a list
        for i in B:
            if type(i) == list: A.extend(i)
            else: A.append(i)
        return "".join([str(i) for i in A]) #convert list into string
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        keypad = {
            '2':['a', 'b', 'c'],
            '3':['d', 'e', 'f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z']
        }
        
        if len(digits)==0:
            return ""
        if len(digits)==1:
            return keypad[str(digits[0])]
        
        L = []
        for i in digits:
            L.append(keypad[i])
            
        outlist =[]; templist =[[]]
        for sublist in L:
            outlist = templist; templist = [[]]
            for sitem in sublist:
                for oitem in outlist:
                    newitem = [oitem]
                    if newitem == [[]]: newitem = [sitem]
                    else: newitem = [newitem[0], sitem]
                    templist.append(self.flatten(newitem))

        outlist = list(filter(lambda x: len(x)==len(L), templist))  # remove some partial lists that also creep in;
        #print(outlist)
            
        return outlist
        
#all combos of 2 lists: https://stackoverflow.com/questions/12935194/permutations-between-two-lists-of-unequal-length

#[(x,y) for x in a for y in b]  # for a list
#convert list of characters to string: https://www.geeksforgeeks.org/python-convert-list-characters-string/

#all combos of list of lists: https://stackoverflow.com/questions/798854/all-combinations-of-a-list-of-lists