class Solution(object):
    def suggestedProducts(self, products, searchWord):
        products.sort()
        
        allResults = []
        pre = ""
        for c in searchWord:
            pre += c
            results = []
            left = -1 #Saves i value of first product found
            for i, product in enumerate(products):
                if product.startswith(pre):
                    left = i
                    results.append(products[i])
                    if (i+1 < len(products) and products[i+1].startswith(pre)):
                        results.append(products[i+1])
                    if (i+2 < len(products) and products[i+2].startswith(pre)):
                        results.append(products[i+2])
                    break
            products = products[i:] #narrow products to first product onward
            allResults.append(results)
        return allResults
        
        '''output = []
        products.sort()
        left, right = 0, len(products)-1
        for i in range(len(searchWord)): #for all characters
            char = searchWord[i]
            while left<=right and len(products[left]) <=i or products[left][i]!=char:
                left+=1
            while left<=right and len(products[right]) <=i or products[right][i]!=char:
                right-=1
                #need word less than or euql length
            subOutput = []
            remain = right-left+1
            for i in range(min(3, remain)):
                subOutput.append(products[left+1])
            output.append(subOutput)
            
        return output'''
                
        
        '''#find common prexif from products and search words
        result = []
        #first, sort lexographically
        products.sort()
        #at most 3 product names after each character is typed
        for i in range(len(searchWord)-1):
            #get the prefix
            prefix = searchWord[0:i+1]
            results = []
            for word in products:
                if word.startswith(prefix):
                    results.append(word)
            result.append(results)
            results = []
        
        return results'''

#max of 3 suggests?
#should have common prefix